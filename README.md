# cropQR
cropQR - will be useful if you have a large number of QR codes that need to be quickly decoded into text. This script only works with .png files.


This script has several dependencies:
1. pyzbar
   install:
   sudo apt-get install libzbar0
   pip install pyzbar
   
2. PIL
   install:
   pip install pillow
   
3. glob
   install:
   pip3 install glob2


Instructions for use:
This script must be placed in the folder with .png files containing QR codes. The script will go through all .png files located inside the folder.

Parameters and arguments:
--help - list all arguments
--here - start decoding without specifying a path
--silent - decode decoding is not accompanied by output to the terminal
