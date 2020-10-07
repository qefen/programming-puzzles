#Given a string, remove the vowels from the string and return the string without vowels.
#Input : what is your name ?
#Output : wht s yr nm ?

#Homemade whith love in python 3.8
import unittest

def removeVowels(text):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    arg=""
    for i in text: 
        if i in vowels:
         i=i
        else:
            arg=arg+i
    return arg

class Vowels(unittest.TestCase):
    def test(self):
        actual  = removeVowels("what is your name ?")
        expected = "wht s yr nm ?";
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()



