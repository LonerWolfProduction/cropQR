#python3
from PIL import Image
from pyzbar.pyzbar import decode
import string
import sys
import glob

visible_out = 1
if __name__ == "__main__":
    if len (sys.argv) == 1:
        print ("if you need help, you need to use the --help (-h) command")
    else:
        param_name = sys.argv[1]

        if (param_name == "--help" or
                param_name == "-h"):
            print ("Launch parameters and arguments:\n--help (-h) : Arguments and launch parameters\n--here (-H) : Perform decoding inside the current folder")
            sys.exit (1)

        if len (sys.argv) < 2:
            print ("if you need help, you need to use the --help (-h) command")
            sys.exit (1)

        if len (sys.argv) > 3:
            print ("if you need help, you need to use the --help (-h) command")
            sys.exit (1)

        if len (sys.argv) == 3:
            if str(sys.argv[2]) == "--silent":
                visible_out = 0

        if (param_name == "--here" or
                param_name == "-H" or
                param_value == "--here" or
                param_value == "H"):
            url1 = "qr ("
            url2 = ").png"
            fout = open("cropQRdata.txt", "a")
            for file in glob.glob(r'*.png'):
                name = file
                result = str(decode(Image.open(name)))
                outdata = str(result)
                if visible_out == 1: print (outdata)
                fout.write(outdata + "\n")
            fout.close()
        else:
            print ("if you need help, you need to use the --help (-h) command")
            sys.exit (1)
