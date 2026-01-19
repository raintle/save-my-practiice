
def try_int():

    while True:
        try:
            num = int(input('number: '))
            #试图转换成int类型，出错则重新输入
        except ValueError:
            print("Please enter a number.")
        else:
            break
    return num

def plus():

    while True:
        num1 = try_int()
        num2 = try_int()
        print(num1 + num2)
        quit_ = input('do you want to quit? (y/n): ')
        if quit_ == 'y':
            break

def print_line(file_name):

    try:
        with open(file_name, 'r', encoding='utf-8') as FILE:
            #尝试读取文件，文件不存在时静默
            for LINE in FILE:
                print(LINE)
    except FileNotFoundError:
        pass
    #静默函数

if __name__ == '__main__':

    plus()

    print_line('cats.txt')
    print_line('dogs.txt')

'''10-10略'''