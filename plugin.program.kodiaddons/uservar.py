import os, xbmc, xbmcaddon
import base64
#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR red]K[/COLOR][COLOR white]O[/COLOR][COLOR blue]D[/COLOR][COLOR red]I-[/COLOR][COLOR white]A[/COLOR][COLOR blue]D[/COLOR][COLOR red]D[/COLOR][COLOR white]O[/COLOR][COLOR blue]N[/COLOR][COLOR red]S-[/COLOR][COLOR white]U[/COLOR][COLOR blue]K[/COLOR]'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = base64.b64decode(b'aHR0cDovL2tvZGlhZGRvbnMudWsva29kaS9rb2RpLWJ1aWxkcy9rb2RpLWFkZG9ucy11ay1idWlsZHMva29kaWFkZG9uc2J1aWxkcy50eHQ=')
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE      = base64.b64decode(b'aHR0cDovL2tvZGlhZGRvbnMudWsva29kaS9BcGtGaWxlcy9hbmRyb2lkYXBwcy50eHQ=')

# Dont need to edit just here for icons stored locally
HOME           = xbmc.translatePath('special://home/')
PLUGIN         = os.path.join(HOME,     'addons',    ADDON_ID)
ART            = os.path.join(PLUGIN,   'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = ''
# Leave as http:// for default icon
ICONMAINT      = os.path.join(ART, 'maintenance.png')
ICONBUILDS     = os.path.join(ART, 'builds.png')
ICONCONTACT    = os.path.join(ART, 'contact.jpg')
ICONSAVE       = os.path.join(ART, 'SaveData.png')
ICONTRAKT      = os.path.join(ART, 'TraktIcon.png')
ICONREAL       = os.path.join(ART, 'RealDebridIcon.jpg')
ICONLOGIN      = os.path.join(ART, 'Login.png')
ICONAPK        = os.path.join(ART, 'apkInstaller.png')
ICONSETTINGS   = os.path.join(ART, 'settings.png')
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'white'
COLOR2         = 'blue'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = '\n\n[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[/B][/COLOR]\r\r\n[COLOR white][B]Please visit www.kodiaddons.uk for support.[/B][/COLOR]\r\n[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[COLOR white][B]=[COLOR blue][B]=[COLOR red][B]=[/B][/COLOR]'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = base64.b64decode(b'aHR0cDovL2tvZGlhZGRvbnMudWsva29kaS9rb2RpLWFkZG9ucy51ay13aXphcmRzL3dpemFyZHVwZGF0ZXMudHh0')
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = 'kodiaddonsUK.repo'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'yes'
# Url to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font14'
HEADERMESSAGE  = '[COLOR red]K[/COLOR][COLOR white]O[/COLOR][COLOR blue]D[/COLOR][COLOR red]I-[/COLOR][COLOR white]A[/COLOR][COLOR blue]D[/COLOR][COLOR red]D[/COLOR][COLOR white]O[/COLOR][COLOR blue]N[/COLOR][COLOR red]S-[/COLOR][COLOR white]U[/COLOR][COLOR blue]K[/COLOR] Message.....'
# url to image if using Image 424x180
HEADERIMAGE    = '[COLOR red]K[/COLOR][COLOR white]O[/COLOR][COLOR blue]D[/COLOR][COLOR red]I-[/COLOR][COLOR white]A[/COLOR][COLOR blue]D[/COLOR][COLOR red]D[/COLOR][COLOR white]O[/COLOR][COLOR blue]N[/COLOR][COLOR red]S-[/COLOR][COLOR white]U[/COLOR][COLOR blue]K[/COLOR] NEWS AND UPDATES'
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = ''
#########################################################