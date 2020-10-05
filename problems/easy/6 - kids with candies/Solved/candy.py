candies = [12,1,12]
extraCandies=10
max=0

for i in candies:
    if max<=i:
        max=i

for i in candies:
    if i+extraCandies >= max:
        print("True")
    else:
        print("False")

print(max)
