# Question 1
def hello_name(user_name):
	print("hello_" + user_name.upper() + "!")

hello_name('username')	


# # Question 2
odd_numbers = list(range(3,100,3))
print(odd_numbers)


 # Question 3
def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max        

print(max_num_in_list([1, 2, 3, 4, 5]))

            


# Question 4
def is_leap_year(a_year):

    if a_year % 400 == 0:
        return True
    elif a_year % 100 != 0:
        return False
    elif a_year % 4 == 0:
        return True

print(is_leap_year(True))
print(is_leap_year(False))
print(is_leap_year(True))				
 				


 # Question 5
def is_consecutive(a_list):
    list1 = [2,3,4,5,6,7]
    list2 = [1,2,4,5]

    for n in list1, list2:
        if list1 > list2:
            return True
        else:
            False    

    is_consecutive(list1) 
    is_consecutive(list2)   