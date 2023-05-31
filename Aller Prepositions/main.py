import random

file_names = {
    "À": "A.txt",
    "À'l": "A_L.txt",
    "À_la": "A_LA.txt",
    "AU": "AU.txt",
    "aux": "aux_.txt",
    "chez": "chez.txt",
    "En": "EN.txt"
}

score = 0  # Initialize the score to 0

while True:
    # Randomly choose a word and its corresponding key
    key = random.choice(list(file_names.keys()))
    file_path = file_names[key]

    # Read the selected file and store the words in a list
    with open(f"prepositions\\{file_path}", 'r', encoding="utf-8") as file:
        words = file.read().splitlines()

    # Randomly select a word from the list
    selected_word = random.choice(words)

    print(f"Guess which key the word [ {selected_word} ] belongs to:")
    for i, option in enumerate(file_names.keys(), 1):
        print(f"{i}) {option}")

    guess_number = input("Enter the number of your guess (Enter 'exit' to quit): ")

    if guess_number.lower() == "exit":
        print("Exiting the game. Goodbye!")
        break

    try:
        guess_number = int(guess_number)
        if guess_number in range(1, len(file_names) + 1):
            guess_key = list(file_names.keys())[guess_number - 1]
            if guess_key == key:
                print("+++ Congratulations! Your guess is correct. +++")
                score += 1
            else:
                print("[!] Sorry, your guess is incorrect. [!]")
                correct_key = key
                print(f"The correct answer is: {correct_key}")

                # Log the wrong guess and the correct answer to the log file
                with open("log.txt", "a", encoding="utf-8") as log_file:
                    log_file.write(f"Wrong guess: {selected_word} (Guessed: {guess_key}, Correct: {correct_key})\n")
        else:
            print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    print("Score:", score)

    # Prompt for continuing the game
    # play_again = input("Do you want to play again? (Enter 'yes' to continue): ")
    # if play_again.lower() == "exit":
    #     print("Exiting the game. Goodbye!")
    #     break