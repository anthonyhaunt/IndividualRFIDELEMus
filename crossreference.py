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
from datetime import datetime, timedelta, date
import numpy as np
import math
# import multiprocessing

# # make sure there is no overlap in datetime stamps on the files in your chosen directory
# pathvv = r"C:\Users\antho\Desktop\cappazip101520\cappa\processed_individual_vv" # use your path for the running data folder you wish to process

# # make sure there is no overlap in datetime stamps on the files in your chosen directory
# pathrfid = r"C:\Users\antho\Desktop\cappazip101520\cappa\processed_RFID" # use your path for the RFID indvrun.py output file you wish to process

# file_name_output_indvdistance_directory = r"C:\Users\antho\Desktop\cappazip101520\cappa\Outputindvtrack"  
# # use desired file name for distance in revolutions

# file_name_output_stats_directory = r"C:\Users\antho\Desktop\cappazip101520\cappa\indivdaystats"  
# # use desired file name for stats


# # Indicate your start dates and end dates in utc for your desired cage output end date is exclusive (include 1 time interval after your desired end time) example ("2020-07-24 15:08:00", "%Y-%m-%d %H:%M:%S") make  sure to set it to noon for the start so that it goes noon to noon
# start = datetime.strptime("2020-08-31 12:00:00", "%Y-%m-%d %H:%M:%S")
# end = datetime.strptime("2020-09-25 00:00:00", "%Y-%m-%d %H:%M:%S")

############### MAGIC CODE STARTS HERE DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING ####################################################################

def crossfunction(pathvv, pathrfid, start, end, distancetablebyday, statsbyday):    

    cages_to_look_at = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    
    all_files_vv = glob.glob(pathvv + "/*.csv")




    # VV
    # create list of dataframes to concat later droping uneeded indexes and renaming header to generalize

    list_of_dataframes_vv = []
    for filename in all_files_vv:
        df_vv = pd.read_csv(filename, usecols=range(25), header=0, names=['Channel_Name', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])
        list_of_dataframes_vv.append(df_vv)

    # print(list_of_dataframes)


    # contact list of dataframes (each csv file) into one dataframe
    frame_vv = pd.concat(list_of_dataframes_vv, axis=0, ignore_index=True)
    # Drop duplicates 
    frame_vv.drop_duplicates(subset="Channel_Name", inplace=True)

    # drop sensor type and channel group
    # frame.drop([0,1], inplace=True)

    # tell it what my time stamps are                                      
    frame_vv['Channel_Name'] = pd.to_datetime(frame_vv['Channel_Name'])
    frame_vv['Channel_Name'] = frame_vv['Channel_Name'].dt.strftime("%Y-%m-%d %H:%M:%S")
    print(frame_vv)

    # RFID

    all_files_rfid = glob.glob(pathrfid + "/*.csv")



    # create list of dataframes to concat later droping uneeded indexes and renaming header to generalize

    list_of_dataframes_rfid = []
    for filename in all_files_rfid:
        df_rfid = pd.read_csv(filename, usecols=range(49), header=0, names=['TS','1a','1b','2a','2b','3a','3b','4a','4b','5a','5b','6a','6b','7a','7b','8a','8b','9a','9b','10a','10b','11a','11b','12a','12b','13a','13b','14a','14b','15a','15b','16a','16b','17a','17b','18a','18b','19a','19b','20a','20b','21a','21b','22a','22b','23a','23b','24a','24b'])
        list_of_dataframes_rfid.append(df_rfid)

    # print(list_of_dataframes)


    # contact list of dataframes (each csv file) into one dataframe
    frame_rfid = pd.concat(list_of_dataframes_rfid, axis=0, ignore_index=True)
    # Drop duplicates 
    frame_rfid.drop_duplicates(subset="TS", inplace=True)

    # drop sensor type and channel group
    # frame.drop([0,1], inplace=True)

    # tell it what my time stamps are                                      
    frame_rfid['TS'] = pd.to_datetime(frame_rfid['TS'])
    frame_rfid['TS'] = frame_rfid['TS'].dt.strftime("%Y-%m-%d %H:%M:%S")

    # for timestamp in frame_rfid['TS']:
    #     frame_rfid.set_value(timestamp, 'TS', timestamp.strftime("%Y-%m-%d %H:%M:%S")) 

    print(frame_rfid)

    # distance data frames

    #need programically make all of the following dataframes by day

    # entries with datetimes individually
    datacountsindvdist = pd.DataFrame(columns=['TS','1a','1b','2a','2b','3a','3b','4a','4b','5a','5b','6a','6b','7a','7b','8a','8b','9a','9b','10a','10b','11a','11b','12a','12b','13a','13b','14a','14b','15a','15b','16a','16b','17a','17b','18a','18b','19a','19b','20a','20b','21a','21b','22a','22b','23a','23b','24a','24b'])



    data_indv_dist_zeros = np.zeros(shape=(1,48))


    # total distances
    data_indv_dist = pd.DataFrame(data_indv_dist_zeros, columns=['1a','1b','2a','2b','3a','3b','4a','4b','5a','5b','6a','6b','7a','7b','8a','8b','9a','9b','10a','10b','11a','11b','12a','12b','13a','13b','14a','14b','15a','15b','16a','16b','17a','17b','18a','18b','19a','19b','20a','20b','21a','21b','22a','22b','23a','23b','24a','24b'])


    #stats on the quality of the data

    dataqualitystatscounts_totals_zeros = np.zeros(shape=(2,24))


    #data quality totals first row is total number of vital view positive rows second row is number of positive vv rows that did not match to a positive rfid number

    dataqualitystatscounts_totals = pd.DataFrame(dataqualitystatscounts_totals_zeros, columns=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])





    # quality counts as percentages 

    dataqualitystats_zeros = np.zeros(shape=(1,24))

    dataqualitystats = pd.DataFrame(dataqualitystats_zeros, columns=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])



    #data for the distances of individuals


    #need to programnically run this for each day 


    for timestamp in frame_vv['Channel_Name']:
        #newthread(newfunction(timestamp))
        timestamp_date = pd.to_datetime(timestamp)
        if not (start <= timestamp_date <= end):
            continue

        rfidcomp = frame_rfid.loc[frame_rfid['TS'] == timestamp]
        vvcomp = frame_vv.loc[frame_vv['Channel_Name'] == timestamp]
        if rfidcomp.empty == True or vvcomp.empty == True:
            continue

        # for loop from 1 -> 24
        for channel_numbers in range(1,25):
            if channel_numbers not in cages_to_look_at:
                continue
            channel_num = str(channel_numbers)
            channel_a = channel_num + 'a'
            channel_b = channel_num + 'b'

            if channel_a not in rfidcomp.columns:
                continue
            if channel_b not in rfidcomp.columns:
                continue
            
            rfid_a = rfidcomp.iloc[0][channel_a]
            rfid_b = rfidcomp.iloc[0][channel_b]
            vvcomp_value = vvcomp.iloc[0][channel_num] * math.pi * 11.43 /100000
            vvcomp_value_half = vvcomp_value / 2.0 
            # runs every time 
            if vvcomp_value > 0 :
                dataqualitystatscounts_totals[channel_num][0] += 1

            # rfid blocks
            if rfid_a > rfid_b :
                data_indv_dist[channel_a][0] += vvcomp_value 
            
            elif rfid_a < rfid_b :
                data_indv_dist[channel_b][0] += vvcomp_value
            
            elif rfid_a == 0 and rfid_b == 0 and vvcomp_value > 0 :
                dataqualitystatscounts_totals[channel_num][1] += 1
            
            elif rfid_a == rfid_b and rfid_a != 0 :
                data_indv_dist[channel_a][0] += vvcomp_value_half
                data_indv_dist[channel_b][0] += vvcomp_value_half




    dataqualitystatscounts_totals.insert(0, "Description", ["total vv counts", "vv counts without RFID"], True)    
    data_indv_dist.insert(0, "Description", ["distance in km"], True)  

    print(dataqualitystatscounts_totals)
    print(data_indv_dist)

    dataqualitystatscounts_totals.to_csv(statsbyday)

    data_indv_dist.to_csv(distancetablebyday)


