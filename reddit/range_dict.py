"""
Hope this code with comment could be of some help.
"""

emotions = {1: "Happiness", 2: "Neutral", 3: "Unhappy", 4: "In love", 5: "Sad"}

# if you want to use range()
for emo_index in range(1, len(emotions)):
    print(emotions[emo_index])

# or you might not want to use range()
for emo_key in emotions:
    print(emo_key, emotions[emo_key])

"""
Please be noted that a dictionary in a for-loop as iterables can only return keys of entries,
so the value of an entry should be accessed with specified key.
"""