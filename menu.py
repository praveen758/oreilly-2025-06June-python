def menu(choices):
    while True:
        s = input('Enter your choice: ').strip()
    
        if s in choices:
            return s

        print(f'{s} is not a valid choice')
