'''

This script checks for a range of internet ports whether they are opened or not
and returns the ports that are opened.

'''

import socket
import re
from colorama import Fore


#specify a range of ports you want to check

host_ip = 'random_string'

ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


#ask for user input for host ip adress

while bool(re.search(ip_pattern,host_ip)) == False:
    
    print("\nplease specify an ipv4 address (num1.num2.num3.num4, where num1-4 are between 0 and 255")
    
    try:
        
        host_ip = input("please give host ip: ")
    except Exception as e:
        print(e)
        
  
        
#Ask for range of port numbers to check on host ip

choice = False

while choice == False:
    
    try:
        
        print("\nPlease specify a range of ports for which you would like to check if they are open")
        lowest_port = int(input("lowest port number: "))
        highest_port = int(input("highest port number: "))
        
    except Exception as e:
        print(e)
        
    else:
        choice = True
        
        if lowest_port > highest_port:
            
            temp = lowest_port
            
            lowest_port = highest_port
            
            highest_port = temp
           
        
        print(f"finding open ports for range {lowest_port}-{highest_port} ...")
       
        
       
 #Check which of the ports in the range are open
 
 
open_port_list = []     
for port_num in range(lowest_port,highest_port+1):
    print(port_num)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  
    try:
        check = s.connect_ex((host_ip, port_num))
        
        if check == 0:
            print(f'port {port_num} is open! ')
            open_port_list.append(port_num)
            
        s.close()
        
        
        
    except Exception as e:
        print(e)
        pass


print("\nThe following ports are " + Fore.GREEN + "opened: \n")
print(open_port_list)
    
