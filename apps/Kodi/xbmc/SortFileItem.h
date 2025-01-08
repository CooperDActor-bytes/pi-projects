/*
 *  Copyright (C) 2005-2018 Team Kodi
 *  This file is part of Kodi - https://kodi.tv
 *
 *  SPDX-License-Identifier: GPL-2.0-or-later
 *  See LICENSES/README.md for more information.
 */

#pragma once

enum class SortMethod
{
  NONE = 0,
  LABEL,
  LABEL_IGNORE_THE,
  DATE,
  SIZE,
  FILE,
  DRIVE_TYPE,
  TRACKNUM,
  DURATION,
  TITLE,
  TITLE_IGNORE_THE,
  ARTIST,
  ARTIST_AND_YEAR,
  ARTIST_IGNORE_THE,
  ALBUM,
  ALBUM_IGNORE_THE,
  GENRE,
  COUNTRY,
  YEAR,
  VIDEO_RATING,
  VIDEO_USER_RATING,
  DATEADDED,
  PROGRAM_COUNT,
  PLAYLIST_ORDER,
  EPISODE,
  VIDEO_TITLE,
  VIDEO_SORT_TITLE,
  VIDEO_SORT_TITLE_IGNORE_THE,
  PRODUCTIONCODE,
  SONG_RATING,
  SONG_USER_RATING,
  MPAA_RATING,
  VIDEO_RUNTIME,
  STUDIO,
  STUDIO_IGNORE_THE,
  FULLPATH,
  LABEL_IGNORE_FOLDERS,
  LASTPLAYED,
  PLAYCOUNT,
  LISTENERS,
  UNSORTED,
  CHANNEL,
  CHANNEL_NUMBER,
  BITRATE,
  DATE_TAKEN,
  CLIENT_CHANNEL_ORDER,
  TOTAL_DISCS,
  ORIG_DATE,
  BPM,
  VIDEO_ORIGINAL_TITLE,
  VIDEO_ORIGINAL_TITLE_IGNORE_THE,
  PROVIDER,
  USER_PREFERENCE,
  SM_MAX
};