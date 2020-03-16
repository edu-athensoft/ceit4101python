"""
emoji converter
"""

dict_emoji= {
    ":)": "😁",
    ":(": "😭"
}

message = input(">")

words = message.split(' ')

# print(words)

output = ""
for word in words:
    output += dict_emoji.get(word, word)+ " "

print(output)