#!/bin/bash
python3 -m smtpd -n localhost &
python3 ./notify_ip_change.py
