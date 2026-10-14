weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


ch = input("Enter a character: ")

if ch.isalpha() and len(ch) == 1:
    print("Alphabet")
else:
    print("Not an alphabet")



v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;   
print("Value of (v+w) * x/ y is ",  z)



name = "Alex"
age = 0
  
if name == "Alex" or name == "John" and age >= 2 : 
  print("Hello! Welcome.")
else :
  print("Good Bye!!")



mean1 = 38
wrong_number=36
correct_number=56
total_number=40
#sum of 40 numbers
sum = mean1*total_number
print("the sum of 40 number: ",sum)

#correct sum of these numbers
num2=sum-((wrong_number)-(correct_number))
print("sum-((wrong_number)-(correct_number)): ",num2)

#the correct mean
mean2=num2/total_number
print(mean2)





#average speed
a = int(input("enter a value: "))
b = int(input("enter value 2 :"))
c = int(input("enter value 3: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d is just higher than %d" %(avg, a))
elif avg > b:
    print("%d is just higher than %d" %(avg, b))
elif avg > c:
    print("%d is just higher than %d" %(avg, c))
else:
  print("invalid input")