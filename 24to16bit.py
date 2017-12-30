
# coding: utf-8

# In[11]:

# 1. Create a folder called audioConv in your root folder, and move the audio folder to the same place
# 2. run the following script

import soundfile as sf
import glob
import os

'''Extract all filenames and save in audioFile array'''
audioFile = []
globbed_files = glob.glob("audio/*.wav")    # Read in all filenames from folder audio

for i in globbed_files:
    base = (os.path.basename(i))    #get pathname
    filename, file_extension = os.path.splitext(base) #Split pathname in pathname + extension
    audioFile.append(filename) # Append to array audioFile

'''convert audio files from 24bit to 16bit and store in folder audioConv'''
for i in audioFile:
    data, samplerate = sf.read('audio/' + i + '.wav') # Read in each of the 24bit filenames
    sf.write('audioConv/' + i + '.wav', data, samplerate, subtype='PCM_16') #write out 16 bit filenames in the folder audioConv/

print('finished converting 24bit to 16bit')

