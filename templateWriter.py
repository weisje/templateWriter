###############################################################################
# Import Name: templateWriter.py
# Version: 1.0
# First Development Date: 27th December 2019 (27/12/2019)
# Last Development Date: 27th December 2019 (27/12/2019)
# Program Name: "Python Comment Template Writer"
# Developer: John Weis
# Purpose: For the generation of Python commenting standards without the need or
# risk of overwriting existing comment Templates.
###############################################################################

#*IMPORT BLOCK BEGIN* (27/12/2019 -JW)
from datetime import date
from os import path

import datetime
import os
#import sys
import time
#*IMPORT BLOCK END* (27/12/2019 -JW)

#*GLOBAL VARIABLE BLOCK BEGIN*
latestDevelopmentDate = "27th December 2019 (27/12/2019)"
versionNum = 1.0
#*GLOBAL VARIABLE BLOCK END*

#*LAMBDA BLOCK BEGIN* (27/12/2019 -JW)
clear = lambda: os.system('cls')
sleep = lambda duration = 2: time.sleep(duration)
todayNum = lambda: date.today().strftime("%d/%m/%Y")
todayReadable = lambda: date.today().strftime("%d %B %Y")
#*LAMBDA BLOCK END* (27/12/2019 -JW)


#*FUNCTION BLOCK BEGIN* (27/12/2019 -JW)

# # Function description
# def foo():
#
#     #**VARIABLE BLOCK BEGIN**
#
#     #**VARIABLE BLOCK END**
#
#     pass

# Main writer for the program.  Does the heavy lifting by taking the user's inputs and generating a .py template for their usage.
def writer(stringFilename, stringProgramName, stringDeveloperName, stringPurpose):

    #**VARIABLE BLOCK BEGIN**
    filename = stringFilename
    defaultFilename = 'defaultFilename.py'
    versionNumber = 0.1
    firstDevelopmentDateReadable = todayReadable()
    firstDevelopmentDateNum = todayNum()
    latestDevelopmentDateReadable = todayReadable()
    latestDevelopmentDateNum = todayNum()
    programName = stringProgramName
    developerName = stringDeveloperName
    purpose = stringPurpose
    #**VARIABLE BLOCK END**

    if not filename.strip():
        filename = defaultFilename
    else:
        filename = filename + ".py"

    if path.exists(filename):
        print("\nFile \'%s\' already exists.  Exiting Template Writer" % filename)
    else:
        fileWriter = open(filename, "w+")
        write = lambda input: fileWriter.write(input)
        write('#' * 79)
        write('\n# Import Name: %s\n# Version: %.1f' % (filename, versionNumber))
        write('\n# First Development Date: %s (%s)' % (str(firstDevelopmentDateReadable), str(firstDevelopmentDateNum)))
        write('\n# Latest Development Date: %s (%s)' % (str(latestDevelopmentDateReadable), str(latestDevelopmentDateNum)))
        write('\n# Purpose: %s' % purpose)
        write('\n' + '#' * 79)
        write('\n')
        write('\n#*IMPORT BLOCK BEGIN*\n')
        write('\n#import datetime\n#import os\n#import sys\n#import time\n')
        write('\n#*IMPORT BLOCK END*\n')
        write('\n#*GLOBAL VARIABLE BLOCK BEGIN*\n')
        write('\nlatestDevelopmentDate = \'%s (%s)\'' % (str(latestDevelopmentDateReadable), str(latestDevelopmentDateNum)))
        write('\n#*GLOBAL VARIABLE BLOCK END*\n')
        write('\n#*LAMBDA BLOCK BEGIN*\n')
        write('\n#clear = lambda: os.system(\'cls\')\n#sleep = lambda seconds = 2: time.sleep(seconds)\n')
        write('\n#*LAMBDA BLOCK END*\n')
        write('\n#*FUNCTION BLOCK BEGIN*\n')
        write('\n## Function Description\n# def foo():\n#\n#\t#**VARIABLE BLOCK BEGIN**\n\n#\t#**VARIABLE BLOCK END**\n#\n#\tpass\n')
        write('\n## Displays information about the program when about() is called.  Prints information to console.\n# def about():\n#\n#\t#**VARIABLE BLOCK BEGIN**\n')
        write('#\timportName = \'%s\'\n#\tversionNum = %.1f' % (filename, versionNumber))
        write('\n#\tfirstDevelopmentDate = \'%s (%s)\'' % (str(firstDevelopmentDateReadable), str(firstDevelopmentDateNum)))
        write('\n#\tlatestDevelopmentDate = latestDevelopmentDate')
        write('\n#\tprogramName = \'%s\'\n#\tDeveloper =  \'%s\'' % (programName, developerName))
        write('\n#\t#**VARIABLE BLOCK END**\n')
        write('\n#\tprint(\"\\nProgram Name: %s\\nVersion Number: %.1f\" % (programName, versionNum))')
        write('\n#\tprint(\"latestDevelopmentDate: %s\" % (latestDevelopmentDate))\n')
        write('#\tprint(\"Developer: %s\" % developerName)\n')
        write('#\t#sleep(2)\n')
        write('\ndef main():\n\n\t#**VARIABLE BLOCK BEGIN**\n\n\t#**VARIABLE BLOCK END**\n\n\tpass\n')
        write('\n#*FUNCTION BLOCK END*\n')
        write('\nif __name__ == \'__main__\':\n\tmain()\n')
        write('\n' + '#' * 79)
        write('\n# Notes:\n#')
        write('\n' + '#' * 79)

        fileWriter.close()

        print("Filename: %s\nVerson Number: %.1f" %(filename, versionNumber))
        print("First Development Date: %s (%s)" % (str(firstDevelopmentDateReadable), str(firstDevelopmentDateNum)))
        print("Latest Development Date: %s (%s)" % (str(latestDevelopmentDateReadable), str(latestDevelopmentDateNum)))
        print("Developer: %s\nProgram Name: %s" % (developerName, programName))
        print("Purpose: %s" % purpose)

