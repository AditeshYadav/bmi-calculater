weight = float(input("Enter your weight. [In kg]\n"))

height = float(input("Enter your height.[In m]\n"))

#Formal bmi = weight/(height**2)
bmi = weight / (height ** 2)

if bmi < 18.5:
   print("underweight.")
elif bmi >= 18.5 and bmi <25:
   print("normal weight.")
else:
    print ("overweight")