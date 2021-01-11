# copy file via python
from shutil import copyfile
copyfile(src, dst)

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

