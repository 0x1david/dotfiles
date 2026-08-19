#!/usr/bin/env bash
if caelestia shell -s >/dev/null 2>&1; then
    caelestia shell --kill
else
    caelestia shell --daemon
fi
