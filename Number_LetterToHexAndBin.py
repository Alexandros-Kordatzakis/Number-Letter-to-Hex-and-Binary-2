
import time


while True: 

    user_input = input("Enter a letter: ")
    letter_as_num = ord(user_input)

 
    time.sleep(1)
    print("Decimal: {:d}".format(letter_as_num))
    print("Hexadecimal: {:02x}".format(letter_as_num))
    time.sleep(0.76)
    print("************************************")
    time.sleep(1)

 