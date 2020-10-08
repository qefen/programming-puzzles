# Remove Vowels

Given a string, remove the vowels from the string and return the string without vowels.

## Examples

```
Input : what is your name ?
Output : wht s yr nm ?
```

## Template

_remove_vowels_test.py_

```py
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
});
```
