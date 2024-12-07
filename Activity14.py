#Write a program to calculate the BMI of a person?
#BMI:-Body Mass Index
#bmi=weight in kgs(heigh*height in meters)

weight=float(input("Enter your weight in kgs"))

height=float(input("Enter your height in meters"))

bmi=weight/(height*height)
print("your bmi is ",bmi)

if bmi<=18.4:
    print("You are underweight.")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=29.9:
    print("You are overweight")
elif bmi<=34.9:
    print("You are severly overweight")
elif bmi<=39.9:
    print("You are obese")
else:
    print("You are severly obese")