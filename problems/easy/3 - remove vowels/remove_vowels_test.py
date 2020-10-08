import unittest

def removeVowels(text):
    #Write your code here
    return 

class Vowels(unittest.TestCase):
    def test(self):
        actual  = removeVowels("what is your name ?")
        expected = "wht s yr nm ?";
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()