import random
import os

def run():
    words_list = []

    with open("./data.txt", "r", encoding="utf-8") as w_l:
        for line in w_l:
            words_list.append(line)

    def choose_random_word(list):
        return random.choice(list)

    def draw_game():
        os.system("clear")
        print("Guess the word!")
        print(''.join(random_word))
        print(''.join(guessed_word))
        print("Tries:", tries)
        print('Used letters:', ', '.join(used_words))

    random_word = list(choose_random_word(words_list))

    if random_word[len(random_word)-1] == "\n":
        random_word.pop()

    guessed_word = list('-' * len(random_word))

    tries = 0
    used_words = []
    input_letter = ""
    last_letter_indexes = []

    while random_word != guessed_word:
        draw_game()
        
        input_letter = input("Type a letter: ")
        used_words.append(input_letter)
        last_letter_indexes.clear()
        tries = tries + 1
        if input_letter in random_word:
            index = 0
            for item in random_word:
                if item == input_letter:
                    last_letter_indexes.append(index)
                    index = index + 1

                else:
                    index = index + 1
            for i in last_letter_indexes:
                guessed_word[i] = input_letter
    
        draw_game()




if __name__ == "__main__":
    run()