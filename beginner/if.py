import operator
from enum import Enum

class ComparisonOperator(Enum):
    greater_than = 1
    less_than = 2
    equals_to = 3
    different_from = 4

#funzione che prende in argomento l'operatore di comparison
def compare_values(firstCondition, secondCondition, comparison_operator):
    return comparison_operator(firstCondition, secondCondition)

print("insert your first part of condition")
firstCondition = input()

print("insert your second part of condition")
secondCondition = input()

print("choose the number of your comparison")

for comp_operator in ComparisonOperator:
    if comp_operator.value == 1:
        print("1: >")
    elif comp_operator.value == 2:
        print("2: <")
    elif comp_operator.value == 3:
        print("3: ==")
    else:
        print("4: !=")

for comp_operator in ComparisonOperator:
    print(comp_operator.name)






