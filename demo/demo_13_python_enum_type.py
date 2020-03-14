"""Enum 的数据类型。

当Enum类型也继承其他数据类型的时候，里面的值必须要符合这个值，否则会报错。
"""

from enum import Enum

class User(list, Enum):
    # 如果这里属性的值不是列表，则会报错
    student = [2]
    teacher = [3]

user = User.student
print(user.value)


