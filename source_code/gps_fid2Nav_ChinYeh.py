# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 2021

@author: Chin-Yeh Chen
"""
import os
import decimal
import numpy as np
import math
from scipy import stats


def LatLonCalculator(stringll, LaLo):
    """
    covert deg+min to deg decimal
    """
    if (LaLo == 'La'):
        deg = stringll[0:2]
        min = stringll[2:9]
    elif (LaLo == 'Lo'):
        deg = stringll[0:3]
        min = stringll[3:10]

    deg_dec = decimal.Decimal(deg)
    min_dec = decimal.Decimal(min)

    min_dec_fin = round(min_dec/60, 6)

    degOfdecimal = deg_dec + min_dec_fin

    return degOfdecimal


def hhmmss2ss(time_sequence):
    """
    pre-processing hhmmss to second
    """
    time_sequence_sec = []
    for ele in time_sequence:
        hour2sec = int(ele[0:2])*3600  # hour
        min2sec = int(ele[2:4])*60  # min
        sec2sec = int(ele[4:6])  # sec
        sum_sec = hour2sec + min2sec + sec2sec

        time_sequence_sec.append(sum_sec)
    return time_sequence_sec


def shotIntervalCheck(DFSHD_1, time_sequence_sec, counter):
    """
    only check the delay shot which causes the worng shot-time-interval
    """
    delta_array = []
    for i in range(0, len(time_sequence_sec)-1, 1):
        delta_array.append(
            int(time_sequence_sec[i+1]) - int(time_sequence_sec[i]))

    delta_array = np.array(delta_array)
    shot_interval = stats.mode(delta_array)[0]  # most  freq number

    for i in range(0, len(delta_array), 1):
        if(delta_array[i] != shot_interval):
            counter += 1
            sp = ' '
            print(sp + ' Firing time problem: between' + sp + 'ffid# ' + str(DFSHD_1[i]) +
                  sp + 'and' + sp + 'ffid# ' + str(DFSHD_1[i+1]) + '!')

    return delta_array


def ffid_skip_check(ffid_sequence, counter):
    """
    check ffid sequence (small to big)
    """

    for i in range(0, len(ffid_sequence)-1, 1):
        next_ffid = ffid_sequence[i+1]
        this_ffid = ffid_sequence[i]
        if((int(next_ffid) - int(this_ffid)) != 1):
            counter += 1
            print(
                f' Check output .nav! FFID number problem: between ffid# {this_ffid} and ffid# {next_ffid}!')


def deg2rad(deg):
    """
    deg2rad
    """
    return deg*(math.pi/180)


def calculate_distance(lon1, lat1, lon2, lat2):
    """
    calculate the distance between two point. (Haversine formula)
    """
    R = 6371  # Radius of the earth in km
    dLon = deg2rad(lon2-lon1)
    dLat = deg2rad(lat2-lat1)  # ' below
    a = math.sin(dLat/2) * math.sin(dLat/2) + \
        math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * \
        math.sin(dLon/2) * math.sin(dLon/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    d = R * c * 1000  # Distance in m

    return str('{:,.2f}'.format(round(d, 2)))


def main(pathO, ffid_file):

    # address the file name
    file_name = ffid_file.split('.')[0]  # 11290852
    file_type = ffid_file.split('.')[1]  # fid

    input_folder_path = pathO + '/input/'
    if not os.path.isdir(input_folder_path):  # if no folder, then create one.
        os.makedirs(input_folder_path, mode=0o777)

    input_file = input_folder_path + file_name + '.' + file_type

    # preparing the array
    DFSHD_1 = []  # string array
    GPGLL_2_N = []
    GPGLL_3_Lat = []
    GPGLL_4_E = []
    GPGLL_5_Lon = []

    GPGLL_time = []

    # read file
    with open(input_file) as f:
        for line in f.readlines():
            s = line.split(',')
            if (s[0] == '$DFSHD'):  # ffid
                DFSHD_1.append(str(s[1].strip()))

            elif (s[0] == '$GPGLL'):
                GPGLL_2_N.append(str(s[2]))  # N
                GPGLL_3_Lat.append(
                    str(LatLonCalculator(s[1], 'La')))  # 22.322495

                GPGLL_4_E.append(str(s[4]))  # E
                GPGLL_5_Lon.append(
                    str(LatLonCalculator(s[3], 'Lo')))  # 120.583592

                GPGLL_time.append(str(s[5].strip()))

    counter = 0
    # ffid skip check
    ffid_skip_check(DFSHD_1, counter)

    # time check
    shotIntervalCheck(DFSHD_1, hhmmss2ss(GPGLL_time), counter)

    if counter == 0:
        print('Successfully Check!')

    # save new nav
    output_folder_path = pathO + '/output/'
    if not os.path.isdir(output_folder_path):
        os.makedirs(output_folder_path, mode=0o777)

    path = output_folder_path + file_name + '.nav'  # path important!
    f = open(path, 'w')  # write

    for i in range(0, len(DFSHD_1), 1):
        sp = ' '
        newLine = GPGLL_time[i] + sp + DFSHD_1[i] + sp + GPGLL_2_N[i] + sp + \
            GPGLL_3_Lat[i] + sp + GPGLL_4_E[i] + sp + GPGLL_5_Lon[i]
        if i == 0:
            newLine = newLine + sp + '0.0'
        else:
            newLine = newLine + sp + \
                calculate_distance(
                    float(GPGLL_5_Lon[i-1]), float(GPGLL_3_Lat[i-1]), float(GPGLL_5_Lon[i]), float(GPGLL_3_Lat[i]))
        f.write(newLine + '\n')

    f.close()

    os.startfile(path)


# -----------------------------------------------------------------------
# main start from here
pathO = os.getcwd()
input_folder = pathO + '/input/'
files = os.listdir(input_folder)
for file in files:
    s = file.split('.')
    if (len(s) > 1):
        if ('fid' == file.split('.')[-1]):
            print(f'This is {file}:')

            main(pathO, file)
print("Press ESC to quit!")
