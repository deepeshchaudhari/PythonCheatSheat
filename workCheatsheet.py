
# intersection of list or set
intersec = list(set(jan) & set(feb))

# colorfull text in output
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))


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
