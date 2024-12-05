def sentence(name):
    def inner(city):
        return f'I am {name} and I come from {city}'

    return inner

new_sentence = sentence('Mike Tyson')
print(new_sentence('New York'))