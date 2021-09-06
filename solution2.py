def RemoveLonger(words: list, max_length: int) -> list:

    result = []

    for word in words:
        if len(word) <= max_length:
            result.append(word)

    return result


print(RemoveLonger(['lion', 'goat', 'lizard', 'crocodile', 'ant'], 4))

# def checkwords(word, number):
#     if len(word) <= number:
#         return True
#     return False


# words = ['lion', 'goat', 'lizard', 'crocodile', 'ant']

# result = filter(lambda word: checkwords(word, 4), words)
# print(list(result))
