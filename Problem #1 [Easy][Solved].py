'''

    This problem was recently asked by Google.

    Given a list of numbers and a number k  return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

    Bonus: Can you do this in one pass?  '''
def sum (list) :
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (list[i] + list[j] == k):
                return True
    return False

list = [10,15,3,7]
k = 9
n = len(list)

print(sum(list))




