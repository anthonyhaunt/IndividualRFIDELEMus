
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
# pathrfid = r"C:\Users\antho\Desktop\cappa\raw_inv\preprocessed_data_(20).csv" # use your path for the RFID folder you wish to process

# file_name_output = r"C:\Users\antho\Desktop\cappa\processed_RFID\processed.csv"  # use desired file name
def run_rfid (inputcsv, outputcsv):
#define variables tell it which mice (which RFID HEX_EPC (coppy the HEX_EPC you know it is from the HEX_EPC column)) are which ports
# portname_a/b = 'HEX_EPC' (noinput tells the program no indivdual tracking was run for that cage)

    #define noinput
    noinput = 'a0000000000000000000008'
    
    #define HEX_EPC 
    one_a = 'e0000000000000000000001a' 
    one_b = 'e0000000000000000000001b'
    two_a = 'e0000000000000000000002a'
    two_b = 'e0000000000000000000002b'
    three_a = 'e0000000000000000000003a'
    three_b = 'e0000000000000000000003b'
    four_a = 'e0000000000000000000004a'
    four_b = 'e0000000000000000000004b'
    five_a = 'e0000000000000000000005a'
    five_b = 'e0000000000000000000005b'
    six_a = 'e0000000000000000000006a'
    six_b = 'e0000000000000000000006b'
    seven_a = 'e0000000000000000000007a'
    seven_b = 'e0000000000000000000007b'
    eight_a = 'e0000000000000000000008a'
    eight_b = 'e0000000000000000000008b'
    nine_a = 'e0000000000000000000009a'
    nine_b = 'e0000000000000000000009b'
    ten_a = 'e0000000000000000000010a'
    ten_b = 'e0000000000000000000010b'
    eleven_a = 'e0000000000000000000011a'
    eleven_b = 'e0000000000000000000011b'
    twelve_a = 'e0000000000000000000012a'
    twelve_b = 'e0000000000000000000012b'
    thirteen_a = 'e0000000000000000000013a'
    thirteen_b = 'e0000000000000000000013b'
    fourteen_a = 'e0000000000000000000014a'
    fourteen_b = 'e0000000000000000000014b'
    fifteen_a = 'e0000000000000000000015a'
    fifteen_b = 'e0000000000000000000015b'
    sixteen_a = 'e0000000000000000000016a'
    sixteen_b = 'e0000000000000000000016b'
    seventeen_a = 'e0000000000000000000017a'
    seventeen_b = 'e0000000000000000000017b'
    eighteen_a = 'e0000000000000000000018a'
    eighteen_b = 'e0000000000000000000018b'
    nineteen_a = 'e0000000000000000000019a'
    nineteen_b = 'e0000000000000000000019b'
    twenty_a = 'e0000000000000000000020a'
    twenty_b = 'e0000000000000000000020b'
    twentyone_a = 'e0000000000000000000021a'
    twentyone_b = 'e0000000000000000000021b'
    twentytwo_a = 'e0000000000000000000022a'
    twentytwo_b = 'e0000000000000000000022b'
    twentythree_a = 'e0000000000000000000023a'
    twentythree_b = 'e0000000000000000000023b'
    twentyfour_a = 'e0000000000000000000024a'
    twentyfour_b = 'e0000000000000000000024b'



    # Magic code starts here (DO NOT EDIT BELOW UNLESS YOU KNOW WHAT YOU ARE DOING):


    df = pd.read_csv(inputcsv) #read rfid csv

    #print(df)

    # tell it what my time stamps are                                      
    df['TIME_STAMP'] = pd.to_datetime(df['TIME_STAMP']) 

    #print(df)

    #define a data frame with only the information for each HEX_EPC in each data frame

    df1a = df[df['HEX_EPC'] == one_a]
    df1b = df[df['HEX_EPC'] == one_b]
    df2a = df[df['HEX_EPC'] == two_a]
    df2b = df[df['HEX_EPC'] == two_b]
    df3a = df[df['HEX_EPC'] == three_a]
    df3b = df[df['HEX_EPC'] == three_b]
    df4a = df[df['HEX_EPC'] == four_a]
    df4b = df[df['HEX_EPC'] == four_b]
    df5a = df[df['HEX_EPC'] == five_a]
    df5b = df[df['HEX_EPC'] == five_b]
    df6a = df[df['HEX_EPC'] == six_a]
    df6b = df[df['HEX_EPC'] == six_b]
    df7a = df[df['HEX_EPC'] == seven_a]
    df7b = df[df['HEX_EPC'] == seven_b]
    df8a = df[df['HEX_EPC'] == eight_a]
    df8b = df[df['HEX_EPC'] == eight_b]
    df9a = df[df['HEX_EPC'] == nine_a]
    df9b = df[df['HEX_EPC'] == nine_b]
    df10a = df[df['HEX_EPC'] == ten_a]
    df10b = df[df['HEX_EPC'] == ten_b]
    df11a = df[df['HEX_EPC'] == eleven_a]
    df11b = df[df['HEX_EPC'] == eleven_b]
    df12a = df[df['HEX_EPC'] == twelve_a]
    df12b = df[df['HEX_EPC'] == twelve_b]
    df13a = df[df['HEX_EPC'] == thirteen_a]
    df13b = df[df['HEX_EPC'] == thirteen_b]
    df14a = df[df['HEX_EPC'] == fourteen_a]
    df14b = df[df['HEX_EPC'] == fourteen_b]
    df15a = df[df['HEX_EPC'] == fifteen_a]
    df15b = df[df['HEX_EPC'] == fifteen_b]
    df16a = df[df['HEX_EPC'] == sixteen_a]
    df16b = df[df['HEX_EPC'] == sixteen_b]
    df17a = df[df['HEX_EPC'] == seventeen_a]
    df17b = df[df['HEX_EPC'] == seventeen_b]
    df18a = df[df['HEX_EPC'] == eighteen_a]
    df18b = df[df['HEX_EPC'] == eighteen_b]
    df19a = df[df['HEX_EPC'] == nineteen_a]
    df19b = df[df['HEX_EPC'] == nineteen_b]
    df20a = df[df['HEX_EPC'] == twenty_a]
    df20b = df[df['HEX_EPC'] == twenty_b]
    df21a = df[df['HEX_EPC'] == twentyone_a]
    df21b = df[df['HEX_EPC'] == twentyone_b]
    df22a = df[df['HEX_EPC'] == twentytwo_a]
    df22b = df[df['HEX_EPC'] == twentytwo_b]
    df23a = df[df['HEX_EPC'] == twentythree_a]
    df23b = df[df['HEX_EPC'] == twentythree_b]
    df24a = df[df['HEX_EPC'] == twentyfour_a]
    df24b = df[df['HEX_EPC'] == twentyfour_b]

    #print(df1a)

    #define a list of frames
    indvframes = [df1a, df1b, df2a, df2b, df3a, df3b, df4a, df4b, df5a, df5b, df6a, df6b, df7a, df7b, df8a, df8b, df9a, df9b, df10a, df10b, df11a, df11b, df12a, df12b, df13a, df13b, df14a, df14b, df15a, df15b, df16a, df16b, df17a, df17b, df18a, df18b, df19a, df19b, df20a, df20b, df21a, df21b, df22a, df22b, df23a, df23b, df24a, df24b]

    #print(indvframes)

    #concat frames
    ndf = pd.concat(indvframes, axis=1, sort=True)

    #print(ndf)

    #drop columns with given names
    # ndf2 = ndf.drop(['Antenna', 'SerialNumber', 'TID'], axis=1)
    #ndf2 = ndf
    #print(ndf2)

    #rename columns
    ndf.columns = ['TS', '1a', 'd', '1b', 'd', '2a', 'd', '2b', 'd', '3a', 'd', '3b', 'd', '4a', 'd', '4b', 'd', '5a', 'd', '5b', 'd', '6a', 'd', '6b', 'd', '7a', 'd', '7b', 'd', '8a', 'd', '8b', 'd', '9a', 'd', '9b', 'd', '10a', 'd', '10b', 'd', '11a', 'd', '11b', 'd', '12a', 'd', '12b', 'd', '13a', 'd', '13b', 'd', '14a', 'd', '14b', 'd', '15a', 'd', '15b', 'd', '16a', 'd', '16b', 'd', '17a', 'd', '17b', 'd', '18a', 'd', '18b', 'd', '19a', 'd', '19b', 'd', '20a', 'd', '20b', 'd', '21a', 'd', '21b', 'd', '22a', 'd', '22b', 'd', '23a', 'd', '23b', 'd', '24a', 'd', '24b']
    print(ndf)
    ndf3 = ndf.replace(to_replace = [one_a, one_b, two_a, two_b, three_a, three_b, four_a, four_b, five_a, five_b, six_a, six_b, seven_a, seven_b, eight_a, eight_b, nine_a, nine_b, ten_a, ten_b, eleven_a, eleven_b, twelve_a, twelve_b, thirteen_a, thirteen_b, fourteen_a, fourteen_b, fifteen_a, fifteen_b, sixteen_a, sixteen_b, seventeen_a, seventeen_b, eighteen_a, eighteen_b, nineteen_a, nineteen_b, twenty_a, twenty_b, twentyone_a, twentyone_b, twentytwo_a, twentytwo_b, twentythree_a, twentythree_b, twentyfour_a, twentyfour_b], value = 1 )
    #print(ndf3)
    ndf3 = ndf3.drop(['d'], axis=1)

    #print(ndf3)

    #to datetime 
    #ndf3['TS'] = pd.to_datetime(ndf3['TS'])

    #fill in datetime  
    ndf4 = ndf3.assign(TS=df['TIME_STAMP'])



    ndf4['TS'] = pd.to_datetime(ndf4['TS'])

    #sum by minute
    ndf5 = ndf4.resample('1T', base=0, on='TS').sum()



    #print(ndf5)
    print(ndf5)

    #save sheet as csv
    ndf5.to_csv(outputcsv)


# run_rfid(r"C:\Users\antho\Desktop\cappa\raw_inv\preprocessed_data_(20).csv", r"C:\Users\antho\Desktop\cappa\processed_RFID\processed.csv")