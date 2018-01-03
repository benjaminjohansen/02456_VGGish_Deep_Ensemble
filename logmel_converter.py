# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 21:14:37 2017

@author: Sofie
"""

from __future__ import print_function

from random import shuffle

import numpy as np
import tensorflow as tf
import resampy
from scipy.io import wavfile

import vggish_input
import vggish_params
import mel_features

import soundfile as sf
import glob
import os
import pandas as pd
import pickle
import matplotlib.pyplot as plt


# Loading labels
meta = pd.read_csv('meta.txt', delimiter = "\t", header = None)
meta.columns  = ["filenames", "labelstring", "sounds", "d", "e", "f", "g", "h"]

filenames = meta.filenames
labelstring = meta.labelstring
sounds = meta.sounds

# Onehot encoding
num_classes = 15
onehot = np.zeros((labelstring.shape[0], num_classes))

for i in range(0,labelstring.shape[0]):
    if labelstring[i] == 'beach':
        onehot[i,0] = 1
    elif labelstring[i] == 'bus':
        onehot[i,1] = 1
    elif labelstring[i] == 'cafe/restaurant':
        onehot[i,2] = 1
    elif labelstring[i] == 'car':
        onehot[i,3] = 1
    elif labelstring[i] == 'city_center':
        onehot[i,4] = 1
    elif labelstring[i] == 'forest_path':
        onehot[i,5] = 1
    elif labelstring[i] == 'grocery_store':
        onehot[i,6] = 1
    elif labelstring[i] == 'home':
        onehot[i,7] = 1
    elif labelstring[i] == 'library':
        onehot[i,8] = 1
    elif labelstring[i] == 'metro_station':
        onehot[i,9] = 1
    elif labelstring[i] == 'office':
        onehot[i,10] = 1
    elif labelstring[i] == 'park':
        onehot[i,11] = 1
    elif labelstring[i] == 'residential_area':
        onehot[i,12] = 1
    elif labelstring[i] == 'train':
        onehot[i,13] = 1
    elif labelstring[i] == 'tram':
        onehot[i,14] = 1

onehot = onehot.astype(np.int32)

# Loading subset of 16bit audio files
audioFile = []
soundName = []
globbed_files = glob.glob("audioConv1/*.wav")    # Read in all filenames from folder audioConv

for i in globbed_files:
    base = (os.path.basename(i))    #get pathname
    filename, file_extension = os.path.splitext(base) #Split pathname in pathname + extension
    audioFile.append(filename) # Append to array audioFile
    soundName.append(filename[0:4])


# Finding labels corresponding to subset
labels_index = np.zeros((len(audioFile), 1))

for i in range(0,len(audioFile)):
    for j in range(0,labelstring.shape[0]):
        str1 = filenames[j]
        str2 = audioFile[i]
        if (str1.find(str2)) > -1:
            labels_index[i] = j

labels_index = labels_index.astype(np.int32)

# Finding exampels and labels on the right form to use for vggish_train_demo
my_examples = vggish_input.wavfile_to_examples('audioConv1/' + audioFile[0] + '.wav')
my_labels = np.array([onehot[labels_index[0,0]]] * my_examples.shape[0])
for i in range(1,labels_index.shape[0]):
    my_example = vggish_input.wavfile_to_examples('audioConv1/' + audioFile[i] + '.wav')
    my_examples = np.concatenate((my_examples,my_example))
    my_label = np.array([onehot[labels_index[i,0]]] * my_example.shape[0])
    my_labels = np.concatenate((my_labels,my_label))

my_labeled_examples = list(zip(my_examples, my_labels))


my_features = [example for (example, _) in my_labeled_examples]
my_labels = [label for (_, label) in my_labeled_examples]

# Saving labeled examples
with open('logmel_subset1.pickle', 'wb') as f:  # Saving my_feature and my_labels: # Python 3: open(..., 'wb')
    pickle.dump([my_features,my_labels], f)


# Finding names of recordings and corresponding labels
my_labels_sound = np.array([onehot[labels_index[0,0]]]*1)
for i in range(1,labels_index.shape[0]):
    my_label_sound = np.array([onehot[labels_index[i,0]]]*1)
    my_labels_sound = np.concatenate((my_labels_sound,my_label_sound))

with open('soundname1.pickle', 'wb') as f:  # Saving soundName and my_labels_sound: # Python 3: open(..., 'wb')
    pickle.dump([soundName,my_labels_sound], f)






