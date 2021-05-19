#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%H:%M:%S",
    color='#C678DD',
    interval=1,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("clock",
    format="  %a %d-%m-%Y ",
    color='#61AEEE',
    interval=1,)

status.register("cpu_usage",
    on_leftclick="termite --title=htop -e 'htop'",
    format="  {usage}%",)

status.register("mem",
    color="#999999",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format=" {avail_mem}/{total_mem} GB",
    divisor=1073741824,)

status.register("disk",
    color='#ABB2BF',
    path="/",
    format=" {avail} GB",)

status.register("keyboard_locks",
    format='{caps} {num}',
    caps_on='Caps Lock',
    caps_off='',
    num_on='Num On',
    num_off='',
    color='#e60053',
    )

status.register("network",
	interface="eth0",
	format_up=": {v4cidr}",
	color_up = "#e74c3c",
	)
#
# Has all the options of the normal network and adds some wireless specific things
# like quality and network names.
#
# Note: requires both netifaces and basiciw

# status.register("backlight",
#     backlight="intel_backlight",
#     format="Bright: {percentage:2.0f}%",)


# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
#status.register("pulseaudio",
#	format="{volume}",
#	)

#Shows mpd status
#Format:
#Cloud connected▶Reroute to Remain
status.register("mpd",
   format="{title}{status}{album}",
   status={
       "pause": "▷",
       "play": "▶",
       "stop": "◾",
   },)

status.register("network",
    interface="eth0",
    graph_style="braille-snake",
    format_up="LAN:  ↑{bytes_sent}/s ↓{bytes_recv}/s",
    start_color="#2980b9",
    end_color="#00ff00",
    auto_units = True,
    format_down="LAN: - ",)

status.register("network",
    interface="tun0",
    unknown_up="True",
    graph_style="braille-snake",
    format_up="VPN: {v4} ↑{bytes_sent}/s ↓{bytes_recv}/s",
    start_color="#d35400",
    end_color="#00ff00",
    auto_units = True,
    format_down="VPN: -",)

status.run()