#END OF CROSS FUNCTION



# crossfunction(start, end, file_name_output_indvdistance, file_name_output_stats)

# modified_date = date + timedelta(days=1)
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def multi(pathvv, pathrfid, file_name_output_indvdistance_directory, file_name_output_stats_directory, start, end):
    start_datetime = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    # Using Pool to limit the number of prcesses created to the CPU count of machine - 1
    # print("Number of CPU cores on this machine:" + str(multiprocessing.cpu_count()))
    # pool = multiprocessing.Pool(processes=multiprocessing.cpu_count() - 1)
    # processes = []
    for start_day_date in daterange(start_datetime, end_datetime):
        daynamestats = file_name_output_indvdistance_directory +"\indivstats" + start_day_date.strftime("%Y-%m-%d") + ".csv"
        daynamedistance = file_name_output_stats_directory +"\indivdistance" + start_day_date.strftime("%Y-%m-%d") + ".csv"
        print(daynamedistance)
        print(daynamestats)
        end_day_date = start_day_date + timedelta(days=1)
        print(" start: " + start_day_date.strftime("%Y-%m-%d %H:%M:%S") + " end: " +end_day_date.strftime("%Y-%m-%d %H:%M:%S"))
        crossfunction(pathvv, pathrfid, start_day_date, end_day_date, daynamedistance, daynamestats)
        # pool.apply_async(crossfunction, args=(pathvv, pathrfid, start_day_date, end_day_date, daynamedistance, daynamestats,))
        # To use Process function uncomment bellow
        # p = multiprocessing.Process(target=crossfunction, args=(pathvv, pathrfid, start_day_date, end_day_date, daynamedistance, daynamestats,))
        # processes.append(p)

    # for each in processes:
    #     each.start()
        
    # for each in processes:
    #     each.join()

    # pool.close()
    # pool.join()
    print('done')
