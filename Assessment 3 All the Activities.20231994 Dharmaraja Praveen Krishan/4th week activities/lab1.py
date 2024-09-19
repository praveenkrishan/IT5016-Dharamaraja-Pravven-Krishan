def password_attempt_system():
    correct_password = "python123"
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        entered_password = input("Enter the password: ")
        if entered_password == correct_password:
            print("Access granted!")
            break  
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect password. You have {max_attempts - attempts} attempt(s) left.")
            else:
                print("Access denied. You have used all your attempts.")
    

password_attempt_system()

