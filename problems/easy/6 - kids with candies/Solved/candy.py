#Input: candies = [2,3,5,1,3], extraCandies = 3
#Output: [true,true,true,false,true]

#Explanation:
#- Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies, the greatest number of candies among the kids.
#- Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.
#- Kid 3 has 5 candies and this is already the greatest number of candies among the kids.
#- Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies.
#- Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.

#Input: candies = [4,2,1,1,2], extraCandies = 1
#Output: [true,false,false,false,false]

#Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.

#Input: candies = [12,1,12], extraCandies = 10
#Output: [true,false,true]

candies = [12,1,12]
extraCandies=10
max=0

for i in candies:
    if max<=i:
        max=i

for i in candies:
    if i+extraCandies >= max:
        print("True",end=",")
    else:
        print("False",end=",")


