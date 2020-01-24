import keyword
import random
print('Hello world!', end=' ')
print(keyword.iskeyword('for'))

# Ternary Operator
ans = input('plz input "123"')
msg = 'Correct' if ans == '123' else 'Wrong'
print(msg)
print('Correct' if ans == '123' else 'Wrong')

# 'Ctrl' + '/' = comment (in VS code)

# string
str1 = "abc" + \
    "def"
str2 = ("ghi"
        "jkl")
str3 = '''
mno
pqr
'''
str4 = '''\
stu\
vwx\
'''
print('str1=: ', str1)
print('str2=: ', str2)
print('str3=: ', str3)
print('str4=: ', str4)

# escape
# \    \\    \'    \"    \n → LF(Line feed)    \r → CR(Carriage return)   \t
print('\now')
print('\\now')
print(r'\now')  # raw string

# upper() lower() strip()
str1 = 'ABC'
str2 = 'abc'
str3 = '   qwer   '
print(str1.lower())
print(str2.upper())
print(str3.strip())

# type
num = 123.456
str_num = str(num)
str_num*5
type(str_num)
int(str_num)
type(str_num)
float(str_num)
type(str_num)

# format
name = 'Jack'
age = 19
"name: %s" % name
"name:%s, age: %d" % (name, age)
"100%"
"100%%"
#"100%s%" % name
"100%s%%" % name

msg = "{0} 's age is {1}"
msg = msg.format(name, age)
msg
msg = "{a} 's age is {b}"
msg = msg.format(b=age, a=name)
msg

'{:.3f}'.format(12.34567)
'{1:.2}, {0:.3f}'.format(1.11111, 2.222222)
print('{:4},{:4},{:4s},{:<8},{:^8},{:>8}'.format(
    12, '12', '12', "left", "mid", "right"))
print('{:=^20s}'.format('div line'))
text = 'div line'
print(f'{text:=^20s}')

a = 15
f'r={a}, r^2={a**2}'

# id
text = 'Hello world!'
id(text)
id('Hello world!')
dir(text)
dir(10)
text
text = None
text
text = 'Hello world!'
text
del text
# text

# list iter
a_list = [
    'abc',
    0
]
b_list = [
    0, 1, 2, 3, 4
]
c_list = [
    5, 6, 7, 8, 9
]
for a, b in zip(a_list, b_list):
    print('a: ', a, 'b: ', b)

iter(a_list)
iter('abc')
# iter(123)
x = iter(b_list)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x))

# any
ans = input('Plz key in \'ab\'')
if any([ans == 'Ab', ans == 'AB', ans == 'ab', ans == 'aB']):
    print('good')
else:
    print('not good')

# range
num_list = list(range(5, 20, 5))
num_list
for i in range(10):
    print(f'|{i:^3}|')

# random
#import random
#from random import randint
a_list = list(range(0, 10))
for i in range(3):
    print(random.choice(a_list))
print(random.randint(0, 9))
print(random.randrange(10))
random.shuffle(a_list)
print(a_list)

for i in range(3):
    print(random.randrange(10))
random.seed(5)
for i in range(3):
    print(random.randrange(10))
random.seed(5)
for i in range(3):
    print(random.randrange(10))
random.seed()
for i in range(3):
    print(random.randrange(10))
random.seed()
for i in range(3):
    print(random.randrange(10))

# function


def area(w, l=None):
    '''computing the area of rect\n
    w: width\n
    l: length
    '''
    # if l == None:
    if l is None:  # is not
        return w*w
    else:
        return w*l


area(3)
sum1 = 0


def add():
    global sum1
    sum2 = 0
    sum1 += 1
    sum2 += 1
    print(sum1, sum2)


add()
add()

#list - 2
a_list = ['a', 'fdsf', 45, 41.5, 45, 'qwertyuiop']
a_list.count(45)
a_list.append('a')
print(a_list)
a_list.insert(20, 'asdf')
print(a_list)
a_list.pop()
a_list.pop(0)
b_list = [0, 1, 2, 3, 4, 5, 6]
a_list.extend(b_list)
print(a_list)
a_list += b_list
print(a_list)
b_list *= 2
print(b_list)
b_list.remove(0)  # first  corresponding item
print(b_list)
del b_list[2]
print(b_list)
