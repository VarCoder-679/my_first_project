##------>BMI Calculator                                               

weight = float(input("enter the weight: "))
unit1 = input("Kilograms (kg) or pounds(lbs): ")
height = float(input("enter the height: "))
unit2 = input("meters(m) or inches(inch) or feet or inches(ft+inch): ")

#Conversion of pounds(lbs) if required
if(unit1=="lbs"):
    weight = weight * 0.453592

# Handling height input
height_unit = input("Is your height in meters (m), inches (inch), or feet and inches (ft+inch)? ")
#Conditions to convert height_unit
if height_unit == "ft+inch":
    feet = float(input("Enter the height (feet): "))
    inches = float(input("Enter the height (inches): "))
    height = (feet * 0.3048) + (inches * 0.0254)  # Convert to meters
elif height_unit == "inch":
    height = float(input("Enter the height in inches: ")) * 0.0254  # Convert to meters
elif height_unit == "m":
    height = float(input("Enter the height in meters: "))
else:
    print("Invalid height unit entered.")
    exit()

#BMI FORMULA
BMI = weight / (height**2)

#Determing the BMI Category
if(BMI <= 18):
    print(f"The BMI of {BMI:.2f} indicate that the person is underweight.")
elif(18.5 <= BMI and BMI <= 24.9):
    print(f"The BMI of {BMI:.2f} indicate that the person is normal.")
elif(25.0 <= BMI and BMI <= 39.9):
    print(f"The BMI of {BMI:.2f} indicate that the person is overweight. ")
else:
    print(f"The BMI of {BMI:.2f} indicate that the person is obese. ")
