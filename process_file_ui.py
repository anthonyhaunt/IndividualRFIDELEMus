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


import tkinter as tk
import tkinter.filedialog as fd
import rfidrun
import os
import vvindvrun
import crossreference
# import multiprocessing


# Code to add widgets will go here...

if __name__ == "__main__":
   top = tk.Tk()


   class My_ui_VitalViewProcess:

      def __init__(self):
         
         inputbutton = tk.Button(top, text="select input Vital View .csv", command=self.browseinput)
         # inputbutton2 = tk.Button(top, text="select input RFID .csv", command=self.browseinput2)

         
         outputbutton = tk.Button(top, text="select output directory", command=self.browseoutput)
         
         tk.Label(top, text="Vital View Processing").grid(row=1, pady = 12)
         
         inputbutton.grid(row=2, column=0)
         # inputbutton2.grid(row=3, column=0)
         outputbutton.grid(row=4, column=0)
      

         tk.Label(top, text="Output file name as form: filename").grid(row=5)
         # tk.Label(top, text="Output Quality Percentage file name as form: filename.csv").grid(row=6)
         # tk.Label(top, text="Start Date as form:").grid(row=7)
         # tk.Label(top, text="End Date as form:").grid(row=8)

         # e1 = tk.Entry(top)
         # e2 = tk.Entry(top)

         # e1.grid(row=7, column=1)
         # e2.grid(row=8, column=1)


         self.output = tk.Entry(top)


         self.output.grid(row=5, column=1)

         # eoutput2 = tk.Entry(top)


         # eoutput2.grid(row=6, column=1)

         # tk.Label(top, text="Daily cycle start time (24hr clock) as form: HH").grid(row=9)
         # ecyclestart = tk.Entry(top)
         # ecyclestart.grid(row=9, column=1)


         runbutton = tk.Button(top, text="run the program", command=self.vitalviewprocess)
         runbutton.grid(row=10, column=0)


      def browseinput(self):
         self.directoryin = fd.askdirectory()
         tk.Label(top,text= self.directoryin).grid(row=2, column=1)

      # def browseinput2(self):
      #    filein2 = fd.askopenfilename()
      #    tk.Label(top,text= filein2).grid(row=3, column=1)

      def browseoutput(self):
         self.fileoutdirectory = fd.askdirectory()
         tk.Label(top,text= self.fileoutdirectory).grid(row=4, column=1)
      
      def vitalviewprocess(self):
         print("run vital view Processs")
         new_path_vv = os.path.join(self.fileoutdirectory, self.output.get() + ".csv")
         print(new_path_vv)
         vvindvrun.vvrun(self.directoryin, new_path_vv)

   class My_ui_RFID_Process:

      def __init__(self):
         
         #inputbutton = tk.Button(top, text="select input Vital View .csv", command=self.browseinput)
         inputbutton2 = tk.Button(top, text="select input for RFID process .csv", command=self.browseinput2)

         
         outputbutton = tk.Button(top, text="select output directory", command=self.browseoutput)
         
         tk.Label(top, text="RFID Processing").grid(row=11, pady = 12)
         
         #inputbutton.grid(row=12, column=0)
         inputbutton2.grid(row=13, column=0)
         outputbutton.grid(row=14, column=0)
   

         tk.Label(top, text="Output file name as form: filename").grid(row=15)
         #tk.Label(top, text="Output Quality Percentage file name as form: filename.csv").grid(row=16)
         #tk.Label(top, text="Start Date as form:").grid(row=17)
         #tk.Label(top, text="End Date as form:").grid(row=18)

      # e1 = tk.Entry(top)
      # e2 = tk.Entry(top)

         #e1.grid(row=17, column=1)
         #e2.grid(row=18, column=1)


         self.output = tk.Entry(top)


         self.output.grid(row=15, column=1)

         #eoutput2 = tk.Entry(top)


         #eoutput2.grid(row=16, column=1)

         # tk.Label(top, text="Daily cycle start time (24hr clock) as form: HH").grid(row=19)
         # ecyclestart = tk.Entry(top)
         # ecyclestart.grid(row=19, column=1)


         runbutton = tk.Button(top, text="run the program", command=self.rfidprocess)
         runbutton.grid(row=20, column=0)


      # def browseinput(self):
      #    filein = fd.askopenfilename()
      #    tk.Label(top,text= filein).grid(row=12, column=1)

      def browseinput2(self):
         self.filein2 = fd.askopenfilename()
         tk.Label(top,text= self.filein2).grid(row=13, column=1)

      def browseoutput(self):
         self.fileoutdirectory = fd.askdirectory()
         tk.Label(top,text= self.fileoutdirectory).grid(row=14, column=1)



      
      def rfidprocess(self):
         print("run rfid Processs")
         new_path_rfid = os.path.join(self.fileoutdirectory, self.output.get() + ".csv")
         print(new_path_rfid)
         rfidrun.run_rfid(self.filein2, new_path_rfid)


   class My_ui_Crossreference:

      def __init__(self):
         
         inputbutton = tk.Button(top, text="select input Vital View directory", command=self.browseinput)
         inputbutton2 = tk.Button(top, text="select input RFID directory", command=self.browseinput2)

        
         outputbutton = tk.Button(top, text="select output directory for quality stats", command=self.browseoutput)
         outputbutton2 = tk.Button(top, text="select output directory for distance", command=self.browseoutput2)

         tk.Label(top, text="Cross Reference Vital View Data with RFID Data").grid(row=21, pady = 12)
         
         inputbutton.grid(row=22, column=0)
      
         inputbutton2.grid(row=23, column=0)
         outputbutton.grid(row=25, column=0)
         outputbutton2.grid(row=24, column=0)

         tk.Label(top, text="Start Date as form: %Y-%m-%d %H:%M:%S -- as an example: 2020-07-24 15:08:00").grid(row=27)
         tk.Label(top, text="End Date as form: %Y-%m-%d %H:%M:%S -- as an example: 2020-07-24 15:08:00").grid(row=28)

         self.start = tk.Entry(top)
         self.end = tk.Entry(top)


         self.start.grid(row=27, column=1)
         self.end.grid(row=28, column=1)


         # tk.Label(top, text="Daily cycle start time (24hr clock) as form: HH").grid(row=29)
         # ecyclestart = tk.Entry(top)
         # ecyclestart.grid(row=29, column=1)


         runbutton = tk.Button(top, text="run the program", command=self.crossreference)
         runbutton.grid(row=30, column=0)


      def browseinput(self):
         self.filein = fd.askdirectory()
         tk.Label(top,text= self.filein).grid(row=22, column=1)

      def browseinput2(self):
         self.filein2 = fd.askdirectory()
         tk.Label(top,text= self.filein2).grid(row=23, column=1)

      def browseoutput(self):
         self.fileoutdirectory = fd.askdirectory()
         tk.Label(top,text= self.fileoutdirectory).grid(row=25, column=1)

      def browseoutput2(self):
         self.fileoutdirectory2 = fd.askdirectory()
         tk.Label(top,text= self.fileoutdirectory2).grid(row=24, column=1)

      
      def crossreference(self):
         print("run crossreference")
         crossreference.multi(self.filein, self.filein2, self.fileoutdirectory, self.fileoutdirectory2, self.start.get(), self.end.get())




   my_My_ui_VitalViewProcess = My_ui_VitalViewProcess()
   my_My_ui_RFID_Process = My_ui_RFID_Process()

   my_My_ui_Crossreference= My_ui_Crossreference()

   top.mainloop()

