#!/bin/bash
# Switch or move a window to DEV/WWW/DOC on the focused monitor
# Usage: ws.sh [switch|move] [DEV|WWW|DOC]

ACTION=$1
GROUP=$2

MONITOR=$(hyprctl monitors -j | jq -r '.[] | select(.focused) | .name')

case "$MONITOR" in
    DP-1) BASE=0 ;;
    DP-2) BASE=3 ;;
    DP-3) BASE=6 ;;
    *)    BASE=0 ;;
esac

case "$GROUP" in
    DEV) WS=$((BASE + 1)) ;;
    WWW) WS=$((BASE + 2)) ;;
    DOC) WS=$((BASE + 3)) ;;
    *)   exit 1 ;;
esac

case "$ACTION" in
    switch) hyprctl dispatch workspace "$WS" ;;
    move)   hyprctl dispatch movetoworkspace "$WS" ;;
esac
