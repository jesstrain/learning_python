# I have created a variable called birth_year 
# and given an input value called 'Birth year: '
# This is so when the program runs it will allow me to write an 
# integer in the terminal and continue with the function.

birth_year = input ('Birth year: ')

# I have then created another variable called age 
# and given it an interger as a data type. 
# In order for the computer to run the function, I need to add the word int
# and put brackets around the other variable - birth_year. This allows the string from the first 
# variable to be converted into an integer and therefore continue the program.

age = 2024 - int(birth_year)

# Once the computer has sucessfully calculated this, the print statement 
# will display the calcuated age in the termminal

print(age)