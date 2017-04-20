#!/bin/bash
until  python free_association_bot.py; do
    echo "'free_association_bot.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