# For the proper sanitization of an inputed string.  Removes illegal spaces/characters from input and returns as a string.  Expected input: "fadsfGSDF4/'//dfdfgdf" Expected output: fadsfGSDF4dfdfgdf (27/12/2019 -JW)
def stringSanitizer(inputString):

    #**VARIABLE BLOCK BEGIN**
    inputString = inputString
    processString = ''
    illegalCharacters = ['*','\"', '.', '\\', '\'', '/', '[', ']', '{', '}', ':', ';', '|', ',', '!', '@', '#', '$', '%', '^', '&', '(', ')', '<', '>', '?', '~', '\`', '+', '=']
    sanitizedString = ""
    #**VARIABLE BLOCK END**

    for character in illegalCharacters:
        inputString = inputString.replace(character, '')

    sanitizedString = inputString
    return sanitizedString

# Displays information about the program when it is called. Prints information to console.
def about():

    #**VARIABLE BLOCK BEGIN** (27/12/2019 -JW)
    importName = "templateWriter.py"
    global versionNum
    firstDevelopmentDate = "27th December 2019"
    global latestDevelopmentDate
    programName = "\"Python Comment Template Writer\""
    developer = "John Weis"
    purpose = "For the generation of Python commenting standards without the need or risk of overwriting existing comment Templates"
    #**VARIABLE BLOCK END** (27/12/2019 -JW)

    clear()

    print("\nProgram Name: %s\nVersion Number: %.1f" % (programName, versionNum))
    print("Developer: %s\nLatest Develoment Date: %s" % (developer, latestDevelopmentDate))
    print("Purpose: %s" % purpose)

    sleep(2)

def main():

    #**VARIABLE BLOCK BEGIN** (27/12/2019 -JW)
    UserInputfileName = ""
    global versionNum
    UserInputprogramName = ""
    UserInputdeveloperName = ""
    UserInputpurpose = ""
    #**VARIABLE BLOCK END** (27/12/2019 -JW)

    clear()

    print("Welcome to Python Comment Template Writer v%.1f!\n" % versionNum)

    sleep(1)

    UserInputfileNameTemp = input("Enter filename for program without file extension(i.e. \'01_templateWriter\'):\n")
    UserInputfileName = stringSanitizer(UserInputfileNameTemp)
    UserInputprogramName = input("Enter the program's name(i.e. \'Template Writer\'):\n")
    UserInputdeveloperName = input("Enter the developer's name:\n")
    UserInputpurpose = input("Enter purpose of this program:\n")

    writer(UserInputfileName, UserInputprogramName, UserInputdeveloperName, UserInputpurpose)


#FUNCTION BLOCK END* (27/12/2019 -JW)

if __name__ == '__main__':
    main()

###############################################################################
# Notes:
# (27/12/2019 -JW) Initial development of program.  Seems to function properly as
# an initial template generator, so upgrading to version number 1.0
###############################################################################
