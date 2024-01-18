import random2

random_number = random2.randint(100, 200)
print(f'Guess the number between 100-200')

data = int(input("Enter a number: "))

if data == random_number:
    print(f'The guessed number {data} is correct.')
else:
    print('Try again')
    print(f'Click r to retry ')
    retry = input("")
    start = 'r'
    if retry == start:
        print(f'Guess the number between 100-200')

data = int(input("Enter a number: "))

if data == random_number:
    print(f'The guessed number {data} is correct.')
