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



xbmcvfs.copy(base64.decodestring('aHR0cDovL2FzazRhY2Nlc3MuY29tL2Fzay1rb2RpL192NC9HdWlkZXMvRk1HLmluaQ=='),'special://profile/addon_data/plugin.video.ask/FMG.ini')

xbmcvfs.copy('special://home/addons/plugin.video.ask/resources/FMGSettings.xml','special://profile/addon_data/plugin.video.FMG/settings.xml')
