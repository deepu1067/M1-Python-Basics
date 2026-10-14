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
