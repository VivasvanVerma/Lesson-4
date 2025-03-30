maths = int(input("Enter maths marks: "))
sci = int(input("Enter science marks: "))
eng = int(input("Enter english marks: "))
hist = int(input("Enter history marks: "))
calc = int(input("Enter calculus marks: "))
geo = int(input("Enter geography marks: "))
percent = ((maths + sci + eng + hist + calc + geo)/600)*100
print("Percent: ", percent, "%")
