#cerner_2^5_2017
import os
import time
WIDTH = 79
#what we are printing
message = "firsthand!".upper()
#shows that each letter is 7 strings
printedMessage = [ "","","","","","","" ]
#strings that will create the characters
characters = {     " " : [ " ", " ", " ", " ", " ", " ", " " ],
	"F" : [ "*****", "*    ", "*    ", "*****", "*    ", "*    ", "*    " ],   
    "I" : [ "*****", "  *  ", "  *  ", "  *  ",	"  *  ", "  *  ", "*****" ],
    "R" : [ "**** ", "*   *", "*  * ", "* *  ", "**   ", "*  * ", "*   *" ],
	"S" : [ "*****", "*   *", "*    ", "*****", "    *", "*   *", "*****" ],
	"T" : [ "*****", "  *  ", "  *  ", "  *  ", "  *  ", "  *  ", "  *  " ],	   
	"H" : [ "*   *", "*   *", "*   *", "*****", "*   *", "*   *", "*   *" ], 
    "A" : [  "  *  ", " * * ", "*   *", "*****", "*   *", "*   *", "*   *" ], 
	"N" : [ "*   *", "**  *", "* * *", "* * *", "*  **", "*  **", "*   *" ],
    "D" : [ "**** ", "*   *", "*   *", "*   *", "*   *", "*   *", "**** " ],  
    "!" : [ "  *  ", "  *  ", "  *  ", "  *  ", "  *  ", "     ", "  *  " ] }
#since our characters are 7 stings long
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

#how far we print the message
offset = WIDTH
while True:
    os.system("cls")
    #print each line
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    #move the message a little to the left.
    offset -=1
    #restart
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    #how fast it comes back
    time.sleep(0.05)