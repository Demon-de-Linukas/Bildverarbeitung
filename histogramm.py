#############################
##
## histogramm.py
## This script provide the method to plot and analyse histogramm.
##
##
#############################
import numpy as np
import time
from matplotlib import pyplot as plt
import scipy.cluster.vq as scp

def matlab_hist(flow,x,y,bins,color,label):
    """

    :param flow: Berechnete Flüsse
    :param x: Position des Pixels zu analysieren
    :param y: Position des Pixels zu analysieren
    :param bins: Anzahl des Bins in Histogramm
    :param color: Farbe des Histogramms
    :param label: zusätzliche Label
    :return:
    """
    n, bins, patches = plt.hist(x=flow[x, y, :], bins=bins, color=color,
                                alpha=0.7, rwidth=0.85,label=label)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.text(23, 45, r'$\mu=15, b=3$')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.legend()

#Flüsse durch Datei lesen
add =''#Pfald der Datei
flow_diskret = np.load(add)
flow_std = (np.std(flow_diskret, axis=2))/(np.mean(flow_diskret, axis=2))


#Histogramm erstellen
plt.figure('Histogram')
matlab_hist(flow_diskret, 132, 175, 30, '#0504aa', 'Spiegel')
matlab_hist(flow_diskret, 363, 331, 30, '#a504aa', 'Kein Spiegelung')
