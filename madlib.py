import re

def get_welcome():
    return 'Welcome to MadLib! Please enter and enjoy!'

# read the file

def read_file(path):

    try:
        with open('./temp.txt') as f:
            return f.read()

    except FileNotFoundError as e:
        print('file not existed on this path')

def ask_question(temp):

    answers = []
    questions = re.findall("{.*?}", temp)

    for q in questions:
        q = q.replace('{','')
        q = q.replace('}','')
        print(f'Enter {q}')
        answers.append(input())

    return answers


def fill_temp(temp, answers):

    converted_temp = re.sub("{.*?}", "{}", temp)
    return converted_temp.format(*answers)


def write_file(path, contents):
    with open(path, 'w') as f:
        f.write(contents)


print(get_welcome())

my_temp = read_file('./temp.txt')

my_answer = ask_question(my_temp)

output = fill_temp(my_temp,my_answer)

print(output)

write_file('./answers.txt', output)


