hello = "wlcome to the quiz"
print(hello)

name= input("Enter your name")

age = int(input("enter your age:"))
if age >= 20:
    print("you can play")
else:print("your can't play")

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("_________")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter A, B, C, or D: ").upper()

        guesses.append(guess)

        correct_guesses += check_answer(questions[key], guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def play_again():
    response = input("Want to play again? (yes or no): ").lower()
    return response == "yes"


def display_score(correct_guesses, guesses):
    print("\nResults")
    print("Answers: ", end="")
    for key in questions:
        print(questions[key], end=" ")
    print("\nYour guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print(f"\nYou got {correct_guesses} out of {len(questions)} questions correct!")



questions = {
    "Which movie features the song 'Let It Go'?": "A",
    "Who plays Iron Man in the Marvel Cinematic Universe?": "B",
    "What is the highest-grossing film of all time as of 2025?": "A",
    "Which character says, 'I'll be back' in The Terminator?": "D",
    "Who directed the movie Inception?": "C",
}

options = [
    ["A. Frozen", "B. Superman", "C. Batman", "D. Slack"],
    ["A. Anna Jim", "B. Robert Downey Jr.", "C. Joey Tim", "D. Sam Cake"],
    ["A. Avatar", "B. The Lord of the Rings", "C. Superman", "D. Back to the Future"],
    ["A. Joe Pesci", "B. Catherine O'Hara", "C. Michael William", "D. Arnold Schwarzenegger"],
    ["A. James Tim", "B. Paul Kevin", "C. Christopher Nolan", "D. Kim John"],
]


while True:
    new_game()
    if not play_again():
        print("Thanks for playing!")
        break