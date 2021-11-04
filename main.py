import os
import glob
import time
import pandas as pd

#linking part code to path
#The variable File_list will basically store all the excel files you put in this current folder
#this will only work if your files ends with xlsl ,
#if other wise just change xlsx to whatever ur extension is  but it should be uniform
File_lists = [x for x in os.listdir() if x.endswith(".xlsx")]
print(File_lists)

# def get_filters():
#     """
#     Asks user to specify a city, month, and day to analyze.
#     Returns:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     """
#     print('Hello User, welcome to Bikeshare!! \nWe have the first six month Data on the following cities : Chicago, \
# New York and Washington.')
#     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle
#     # invalid inputs
#
#     city = ''
#     # looping until expected input is given
#     while city not in USER_CITY_INPUT:
#         city = input('Which city from the given list would you like to get information on ? Type "Ch" for Chicago , \
# "Ny" for New York and "Wa" for Washington.\n').lower()
#         if city not in USER_CITY_INPUT:
#             city = input(f'you entered "{city}", Please Type "Ch" for Chicago ,"Ny" for New York and "Wa" for '
#                          'Washington.\n').lower()
#         else:
#             break
