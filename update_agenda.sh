#!/bin/bash
cd /home/luc/Agenda_Beatrice || exit 1
git pull --ff-only
python3 Agenda.py