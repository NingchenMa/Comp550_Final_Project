# -*- coding: utf-8 -*-
"""gen_diagrams.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q5d5tPkcwBgrzeuWX7TKH2NNuaeAyBM4
"""

import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

loopsum = pd.read_csv('LoopSum.csv')
matchsum = pd.read_csv('MatchSum.csv')
pnsum = pd.read_csv('PNSum.csv')
pointgen = pd.read_csv('PointGen.csv')

models=[]
models.append(loopsum)
models.append(matchsum)
models.append(pnsum)
models.append(pointgen)

"""## LoopSum model

### Relavence
"""

loopsum_rel=[]
for index in range(2,10):
  cols = [0,index]
  df = loopsum[loopsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  tau, p_value = stats.kendalltau(t1, t2)
  loopsum_rel.append(tau)
print(loopsum_rel)

"""### Coherence"""

loopsum_coh=[]
for index in range(2,10):
  cols = [1,index]
  df = loopsum[loopsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  tau, p_value = stats.kendalltau(t1, t2)
  loopsum_coh.append(tau)
print(loopsum_coh)

"""### Table"""

loopsum_rel = ["Relavence"]+loopsum_rel
loopsum_coh = ["Coherence"]+loopsum_coh
loopsum_table = [loopsum_rel,loopsum_coh]
loopsum_table


df = pd.DataFrame(loopsum_table, columns =["correlation",'Rouge 1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor'],
                                           dtype = float) 
display(df)

"""### Plots"""

evaluators = ['Rouge_1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor']
pointgen_rel=[]
for index in range(2,10):
  a=index
  cols = [0,index]
  df = loopsum[loopsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  plt.figure()
  plt.scatter(t2, t1, alpha=0.5)
  plt.title("LoopSum Model")
  plt.xlabel(evaluators[a-2])
  plt.ylabel("Relavence")
  name = 'LoopSum_'+'Relavence_'+evaluators[a-2] +'.png'
  plt.savefig(name)
  plt.show()
  plt.close()
  from google.colab import files
  files.download('/content/'+name)

evaluators = ['Rouge_1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor']
pointgen_rel=[]
for index in range(2,10):
  a=index
  cols = [1,index]
  df = loopsum[loopsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  plt.figure()
  plt.scatter(t2, t1, alpha=0.5)
  plt.title("LoopSum Model")
  plt.xlabel(evaluators[a-2])
  plt.ylabel("Coherence")
  name = 'LoopSum_'+'Coherence_'+evaluators[a-2] +'.png'
  plt.savefig(name)
  plt.show()
  plt.close()
  from google.colab import files
  files.download('/content/'+name)

"""## MatchSum

### Relavence
"""

matchsum_rel=[]
for index in range(2,10):
  cols = [0,index]
  df = matchsum[matchsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  tau, p_value = stats.kendalltau(t1, t2)
  matchsum_rel.append(tau)
print(matchsum_rel)

"""### Coherance"""

matchsum_coh=[]
for index in range(2,10):
  cols = [1,index]
  df = matchsum[matchsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  tau, p_value = stats.kendalltau(t1, t2)
  matchsum_coh.append(tau)
print(matchsum_coh)

"""### Table"""

matchsum_rel = ["Relavence"]+matchsum_rel
matchsum_coh = ["Coherence"]+matchsum_coh
matchsum_table = [matchsum_rel,matchsum_coh]
matchsum_table


df = pd.DataFrame(matchsum_table, columns =["correlation",'Rouge 1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor'],
                                           dtype = float) 
display(df)

"""### Plots"""

evaluators = ['Rouge_1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor']
pointgen_rel=[]
for index in range(2,10):
  a=index
  cols = [0,index]
  df = matchsum[matchsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  plt.figure()
  plt.scatter(t2, t1, alpha=0.5)
  plt.title("MatchSum Model")
  plt.xlabel(evaluators[a-2])
  plt.ylabel("Relavence")
  name = 'MatchSum_'+'Relavence_'+evaluators[a-2] +'.png'
  plt.savefig(name)
  plt.show()
  plt.close()
  from google.colab import files
  files.download('/content/'+name)

evaluators = ['Rouge_1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor']
pointgen_rel=[]
for index in range(2,10):
  a=index
  cols = [1,index]
  df = matchsum[matchsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  plt.figure()
  plt.scatter(t2, t1, alpha=0.5)
  plt.title("MatchSum Model")
  plt.xlabel(evaluators[a-2])
  plt.ylabel("Coherence")
  name = 'MatchSum_'+'Coherence_'+evaluators[a-2] +'.png'
  plt.savefig(name)
  plt.show()
  plt.close()
  from google.colab import files
  files.download('/content/'+name)

"""## PNSum

### Relavence
"""

pnsum_rel=[]
for index in range(2,10):
  cols = [0,index]
  df = pnsum[pnsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  tau, p_value = stats.kendalltau(t1, t2)
  pnsum_rel.append(tau)
print(pnsum_rel)

"""### Coherence"""

pnsum_coh=[]
for index in range(2,10):
  cols = [1,index]
  df = pnsum[pnsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  tau, p_value = stats.kendalltau(t1, t2)
  pnsum_coh.append(tau)
print(pnsum_coh)

pnsum_rel = ["Relavence"]+pnsum_rel
pnsum_coh = ["Coherence"]+pnsum_coh
pnsum_table = [pnsum_rel,pnsum_coh]
pnsum_table


df = pd.DataFrame(pnsum_table, columns =["correlation",'Rouge 1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor'],
                                           dtype = float) 
display(df)

"""### Plots"""

evaluators = ['Rouge_1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor']
pointgen_rel=[]
for index in range(2,10):
  a=index
  cols = [0,index]
  df = pnsum[pnsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  plt.figure()
  plt.scatter(t2, t1, alpha=0.5)
  plt.title("PNSum Model")
  plt.xlabel(evaluators[a-2])
  plt.ylabel("Relavence")
  name = 'PNSum_'+'Relavence_'+evaluators[a-2] +'.png'
  plt.savefig(name)
  plt.show()
  plt.close()
  from google.colab import files
  files.download('/content/'+name)

evaluators = ['Rouge_1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor']
pointgen_rel=[]
for index in range(2,10):
  a=index
  cols = [1,index]
  df = pnsum[pnsum.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  plt.figure()
  plt.scatter(t2, t1, alpha=0.5)
  plt.title("PNSum Model")
  plt.xlabel(evaluators[a-2])
  plt.ylabel("Coherence")
  name = 'PNSum_'+'Coherence_'+evaluators[a-2] +'.png'
  plt.savefig(name)
  plt.show()
  plt.close()
  from google.colab import files
  files.download('/content/'+name)

"""## PointGen

### Relavence
"""

pointgen_rel=[]
for index in range(2,10):
  cols = [0,index]
  df = pointgen[pointgen.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  tau, p_value = stats.kendalltau(t1, t2)
  pointgen_rel.append(tau)
print(pointgen_rel)

evaluators = ['Rouge_1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor']
pointgen_rel=[]
for index in range(2,10):
  a=index
  cols = [1,index]
  df = pointgen[pointgen.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  plt.figure()
  plt.scatter(t2, t1, alpha=0.5)
  plt.title("PointGen Model")
  plt.xlabel(evaluators[a-2])
  plt.ylabel("Coherence")
  name = 'PointGen_'+'Coherence_'+evaluators[a-2] +'.png'
  plt.savefig(name)
  plt.show()
  plt.close()
  from google.colab import files
  files.download('/content/'+name)

evaluators = ['Rouge_1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor']
pointgen_rel=[]
for index in range(2,10):
  a=index
  #print("evaluator "+str(index))
  cols = [0,index]
  df = pointgen[pointgen.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  plt.figure()
  plt.scatter(t2, t1, alpha=0.5)
  plt.title("PointGen Model")
  plt.xlabel(evaluators[a-2])
  plt.ylabel("Relavence")
  name = 'PointGen_'+'Relavence_'+evaluators[a-2] +'.png'
  plt.savefig(name)
  plt.show()
  plt.close()
  from google.colab import files
  files.download('/content/'+name)

"""### Coherence"""

pointgen_coh=[]
for index in range(2,10):
  cols = [1,index]
  df = pointgen[pointgen.columns[cols]]
  df=df.values.tolist()
  t1=[]
  t2=[]
  for index in range(len(df)):
    t1.append(df[index][0])
  for index in range(len(df)):
    t2.append(df[index][1])
  tau, p_value = stats.kendalltau(t1, t2)
  pointgen_coh.append(tau)
print(pointgen_coh)

pointgen_rel = ["Relavence"]+pointgen_rel
pointgen_coh = ["Coherence"]+pointgen_coh
pointgen_table = [pointgen_rel,pointgen_coh]
pointgen_table


df = pd.DataFrame(pointgen_table, columns =["correlation",'Rouge 1', 'Rouge 2', 'Rouge 3','Rouge 4','Rouge L','Bleu', 'Chrf','Meteor'],
                                           dtype = float) 
display(df)

"""### Plots"""