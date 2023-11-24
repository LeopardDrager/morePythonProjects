import ipaddress

while True:
    ip=input("Enter an IP address ")
    try:
        #ipaddress.ip_address(takes in an string that should be a valid IP address)
        print(ipaddress.ip_address(ip))
        print("Valid IP address")
    except:
        print("Invalid IP address")
    finally:
        if ip == "q":
            print("stopped")
            break