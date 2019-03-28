'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


'''
def min (list):
    n = len(list)
    for i in range(n):
        if(list[i]>0):
            minimum = i
            break
    for i in range(n):
        if(list[i]<list[minimum] and list[i]>0):
            minimum = i
    return list[minimum]

def first_missing(list):
    n = len(list)
    i = 0
    min_elt = min(list)+1
    while (i<n) :
        if(list[i]==min_elt):
            i = 0
            min_elt = min_elt + 1
        else: i = i + 1
    return min_elt

list = [3, 4, -1, 1]
print(first_missing(list))
