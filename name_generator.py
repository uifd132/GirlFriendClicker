import csv
import numpy as np
import sys

def nameGen():
    if sys.platform == 'win32':
        string = r".\GirlNames.csv"
    else:
        string = r"./GirlNames.csv"
    with open(string) as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        names = [row for row in reader]

    names = np.asarray(names)
    names = names[:,0]
    length = names.size
    r = np.random.randint(0,length)

    return names[r]
