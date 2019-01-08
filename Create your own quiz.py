# A list of replacement words to be passed in to the play game function.
name = ["PROJECT", "PHYTON", "BUILD", "NOUN"]


# The following are some test strings to pass in to the play_game function.
test_string2 = "In this PROJECT , you will use the PHYTON programming language to BUILD your own quiz. You will use a fill-in-the blank style to create a quiz that can even be used as a study tool to help you remember important vocabulary.."


# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None


# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


print play_game(test_string2, name)