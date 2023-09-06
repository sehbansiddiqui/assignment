#Import Section

from datetime import date   #import this for Date
import getpass              #import this for User

#Flower Box Section

#########################################################
#                                                       
#   Name:  Sehban Siddiqui                        
#   Date:  08/28/23
#  This program is generating a list of usernames based on the input provided by the user of first and last name as well as year. The program creates usernames based on the first initial of first name, last name, and then last two years of birth year. 
#                                                       
#########################################################

#Variables section
username_list=[]
username_sorted_list = []
employee_data_dictionary = {}

#Functions section

    #Starting on project 4 all functions created will be in this section

#Input section

num_employees = 5



#process section


all_employee_data_in_tuples_list = list(zip(first_name_list, last_name_list, year_born_list)) #zips all data inside of the tuples
for employee in all_employee_data_in_tuples_list: #creates a for loop which will be based on the information provided below
    employee_first_name=employee[0] #returns first letter of each employee's first name
    employee_last_name=employee[1] #returns last name of each employee
    employee_year_born=employee[2] #returns last two years of employee's birth year.




    first_initial=employee_first_name[0].lower() #uses tuple to show first initial of employee's first name
    last_two_digits_year_born = employee_year_born[-2] #uses tuple to show last 2 years of employee's birth year

    username=first_initial+employee_last_name.lower()+last_two_digits_year_born #outputs username as the initial of employee's first name, last name, and then last two digits of birth year.

    username_list.append(username) #appends the username list
    employee_data_dictionary[username] = employee #creates a dictionary of employee usernames with value and key holding the values

username_test_set = set(username_list) #creates username sets

username_no_dups_list = list(username_test_set) #shows list with first duplicate removed

for username in username_no_dups_list: #removes all duplicates in list
    username_sorted_list.append(username) #displays usernames as a list.

username_sorted_list.sort() #sorts all usernames in alphabetical order.

#Output section
print(getpass.getuser()) #outputs username on PC
print(date.today()) #outputs today's date
print()
print(all_employee_data_in_tuples_list) #prints all employee data inside of the tuples list
print(username_list) #Prints username list
print(username_no_dups_list) #prints username list without duplicates
print(employee_data_dictionary) #outputs employee data dictionary