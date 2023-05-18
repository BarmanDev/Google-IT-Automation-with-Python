#!/usr/bin/env python3

import os
import re
import sys
import operator
import csv

error_counter = {}
error_user = {}
info_user = {}


def search_file():
    with open('syslog.log', "r") as myfile:
        for line in myfile:
            if " ERROR " in line:
                find_error(line)
                add_user_list(line, 1)
            elif " INFO " in line:
                add_user_list(line, 2)
    return


def find_error(str):
    match = re.search(r"(ERROR [\w \[]*) ", str)
    if match is not None:
        aux = match.group(0).replace("ERROR ", "").strip()
        if aux == "Ticket":
            aux = "Ticket doesn't exist"
        if not aux in error_counter:
            error_counter[aux] = 1
        else:
            error_counter[aux] += 1
    return


def add_user_list(str, op):
    match = re.search(r'\(.*?\)', str)
    user = match.group(0)
    userA = user.strip("()")
    if op == 1:
        if not userA in error_user:
            error_user[userA] = 1
        else:
            error_user[userA] += 1
    elif op == 2:
        if not userA in info_user:
            info_user[userA] = 1
        else:
            info_user[userA] += 1
    return


def sort_list(op, list):
    if op == 1:
        s = sorted(list.items(), key=operator.itemgetter(1), reverse=True)
    elif op == 2:
        s = sorted(list.items(), key=operator.itemgetter(0))
    return s


def getErrValue(keyV):
    for key, value in error_user:
        if key is keyV:
            return value
    return 0


def write_csv(op):
    if op == 1:
        with open('user_statistics.csv', 'w', newline='') as output:
            fieldnames = ['Username', 'INFO', 'ERROR']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in info_user:
                valError = getErrValue(key)
                csvw.writerow(
                    {'Username': key, 'INFO': value, 'ERROR': valError})
    if op == 2:
        with open('error_message.csv', 'w', newline='') as output:
            fieldnames = ['Error', 'Count']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in error_counter:
                csvw.writerow({'Error': key, 'Count': value})
    return


def add_zeros():
    for user in error_user.keys():
        if user not in info_user:
            info_user[user] = 0
    for user in info_user.keys():
        if user not in error_user:
            error_user[user] = 0
    return


search_file()
add_zeros()
error_counter = sort_list(1, error_counter)
error_user = sort_list(2, error_user)
info_user = sort_list(2, info_user)
write_csv(1)
write_csv(2)
