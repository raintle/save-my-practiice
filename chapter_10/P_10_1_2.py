with open('python知识点.txt', encoding='UTF-8') as f:
    content = f.read()
    print(content, '\n')

with open('python知识点.txt', encoding='UTF-8') as f:
    for line in f:
        print(line)