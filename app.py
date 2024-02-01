from enum import Enum
import random
import string


class App:
    clsattr1 = 1

    def __init__(self, attr):
        self.clsattr = attr
        self.clsattr1 = attr


app = App(2)
print(app.clsattr)
print(App.clsattr1)


def add_factor(factor):
    def inner(b):
        return factor+b
    return inner

f_with_add_factor = add_factor(5)

print(f_with_add_factor(7))


# как передать параметры в фикстуру напрямую
# def calc_data(a, b):
#     return a+b
#
# @pytest.fixture()
# def get_data():
#     return calc_data


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("BEFORE")
            result = []
            for _ in range(n):
                r = func(*args, **kwargs)
                result.append(r)
            print("AFTER")
            return result
        return wrapper
    return decorator


@repeat(3)
def say_hi(name):
    print(f"Hi, my name is {name}")
    return 1

print(say_hi("Dima"))

num = 231

result = 0

while num:
    result += num % 10  # 1, 3, 2
    num = num // 10  # 23 2 0

print(result)

if num < 0:
    print("Negative")
else:
    print("Positive")

s1 = "Nagative"
s2 = "Positive"

print(s1[s1.index("a")::-1])

chislo = -6327
lst = [1, 2, 3, 4, 5, 6]
print(lst[::2])

print(len(str(abs(chislo))))

print(set(list(s1)))
d = {
    'year': '2025',
    'month': '12',
    'day': '31',
}

print(f"{d['year']}-{d['month']}-{d['day']}")

print(list(range(1, 101))[::-1])

lstq = [i for i in range(1, 101) if i % 3 == 0]

print(lstq)

dd = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

sum_d = sum(dd.values())
sum_dsqrt = {key: value*2 for key, value in dd.items()}

print(sum_dsqrt)

password_string = "".join([random.choice(string.ascii_lowercase) for n in range(8)])
password_string2 = "".join(random.choices(string.ascii_lowercase, k=8))

print(password_string)
print(password_string2)

string = "Python - это отличный язык программирования. Python предоставляет простой синтаксис и мощные инструменты."

non_word_symbols = ".-"
unique_words = list(set([word.strip(non_word_symbols) for word in string.split() if word not in non_word_symbols]))

print(unique_words, len(unique_words))


class Status(str, Enum):
    OK = 0
    ERROR = 1
    WARNING = 2

    def __str__(self):
        return self.value


print(Status.ERROR)


def func_name(*args, **kwargs):
    return "Run function"


def is_palindrome(str_value: str) -> bool:
    reversed_str_value = reversed(str_value)
    for i in range(int((len(str_value)-1)/2)):
        if str_value[i] != next(reversed_str_value):
            return False

    return True


def is_palindrome_iter(str_value: str) -> bool:
    left = 0
    right = len(str_value) - 1

    while left < right:
        if str_value[left] != str_value[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(func_name())

    print(is_palindrome_iter("fdfdjajdfdf"))

