# MIT License

# Copyright (c) 2020 Anthony Raus and The University of California, Irvine

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import glob
import pandas as pd
from datetime import datetime
import numpy as np
import math

# # make sure there is no overlap in datetime stamps on the files in your chosen directory
# pathvv = r"C:\Users\antho\Desktop\cappa\raw_vv" # use your path for the running data folder you wish to process

# # make sure there is no overlap in datetime stamps on the files in your chosen directory

# file_name_output = r"C:\Users\antho\Desktop\cappa\processed_individual_vv\processedvv.csv"  # use desired file name


# Magic code starts here (DO NOT EDIT BELOW UNLESS YOU KNOW WHAT YOU ARE DOING):
def vvrun(inputdirectory, outputfile):
    all_files = glob.glob(inputdirectory + "/*.csv")

    # create list of dataframes to concat later droping uneeded indexes and renaming header to generalize

    list_of_dataframes = []
    for filename in all_files:
        df = pd.read_csv(filename, usecols=range(25), header=0, names=['Channel_Name', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
        # df.drop_duplicates(subset=None, inplace=True)
        # df.drop([0,1], inplace=True)
        df = df[df['Channel_Name'] != 'Channel Name:']
        df = df[df['Channel_Name'] != 'Sensor Type:']
        df = df[df['Channel_Name'] != 'Channel Group:']
        list_of_dataframes.append(df)

    # print(list_of_dataframes)


    # contact list of dataframes (each csv file) into one dataframe
    frame = pd.concat(list_of_dataframes, axis=0, ignore_index=True)
    # Drop duplicates 
    frame.drop_duplicates(subset="Channel_Name", inplace=True)

    # drop sensor type and channel group
    # frame.drop([0,1], inplace=True)

    # tell it what my time stamps are                                      
    frame['Channel_Name'] = pd.to_datetime(frame['Channel_Name']) 
    #need to convert to utc
    #sum by minute
    framev = frame.resample('1T', base=0, on='Channel_Name').sum()
    framev.to_csv(outputfile)

    # import rfid sumframe files to idf
    # all_filesi = glob.glob(pathrfid + "/*.csv")

    # create list of dataframes to concat later droping uneeded indexes and renaming header to generalize


    # list_of_dataframesi = []
    # for filenamei in all_filesi:
    #    idf = pd.read_csv(filenamei)
    #    list_of_dataframesi.append(idf)

    # print(list_of_dataframesi)


    # contact list of dataframes (each csv file) into one dataframe
    # framei = pd.concat(list_of_dataframesi, axis=0, ignore_index=True)
    # Drop duplicates 
    # frame.drop_duplicates(subset=None, inplace=True)

    # drop sensor type and channel group
    # frame.drop([0,1], inplace=True)

    # tell it what my time stamps are                                      
    # framei['TS'] = pd.to_datetime(framei['TS']) 


    #compare frames for each minute assigning the minutes with a majority in either A or B to that number and assigning half to each if A = B. If A+B= 0 for that minute it will assign to A





    #Create a sumframe per day starting at noon and writing to csv