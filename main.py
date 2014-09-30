#      _   _        __   __
#     /_\ | |__ _ _ \ \ / /_ _ _ _ __ _ ___
#    / _ \| / _` | ' \ V / _` | '_/ _` / _ \
#   /_/ \_\_\__,_|_||_\_/\__,_|_| \__, \___/
#                                 |___/
# access by os.stat
#
import os
import datetime
import time

PathFile = os.stat('C:\\boot.ini')
st_time = PathFile.st_mtime
a, b, c, d, e, f, g, h, i=time.localtime(st_time)
print datetime.datetime(a, b, c, d, e, f, g)
print h,i
print PathFile.n_fields

#
# access by win32api
#
import win32con
import win32api

print 'attribs'
atrbs = win32api.GetFileAttributes('C:\\boot.ini')
print atrbs
win32api.SetFileAttributes('C:\\boot.ini',
                           win32con.FILE_ATTRIBUTE_NORMAL
                           )
print atrbs