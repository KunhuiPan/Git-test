import random

hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


b = ({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
j=""


print(sum((1,2)))



substitute_chance = 1

    overall_scores = [] # accumulate scores for all hands
    scores = 0
    hand_num = int(input("Enter total number of hands:"))


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    substitute_chance = 1

    overall_scores = []  # accumulate scores for all hands
    scores = 0
    hand_num = int(input("Enter total number of hands:"))

    while hand_num > 0:

        hand = deal_hand(HAND_SIZE)
        print("Current hand:", end=' '), display_hand(hand)

        if substitute_chance == 1 and hand_num > 0:
            sub_option = input("Would you like to substitute a letter?")
            if sub_option.lower() == "yes":
                letter_replace = input("Which letter would you like to replace:")
                hand = substitute_hand(hand, letter_replace)
        print()
        hand_score = play_hand(hand, word_list)
        substitute_chance -= 1
        replay_num = hand_num - 1
        hand_num -= 1

        if replay_num > 0:  # substitute_chance == 0
            replay_option = input("would you like to replay the hand?")
            if replay_option.lower() == "yes":
                replay_score = play_hand(hand, word_list)
                scores += max(replay_score, hand_score)
                hand_num -= 1
            else:
                substitute_chance = 1
                scores += hand_score
        scores += hand_score
        overall_scores.append(scores)
        continue

    print("Total score over all hands: ", sum(overall_scores))