#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Futures
from __future__ import unicode_literals

"""The script is to convert Akamai Shield dynamic IP list
 to PaloAltoNetworks NextGen firewall EDL list to publish on a webserver"""

__author__ = "Sergey Rogatnev"
__copyright__ = "Copyright 2020, The Akamai To PANOS NextGen Firewall EDL"
__credits__ = [""]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Sergey Rogatnev"
__email__ = "akaserg@gmail.com"
__status__ = "Development"


# Generic/Built-in
# import os
# import os.path
# import re
# import ipaddress

# Other Libs
from os import path
from re import match

# TO_DO
# Fetch_prefix_list_from_Akamai_and_save_it_in_local_file_"akamai.txt"

# TO_DO
# Input_interaction_if_any


# Verify if file exists
fn = "akamai.txt"


def file_exists(fn):
    """Function to check if file exists, returning boolean True or False """
    f_exists = path.exists(fn)
    return f_exists


def total_prefixes():
    """Function to calculate amount of prefixes"""
    p_total = sum(1 for line in open(fn)) - 4
    return p_total


if file_exists(fn) is True:
    print('')
    print("Filename with prefixes: ", fn)
    print('')
    p_total = total_prefixes()
    print("Prefixes total: ", p_total)
    f = open(fn)
    readfile = f.read()
    file_list = readfile.split()
# Clean_the_list_keeping_prefixes_only
    ip_list = list(filter(lambda v: match('\d', v), file_list))
    edl_list = "akamai-edl.html"
    if file_exists(edl_list) is True:
        print('')
        print("File exists:", edl_list)
        print("Updating ", edl_list, " file")
        with open(edl_list, 'w') as edl:
            for i in ip_list:
                edl.write('%s\n' % i)
    else:
        print('')
        print("File does not exists, creating a new file: ", edl_list)
        with open(edl_list, 'w') as edl:
            for i in ip_list:
                edl.write('%s\n' % i)
    print('')
    print("Here is a new: ", edl_list)
    edl_html_file = open(edl_list)
    print('')
    print(edl_html_file.read())
else:
    print("You have to use 'akamai.txt' file")
    print("I can't find ", fn, " file, please correct it and run script again")
    quit()

# TO_DO
# Verify_if_all_prefixes_are_valid_IPv4

# TO_DO
# Update_html_page_on_a_webserver_with_new_EDL_list

# TO_DO
# Send email to provide status

