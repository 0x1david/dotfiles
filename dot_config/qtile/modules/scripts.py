from libqtile.lazy import lazy
from libqtile.backend.x11.window import Window

@lazy.window.function
def switch_group(target):
    Window.cmd_togroup(target)

    
