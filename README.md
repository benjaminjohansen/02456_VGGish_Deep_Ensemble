# 02456_VGGish_Deep_Ensemble
A VGGish implementation with Deep Ensemble used for the TUT Acoustic Scene dataset

### Download data samples and pre-trained weights:
Pretrained model weights (aprox. 660 mb):
wget https://www.dropbox.com/s/i5ufh61xzox5f05/VGGish_concate1.ckpt.data-00000-of-00001?dl=0

If you want to only use the test data, download the following subsample (aprox. 800 mb)

wget https://www.dropbox.com/s/9lnnuabmy6jqi4d/Eval1_RIGHT.pickle

wget https://www.dropbox.com/s/6g2ujcajfrrsxja/Eval1.pickle

If you want to train the model use the following

wget http://www.dropbox.com/s/x7t82y3kzmzhdc2/logmel_subset1.pickle

wget https://www.dropbox.com/s/1gd6gmyjrzo6auj/logmel_subset1_right.pickle



### Run the notebook
Open the jupyter notebook A_vggish_Ensemble-Lite. Make sure you are running Python 3.0 and Tensorflow 1.2.
Data download links are in the script.

The following script will run a lite version of a VGGish Ensemble method to be used on the [TUT Acoustic Scene data set](cs.tut.fi/sgn/arg/dcase2017/challenge/task-acoustic-scene-classification-results#). 

The first parts of the script will import the data, split as specified at the competion. For this version, a subset of preprossed data has been added. To run the fool data, use the logmel converter script, and place the files accordingly.

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
