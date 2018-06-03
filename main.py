#!/usr/bin/env python3
# coding: utf-8

"""
ISODATA-python
ISODATA image classifier in Python
Author:     Lucka
Version:    0.1.3
License:    MIT
"""

# Command line options
optionsHelp = """Command line options:
    \033[1m   --input\t<filename>\033[0m\tFilename of input image
    \033[1m   --output\t<filename>\033[0m\tFilename of output image
    \033[1m   --rgb\t\t\033[0m\tProcess image in RGB
    \033[1m   --gray\t\t\033[0m\tProcess image in grayscale (Default)
    \033[1m   --K\t<number>\033[0m\tThe number of expected clusters
    \033[1m   --TN\t<number>\033[0m\tMininum of sample in one cluster
    \033[1m   --TS\t<number>\033[0m\tStandard deviation
    \033[1m   --TC\t<number>\033[0m\tMininum of distance between two clusters
    \033[1m   --L\t<number>\033[0m\tMaxinum of merging during every iteration
    \033[1m   --I\t<number>\033[0m\tMaxinum of iteration
    \033[1m-h --help\033[0m\t\t\tDisplay this help text
"""

# Modules
import sys, getopt, time
from PIL import Image
import numpy
import matplotlib.pyplot as plot
import ISODATAKit

def main():
    # Process the command line parameters
    try:
        opts, args = getopt.getopt(sys.argv[1:],
            "h",
            ["help", "input=", "output=",
             "rgb", "gray",
             "K=", "TN=", "TS=", "TC=", "L=", "I="])
    except getopt.GetoptError as error:
        print("Error: {error}".format(error = error))
        print(optionsHelp)
        exit()

    print(__doc__)
    if len(opts) == 0:
        print("Command line options are required.")
        print(optionsHelp)
        exit()

    inputFilename = ""
    outputFilename = ""
    isRGB = False
    argvK = 3
    argvTN = 3
    argvTS = 4.0
    argvTC = 40
    argvL = 10
    argvI = 8

    for opt, argv in opts:
        if opt in ("-h", "--help"):
            print(optionsHelp)
            return

        elif opt in ("--input"):
            inputFilename = argv

        elif opt in ("--output"):
            outputFilename = argv

        elif opt in ("--rgb"):
            isRGB = True

        elif opt in ("--gray"):
            isRGB = False

        elif opt in ("--K"):
            argvK = int(argv)

        elif opt in ("--TN"):
            argvTN = int(argv)

        elif opt in ("--TS"):
            argvTS = float(argv)

        elif opt in ("--TC"):
            argvTC = float(argv)

        elif opt in ("--L"):
            argvL = int(argv)

        elif opt in ("--I"):
            argvI = int(argv)

        else:
            print("The option \`{opt}\` is invalid.".format(opt))
            print(optionsHelp)

    if inputFilename == "":
        print("Input filename undefined, use --input.")
        exit()
    if outputFilename == "":
        print("Output filename undefined, use --output.")
        exit()

    if isRGB:
        image = Image.open(inputFilename)
        result = ISODATAKit.doISODATARGB(image, argvK, argvTN, argvTS, argvTC, argvL, argvI)
        plot.figure("Result")
        plot.imshow(result)
        plot.show()
    else:
        image = Image.open(inputFilename).convert("L")
        result = ISODATAKit.doISODATAGray(image, argvK, argvTN, argvTS, int(argvTC), argvL, argvI)
        plot.figure("Result")
        plot.imshow(result, cmap = "gray")
        plot.show()

    result.save(outputFilename)


if __name__ == '__main__':
    main()
