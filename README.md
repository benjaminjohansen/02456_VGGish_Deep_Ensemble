# 02456_VGGish_Deep_Ensemble
A VGGish implementation with Deep Ensemble used for the TUT Acoustic Scene dataset.

Due to limit on the size of files that can be uploaded to github links to the data and pretrained weights found on dropbox is given. Due to lack of space on dropbox only a subset of the data is given.

If you want to run the full dataset the data can be downloaded from [TUT Acoustic Scene data set](http://www.cs.tut.fi/sgn/arg/dcase2017/challenge/task-acoustic-scene-classification#audio-dataset). It should then be converted to 16bit with the file 24to16bit.py. Spectrograms and onehot encoded labels can then be created by using the script logmel_converter.py with either vggish_input.py or vggish_input_RIGHT to create mono and right spectrograms, respectively.

To run just a subset of the data, do the following:

### Download preprocessed data samples and pretrained weights:
If you want to train the model the pretrained model weights for the original VGGish model (baseline) can be found here:

wget https://www.dropbox.com/s/txxoxkuxdc0ivfm/vggish_model.ckpt?dl=0

If you want to just test the model the trained model weights for the final model can be found here (approx. 660 mb):

wget https://www.dropbox.com/sh/9f8gjav0iqkp274/AACXXWlFQ9WEQui9vH72LW6Ja?dl=0

Use the file soundname1.pickle from the folder Data as well.

If you want to only use the test data, download the following subsample (approx. 800 mb)

wget https://www.dropbox.com/s/9lnnuabmy6jqi4d/Eval1_RIGHT.pickle

wget https://www.dropbox.com/s/6g2ujcajfrrsxja/Eval1.pickle

If you want to train the model use the following

wget http://www.dropbox.com/s/x7t82y3kzmzhdc2/logmel_subset1.pickle

wget https://www.dropbox.com/s/1gd6gmyjrzo6auj/logmel_subset1_right.pickle



### Run the notebook
Open the jupyter notebook A_vggish_Ensemble-Lite. Make sure you are running Python 3.0 and Tensorflow 1.2.

The script will run a lite version (only a subset of the data) of a VGGish Ensemble method to be used on the [TUT Acoustic Scene data set](http://www.cs.tut.fi/sgn/arg/dcase2017/challenge/task-acoustic-scene-classification#audio-dataset). 

The VGGish Deep Ensemble consist of:
A VGGish implementation proposed by Hershey, S. et. al., [CNN Architectures for Large-Scale Audio Classification](https://research.google.com/pubs/pub45611.html), ICASSP 2017
 
![VGGish implementation](https://github.com/benjaminjohansen/02456_VGGihs_Deep_Ensemble/blob/master/figs/VGGish.PNG)

The baseline model looks like

![Baseline](https://github.com/benjaminjohansen/02456_VGGihs_Deep_Ensemble/blob/master/figs/flowchart_baseline.png)

And our implementation:

![Deep Ensemble](https://github.com/benjaminjohansen/02456_VGGihs_Deep_Ensemble/blob/master/figs/Toplayers.PNG)

The full model is like this:

![final flowchart](https://github.com/benjaminjohansen/02456_VGGihs_Deep_Ensemble/blob/master/figs/flowchart_final.png)

Contributors:
Amalie Ekstrand, Benjamin Johansen, and Sofie Knøsgaard
