
    
height = int(input("Input the height you would like for the pyramid!"))
for i in range (height):
    print(' ' * (height - i - 1) + "#" * (i + 1) + ' ' + "#" * (i+1))