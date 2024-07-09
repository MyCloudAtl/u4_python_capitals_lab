from capitals import states
import random

def game():
    #state = random.getstate()
    random.shuffle(states)

    correct_answers = 0
    incorrect_answers = 0
    total_questions = len(states)

    print("Welcome to our Capitals Quiz game!") 
    print("We will be testing your knowledge of the capitals of all 50 states. Good luck!")
    print("Hit enter to ACCEPT our challenge")
    input("")

    
    for state_det in states:
        state = state_det["name"]
        capital = state_det["capital"]
        user_guess = input(f"What is the capital of {state}? ").strip()

        if user_guess.lower() == capital.lower():
            print("Correct!")
            correct_answers += 1
            print(f"Running Score: Correct - {correct_answers}, Incorrect - {incorrect_answers}")
            print("")
        else:
            print("")
            hint = capital[:3]
            print(f"Here's a hint: {hint}")
            user_guess.lower() != capital.lower()
            user_guess = input(f"What is the capital of {state}? ").strip()
            print("")
            if user_guess.lower() == capital.lower():
                print("Correct!")
                correct_answers += 1
                print(f"Running Score: Correct - {correct_answers}, Incorrect - {incorrect_answers}")
                print("")
            else:
                print(f"Incorrect...") 
                print(f"The correct answer for the capital of {state} is {capital}.")
                incorrect_answers += 1
                print(f"Running Score: Correct - {correct_answers}, Incorrect - {incorrect_answers}")
                print("")
    
    print("Quiz completed!")
    print(f"Final Score: Correct - {correct_answers}/{total_questions}, Incorrect - {incorrect_answers}/{total_questions}")

    play_again = input('Play again? (yes/no): ').lower()
    if play_again != "yes":
         print("Done!")
    else:
        game()

game()



