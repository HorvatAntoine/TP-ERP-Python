from enum import Enum


class TypeEmploye(Enum):
    DEV = 1
    GESTION = 2

print(TypeEmploye.DEV)
# <Animal.DOG: 1>
print(TypeEmploye.DEV.value)
# 1
print(TypeEmploye.DEV.name)
# DEV