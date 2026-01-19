with open('python知识点.txt', encoding='UTF-8') as f:
    '''打开该文件，并将该文件称作f'''
    content = f.read()
    #读取文件中内容
    print(content, '\n')

with open('python知识点.txt', encoding='UTF-8') as f:
    for line in f:
        #将文件内容每一行视作列表元素
        print(line)

with open('python知识点.txt', encoding='UTF-8') as f:
    content = f.read()
    content = content.replace('python', 'c')
    #文本替换
    print(content)