from libqtile.config import DropDown, Group, Key, ScratchPad
from .keybindings import browser_app, keys, notes
from .preferences import mod, terminal
from libqtile.lazy import lazy
from libqtile.command import lazy as lazycomm
# groups = [Group(str(i), screen_affinity=i%3) for i in range(1,7)]

# for it, i in enumerate(groups):
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )


groups = [
    Group(name="DEV", layout="spiral"),
    Group(name="WWW", layout="spiral"),
    Group(name="DOC", layout="spiral"),
    ScratchPad("CMD", [
         DropDown("term", terminal, opacity=0.8, x=0.25 ,y=0.15, height=0.7, width=0.5)
    ]),
    ScratchPad("OBS", [
        DropDown("obsidian",'obsidian "obsidian://open?vault=Engineering"'  , opacity=0.8, x=0.25 ,y=0.15, height=0.7, width=0.5)
    ]),
    ScratchPad("WEB", [
        DropDown("browser", browser_app + "https://google.com", opacity=0.9, x=0.25 ,y=0.15, height=0.7, width=0.5)
    ]),

]
keys.extend([
            Key([mod], "semicolon", lazy.group["DEV"].toscreen(), desc="Switch to group {}".format("DEV"),),
            Key([mod, "control"], "semicolon", lazy.window.togroup("DEV", switch_group=True), desc="Switch to & move focused window to group {}".format("DEV"),),
            Key([mod], "apostrophe", lazy.group["WWW"].toscreen(), desc="Switch to group {}".format("WWW"),),
            Key([mod, "control"], "apostrophe", lazy.window.togroup("WWW", switch_group=True), desc="Switch to & move focused window to group {}".format("WWW"),),
            Key([mod], "slash", lazy.group["DOC"].toscreen(), desc="Switch to group {}".format("DOC"),),
            Key([mod, "control"], "slash", lazy.window.togroup("DOC", switch_group=True), desc="Switch to & move focused window to group {}".format("DOC"),), 
            Key([mod], "F11", lazy.group['CMD'].dropdown_toggle('term')),
            Key([], "F12", lazy.group['WEB'].dropdown_toggle('browser')),
            Key([mod], "F12", lazy.group["OBS"].dropdown_toggle('obsidian')),
                ]
            )
