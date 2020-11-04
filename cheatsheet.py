# python3 competitive cheatsheat

# intersection of list or set
intersec = list(set(jan) & set(feb))


# taking with space

 A = input().split() # python 3 type(string)
    or
 A= raw_input().split() #python2
# sort in decreasing order
ist_name=[1,2,3,4,5]
ist_name.sort(reverse=True)

#Binary to Int
binary1 = "0b100"
print(int(binary1,2))

#Int to binary
IntA= 10
print(bin(intA).replace("0b",""))

#Add Binary Number
binary1 = "0b100"
binary2 = "0b110"

integer_sum = int(binary1, 2) + int(binary2, 2)
binary_sum = bin(integer_sum)
print(binary_sum)


# implement min and maxheap
import heapq 
L=[10,20,5,90,52]
negL=[-10,-20,-5,-90,-52]
MinH = heapq.heapify(L) #min heap
MaxH = heapq.heapify(negL) #min heap
MinH.heapq.heappush(18)
MaxH.heapq.heappush(-1*18)
MinH.heapq.heappop()  # return 5
MaxH.heapq.heappop()  # return 90

# lambda function and reduce
from functools import reduce 
L = [1,2,3,4,5]
mulL= reduce(lambda x,y :x*y, L) #return 120


# list of int to string
s = ['8','80']
print("".join(s))
# 880

# split string in list without split
string ="abcdefg"
intstr= 1234567890
i,s=[],[]
i[:0]=str(intstr)
print(i)

s[:0]=string
print(s)

# append list in list from beginning
i[:0]=s
print(i)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# add list in list from beggining=s
print(i+s)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g']

# concat integer digit in int
type(eval(f"{10}{20}"))

# list comprehension
s = [x for x in i]

# sort with comparator function
from functools import cmp_to_key
def desc(a,b):
    if b>a:
        return -1
    else:
        return 1

data = [4,3,99,90,2,1]
print(sorted(data, key=cmp_to_key(compare)))

# permmutation & combination of list
from itertools import permutations 
from itertools import combinations 
from itertools import combinations_with_replacement

a_list = [1, 2, 3, 1]
p = permutations(a_list,2)
c = combinations(a_list,2)
cr =combinations_with_replacement(a_list,3)
permutations_list = list(p)
combinations_list =list(c)
combinations_with_replacement_list=list(cr)

print(permutations_list)

print(combinations_list)

print(combinations_with_replacement_list)
# [(1, 2), (1, 3), (1, 1), (2, 1), (2, 3), (2, 1), (3, 1), (3, 2), (3, 1), (1, 1), (1, 2), (1, 3)]

# [(1, 2), (1, 3), (1, 1), (2, 3), (2, 1), (3, 1)]

# [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 1), (1, 2, 2), (1, 2, 3), (1, 2, 1), (1, 3, 3), (1, 3, 1), 
# (1, 1, 1), (2, 2, 2), (2, 2, 3), (2, 2, 1), (2, 3, 3), (2, 3, 1), (2, 1, 1), (3, 3, 3), (3, 3, 1), 
# (3, 1, 1), (1, 1, 1)]
