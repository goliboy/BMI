import sys


if len(sys.argv) == 3:
    script_name = sys.argv[0]
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    weight = 70.0    
    height = 1.75     
    print("No input given — using default values:")


bmi = weight / (height * height)


print("\n--- BMI Calculation ---")
print("Script Name:", script_name)
print("Weight (kg):", weight)
print("Height (m):", height)
print("BMI:", bmi)
