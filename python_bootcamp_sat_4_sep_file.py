from pprint import pprint

message = "learning programming is a very important skill in our today world and in the future"
letter_count = {}

for character in message:
    letter_count.setdefault(character, 0)
    letter_count[character] += 1

pprint(letter_count)


