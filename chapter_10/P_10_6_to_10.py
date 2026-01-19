
def try_int():

    while True:
        try:
            num = int(input('number: '))
        except ValueError:
            print("Please enter a number.")
        else:
            break
    return num


plus = False
while plus:
    num1 = try_int()
    num2 = try_int()
    print(num1 + num2)
    quit_ = input('do you want to quit? (y/n): ')
    if quit_ == 'y':
        break

def print_line(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as FILE:
            for LINE in FILE:
                print(LINE)
    except FileNotFoundError:
        pass

print_line('cats.txt')
print_line('dogs.txt')