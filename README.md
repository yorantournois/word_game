# word_game

# Simple vocab game with the following rules
# - Each player gets a random letter
# - For each valid word entered, starting with the given letter, a player gets points
# - Each player has 60 seconds to enter as many words as possible
# - The player with the most points wins

# Here, "valid" means the word appears in the dictionary


# Each word is worth len(word) points, plus a possible bonus:
# - If the valid word contains 10 or more letters, an additional bonus point is awarded
# - If the valid word is the first word played that has that second letter, an additional bonus point is awarded. For example, if "b" is the starting letter, playing "break" yields one additional bonus point ("r" has not appeared as a second letter thus far), but subsequently playing "brand" does not.

# In addition, the second point above adds one second to the clock. 

