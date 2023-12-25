# Kartik Vanjani
# Password Generator Project
# Elements Involved: Conditionals, Loops, Arrays, Strings, Rnadom Library

#import libraries
import string
import random


def password():
    # List of elements to choose from and the password array
    list = ""
    password = []
    
    x = int(input('Enter the desired password length: '))  # Desired password length based on user input
    
    # If the length is not valid, or negative, use a while loop to prompt the user to enter a valid length until it is positive
    while x<0:
        x = int(input('Error: Enter a positive length: '))
    
    # Ask the user what password they would like based on the guidelines of the website they want to make a password for
    print('(a) Only Numbers (Weak Password)')
    print('(b) Only Letters (Weak Password)')
    print('(c) Numbers, Letters, and Special Characters (Strong Password)')
    print('(d) Custom phrase in password and random after that (Strong Password')
    choice = input('Which type of password would you like? ') #input

    # if the choice is not one of a, b, c, or d, prompt the user for one of those choices till a selection of one of those is made
    while choice not in ["a","b","c","d"]:
        choice = input('Error: Enter a, b, c, or d: ')
    
    # if the choice is a
    if choice == "a":
         list = list + string.digits  #add to the list digits
    
    # if the choice is b
    elif choice == "b":
         list = list + string.ascii_letters #add to the list letters
   
    # if the choice is c
    elif choice == "c":
        list = list + string.ascii_letters  # letters
        list += string.digits    # digits
        list += string.punctuation   # special characters
    
    # if choice is d
    elif choice == "d":
        phrase = input('Enter the phrase you would like in the password: ')  #ask user for phrase
        password+=phrase  #add it to the password array
        x = x - len(phrase)  #change the length since the length of the password now is only the length of the remaining characters after including the phrase
        list += string.digits  #digits
        list += string.punctuation #special characters
    
    for i in range (x): #loop to x
        y = random.choice(list)  #choose randonly from the list
        password.append(y)  #add this random element from the list to the array
    print('Your password is: ' +  "".join(password))  #print out the password, and use .join to make the array a string. 
    # if the choice is d, it will join the phrase and the rest of the random elements from the digits and special characters

# main function to run the program
def main():
    password()

# call the main function
if __name__ == '__main__':
    main()

