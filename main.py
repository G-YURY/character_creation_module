from random import randint


def attack(char_name, char_class):
    attack_text = char_name + ' нанёс урон противнику равный '
    attack_loss = [(3, 5), (5, 10), (-3, -1)]

    if char_class == 'warrior':
        loss_level = 5 + randint(attack_loss[0])
        return (attack_text, loss_level)

    if char_class == 'mage':
        loss_level = 5 + randint(attack_loss[1])
        return (attack_text, loss_level)

    if char_class == 'healer':
        loss_level = 5 + randint(attack_loss[2])
        return (attack_text, loss_level)
    return (f'{char_name} не нанёс противнику никакого урона')


def defence(char_name, char_class):
    defence_text = char_name + ' блокировал '
    defence_block = [(5, 10), (-2, 2), (2, 5)]
    if char_class == 'warrior':
        block_level = 5 + randint(defence_block[0])
        return (f'{defence_text} {block_level} урона')
    if char_class == 'mage':
        block_level = 5 + randint(defence_block[1])
        return (f'{defence_text} {block_level} урона')
    if char_class == 'healer':
        block_level = 5 + randint(defence_block[2])
        return (f'{defence_text} {block_level} урона')
    return (f'{char_name} не блокировал никакого урона')


def special(char_name, char_class):
    sp_text = char_name + ' применил специальное умение '
    sp_ability = ['Выносливость 105', 'Атака 45', 'Защита 40']
    if char_class == 'warrior':
        return (f'{sp_text} «{sp_ability[0]}»')
    if char_class == 'mage':
        return (f'{sp_text} «{sp_ability[1]}»')
    if char_class == 'healer':
        return (f'{sp_text} «{sp_ability[2]}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence'
          ' — чтобы блокировать атаку противника или special'
          ' — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую '
                               'другую кнопку, чтобы выбрать '
                               'другого персонажа ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
