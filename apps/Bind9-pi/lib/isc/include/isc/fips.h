/*
 * Copyright (C) Internet Systems Consortium, Inc. ("ISC")
 *
 * SPDX-License-Identifier: MPL-2.0
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, you can obtain one at https://mozilla.org/MPL/2.0/.
 *
 * See the COPYRIGHT file distributed with this work for additional
 * information regarding copyright ownership.
 */

#pragma once

/*****
***** Module Info
*****/

/***
 *** Imports
 ***/

#include <isc/types.h>

/***
 *** Functions
 ***/

bool
isc_fips_mode(void);
/*
 * Return if FIPS mode is currently enabled or not
 */

isc_result_t
isc_fips_set_mode(int mode);
/*
 * Enable FIPS mode.
 */
