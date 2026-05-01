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

i=0
while i <10:
    i += 1
    print(i)
print("End of the program")

i=0
while True:
    i += 1

    if i>10:
        break
    print(i)
print("End of the program")

i=0
while True:
    i += 1
    if i > 10:
        break
    if i % 2 == 1:
        continue
    print(i)
print("処理を終了します")

for i in range(11):
    print(i)

for i in range(1,5):
    print(i) 

for i in range(1,20,3):
    print(i)

for i in range(20,0,-3):
    print(i)

for i in range(11):
    for j in range(0,11,3):
        print(f"{i} + {j} = {i + j}")

i=0
while True:
    i += 1
    if i > 20:
        break
    if i % 2 == 1:
        pass
    print(i)
print("処理を終了します")

i=7
if i != 7 and i % 7 == 0:
    print("７の倍数です")
else:
    print("７の倍数ではありません")
print(i)

i=9
if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
    pass
else:
    print(i)

try:
    score = int(a)
except ValueError:
    print("エラー: 数値を入力してください")
except:
    print("エラー: 何らかのエラーが発生しました")
else:
    if score >= 60:
        print("合格です")
        print("おめでとうございます！")
finally:
    print("処理を終了します")

def kaibun(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = "asikjedjsjl"
result = kaibun(s)

if result:
    print(f"「{s}」は回文です！")
else:
    print(f"「{s}」は回文ではないようです。")


a = [2, 5, 3, 6, 1, 4]
b = ["tanaka", "suzuki", "takahashi"]
c = []

print(c)
type(c)

e = list("aiueo")
e

f = list(range(1,4,6,8))
f

a[0]
b[:1]

nums = []
for i in range(5, 11):
    nums.append(i * 3.14)
nums

fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("orange")
fruits.insert(1, "peach")

counter = 0
for s in fruits:
    print((f"{counter=}, {s=}"))
    counter += 1     

nums = [10, 20, 30]
a, b, c = nums
print(a)
print(b)
print(c)

ta = list("Tech Academy")
char = "e"
char_count = ta.count(char)
if char_count:
    print(f"文字「{char}」はリスト{ta}に{char_count}回含まれます。")
else:
    print(f"文字「{char}」はリスト{ta}に含まれません。")

print(ta.index("a"))

num = [4, 7, 1, 6, 3, 2, 5]
num.reverse()
num

nums = sorted(num)
print(num)
print(nums)

nums2 = sorted(nums, reverse=True)
print(nums)
print(nums2)

nums_oneline = [i * 3.14 for i in range(5, 11)]
nums_oneline

math_numbers = [3.1415926535897, 2.71828182846, 1.618033988749894848204]
math_numbers_new = []
for num in math_numbers:
    math_numbers_new.append(round(num, 3))
math_numbers = math_numbers_new
math_numbers

math_numbers = [3.1415926535897, 2.71828182846, 1.618033988749894848204]
math_numbers = [round(num, 3) for num in math_numbers]
math_numbers

num4 = [i for i in range(11) if i % 2 == 0 and i % 3 ==0]
num4

num4 = ["even" if i % 2 ==0 else "odd" for i in range(11)]
num4

num4 = ["low" if i <3 else "mid" if i < 8 else "hi" for i in range(11)]
num4