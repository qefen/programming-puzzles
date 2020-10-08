#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

#Input: nums = [1,1,1,1,1]
#Output: [1,2,3,4,5]
#Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

#Made in Python 3.8.5
import unittest

def runningSum(num):
    count=1
    while count< len(num):
        num[count]+=num[count-1]
        count+=1
    return num

class Sum(unittest.TestCase):
    def test1(self):
        actual=runningSum([1,2,3,4])
        expected=[1,3,6,10]
        self.assertEqual(actual,expected)

class Sum(unittest.TestCase):
    def test2(self):
        actual=runningSum([1, 1, 1, 1, 1])
        expected=[1, 2, 3, 4, 5]
        self.assertEqual(actual,expected)

class Sum(unittest.TestCase):
    def test3(self):
        actual=runningSum([3, 1, 2, 10, 1])
        expected=[3, 4, 6, 16, 17]
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main()
