# python3 competitive cheatsheat

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

# load and export pickle data
p = open(PickleFileName, "wb")
pickle.dump(df, p)
p.close()
p  = open(PickleFileName,"rb")
see = pickle.load(p)
p.close()


# load json address
f =  open(path_to_json)
data = json.load(f)
f.close()
# write/export json file
with open(json_file_name+".json", 'w') as file:
    json_string = json.dumps(dct, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    file.write(json_string)
