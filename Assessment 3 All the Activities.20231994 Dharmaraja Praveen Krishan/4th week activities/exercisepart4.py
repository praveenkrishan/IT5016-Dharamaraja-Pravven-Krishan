import random
def use_number_guess(computer_num):
    prompt = "enter ur guess (1- 99)"
    num_guesses = 0
    number = 0
    while number != computer_num:
        number = int(input(prompt))
        num_guesses += 1
        if number < computer_num:
            print("too low")
        elif number > computer_num:
            print("too high")
        else:
            print(f"correct ! number of guess: {num_guesses}")
def main():
    use_number_guess(random.randrange(1,100))
main()                    
