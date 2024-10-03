# Write a program that will ask for a user body weight in pound(lbs) and convert it in kilogram
# define the variable weight in pound
weight = float(input("What is your body weight in pound:\t"))

# convert a user body weight in pound to a body weight in kilogram
weight_convert = weight * 0.453592

# Display the result
print (f"Your body weight in pound is: {weight} in lbs and the equivalent in kgs is: {weight_convert: .3f} kg. \n Thank you!")
