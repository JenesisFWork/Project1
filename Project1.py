#--------------------------------------------------------------------------------------------------------------------------
#Student Name: Jenesis Fabia
#Course: CIT 134A
#Term/Year: Fall 2022
#Date: 9/12/2022
#Project Number: 1
#--------------------------------------------------------------------------------------------------------------------------

#display the titles
print("Employee Management System")
print("-----------------------------------------------------------")
print("Your Information")
print("------------------------")

#User Information
first_name = input ("First Name: ")
last_name = input ("Last Name: ")
company_name = input ("Company: ")
street_address = input ("Street Address: ")
city = input ("City: ")
state = input ("State: ")
zip_code = input("Zip Code: ")
hire_year = input ("Hire Year: ")

#User Profile Temporary Address
print("-----------------------------------------------------------")
print("Your Profile")
print("------------------------")

#User Temporary Password
print(last_name, first_name)
print(company_name)
print(street_address)
print(city, state, zip_code)
print("Your temporary password:" + first_name + "*" + last_name + "%" +hire_year)
print("Congratulations! Your profile has been created.")
print("-----------------------------------------------------------")
print("Bye!")