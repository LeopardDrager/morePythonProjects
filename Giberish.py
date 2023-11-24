import random 



responce = int(input("How much gibberish would you like? "))

numberOfGib = 0 

final = []


while numberOfGib < responce:   
    excluded_numbers = [0,1,2,3,4,5,6,7,8,9,10,11]
    number = random.choice([i for i in range(0,126) if i not in excluded_numbers])
    numberOfGib+= 1
    final.extend([chr(number)])
    


while True: 
    print(''.join(final))   
