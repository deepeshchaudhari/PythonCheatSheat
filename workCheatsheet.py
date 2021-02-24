# access variable from different notebook
# notebook1
a= 45
%store a
# notebook2
%store -r 
print(a)


#  plot graph in python
plt.plot(range(10,20),range(10,20),marker='o')
for cluster,value in zip(range(10,20),range(10,20)): 
    plt.text(cluster,value, str(value))
    
plt.ylabel('y:# of Cosine Similar Accounts')
plt.xlabel('x: Epsilon Value 10^-x')
plt.title("Cosine Similarity Feb(1-28)")
plt.savefig('CosineSimiliarity[1-28feb]-range[10,20]-cluster 9')
-----------------



# sort list of tuple according to tuple key
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]  
tup.sort(key = lambda x:x[1])

# output:[('akash', 5), ('rishav', 10), ('gaurav', 15), ('ram', 20)]

# cosine similiarity between vector
form scipy import spatial
vector1 = [1, 2, 3]
vector2 = [1, 2, 0]

cosine_similarity = 1 - spatial.distance.cosine(vector1, vector2)
print(cosine_similarity)


# union/intersection of multiple set in one line
list_of_set = [{1,2,3},{21,3},{2,3,4}]
unioin_set = set().(*list_of_set)


# replace vlaue in dataframe
nums = {
    'Car Model Number': [223, np.nan, 237, 195, np.nan, 575, 110, 313, np.nan, 190, 143,np.nan], 
	'Engine Number': [4511, np.nan, 7570, 1565, 1450, 3786, 2995, 5345, 7777, 2323, 2785, 1120]
} 
# Create the dataframe 
df = pd.DataFrame(nums, columns =['Car Model Number']) 
# Apply the function 
df['Car Model Number'] = df['Car Model Number'].replace(np.nan, 1) 


# copy file via python
from shutil import copyfile
copyfile(src, dst)

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


# fast operations
out = "<html>%s %s %s %s</html>" % ('head', 'prologue', 'dsaf', 4)

somelist = [4,5,6,2,3,1,5,87]
slist = [str(elt) for elt in somelist]
s = "".join(slist)
# s 456231587



# check dataset contain any NaN or infinite 
import numpy as np
np.all(np.isfinite(y))
np.any(np.isnan(x))

# clean dataset from nan and infinite
import pandas as pd
def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)
#     return dataframe 

# convert name to int label
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['Species']= label_encoder.fit_transform(df['Species']) 
df['Species'].unique() 

# inspect function code
import inspect
print(inspect.getsource(<function_name>))

# progress bar in python
import time
from tqdm import tqdm 
for i in tqdm (range (100), desc="Loading..."): 
    time.sleep(0.1)

# grahs from networkx
multigraph = nx.MultiDiGraph()
digraph = nx.DiGraph()
undirect = nx.Graph()

multigraph.add_edge(1,2)
multigraph.add_node(1)
multigraph.add_node([1,2,3,4,5])


# get date time day from bitcoin timestamp
>>  date -d@1582940628
Sat Feb 29 07:13:48 IST 2020

# miltitreading/multiprocessing
from multiprocessing import Process
p1 = multiprocessing.Process(target = multiprocessing_block, args = (619309,))
p1.start()

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
    
# clear output from screen
from IPython.display import clear_output
print("Hello World!")
clear_output()

# get directory file in list
import os
entries = os.listdir('my_directory/')

