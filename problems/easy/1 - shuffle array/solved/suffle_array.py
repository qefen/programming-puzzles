#Given the array nums consisting of 2n elements in the form
#[x1,x2,...,xn,y1,y2,...,yn]. 
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#Constraints: nums.length == 2n

#Homemade whith love in python 3.8.5

nums = [1,2,3,4,4,3,2,1]
#      [1,4,2,3,3,2,4,1]

count=0
half = int(len(nums)/2)

print("Array suffle : "+str(nums))
print("N : "+str(half))

for i in nums :
    if count<len(nums)/2:
        print(nums[count],end=" "+str(nums[half+count])+" ")
    count=count+1
        