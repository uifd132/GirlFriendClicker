import numpy as np
from os import listdir
from os.path import isfile, join
from name_generator import nameGen
from classes import girl
import pygame

def girlGen(bought):
    im_path = r"./images/girls"
    g_models = np.asarray([f for f in listdir(im_path) if isfile(join(im_path, f))])
    
    r = np.random.randint(0,g_models.size)
    image = str((r"./images/girls/"+g_models[r]))
    temp_girl = girl(nameGen(),image,2.5**(bought+1))
    return temp_girl