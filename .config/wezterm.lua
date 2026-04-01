local wezterm = require 'wezterm'

return {
  default_prog = { 'wsl.exe', '-d', 'archlinux' },
  font = wezterm.font('JetBrains Mono'),
  font_size = 13.0,
  hide_tab_bar_if_only_one_tab = true,
  audible_bell = 'Disabled',
  window_close_confirmation = 'NeverPrompt',

  colors = {
    foreground = '#bbc2cf',
    background = '#242730',
    cursor_bg = '#bbc2cf',
    cursor_fg = '#242730',
    cursor_border = '#bbc2cf',
    selection_fg = '#bbc2cf',
    selection_bg = '#6A8FBF',
    ansi = {
      '#2a2e38', '#ff665c', '#7bc275', '#fcce7b',
      '#51afef', '#C57BDB', '#5cEfFF', '#DFDFDF',
    },
    brights = {
      '#484854', '#ff665c', '#99bb66', '#ecbe7b',
      '#51afef', '#c678dd', '#46D9FF', '#bbc2cf',
    },
  },

  keys = {
    { key = 'v', mods = 'CTRL|SHIFT', action = wezterm.action.SplitHorizontal { domain = 'CurrentPaneDomain' } },
    { key = 's', mods = 'CTRL|SHIFT', action = wezterm.action.SplitVertical { domain = 'CurrentPaneDomain' } },
    { key = 'x', mods = 'CTRL|SHIFT', action = wezterm.action.CloseCurrentPane { confirm = false } },
  },
}
