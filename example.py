print("Hello, world!")
print(type(1))
print(type(3.14159))
print(type(1.))
print(type(.5))
print(type(-1))
print(1e+5)
print(1e-4)
print(10000 + 300 - 2000)
print(8 * 4)
print(54 / 6)
print(21 / 8)
print(21 // 8)
print(21 % 8)
print(10 ** 10)
print(2^6)
print(3 * 4.6)
print(0.1 + 0.1 + 0.1)
print(round(3 * 4.6, 1))
print(int(123.456))
print(int(0.999))
print(int("1234567890"))
float("3.14159265358")
float("9414513")
int("3.0")
int(float("3.0"))
int("一九九九")
int("1,999,000")
print("Hello, "Python" world!")
print('I'm Taro Tech')
print('Hello, "Python" world!')
print("Hello,\"python\" world")
print('Hello, \'Python\' world!')
print("Hello, \npython\nworld!)")
"aiu"*3
str(123)
type(str(123))
len(str(123))
type(100000)
print(float(789))
a=11
b=1999
print(a)

11+1999
a+b
a/b
c = a + b
print(c)
d=c*1000
print(d)
f=100000
f=f*1000000
print(f)
del f
print(f)

a=123
type(a)
a="あいう"
type(a)
a=12345
a+1
a+=10000
a
int(True)
int(False)
age=32
age!=21
(age>=18)and(age<=65)
(age>=18)or(age<=65)
not(age>=18)
#これはコメントだよん
a=100; b=10; c=500
print(a)
print(b)
print(c)
print(a); print(b); print(c)
num=1000000
suji=str(num)
len(suji)
name="python-san"
print("Your name is",name,"!")
print("Your name" + name +"!")
print(f"Your name is{name}！")

num="1000"
num=int(num)
num=num+100
num

num_fake="テスト"
num=int(num_fake)
num

exec("""a="JTB"
b="JBX"
g=a + "は" + b + "の親会社です。"
print(g)""")

exec("name = 'kanako'")
name

def Hello():
    print("Hello")
    print("It is a fine day today!")

def good_morning():
    print("Good morning!")
    print("Have a nice day!")
Hello()
good_morning()

def introduce(name, age):
    print("Hello")
    print(f"My name is {name}.")
    print(f"I'm {age} years old.")
introduce("momota", 31)
introduce("takagi", 32)
introduce(name="tamai",age=30)
introduce(age=29, name="sasaki")

def introduce(name="noname",age=0):
    print("Hello")
    print(f"My name is {name}.")
    print(f"I'm {age} years old.")
introduce("tanaka",50)
introduce("suzuki")
introduce(age=32)
introduce()

def calc_bmi(height,weight):
    ret=weight/(height**2)
    return ret

    