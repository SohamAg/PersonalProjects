questions = ['Is your character male? ', 'is your character real? ', 'Is your character of or more than 50 years of age? ', 'Is your chatracter a Muslim? ', 'Is your character a villain? ', 'Does your character have kids? ', 'Has your character ever played in a superhero movie/a superhero? ', 'Is your character married? ', 'Is your character dead? ', 'Is your character over 30 years old? ', 'Has your character played in a medieval movie/or from a medieval movie?', 'is the complextion of your character fair?', 'does you character have family lefacy in the film industry', 'is your character from the housefull or golmaal franchise?', 'is your character a star from the 2000s or the 1990s', 'has your character even been to hollywood?', 'is your character usually associated with romance?', 'is your character usually assosciated with action?', 'is your character usually assosciated with comedy?']


def takeinput (i):
    value = eval(input(questions[i]))
    while value < 0:
        print('Error! Please enter O or a positive value')
        value = eval(input(questions[i]))
    if value == 0:
        ans = 'n'
    else:
        ans = 'y'
    return ans