import os

morse = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9"
}

def morseToWords(sentence):
    letters = sentence.split(" / ")
    
    word = ""
    for i in letters:
        splitspace = i.split(" ")
        for i in splitspace:
            if i not in morse:
                word += "*"
                continue
            word += morse.get(i)
        word += " "
    return word

sentence = input("Write Morse using dots and dashes with / as space between words: ")

print(morseToWords(sentence))
