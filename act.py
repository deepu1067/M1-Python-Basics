num1 = 3
num2 = 6
num3 = 8

avg = (num1+num2+num3)/3.0

print(f"Average: {avg}")


notes = ["english", "math", "science"]
count_note = 0

for i in count_note:
    count_note += 1

print(f"Count Note: {count_note}")


obtained_marks = 450
total_marks = 500

percentage = (obtained_marks / total_marks) * 100

print(f"Percentage: {percentage}%")

import math

num = 25
result = math.sqrt(num)

print(result)


if result > 6:
    print("Nice")
else:
    print("Try")


cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    percentage = (profit / cost_price) * 100
    print("Profit:", profit)
    print(f"Profit percentage: {percentage}%")

elif cost_price > selling_price:
    loss = cost_price - selling_price
    percentage = (loss / cost_price) * 100
    print("Loss:", loss)
    print(f"Loss percentage: {percentage}%")

else:
    print("No profit, no loss.")



a = 5
b = 4

if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")


if a%2 == 0:
    print("Even")
else:
    print("Odd")


if a%5 == 0 and a%3 == 0:
    print("naba")
elif a%4 == 0 or a%2 == 0:
    print("bana")
elif a != 3:
    print("nab")