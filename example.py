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

a="Today is a funny day!"
a.replace("Today","Tomorrow")
a.replace("is","will be")

a.lower()   
a.upper() 
a.count("a")

a="     Tech Acdemy     "
a=a.strip()
a

a = """
ゥ

"""
a = a.strip()
a

str1="信号の色は{}と{}と{}"
str1=str1.format("Red","yellow","blue")
str1

station1="tennozu"
station2="shiodome"
price=140
str1=f"{station1}から{station2}までの運賃は{price}円です。"
str1
price=2000000
print(f"It's {price:,}yen tax include ")

score=int(input("please input your score:"))
if score >= 60:
    print("You are pass!")
print("End of the process.")

def exam(score):
    if score >= 60:
        print("素晴らしい！合格です")
        print("おめでとうございます!!!")
    print("処理を終了します")
exam(-1000)


def age(age):
    if(age >= 18)and(age <= 80):
        print("Go ahead!")
    print("End of the process.")

age(32)

def age(age):
    if (age >= 18) and (age <= 80):
        print("Go ahead!")
    print("End of the process.")

age(25)

def your_age(age):
    if age >= 20:
        if age <= 60:
            print("Go ahead")
print("End the process")

age(5)

def your_score(score):
    if score >= 50:
        print("You are pass!")
        print("congratulation")
    else:
        print("You are fail")
        print("You should work hard")
    print("End of the process")

your_score(30)

def your_score(score):

    if score >=90:
        print("You're great!")
        print("Well done!!!")

    elif score >=60:
        print("You are pass!")
        print("congratulation")
    
    else:
        print("You are fail")
        print("You should work hard")

    print("End of the process")

your_score(60)

def your_score(score):
    if score >=90:
        print("You're great!")
        print("Well done!!!")
    else:
        if score >=60:
            print("You are pass!")
            print("congratulation")
        else:
            print("You are fail")
            print("You should work hard")
    print("End of the process")

your_score(45)

def kisetsu(season):
    if season == "spring":
        print("春はあけぼの")
    elif season == "summer":
        print("夏は夜")
    elif season == "autumn":
        print("秋は夕暮れ")
    elif season == "winter":
        print("冬はつとめて")

    else :
        print("エラー")

    print("処理を終了します")

kisetsu("autumn")

def kisetsu(season):
    match season:
        case "spring":
            print("春はあけぼの")
        case "summer":
            print("夏は夜")
        case "autumn":
            print("秋は夕暮れ")
        case "winter":
            print("冬はつとめて")
        case _:
            print("エラー")
    print("処理を終了します")
kisetsu("autumn")
