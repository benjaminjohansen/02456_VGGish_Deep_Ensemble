# 02456_VGGihs_Deep_Ensemble
A VGGish implementation with Deep Ensemble used for the TUT Acoustic Scene dataset

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
