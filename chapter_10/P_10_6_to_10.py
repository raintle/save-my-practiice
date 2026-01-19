
def try_int():

    while True:
        try:
            num = int(input('number: '))
        except ValueError:
            print("Please enter a number.")
        else:
            break
    return num

while True:
    num1 = try_int()
    num2 = try_int()
    print(num1 + num2)
    quit_ = input('do you want to quit? (y/n): ')
    if quit_ == 'y':
        break

