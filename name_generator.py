import csv
import numpy as np

def gen_name():
    with open(r".\GirlNames.csv") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        names = [row for row in reader]
    
    names = np.asarray(names)
    names = names[:,0]
    length = names.size
    r = np.random.randint(0,length)  
        
    return names[r]