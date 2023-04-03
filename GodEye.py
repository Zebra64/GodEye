import socket
import os
from os import system
import time
import whois


system("title " + 'GodEye by Zebra')
os.system('color 0f')

os.system('cls')
print(
    """\033[1;32m


                                ░██████╗░░█████╗░██████╗░███████╗██╗░░░██╗███████╗
                                ██╔════╝░██╔══██╗██╔══██╗██╔════╝╚██╗░██╔╝██╔════╝
                                ██║░░██╗░██║░░██║██║░░██║█████╗░░░╚████╔╝░█████╗░░
                                ██║░░╚██╗██║░░██║██║░░██║██╔══╝░░░░╚██╔╝░░██╔══╝░░
                                ╚██████╔╝╚█████╔╝██████╔╝███████╗░░░██║░░░███████╗
                                ░╚═════╝░░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝
                                By Zebra
    """
)
time.sleep(4)

while True:
    os.system('cls')
    os.system('color 0f')

    

    print("Choose menu:")

    print(
    """
    [01] Website
    
    """)

    choose = int(input())

    os.system('cls')

    if choose == 1:
        print("Choose Option:")

        print(
        """
        [01] Domain Availability
        [02] Domain Creation Information
        [03] Domain E-mails
        [04] Domain Geolocation
        [05] Domain Ip-adres\n
        Experimental:
        [06] Domain/Ip Open Ports (Slow / 1s - port)
        """)
        choose2 = int(input())
        
        if choose2 == 6:
            os.system('cls')
            print("\nEnter Domain: ")
            domain1 = str(input())
            
            def is_registered(domain_name):
                """
                A function that returns a boolean indicating 
                whether a `domain_name` is registered
                """
                try:
                    w = whois.whois(domain_name)
                except Exception:
                    return False
                else:
                    return bool(w.domain_name)
            
            if is_registered(domain1) == True:
                
                try:
     
                    # will scan ports between 1 to 65,535
                    for port in range(1,65535):
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        socket.setdefaulttimeout(1)
                        
                        # returns an error indicator
                        result = s.connect_ex((domain1,port))
                        if result ==0:
                            print("Port {} is open".format(port))
                        s.close()
                        

                        
                except KeyboardInterrupt:
                        print("\n Exiting Program !!!!")
                        print("\nPress Enter To Continue")
                        input()
                        continue
                except socket.gaierror:
                        print("\n Hostname Could Not Be Resolved !!!!")
                        print("\nPress Enter To Continue")
                        input()
                        continue
                except socket.error:
                        print("\ Server not responding !!!!")
                        print("\nPress Enter To Continue")
                        input()
                        continue
                
                print("\nPress Enter To Continue")
                input()
                continue
                
            else:
                print("\nUnknown Domain")
                print("\nPress Enter To Continue")
                input()
                continue
        
        if choose2 == 5:
            os.system('cls')
            print("\nEnter Domain: ")
            domain1 = str(input())
            
            def is_registered(domain_name):
                """
                A function that returns a boolean indicating 
                whether a `domain_name` is registered
                """
                try:
                    w = whois.whois(domain_name)
                except Exception:
                    return False
                else:
                    return bool(w.domain_name)
            
            if is_registered(domain1) == True:
                
                print(domain1 + ' IP = ' + socket.gethostbyname(domain1))
                
                print("\nPress Enter To Continue")
                input()
                continue
                
            else:
                print("\nUnknown Domain")
                print("\nPress Enter To Continue")
                input()
                continue
        
        if choose2 == 4:
            os.system('cls')
            print("\nEnter Domain: ")
            domain1 = str(input())
            
            def is_registered(domain_name):
                """
                A function that returns a boolean indicating 
                whether a `domain_name` is registered
                """
                try:
                    w = whois.whois(domain_name)
                except Exception:
                    return False
                else:
                    return bool(w.domain_name)
            
            if is_registered(domain1) == True:
                
                w = whois.whois(domain1)
                
                print("\nDnssec: " + str(w.dnssec))
                print("Name: " + str(w.name))
                print("Org: " + str(w.org))
                print("Adress: " + str(w.address))
                print("State: " + str(w.state))
                print("Registrant postal code: " + str(w.registrant_postal_code))
                print("Country: " + str(w.country))
                
                
                
                print("\nPress Enter To Continue")
                input()
                continue
            
            else:
                print("\nUnknown Domain")
                print("\nPress Enter To Continue")
                input()
                continue
        
        if choose2 == 3:
            os.system('cls')
            print("\nEnter Domain: ")
            domain1 = str(input())
            
            def is_registered(domain_name):
                """
                A function that returns a boolean indicating 
                whether a `domain_name` is registered
                """
                try:
                    w = whois.whois(domain_name)
                except Exception:
                    return False
                else:
                    return bool(w.domain_name)
            
            if is_registered(domain1) == True:
                
                w = whois.whois(domain1)
                
                print(w.emails)
                
                print("\nPress Enter To Continue")
                input()
                continue
            
            else:
                print("\nUnknown Domain")
                print("\nPress Enter To Continue")
                input()
                continue
                
        
        if choose2 == 2:
            os.system('cls')
            print("\nEnter Domain: ")
            domain1 = str(input())
            
            def is_registered(domain_name):
                """
                A function that returns a boolean indicating 
                whether a `domain_name` is registered
                """
                try:
                    w = whois.whois(domain_name)
                except Exception:
                    return False
                else:
                    return bool(w.domain_name)
            
            if is_registered(domain1) == True:
                whois_info = whois.whois(domain1)
                
                print("\nDomain registrar:", whois_info.registrar)
                print("WHOIS server:", whois_info.whois_server)
                print("Domain creation date:", whois_info.creation_date)
                print("Expiration date:", whois_info.expiration_date)
                print("\nPress Enter To Continue")
                input()
                continue
                
            else:
                print("\nUnknown Domain")
                print("\nPress Enter To Continue")
                input()
                continue
            
        if choose2 == 1:
            os.system('cls')
            print("\nEnter Domain: ")
            domain1 = str(input())
            
            def is_registered(domain_name):
                """
                A function that returns a boolean indicating 
                whether a `domain_name` is registered
                """
                try:
                    w = whois.whois(domain_name)
                except Exception:
                    return False
                else:
                    return bool(w.domain_name)
            
            print(domain1, "is registered" if is_registered(domain1) else "is not registered")
            
            
            
            print("\nPress Enter To Continue")
            input()
            continue
            