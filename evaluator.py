from sacrebleu import CHRF
import nltk
from nltk.translate import meteor_score
nltk.download('wordnet')


chrf = CHRF()

ref=[]
pred=[]
for index in range(50):
    with open('./Comp550_Final_Project/ref/' + str(index) + '.ref', "r") as f:
        txt = f.readlines()
        ref.append(txt)

for index in range(50):
    with open('./Comp550_Final_Project/dec/PGen/' + str(index) + '.dec', "r") as f:
        txt = f.readlines()
        pred.append(txt)

for i in range(50):
    print(meteor_score.single_meteor_score("".join(ref[i]), "".join(pred[i]), alpha=0.9, beta=3, gamma=0.5))

for i in range(50):
    print(chrf.corpus_score(pred[i], [ref[i]]))

