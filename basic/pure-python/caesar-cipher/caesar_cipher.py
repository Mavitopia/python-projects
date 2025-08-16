import string

def caesar(message, shift_amount, method):
    alphabet = string.ascii_lowercase
    message_chars = list(message)
    
    for i, char in enumerate(message):
        index = alphabet.find(char)
        if index != -1:
            if method == 1:
                new_index = (index + shift_amount) % len(alphabet)
            else:
                new_index = (index - shift_amount) % len(alphabet)
            message_chars[i] = alphabet[new_index]
    
    return "".join(message_chars)



keep_running = True

while keep_running:
        
    while True:
        try:
            choice = int(input("Select a function:\n1. Encrypt\n2. Decrypt\nYour choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if choice in (1, 2):
            break
        else:
            print("Please enter 1 or 2.")

    valid_message = False
    while not valid_message:
        text = input(f"Enter the message to {'encrypt' if choice == 1 else 'decrypt'}: ").strip().lower()
        if all(char in string.ascii_lowercase or char == " " for char in text):
            valid_message = True
        else:
            print("Letters only! Digits and punctuation are not allowed.")
            

    while True:
        try:
            shift_value = int(input("Enter the shift number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
            
    result = caesar(text, shift_value, choice)
        
    print(f"Result: {result}")
            
    while True:
        try:
            continue_choice = int(input("Do you want to continue?\n1. Yes\n2. No\nYour choice: "))
            if continue_choice in (1, 2):
                keep_running = continue_choice == 1
                break
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")