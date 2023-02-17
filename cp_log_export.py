#!/usr/bin/python3
import numpy as np
import os
import re
import datetime
# %%aaa
INTERVAL = 30  # in minutes, you can change this
MAX_INTERVAL = datetime.timedelta(minutes=INTERVAL)
CURRENT_TIME = datetime.datetime.now()
FORMAT = '%d %b %H:%M:%S'
OUTPUTPATH = os.path.join(".", os.path.splitext(os.path.basename(__file__))[0])

# %%aaa
if not os.path.exists(OUTPUTPATH):
    os.makedirs(OUTPUTPATH)


def str_to_datetime(string):
    '''
    Parameters
    ----------
    string : TYPE
        DESCRIPTION.

    Returns
    -------
    date1 : TYPE
        DESCRIPTION.
    '''
    str1 = str(CURRENT_TIME.year) + ' ' + string
    parser = '%Y ' + FORMAT
    date1 = datetime.datetime.strptime(str1, parser)
    if date1 > datetime.datetime.now():
        str1 = str(-1 + CURRENT_TIME.year) + ' ' + string
        date1 = datetime.datetime.strptime(str1, parser)
    return date1


def time_exceed(log_time):
    if CURRENT_TIME - log_time > MAX_INTERVAL:
        return CURRENT_TIME - log_time
    return False


with open('./cp_log_export_output.txt', encoding="utf-8") as f:
    test_str = f.read()

regex = r"(?m)(name:\s(.+?)\s.*\n\s+" \
        r"status:\s(.+?)\s.*\n\s+" \
        r"last log read at:\s(.*)\n)"
matches = re.finditer(regex, test_str)

'''
     這裡使用到debugger & Variable Explorer
    '''
new_list = [[x for x in match.groups()] for match in matches]
'''
    這裡就我的想法而言，我會做３次，將status/timestamp/name分開
    優：可讀性較高？不用再去理解new_list -- [1][2][3]

    另外我會連names_list一起命名，下面的new_list[i][1]改成 -- names_list[i]
    '''
status_list = [inner_list[2] for inner_list in new_list]
timestamp_list = [str_to_datetime(inner_list[3]) for inner_list in new_list]

outputs = []
'''原本找不到output Name 利用dugger'''
for i, status in enumerate(status_list):
    reason = ""
    if status != "Running":
        reason += "Not running\n"
    duration = time_exceed(timestamp_list[i])
    if duration:
        reason += "Exceed max_interval: " + str(INTERVAL) + " Mins\n" \
            + "Current Time: " + CURRENT_TIME.strftime(FORMAT) \
            + "(Interval: " + str(int(duration.total_seconds()/60)) + ")\n"
    if reason == "":
        outputs.append(new_list[i][1] + " is ok")
    else:
        reason = f'Server: {new_list[i][1]}:\nReason: {reason}' \
            f'Detail:\n{new_list[i][0]}'
        outputs.append(reason)

with open(os.path.join(OUTPUTPATH, 'output.txt'), "w") as f:
    f.write("\n".join(outputs))
