largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if largest is None or largest < num:
            largest = num
        if smallest is None or smallest > num:
            smallest = num
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

large = None
small = None

while True:
    num = input("enter the number ")
    if num == 'done':
        break
    try:
        num = int(num)
        if large is None or large<num:
            large=num
        if small is None or small >num:
            small = num
    except:
        print("Invalid number")
print(large)
print(small)