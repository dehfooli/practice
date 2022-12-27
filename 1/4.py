height = float(input("Enter height in cm: "))
weight = int(input("Enter weight in kg: "))

BMI = weight / (height ** 2)

if BMI <= 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal")
elif BMI >= 25 and BMI <= 29.9:
    print("Overweight ")
elif BMI >= 30 and BMI <= 34.9: 
     print("Obesity")
elif BMI >= 35 and BMI <= 39.9:
    print("Extreme Obesity")
else:
    print("You are severely obese.")
