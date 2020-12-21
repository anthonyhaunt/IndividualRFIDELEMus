Read Me 
Ivy Lab Individual Mouse Tracking Program

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

# VitalView is a trade mark of STARR Life Sciences Corporation.
# Part of this program was written to process data outputed by the VitalView included software.

Ivy Lab Individual Mouse Tracking Program (refered to after as program) consists of 4 scripts packaged as one executable file.
The Program was written for Windows 10 build 19041.685.

process_file_ui.py utilizes the tkinter library to interface with the other 3 scripts with a graphical user interface (gui). 
Variables entered into the UI as directed by text on the buttons and entry lables are passed through the other 3 scripts.
The script consists of 3 classes, one for each of the 

vvindivrun.py is appears first in the UI as My_ui_VitalViewProcess.
This script takes a directory of .csv files as an input (assuming the .csv files are in the form datetime, channel 1, 2, 3, 4... with datetime incriments less than 1 minute).
It also takes an output file name and desired output file directory.
Once inputs are received the program can be executed from the gui by clicking the button"run the program."
The program formats the table for agreement with crossreference.py and resamples the input table over 1 minute incriments.

rfidrun.py appears second as My_ui_RFID_Process. 
This script asks for a .csv file containing a table of the form: TIME_STAMP, HEX_EPC.
HEX_EPC codes must be formated as 'e0000000000000000000001a' and must correspond to the names of the channel columns with which they are associated with for example: 'e0000000000000000000001a' would correspond to mouse a from channel 1.
As it is written only channels named 1-24 a and b can be recognized.
The script expects column headers exactly as written above.
It outputs a file of the indicated file name in the indicated directory and can be run by pressing the "run the program" buttun indicated in its section in the gui.
The output is a table of each HEX_EPC name and the number of RFID hits resampled over one minute incriments. 

crossreference.py appears third as My_ui_Crossreference.
This takes input directories corresponding to vvindivrun.py outputs and rfidrun.py outputs.
It also asks for desired output directories corresponding to distance traveled in kilometers (assuming the diameter of your wheel is 11.43cm) and the statistics of how many vital view hits do not correspond with RFID hits.
It also asks for the time frame you desire to analyze in the form: %Y-%m-%d %H:%M:%S for python 3.9 and the library datetime.
The output is two files created for each day resampled from noon on the labled day to noon of the next; one file will contain stats and one file will contain distance.

