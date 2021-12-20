import numpy as np
import pandas as pd
from sklearn import preprocessing
from scipy.stats import kendalltau
import random
import csv

files = ["MatchSum", "PNSum", "PointGen", "LoopSum"]

meanscores = [["", "human-relevance", "human-coherence", "rouge 1", "rouge2", "rouge3", "rouge4", "rougeL", "bleu", "chrf", "meteor"]]

for ff in files:
    scores = pd.read_csv("./data/" + ff + ".csv")

    hr = np.array(scores['human-rel'])
    hc = np.array(scores['human-coh'])

    r1 = np.array(scores['rouge1'])
    r2 = np.array(scores['rouge2'])
    r3 = np.array(scores['rouge3'])
    r4 = np.array(scores['rouge4'])
    rL = np.array(scores['rougeL'])
    bl = np.array(scores['bleu'])
    ch = np.array(scores['chrf'])
    me = np.array(scores['meteor'])

    hrm =np.mean(hr)
    hcm =np.mean(hc)

    r1m = np.mean(r1)
    r2m = np.mean(r2)
    r3m = np.mean(r3)
    r4m = np.mean(r4)
    rLm = np.mean(rL)
    blm = np.mean(bl)
    chm = np.mean(ch)
    mem = np.mean(me)

    means = [ff, hrm, hcm, r1m, r2m, r3m, r4m, rLm, blm, chm, mem]
    meanscores.append(means)


    correlations = [[" ", "rouge 1", "rouge2", "rouge3", "rouge4", "rougeL", "bleu", "chrf", "meteor"]]

    for dn, dim in [("relevance", hr), ("coherence", hc)]:
        cr = [dn]
        for en, ev in [("r1", r1), ("r2", r2), ("r3", r3), ("r4", r4), ("rL", rL), ("bl", bl), ("ch", ch), ("me", me)]:
            kcor, kp = kendalltau(dim, ev)
            cr.append(kcor)
        correlations.append(cr)

    with open('./results/' + ff + ".csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for rrow in correlations:
            writer.writerow(rrow)

with open("./results/Means.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for sc in meanscores:
        writer.writerow(sc)
