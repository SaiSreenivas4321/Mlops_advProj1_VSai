# 1. Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

# # = 5
# O = 3
# X = 1
# ! = -1
# !! = -3
# !!! = -5

# A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.

# If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.

list1 = ["#","O","X","!","!!","!!!",[5, 3, 1, -1 -3, -5]]
total_score = 0

for i in list1:
    print(i)

