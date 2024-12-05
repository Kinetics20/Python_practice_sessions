def sentence(name):
    def inner(city):
        return f'I am {name} and I come from {city}'

    return inner

new_sentence = sentence('Mike Tyson')
# sent = new_sentence('New York')
# sent_2 = new_sentence('Chicago')
#
# print(sent)
# print(sent_2)

# new_sentence = sentence('Mike Tyson')('Warsaw')
# print(new_sentence)