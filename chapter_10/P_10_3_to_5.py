run_guest = True
run_greeting = True
run_survey = True

while run_guest:
    with open('guests.txt', 'a') as f:
        #文件附加
        guest_name = input('Guest name: ')
        if guest_name == 'q':
            run_guest = False
            continue
        f.write(guest_name + '\n')

while run_greeting:
    with open('guests_book.txt', 'w') as f:
        #文件只写，且写入前清空文件
        guest_name = input('Guest name_: ')
        if guest_name == 'q':
            run_greeting = False
            continue
        f.write(guest_name + '\n')
        #写入输入
        print('hello!', guest_name)

while run_survey:
    with open('survey.txt', 'a') as f:
        survey_name = input('Survey: ')
        if survey_name == 'q':
            run_survey = False
            continue
        f.write(survey_name + '\n')