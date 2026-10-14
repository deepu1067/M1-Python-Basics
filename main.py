import keyword

# starting now
print("Welcome to the world of programming!")
print("The World shall know pain")


num1 = 1
num2 = 2

print(f"sum: {num1 + num2}")

# print all the Python keywords
print("Python keywords are...\n")
print(keyword.kwlist)

birthday = "1998-05-15"

print(birthday)


#swap number
a = 4
b= 6

print(a, " ", b)

temp = a
a = b
b = temp

print(a, " ", b)



agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

value = input("Enter a value: ")

first_name = "Delwar Shahadat"
last_name = "Deepu"

full_name = first_name + last_name

print(f"Congratulation {full_name}🎉")

print(f"Value before type cast: {type(value)}")
value =  int(value)
print(f"Value beafterore type cast: {type(value)}")
print("Agent Number:", agent_number, "-> type:", type(agent_number))
print("Speed Rating:", speed_rating, "-> type:", type(speed_rating))
print("Mission Count:", mission_count, "-> type:", type(mission_count))
print("Height (m):", height_m, "-> type:", type(height_m))
print("Is Active:", is_active, "-> type:", type(is_active))



op = input("Enter an operator: ")

if op == "+":
    print("Addition operator")
elif op == "-":
    print("Subtraction operator")
elif op == "*":
    print("Multiplication operator")
elif op == "/":
    print("Division operator")
elif op == "%":
    print("Modulus operator")
elif op == "//":
    print("Floor division operator")
elif op == "**":
    print("Exponentiation operator")
else:
    print("Invalid operator")


a = 10

b = -10


# print bitwise right shift operator

print("a >> 1 =", a >> 1)

print("b >> 1 =", b >> 1)

 
a = 5

b = -10

 
# print bitwise left shift operator

print("a << 1 =", a << 1)

print("b << 1 =", b << 1)



marks = float(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: A-")
elif marks >= 50:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: F")


