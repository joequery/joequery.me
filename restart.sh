#!/bin/bash
. env/bin/activate
python genfeed.py
touch /var/run/uwsgi/joequery.pid
