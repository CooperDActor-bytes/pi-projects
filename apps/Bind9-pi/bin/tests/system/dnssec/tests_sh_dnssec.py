# Copyright (C) Internet Systems Consortium, Inc. ("ISC")
#
# SPDX-License-Identifier: MPL-2.0
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0.  If a copy of the MPL was not distributed with this
# file, you can obtain one at https://mozilla.org/MPL/2.0/.
#
# See the COPYRIGHT file distributed with this work for additional
# information regarding copyright ownership.

import pytest

pytestmark = pytest.mark.extra_artifacts(
    [
        "K*",
        "canonical*",
        "delv.out*",
        "dig.out.*",
        "dnssectools.out.*",
        "dsfromkey.out.*",
        "keygen*.err*",
        "named.secroots.*",
        "nsupdate.out.*",
        "python.out.*",
        "rndc.out.*",
        "signing.out.*",
        "*/K*",
        "*/dsset-*",
        "*/managed.conf",
        "*/trusted.conf",
        "*/*.bk",
        "*/*.jnl",
        "*/*.jbk",
        "*/*.signed",
        "*/*.mkeys*",
        "ans*/ans.run",
        "ans*/query.log",
        "ns1/managed.key.id",
        "ns1/root.db",
        "ns1/trusted.keys",
        "ns2/algroll.db",
        "ns2/badparam.db",
        "ns2/badparam.db.bad",
        "ns2/cdnskey-update.secure.db",
        "ns2/cdnskey-update.secure.id",
        "ns2/cdnskey-x.secure.db",
        "ns2/cdnskey.secure.db",
        "ns2/cds-update.secure.db",
        "ns2/cds-update.secure.id",
        "ns2/cds-x.secure.db",
        "ns2/cds.secure.db",
        "ns2/example.db",
        "ns2/in-addr.arpa.db",
        "ns2/lazy-ksk.db",
        "ns2/managed.db",
        "ns2/nsec3chain-test.db",
        "ns2/settime.out.updatecheck-kskonly.secure.ksk",
        "ns2/settime.out.updatecheck-kskonly.secure.zsk",
        "ns2/single-nsec3.db",
        "ns2/too-many-iterations.db",
        "ns2/trusted.db",
        "ns2/updatecheck-kskonly.secure.ksk.id",
        "ns2/updatecheck-kskonly.secure.ksk.key",
        "ns2/updatecheck-kskonly.secure.zsk.id",
        "ns2/updatecheck-kskonly.secure.zsk.id2",
        "ns2/updatecheck-kskonly.secure.zsk.id3",
        "ns2/updatecheck-kskonly.secure.zsk.key",
        "ns3/NSEC",
        "ns3/NSEC3",
        "ns3/auto-nsec.example.db",
        "ns3/auto-nsec3.example.db",
        "ns3/badds.example.db",
        "ns3/bogus.example.db",
        "ns3/disabled.managed.db",
        "ns3/disabled.trusted.db",
        "ns3/dname-at-apex-nsec3.example.db",
        "ns3/dnskey-nsec3-unknown.example.db",
        "ns3/dnskey-nsec3-unknown.example.db.tmp",
        "ns3/dnskey-unknown.example.db",
        "ns3/dnskey-unknown.example.db.tmp",
        "ns3/dnskey-unsupported-2.example.db",
        "ns3/dnskey-unsupported.example.db",
        "ns3/dnskey-unsupported.example.db.tmp",
        "ns3/dynamic.example.db",
        "ns3/enabled.managed.db",
        "ns3/enabled.trusted.db",
        "ns3/example.bk",
        "ns3/expired.example.db",
        "ns3/expiring.example.db",
        "ns3/future.example.db",
        "ns3/keyless.example.db",
        "ns3/kskonly.example.db",
        "ns3/lower.example.db",
        "ns3/managed-future.example.db",
        "ns3/multiple.example.db",
        "ns3/nsec3-unknown.example.db",
        "ns3/nsec3.example.db",
        "ns3/nsec3.nsec3.example.db",
        "ns3/nsec3.optout.example.db",
        "ns3/nsec3chain-test.bk",
        "ns3/occluded.example.db",
        "ns3/optout-unknown.example.db",
        "ns3/optout.example.db",
        "ns3/optout.nsec3.example.db",
        "ns3/optout.optout.example.db",
        "ns3/revkey.example.db",
        "ns3/revoked.managed.db",
        "ns3/revoked.trusted.db",
        "ns3/rfc2335.example.bk",
        "ns3/rsasha256.example.db",
        "ns3/rsasha512.example.db",
        "ns3/secure.below-cname.example.db",
        "ns3/secure.example.db",
        "ns3/secure.managed.db",
        "ns3/secure.nsec3.example.db",
        "ns3/secure.optout.example.db",
        "ns3/secure.trusted.db",
        "ns3/siginterval.conf",
        "ns3/siginterval.example.db",
        "ns3/split-dnssec.example.db",
        "ns3/split-smart.example.db",
        "ns3/trusted-future.key",
        "ns3/ttlpatch.example.db",
        "ns3/ttlpatch.example.db.patched",
        "ns3/unsupported.managed.db",
        "ns3/unsupported.managed.db.tmp",
        "ns3/unsupported.trusted.db",
        "ns3/unsupported.trusted.db.tmp",
        "ns3/update-nsec3.example.db",
        "ns3/update-nsec3.example.db.signed",
        "ns3/upper.example.db",
        "ns3/upper.example.db.lower",
        "ns4/managed.conf",
        "ns4/managed-keys.bind",
        "ns4/named.secroots",
        "ns4/named_dump.db.*",
        "ns5/revoked.conf",
        "ns5/trusted.conf",
        "ns6/optout-tld.db",
        "ns7/split-rrsig.db",
        "ns7/split-rrsig.db.unsplit",
        "signer/example.db",
        "signer/example.db.after",
        "signer/example.db.before",
        "signer/example.db.changed",
        "signer/example2.db",
        "signer/example3.db",
        "signer/general/dsset-*",
        "signer/general/signed.zone",
        "signer/general/signer.out.*",
        "signer/nsec3param.out",
        "signer/prepub.db",
        "signer/revoke.example.db",
        "signer/signer.err.*",
        "signer/signer.out.*",
    ]
)


def test_dnssec(run_tests_sh):
    run_tests_sh()