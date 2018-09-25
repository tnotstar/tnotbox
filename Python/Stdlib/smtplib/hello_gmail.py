#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib

from_addr = "my_address@example.com"
to_addr = "your_address@example.com"
msg_text = "Hello, world!"

try:
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.set_debuglevel(1)
    smtp.sendmail(from_addr, to_addr, msg_text)
    smtp.quit()
except:
    print("Oops: something is wrong")

# EOF