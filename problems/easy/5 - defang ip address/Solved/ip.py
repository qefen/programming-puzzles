#Given a valid (IPv4) IP address, return a defanged version of that IP address. A defanged IP address replaces every period "." with "[.]".
#Constraints: The given address is a valid IPv4 address.

#Input: address = "1.1.1.1"
#Output: "1[.]1[.]1[.]1"

#Input: address = "255.100.50.0"
#Output: "255[.]100[.]50[.]0"

ip="10.72.138.230"
defang=""
for i in ip:
    if i==".":
        defang=defang+"[.]"
    else:
        defang=defang+i
    
print(ip)
print(defang)
