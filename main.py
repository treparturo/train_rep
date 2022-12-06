class Man:
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Invalid type, expected 'str'")
        self.__name = value

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Invalid type, expected 'int'")
        self.__age = value

    def do_work(self):
        print(f'man {self.name} is working')

    def __init__(self):
        self.__name: str = ''
        self.__age: int = 10


class Engineer(Man):
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Invalid type, expected 'str'")
        self.__category = value

    def do_work(self):
        print(f'engineer {self.name} is working')

    def __init__(self):
        self.__name: str = ''
        self.__age: int = 10
        self.__category: str = ''


class Medic(Man):
    @property
    def hospital(self) -> str:
        return self.__hospital

    @hospital.setter
    def hospital(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Invalid type, expected 'str'")
        self.__hospital = value

    def do_work(self):
        print(f'medic {self.name} is working')

    def __init__(self):
        self.__name: str = ''
        self.__age: int = 10
        self.__hospital: str = ''


e = Engineer()
e.name = "Kostya"
e.category = 'A'

m = Medic()
m.name = "Alena"
m.hospital = "Central"

men = [e, m]
for man in men:
    man.do_work()

# Encapsulation
# class CombEng:
#
#     def __init__(self):
#         self.__type: str = ''
#         self.__liter: int = 2
#
#     @property
#     def type(self) -> str:
#         return self.__type
#
#     @type.setter
#     def type(self, value: str):
#         if not isinstance(value, str):
#             raise TypeError("Expected string value!")
#         self.__type = value
#
#     @property
#     def liter(self) -> int:
#         return self.__liter
#
#     @liter.setter
#     def liter(self, value: int):
#         if value < 1:
#             raise ValueError("Engine must have capacity more than 1 liter!")
#         self.__liter = value
#
#
# petrol = CombEng()
# petrol.type = "gasoline"
# petrol.liter = 2
# print(petrol.type)
# print(petrol.liter)


# CODEWARS EXERCISES
'''
There are two lists, possibly of different lengths. The first one consists of keys, the second one consists of values.
Write a function createDict(keys, values) that returns a dictionary created from keys and values.
If there are not enough values, the rest of keys should have a None (JS null)value.
If there not enough keys, just ignore the rest of values.

Example 1:

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}

Example 2:

keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}
'''

# def createDict(keys, values):
#     """
#     Write your code here.
#     """
#     dict = {}
#
#     if len(keys) < len(values):
#         dict = {keys[n]: values[n] for n in range(len(keys))}
#
#     if len(values) < len(keys):
#         for i in range(len(keys) - len(values)):
#             values.append(None)
#         dict = {keys[n]: values[n] for n in range(len(values))}
#
#     else:
#         dict = {keys[n]: values[n] for n in range(len(keys))}
#
#     print(dict)
#
#
# keys = ["a", "b", "c", "d"]
# values = [1, 2, 3]
# createDict(keys, values)

# List in reverse

# def reverse_list(l):
#
#     for i in range(len(l)):
#         last_el = l.pop()
#         l.insert(i, last_el)
#
#     print(l)
#
# l = [1, 2, 3, 4]
# reverse_list(l)


# def next_item(xs, item):
#     a = next(xs, item)
#     return a
#     # if item not in xs:
#     #     return None
#     # else:
#     #     return None

# xs = iter(range(1, 30000))
# item = 12
# it = iter(xs)
# next(iter(x for x in it if x == item), None)
# print(next(it, None))

# def my_languages(results):
#     # your fantastic code here
#     sorted_res = sorted(results, key=results.get(), reverse=True)
#     res = []
#     # Need to receive dictionary and filter it to list with values above 60
#     for key, value in sorted_res.items():
#
#         if value == 60 or value > 60:
#             res.append(key)
#         else:
#             res = []
#
#
#     print(res)
#
#
# results = {"Hindi": 60, "Dutch": 80, "Greek": 65}
# my_languages(results)

# def fac(n):
#     if n == 1: return 1
#     return (n + (fac(n-1)))
#
# n = 5
# print(fac(n))
#

# def func(string):
#     d = {}
#     key = ''
#     value = 0
#     for i in string:
#         if i != ' ':
#             key += i
#         if i == ' ' and key not in d:
#             d.update({key: 1})
#             key = ' '
#         if i == ' ' and key in d:
#             d[key] += 1
#             key = ' '
#     return d
# print(func("as aa fnc aS kka aa a"))

# fgh = [None, 1, 2.2, True, False, 'string', [1, 2], (1, 2), {1, True, 'f'}, {'kot': 44}]

# ctr = iter(fgh)
# while ctr:
#     print(type(next(ctr)))

# def fib():
#     a, b = 0, 1
#     while 1:
#         yield a
#         a, b = b, a + b
#
#
# x = fib()
#
# for i in range(6):
#     print(next(x))

# a_list = [0, 0, 1, 0, True, 'sd']
#
# if any(a_list):
#     print(list(filter(None, a_list)))
#     print([e for e in a_list if e])
#
# if __name__ == '__main__':
#     pass
#     # print(bool(a_list))
#     # print(all(a_list))
#     # print(any(a_list))

# import sqlite3 as sq
#
# with sq.connect('saperr.db') as con:
#     cur = con.cursor()
#     # cur.execute("DROP TABLE IF EXISTS female")
#     # cur.execute("DROP TABLE IF EXISTS students")
#     # cur.execute("DROP TABLE IF EXISTS marks")
#     cur.execute("""CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     sex INTEGER NOT NULL DEFAULT 1,
#     old INTEGER
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS marks (
#     id INTEGER,
#     subject TEXT NOT NULL,
#     mark INTEGER
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS female (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     sex INTEGER NOT NULL DEFAULT 1,
#     old INTEGER
#     )""")
#
#     # cur.execute("DROP TABLE IF EXISTS tab2")
#     # user_id INTEGER PRIMARY KEY AUTOINCREMENT
#
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users (
#     # name TEXT NOT NULL,
#     # sex INTEGER NOT NULL DEFAULT 1,
#     # old INTEGER,
#     # score INTEGER
#     # )""")
#
#     # cur.execute("""CREATE TABLE IF NOT EXISTS games (
#     # user_id TEXT NOT NULL,
#     # score INTEGER,
#     # time INTEGER
#     # )""")
#
#     # cur.execute("""CREATE TABLE IF NOT EXISTS tab1 (
#     # score INTEGER NOT NULL DEFAULT 1,
#     # 'from' TEXT NOT NULL
#     # )""")
#     #
#     # cur.execute("""CREATE TABLE IF NOT EXISTS tab2 (
#     # val INTEGER NOT NULL DEFAULT 1,
#     # type TEXT NOT NULL
#     # )""")
#
#     # cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
#     # # result = cur.fetchall()
#     # result1 = cur.fetchone()
#     # result2 = cur.fetchmany(2)
#     # print(result1, result2)
#     # for result in cur:
#     #     print(result)
#
# # con.close()

#oh my god
#123
