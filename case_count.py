def CaseCount(word):
    case_count = {'upper': 0, 'lower': 0}

    for letter in word:
        if letter != ' ':
            if letter.isupper():
                case_count['upper'] += 1
            else:
                case_count['lower'] += 1
    
    return case_count


print(CaseCount("The University of Lagos"))