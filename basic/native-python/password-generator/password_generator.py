import random
import string

def check_input(prompt):
    while True:
        number_user = input(prompt)
        try:
            number = int(number_user)
            return number
        except ValueError:
            print("Please enter a valid number.")
    
def get_list(list,number):
    selected_list = []
    for i in range(0,number):
        selected_list.append(random.choice(list))
    return selected_list
        

print("how many letters in the password")
letters = string.ascii_letters
number_of_letters = check_input("input: ")
    

print("how many symbols in the password")
symbols = string.punctuation
number_of_symbols = check_input("input: ")


print("how many numbers in the password")
numbers = string.digits
number_of_numbers = check_input("input: ")


letters_list = get_list(letters,number_of_letters)
symbols_list = get_list(symbols,number_of_symbols)
numbers_list = get_list(numbers,number_of_numbers)

overall_list = letters_list + symbols_list + numbers_list

random.shuffle(overall_list)

password = ''.join(overall_list)
print(f"Your password is: {password}")