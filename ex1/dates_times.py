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

# Define a function named last_of_month that takes an argument dt of type date
# and returns a date object representing the last day of the month dt was in.

import datetime

def last_of_month(dt):
    """Return a date object with the last day of the month of the provided date
    """
    dt = dt.replace(day=1) + datetime.timedelta(days=31)
    dt= dt.replace(day=1)
    return dt - datetime.timedelta(days=1)
    

# Define a function named feed_the_gremlin which takes a time object as an
# argument. It should return False between midnight and 6:30AM and True
# otherwise.

def feed_the_gremlin(time):
    """Tells you wether or not to feed the gremlin at a given time
    """
    return not (time.hour <= 6)&(time.minute < 30)


# Define a function named how_long that takes two datetime objects dt and ref
# where ref is the reference datetime, calculates the difference between them and
# returns the difference as a string formatted like:
# "01 days, 01 minutes, 01 seconds until 2000-12-31 15:59:59"
# If ref is before dt then use 'since' instead of 'until'

dt = datetime.datetime(1987, 1, 31, 23, 50, 50)
ref = datetime.datetime(1986, 3, 25, 21, 25, 14)

def how_long(dt, ref):
    """Gives the days, minutes and seconds until or since a reference time
    """
    
    delta = abs(dt-ref)
    days = delta.days
    secs = delta.seconds
    minutes = int(secs/60.)
    secs = secs - minutes*60
    
    sep = 'since' if ref < dt else 'until'
    return '%02i days, %02i minutes, %02i seconds ' % (days,minutes,secs) + sep + ref.strftime(" %Y-%m-%d %H:%M:%S")
    
    



