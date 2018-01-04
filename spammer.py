#!/usr/bin/python

# - Spammer v2
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Author: P4kL0nc4t
# | Date: 5/12/2017
# | Disclaimer: Editing author will not make you the real coder

import spammer_class
spammer = spammer_class.Spammer()
spammer.author = "P4kL0nc4t"
try:
    spammer.main()
except KeyboardInterrupt:
    print "\r[!][except] KeyboardInterrupt detected! Exiting . . ."
    exit()
