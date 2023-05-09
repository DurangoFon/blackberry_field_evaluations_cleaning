import re 
import numpy as np

def trans_mp(entrada = str):
    regex = re.compile(r'-?\d+.\d+\s\d+.\d+')
    b = regex.findall(entrada)
    regex1 = re.compile(r'-?\d+.\d+')
    d = []
    for i in b:
        c = regex1.findall(i)
        d.append(c)
    d = np.array(d)
    d = d.astype(float)
    return d