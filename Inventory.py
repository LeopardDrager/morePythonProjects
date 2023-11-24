
#Please make sure you have a text file named Inventory.txt in the same directory/folder as this script.
#or it should auto make one, but I'm not 100% sure. 
file = open("Inventory.txt" , "a+")
file.seek(0)
print(file.read())

i = 0

numInput=int(input("How many things are you going to input? "))

while i < numInput:

    deviceName=input("Device Name ")
    deviceType=input("Device Type ")
    deviceLocation=input("Device Location ")
    deviceStaticIP=input("Device Static IP ")
    i+= 1

    file.write( "\n" +deviceName+' | '+ deviceType+' | '+deviceLocation+' | '+ deviceStaticIP)
file.close()