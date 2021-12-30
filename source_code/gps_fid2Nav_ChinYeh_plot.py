# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 2021

@author: Chin-Yeh Chen
"""
import os
import decimal
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats.stats import _compute_dminus

#
'''

'''
def scale_lat_lon(coordinates_list):
    coordinates_list_re = []
    for ele in coordinates_list:
        ll = [] #lat or lon
        for elell in ele:
            elex_dec = decimal.Decimal(elell)
            new_elex = elex_dec*100000000
            ll.append(new_elex)
        coordinates_list_re.append(ll)
    return coordinates_list_re

'''
simply get the lat and lon data from file
'''
def read_data_from_file(input_file):
    lon = []
    lat = []
    coordinates_list = [lon,lat]
    with open(input_file) as f:
        for line in f.readlines():
            s = line.split()
            lat.append(s[2].strip())
            lon.append(s[4].strip())
    return coordinates_list

def plot(count, coordinates_list):
    fig, ax = plt.subplots(figsize = (10, 10)) #創建畫布
    # ax.plot(coordinates_list[0], coordinates_list[1]) #畫圖
    ax.scatter(coordinates_list[0], coordinates_list[1], s=0.001, color='blue', marker=',') #畫圖

    
    ax.set_title('Method 2')
    ax.set_xlabel('Label X', fontsize = 14, fontfamily = 'sans-serif', color = 'blue', fontstyle = 'italic')
    ax.set_ylabel('Label Y', fontsize = 14, fontfamily = 'sans-serif', color = 'blue', fontstyle = 'oblique')

    name_first = 'test'
    plt.savefig(name_first + count + '.pdf', dpi=600)

def count_run(file):
    with open(file) as f:
        new_count = 0
        for line in f.readlines():
            s = line.split()
            if not len(s[0]):
                new_count = new_count
            new_count = int(s[0].strip()) + 1
    return str(new_count)

def write_back(file, new_count):
    f = open(file, 'w') #write
    f.write(str(new_count))
    f.close()

def main():

    pathO = os.getcwd()
    count_file = pathO + "/count.txt"
    input_file = pathO + "/output/" + "L16.nav"

    count = count_run(count_file)
    write_back(count_file, count)

    plot(count, scale_lat_lon(read_data_from_file(input_file)))


main()
