def whileLoop(n, m):
    for i in range(0,n):
        result = i*m
        print("At the top i is %d" % result)
        numbers.append(result)

        print("Numbers now: ", numbers)
        j = result + m
        print("At the bottom i is %d" % j)

i=0
numbers = []

whileLoop(10, 2)

print("The numbers: ")
for num in numbers: 
    print(num)

