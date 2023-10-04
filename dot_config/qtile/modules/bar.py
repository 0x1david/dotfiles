from libqtile import bar, widget, qtile
from libqtile.config import Screen
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration, BorderDecoration
from .preferences import launcher, power_menu
from .colorscheme import theme as colors
def open_pavu():
    qtile.cmd_spawn("pavucontrol")

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize = 14,
    padding = 1,
)

powerline = {
    "decorations": [
        PowerLineDecoration(path="back_slash")
    ]
}

dec_group_format = dict(radius=10, filled=True, padding_y=6, group=True)

decoration_group = {
    "decorations": [
        RectDecoration(colour=colors['blacker'], **dec_group_format)
    ],
}
decoration_group_red = {
    "decorations": [
        RectDecoration(colour=colors['red'], **dec_group_format)
    ],
}
decoration_group_green = {
    "decorations": [
        RectDecoration(colour=colors['green'], **dec_group_format)
    ],
}
decoration_group_blue = {
    "decorations": [
        RectDecoration(colour=colors['blue'], **dec_group_format)
    ],
}
decoration_group_yellow = {
    "decorations": [
        RectDecoration(colour=colors['yellow'], **dec_group_format)
    ],
}
extension_defaults = widget_defaults.copy()


screens = [
        Screen(top=bar.Bar(
            [
                widget.Sep(linewidth=0, padding=15, size_percent=40),
                widget.TextBox(
                    text=' 󰣇 ',
                    foreground=colors['blue'],
                    padding=20,
                    fontsize=22,
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(launcher)},
                    **decoration_group
                ),
                widget.Sep(linewidth=0, padding=20, size_percent=40),
                widget.GroupBox(
                    borderwidth=1,
                    active = colors['blue'],
                    inactive = colors['fg'],
                    highlight_method = "text",
                    this_current_screen_border = colors['green'],
                    disable_drag = True,
                    hide_unused=False,
                    padding=10,
                    spacing=5,
                    **decoration_group
                ),
                widget.Spacer(),
                widget.WindowName(
                    foreground = colors['cream'],
                    width=bar.CALCULATED,
                    decorations=[
                        BorderDecoration(
                            colour = colors['cream'],
                            border_width = [0, 0, 2, 0],
                        )
                    ],
                 ),
                widget.Spacer(),
                widget.Systray(
                    icon_size = 16,
                    padding = 20,
                    background=colors['transparent'],
                ),
                widget.Sep(linewidth=0, padding=20, size_percent=40),
                widget.TextBox(
                    text=" ",
                    foreground=colors["cyan"],
                    background=colors["transparent"],
                    font="Font Awesome 10 Free Solid",
                    fontsize=16,
                ),
                widget.PulseVolume(
                    foreground=colors["cyan"],
                    limit_max_volume="True",
                ),
                widget.Sep(linewidth=0, padding=10, size_percent=40),
                widget.Net(
                    interface="wlan0",
                    format="{down} ↓↑ {up}",
                    foreground=colors["magenta"],
                    background=colors["transparent"],
                    prefix="k",
                ),
                widget.Sep(linewidth=0, padding=20, size_percent=40),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors["yellow"],
                    background=colors["transparent"], 
                ),
                widget.Clock(
                    format="%a, %d %b",
                    foreground=colors["yellow"],
                    background=colors["transparent"],
                ),
                widget.Sep(linewidth=0, padding=20, size_percent=40),
                widget.Clock(
                    foreground=colors['green'],
                    padding = 10,
                    format="  %I:%M %p",
                    **decoration_group
                ),
                widget.Sep(linewidth=0, padding=15, size_percent=40),
                widget.TextBox(
                    text='  ',
                    foreground=colors['red'],
                    padding=20,
                    **decoration_group,
                    fontsize="18",
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(power_menu)},
                ),
                widget.Sep(linewidth=0, padding=14, size_percent=40),

            ], opacity=1.0, size=44, margin=0, background=colors['transparent']
        ))
    ]
