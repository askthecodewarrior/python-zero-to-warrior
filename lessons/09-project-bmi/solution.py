# BMI calculator

# 1. Ask for the weight and the height
weight = float(input("Weight in kg: "))
height = float(input("Height in meters: "))
print(f"You entered {weight} kg and {height} m")

# 2. Work out the BMI
bmi = weight / height ** 2

# 3. Show the BMI and the chart
print(f"Your BMI is {bmi:.1f}")
print("=" * 32)
print("Underweight      less than 18.5")
print("Healthy weight   18.5 to less than 25")
print("Overweight       25 to less than 30")
print("Obesity          30 or greater")
