#!/bin/bash
python3 -m smtpd -n &
python3 ./notify_ip_change.py
