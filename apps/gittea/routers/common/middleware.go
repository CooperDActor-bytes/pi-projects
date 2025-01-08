// Copyright 2021 The Gitea Authors. All rights reserved.
// SPDX-License-Identifier: MIT

package common

import (
	"fmt"
	"net/http"
	"strings"

	"code.gitea.io/gitea/modules/cache"
	"code.gitea.io/gitea/modules/httplib"
	"code.gitea.io/gitea/modules/reqctx"
	"code.gitea.io/gitea/modules/setting"
	"code.gitea.io/gitea/modules/web/routing"
	"code.gitea.io/gitea/services/context"

	"gitea.com/go-chi/session"
	"github.com/chi-middleware/proxy"
	"github.com/go-chi/chi/v5"
)

// ProtocolMiddlewares returns HTTP protocol related middlewares, and it provides a global panic recovery
func ProtocolMiddlewares() (handlers []any) {
	// the order is important
	handlers = append(handlers, ChiRoutePathHandler())   // make sure chi has correct paths
	handlers = append(handlers, RequestContextHandler()) //	prepare the context and panic recovery

	if setting.ReverseProxyLimit > 0 && len(setting.ReverseProxyTrustedProxies) > 0 {
		handlers = append(handlers, ForwardedHeadersHandler(setting.ReverseProxyLimit, setting.ReverseProxyTrustedProxies))
	}

	if setting.IsRouteLogEnabled() {
		handlers = append(handlers, routing.NewLoggerHandler())
	}

	if setting.IsAccessLogEnabled() {
		handlers = append(handlers, context.AccessLogger())
	}

	return handlers
}

func RequestContextHandler() func(h http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(resp http.ResponseWriter, req *http.Request) {
			profDesc := fmt.Sprintf("%s: %s", req.Method, req.RequestURI)
			ctx, finished := reqctx.NewRequestContext(req.Context(), profDesc)
			defer finished()

			defer func() {
				if err := recover(); err != nil {
					RenderPanicErrorPage(resp, req, err) // it should never panic
				}
			}()

			ds := reqctx.GetRequestDataStore(ctx)
			req = req.WithContext(cache.WithCacheContext(ctx))
			ds.SetContextValue(httplib.RequestContextKey, req)
			ds.AddCleanUp(func() {
				if req.MultipartForm != nil {
					_ = req.MultipartForm.RemoveAll() // remove the temp files buffered to tmp directory
				}
			})
			next.ServeHTTP(context.WrapResponseWriter(resp), req)
		})
	}
}

func ChiRoutePathHandler() func(h http.Handler) http.Handler {
	// make sure chi uses EscapedPath(RawPath) as RoutePath, then "%2f" could be handled correctly
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(resp http.ResponseWriter, req *http.Request) {
			ctx := chi.RouteContext(req.Context())
			if req.URL.RawPath == "" {
				ctx.RoutePath = req.URL.EscapedPath()
			} else {
				ctx.RoutePath = req.URL.RawPath
			}
			next.ServeHTTP(resp, req)
		})
	}
}

func ForwardedHeadersHandler(limit int, trustedProxies []string) func(h http.Handler) http.Handler {
	opt := proxy.NewForwardedHeadersOptions().WithForwardLimit(limit).ClearTrustedProxies()
	for _, n := range trustedProxies {
		if !strings.Contains(n, "/") {
			opt.AddTrustedProxy(n)
		} else {
			opt.AddTrustedNetwork(n)
		}
	}
	return proxy.ForwardedHeaders(opt)
}

func Sessioner() func(next http.Handler) http.Handler {
	return session.Sessioner(session.Options{
		Provider:       setting.SessionConfig.Provider,
		ProviderConfig: setting.SessionConfig.ProviderConfig,
		CookieName:     setting.SessionConfig.CookieName,
		CookiePath:     setting.SessionConfig.CookiePath,
		Gclifetime:     setting.SessionConfig.Gclifetime,
		Maxlifetime:    setting.SessionConfig.Maxlifetime,
		Secure:         setting.SessionConfig.Secure,
		SameSite:       setting.SessionConfig.SameSite,
		Domain:         setting.SessionConfig.Domain,
	})
}