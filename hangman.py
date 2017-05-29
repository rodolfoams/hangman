from os import system

states = ["    _____\n   |     |\n   |     O\n   |    /|\\\n   |     |\n   |    / \\\n   |\n___|___", \
          "    _____\n   |     |\n   |     O\n   |    /|\\\n   |     |\n   |\n   |\n___|___",         \
          "    _____\n   |     |\n   |     O\n   |     |\n   |     |\n   |\n   |\n___|___",           \
          "    _____\n   |     |\n   |     O\n   |\n   |\n   |\n   |\n___|___",                       \
          "    _____\n   |     |\n   |\n   |\n   |\n   |\n   |\n___|___"]

def play_game(secret, hint, attempts_left, current_array, used_letters):
    system("clear")
    print states[attempts_left]
    print "Letters used:", " ".join(used_letters)
    if "".join(current_array) == secret: return True
    if attempts_left == 0:
        print " ".join(current_array)
        print "(Hint: %s)" % (hint)
        return False
    print " ".join(current_array)
    print "(Hint: %s)" % (hint)
    print "Mistakes allowed:", attempts_left - 1
    guess = raw_input("Guess a letter in the word: ")
    if len(guess) == 0 or guess[0] in used_letters: return play_game(secret, hint, attempts_left, current_array, used_letters)
    used_letters.append(guess[0])
    used_letters.sort()
    matched = False
    for i in xrange(len(secret)):
        if secret[i] == guess[0]:
            current_array[i] = secret[i]
            matched = True
    if not matched: attempts_left -= 1
    return play_game(secret, hint, attempts_left, current_array, used_letters)

def main():
    secret = raw_input('Enter a secret word (empty string to terminate): ')
    while secret != "":
        hint = raw_input('Enter a hint: ')
        initial_array = ['_'] * len(secret)
        for i in xrange(len(secret)):
            if secret[i] == " ": initial_array[i] = " "
            if secret[i] == "-": initial_array[i] = "-"
        solved = play_game(secret, hint, len(states)-1, initial_array, [])
        if not solved:
            print "You lose!"
        else:
            print "You win!"
        secret = raw_input('Enter a secret word (empty string to terminate): ')

if __name__ == "__main__":
    main()
