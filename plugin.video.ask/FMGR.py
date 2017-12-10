import urllib
import urllib2
import datetime
import re
import os
import base64,time,datetime
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback


xbmcvfs.delete('special://profile/addon_data/plugin.video.ask/FMG.ini')

xbmcvfs.delete('special://profile/addon_data/plugin.video.FMG/settings.xml')
