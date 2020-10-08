#Given a valid (IPv4) IP address, return a defanged version of that IP address. A defanged IP address replaces every period "." with "[.]".
#Constraints: The given address is a valid IPv4 address.

#Input: address = "1.1.1.1"
#Output: "1[.]1[.]1[.]1"

#Input: address = "255.100.50.0"
#Output: "255[.]100[.]50[.]0"
import unittest

def defangIPaddr(ip):
    defang=""
    for i in ip:
        if i==".":
            defang=defang+"[.]"
        else:
            defang=defang+i
    return defang

class Ip(unittest.TestCase):
    def test(self):
        actual="1.1.1.1"
        expected="1[.]1[.]1[.]1"
        self.assertEquals(defangIPaddr(actual),expected)
    def test1(self):
        actual="255.100.50.0"
        expected="255[.]100[.]50[.]0"
        self.assertEquals(defangIPaddr(actual),expected)
    def test3(self):
        actual="10.72.138.230"
        expected="10[.]72[.]138[.]230"
        self.assertEquals(defangIPaddr(actual),expected)
            

if __name__ == '__main__':
    unittest.main()
 
