# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
Exercises for using the datetime and the calendar module
'''

import calendar
from datetime import date

# Define a function named last_of_month that takes an argument dt of type date
# and returns a date object representing the last day of the month dt was in.


def last_of_month(dt):
    """
    Get the last date of the month.

    Parameters
    ----------
    dt: datetime.date
        Provides the year and month of which the last day is found.

    Returns
    -------
    end: datetime.date
        Last day of month that dt is in.
    """
    weekday, last_day = calendar.monthrange(dt.year, dt.month)
    return date(dt.year, dt.month, last_day)

# Define a function named feed_the_gremlin which takes a time object as an
# argument. It should return False between midnight and 6:30AM and True
# otherwise.


def feed_the_gremlin(t):
    """
    Can we feed the gremlin?

    Parameters
    ----------
    t: datetime.time
        Time we want to know if it is safe to feed the gremlin

    Returns
    -------
    f: bool
       True if we can feed it, False otherwise
    """
    return t.hour >= 6 and t.minute >= 30

# Define a function named how_long that takes two datetime objects dt and ref
# where ref is the reference datetime, calculates the difference between them and
# returns the difference as a string formatted like:
# "01 days, 01 minutes, 01 seconds until 2000-12-31 15:59:59"
# If ref is before dt then use 'since' instead of 'until'


def how_long(dt, ref):
    """
    Return difference between two datetimes as a formatted string.
    The format is
    "01 days, 01 minutes, 01 seconds until 2000-12-31 15:59:59"
    or
    "01 days, 01 minutes, 01 seconds since 2000-12-31 15:59:59"

    Parameters
    ----------
    dt: datetime.datetime
        Current datetime.
    ref: datetime.datetime
        Reference datetime.

    Returns
    -------
    s: string
       Formatted string.
    """
    template = "{:02d} days, {:02d} minutes, {:02d} seconds {} %Y-%m-%d %H:%M:%S"

    if ref > dt:
        w = 'until'
        diff = ref - dt
    else:
        w = 'since'
        diff = dt - ref

    return ref.strftime(template.format(diff.days,
                                        diff.seconds // 60,
                                        diff.seconds % 60,
                                        w))
