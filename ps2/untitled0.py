#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 18:37:48 2022

@author: maoyubohe618
"""

        
# =============================================================================
#         # Entre a invalid input
#         if str.isalpha(str_letters) == False:
#             # If there is more than one warning left, lose a warning
#             if warnings >= 1:
#                 warnings -= 1
#                 print("Oops! That is not a valid letter. You have", warnings, "left: ", get_guessed_word(secret_word, guessed_letters))
#                 print("--------------------")
#             # If there is no warnings left, lose a guess
#             else:
#                 guesses -= 1
#                 
#         # The letter has been guessed
#         if str.isalpha(str_letters) == True and str_letters in guessed_letters == True:
#             if warnings >= 1:
#                 warnings -= 1
#                 print("You have already guessed that letter. You now have", warnings, "warnings:", get_guessed_word(secret_word, guessed_letters))
#                 print("--------------------")
#             else: 
#                 guesses -= 1
#        
#         # The letter has not been guessed and the letter heats the guess
#         if str.isalpha(str_letters) == True and str_letters in guessed_letters == False and str_letters in secret_word == True:
#             guesses -= 0
#             print("Good guess:", get_guessed_word(secret_word, guessed_letters))
#             print("--------------------")
#         # The letter has not been guessed and the letter doesn't heat the guess
#         if str.isalpha(str_letters) == True and str_letters in guessed_letters == False and str_letters in secret_word == False:
#             guesses -= 1
#             print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, guessed_letters) )
#             print("--------------------")
# =============================================================================
