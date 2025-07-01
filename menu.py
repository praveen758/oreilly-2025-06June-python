def menu(choices):
    while True:
        s = input('Enter your choice: ').strip()
    
        if s in choices:
            return s

        print(f'{s} is not a valid choice')

if __name__ == '__main__':
    user_choice = menu(['a', 'b', 'c'])

    print(f'You chose {user_choice}')