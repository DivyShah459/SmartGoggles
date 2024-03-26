#First take the Braille input as a string. This output will be from our machine learning algorithm 
# and it will be in UEF
braillestring = input("Enter Braille: ")

#Braille dictionary for letters. Credit: https://abcbraille.com/braille
brailleletterdict = {"⠟": "q", "⠺":"w", "⠑":"e", "⠗":"r", "⠞":"t", "⠽":"y", "⠥":"u", 
               "⠊":"i","⠕":"o","⠏":"p","⠁":"a","⠎":"s","⠙":"d","⠋":"f","⠛":"g",
               "⠓":"h","⠚":"j","⠅":"k","⠇":"l","⠵":"z","⠭":"x","⠉":"c","⠧":"v",
               "⠃":"b","⠝":"n","⠍":"m",
               "⠹": "th", "⠡": "ch", "⠱":"wh", "⠣":"gh", "⠜":"ar", "⠪":"ow", "⠳":"ou", "⠷":"of", 
               "⠔":"in", "⠫":"ed", "⠢":"en", "⠻":"er", "⠌":"st", "⠿":"for", "⠾":"with", "⠮":"the", "⠩": "sh", "⠲": ".", "⠀": " ", " ": " ", "⠂": ","}

#Braille dictionary for numbers. Credit: https://abcbraille.com/braille
braillenumberdict = {"⠀": " ", "⠁": "1", "⠃":"2", "⠉":"3", "⠙":"4", "⠑":"5", "⠋":"6", "⠛":"7", "⠓":"8", "⠊":"9", "⠚":"0", " ": " "}

numberflag = 0
fullupperflag = 0
onlyletterupperflag = 0
englishstring = ""

#loop for translating code
for i in range(len(braillestring)):
    #checking if it is a number
    if braillestring[i] == "⠼":
        numberflag = 1
        continue
    #checks for letters -- especially capital letters
    elif braillestring[i] == "⠠":
        numberflag = 0
        onlyletterupperflag = 1
        if i > 0 and braillestring[i-1] == "⠠":
            fullupperflag = 1
        continue
    #if the number flag is not there, go to the numbers dictionary
    if numberflag == 0:
        if onlyletterupperflag == 1 or fullupperflag == 1:
            englishstring += brailleletterdict[braillestring[i]].upper()
        else:
            englishstring += brailleletterdict[braillestring[i]]
        if braillestring[i] != "⠠":
            onlyletterupperflag = 0
    #otherwise look at the dictionary with numbers
    else:
        #add each translated character to the final string
        englishstring += braillenumberdict[braillestring[i]]
    #print(englishstring)
#Print the final string: 
print(f"Final English String: {englishstring}")
    