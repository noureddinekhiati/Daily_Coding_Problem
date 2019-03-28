'''

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers
in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

'''

def mult (list ,index) :
    n = len(list)
    product = 1
    for i in range(n):
        if i == index : continue
        product = product * list[i]
    return product


def construct_list (list) :
    list2 = []
    for i in range(len(list)):
        list2.append(mult(list,i))
    return list2

list = [1, 2, 3, 4, 5]
print(construct_list(list))
