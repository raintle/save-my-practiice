import json

def try_read():

    with open('user_number.json', 'r', encoding='utf-8') as f:
        message_ = json.load(f)
        #读取文件内容
        print('love number is:', message_)
        return message_

def write_numbers():

    with open('user_number.json', 'w', encoding='utf-8') as f:
        #写入文件内容
        print('input your number')
        json.dump(input(), f)
        #存储输入
        try_read()

def p_11():

    try:
        try_read()
    except FileNotFoundError:
        write_numbers()

if __name__ == '__main__':
    p_11()
    message = input()
    message_check = try_read()
    if message == message_check:
        print('welcome')
    else:
        write_numbers()
        try_read()