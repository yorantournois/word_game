import random
import datetime
from nltk.corpus import words as nltk_words

def is_english_word(word):

    dictionary = dict.fromkeys(nltk_words.words(), None)
    try:
        dictionary[word]
        return True
    except KeyError:
        return False


class Player:

    def __init__(self, name, score, used_letters, played_words, time_limit, bonus):
        self.name = name
        self.score = score
        self.used_letters = used_letters
        self.played_words = played_words
        self.time_limit = time_limit
        self.bonus = bonus


# generate random first letter from alphabet
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)
            if chr(i) not in ('q', 'x', 'y', 'z')]

# initiate game: number players, names and so on
while True:
    list_players = input("enter player names: ").split()
    if list_players:
        break
    else:
        print("try again...")
number_players = len(list_players)


d = {}
for name in list_players:
    d[name] = Player(name, 0, [], [], 60, 0)


print(50 * "-")
for x in d.keys():
    player = d[x]
    print("")
    print(f"{player.name}'s turn!")
    input("press any key to start: ")

    # starting time attribute of player. Bonus +=1 implies starting time +=1!
    starting_letter = random.choice(alphabet)
    print(f"Your starting letter is {starting_letter}")

    # Start game, print starting letter, set timer to TIME
    start = datetime.datetime.now()

    while True:
        offset = 0
        bonus = 0

        if (datetime.datetime.now() - start).seconds > player.time_limit:
            print("time is up!")
            break

        word = input("input word: ")

        if not word or word in player.played_words or word[0] != starting_letter:
            print("please enter a valid word")
            continue

        player.played_words.append(word)

        if not is_english_word(word):
            print(f"{word} is not in the dictionary")
            continue

        player.score += len(word)
        if len(word) > 10:
            print("bonus! word is longer than 10 letters")
            bonus += 1

        if len(word) > 1:
            if word[1] not in player.used_letters:
                player.used_letters.append(word[1])
                print("bonus! second letter was not used before")
                bonus += 1
                offset += 1
                player.time_limit += offset

        player.score += bonus
        player.bonus += bonus

        print(f"your score: {player.score}")
        print(
            f"time left: {player.time_limit - (datetime.datetime.now() - start).seconds} seconds ")

print("")
print("scores:")
for x in d.keys():
    if len(d[x].played_words) > 0:
        efficiency = d[x].score / len(d[x].played_words)
    else:
        efficiency = 0

    print(f'{d[x].name} has {d[x].score} points, averaging {round(efficiency,2)} points per word and getting a total bonus of {d[x].bonus}')
