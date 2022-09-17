age = float(input("Enter your age: "))

if age < 0:
    print("You're not even existed")
if  0< age <2:
    print("You're newborn")
if 2< age<6:
    print("You're a child")
    
if  6 < age <13 :
    print("You're a kid")
if  13< age <18:
    print("You're minor")
if  18< age <40:
    print("You're young")
if  40< age <70:
    print("You're middle-aged")
if  70< age <90:
    print("You're aged")
elif age >90:
    print("You're old")