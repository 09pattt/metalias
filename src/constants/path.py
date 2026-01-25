from utils.file import *

def get_apath(relative):
    return join(appdir(), relative)

REQUIREMENTS_RPATH = 'requirements.txt'
REQUIREMENTS_APATH = get_apath(REQUIREMENTS_RPATH)

APPDATA_RPATH = '.metalias'
APPDATA_APATH = get_apath(APPDATA_RPATH)