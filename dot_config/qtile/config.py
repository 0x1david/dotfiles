from libqtile import hook
from modules.bar import screens 
from modules.preferences import *
from modules.keybindings import *
from modules.layouts import *
from modules.groups import *
import subprocess


@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/bash/autostart.sh'])

