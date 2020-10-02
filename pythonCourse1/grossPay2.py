hrs = input("Enter Hours:")
h = float(hrs)
rph = float(input("Enter rate per hours:"))

if h > 40:
    print(40 * rph + (h - 40) * rph * 1.5)
else:
    print(h * rph)

hrs1 = input("input the hours")
h1 = float(hrs1)
rate = float(input("Enter the rate"))

if h1 > 40:
    print(40 * rate + (h1 - 40) * rate * 1.5)
else:
    print(rate * h1)
