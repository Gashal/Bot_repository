def say_hello(name):
    print(f'Hello my friend {name}')

say_hello('Egor')

def multy_num_and_word(num: int, word: str) -> str:
    word = word.capitalize()
    return word * 3 * num
