import random
import string
import subprocess

website = input("What website are you using this password for? ")
command = "chmod 600 passwords.txt"

username_length = int(input("How many characters do you want in your username? "))
username_characters = string.ascii_letters + string.digits  # possible characters
username = ''.join(random.choice(username_characters) for _ in range(username_length))



upperCaseAmount = 0
lowerCaseAmount = 0
numberCaseAmount = 0
specialCaseAmount = 0

# used this for acsii values https://www.johndcook.com/blog/2022/05/28/how-to-memorize-the-ascii-table/
# used this for things I could do with random https://pynative.com/python-random-randrange/
print ("The next few questions will be asking you how many of each character you want in your password.")
upperCaseInput=int(input(("How many uppercase letters do you want? ")))
lowerCaseInput=int(input(("How many lowercase letters do you want? ")))
numberCaseInput=int(input(("How many numbers do you want? ")))
specialCaseInput=int(input(("How many special characters do you want? ")))


final = []

while upperCaseAmount < upperCaseInput: 
    
        upperCase = random.randint(65, 90)
        upperCaseAmount = upperCaseAmount + 1
        final.extend([chr(upperCase)])

while lowerCaseAmount < lowerCaseInput:    

        lowerCase = random.randint(97, 122)
        lowerCaseAmount = lowerCaseAmount + 1
        final.extend([chr(lowerCase)])

while numberCaseAmount < numberCaseInput:
        numberCase = random.randint(48, 57)
        numberCaseAmount = numberCaseAmount + 1
        final.extend([chr(numberCase)])

while specialCaseAmount < specialCaseInput:
        #used github copilot for this part
        excluded_numbers = [34,39,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93] #used this cause I didn't wanna type out all the numbers https://numbergenerator.org/numberlist/1-64#!low=43&high=64&csv=csv&oddeven=&step=1&addfilters=
        number = random.choice([i for i in range(32, 65) if i not in excluded_numbers])
        specialCaseAmount = specialCaseAmount + 1
        final.extend([chr(number)])        

       
        
random.shuffle(final)



print(f"Generated username: {username}")
print("Your password is "+''.join(final))

with open ("passwords.txt", "a+") as file:
    file.write("\n"+website+" | "+username+" | "+''.join(final))
    file.close()
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result)



        