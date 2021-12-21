
# !pip install wmd
# !pip install summ-eval
# !pip install bert_score
# !pip install sacrebleu
# !pip install wmd
# !pip install sentencepiece
# !pip install .nmt_bleu
# !pip install datasets
# !pip install nltk

""" Bleu Metric"""

from multiprocessing import Pool
import gin
import sacrebleu
from summ_eval.metric import Metric

_DESCRIPTION = " "

_KWARGS_DESCRIPTION = " "

_CITATION = " "

class BleuMetric(Metric):
    
    def __init__(self, sent_smooth_method='exp', sent_smooth_value=None, sent_use_effective_order=True, \
       smooth_method='exp', smooth_value=None, force=False, lowercase=False, \
       use_effective_order=False, n_workers=24):
        """
        BLEU metric

        Args:
                :param smooth_value: For 'floor' smoothing, the floor value to use.
                :param use_effective_order: Account for references that are shorter than the largest n-gram.
                :param force: Ignore data that looks already tokenized
                :param lowercase: Lowercase the data
                :param n_workers: number of processes to use if using multiprocessing
                sent* parameters are the same but specify what is used for evaluate_example

        """
        self.sent_smooth_method = sent_smooth_method
        self.sent_smooth_value = sent_smooth_value
        self.sent_use_effective_order = sent_use_effective_order
        self.smooth_method = smooth_method
        self.smooth_value = smooth_value
        self.force = force
        self.lowercase = lowercase
        self.use_effective_order = use_effective_order
        self.n_workers = n_workers

    def evaluate_example(self, summary, reference):
        if isinstance(reference, str):
            reference = [reference]
        score = sacrebleu.sentence_bleu(summary, reference, smooth_method=self.sent_smooth_method, \
             smooth_value=self.sent_smooth_value, use_effective_order=self.sent_use_effective_order)
        score_dict = {"bleu" : score.score}
        return score.score

   os.rename(old_name, new_name)

""" Bleu Scores"""

#Load summaries and references...

from pathlib import Path 
bleu = BleuMetric() 

ref = []
for index in range(50):
  txt = Path(str(index)+'.ref').read_text()
  ref.append(txt)

loop_sum = []
for index in range(50):
  txt = Path("loop_sum_"+str(index)+'.dec').read_text()
  loop_sum.append(txt)

match_sum = []
for index in range(50):
  txt = Path("match_sum_"+str(index)+'.dec').read_text()
  match_sum.append(txt)

pgen=[]
for index in range(50):
  txt = Path("pgen_"+str(index)+'.dec').read_text()
  pgen.append(txt)
  
pnbert= []
for index in range(50):
  txt = Path("pnbert_"+str(index)+'.dec').read_text()
  pnbert.append(txt)

#Calculate scores...

loop_sum_bleu = []
for index in range(50):
  score = bleu.evaluate_example(loop_sum[index],ref[index])
  loop_sum_bleu.append(score)
  #print(score)

match_sum_bleu = []
for index in range(50):
  score = bleu.evaluate_example(match_sum[index],ref[index])
  match_sum_bleu.append(score)
  #print(score)

pgen_bleu = []
for index in range(50):
  score = bleu.evaluate_example(pgen[index],ref[index])
  pgen_bleu.append(score)
  #print(score)

pnbert_bleu = []
for index in range(50):
  score = bleu.evaluate_example(pnbert[index],ref[index])
  pnbert_bleu.append(score)


import sacrebleu as scb
from packaging import version
from sacrebleu import CHRF

import datasets

@datasets.utils.file_utils.add_start_docstrings(_DESCRIPTION, _KWARGS_DESCRIPTION)

class ChrF(datasets.Metric):

    def _compute(
        self,
        predictions,
        references,
        char_order: int = CHRF.CHAR_ORDER,
        word_order: int = CHRF.WORD_ORDER,
        beta: int = CHRF.BETA,
        lowercase: bool = False,
        whitespace: bool = False,
        eps_smoothing: bool = False,
    ):
        references_per_prediction = len(references[0])
        if any(len(refs) != references_per_prediction for refs in references):
            raise ValueError("Sacrebleu requires the same number of references for each prediction")
        transformed_references = [[refs[i] for refs in references] for i in range(references_per_prediction)]

        sb_chrf = CHRF(char_order, word_order, beta, lowercase, whitespace, eps_smoothing)
        output = sb_chrf.corpus_score(predictions, transformed_references)

        return output.score

"""## Chrf Score"""

C = ChrF()

#Calculate scores...

loop_sum_chrf = []
for index in range(50):
  score = C._compute(loop_sum[index],ref[index])
  loop_sum_chrf.append(score)
  #print(score)

match_sum_chrf = []
for index in range(50):
  score = C._compute(match_sum[index],ref[index])
  match_sum_chrf.append(score)
  #print(score)

pgen_chrf = []
for index in range(50):
  score = C._compute(pgen[index],ref[index])
  pgen_chrf.append(score)
  #print(score)

pnbert_chrf = []
for index in range(50):
  score = C._compute(pnbert[index],ref[index])
  pnbert_chrf.append(score)
  #print(score)

""" METEOR metric. """

nltk.download('wordnet')
import nltk
nltk.download('punkt')
import numpy as np
from nltk.translate import meteor_score
import datasets
from datasets.config import importlib_metadata, version
NLTK_VERSION = version.parse(importlib_metadata.version("nltk"))
if NLTK_VERSION >= version.Version("3.6.4"):
    from nltk import word_tokenize

@datasets.utils.file_utils.add_start_docstrings(_DESCRIPTION, _KWARGS_DESCRIPTION)
class Meteor(datasets.Metric):

    def _compute(self, predictions, references, alpha=0.9, beta=3, gamma=0.5):
        if NLTK_VERSION >= version.Version("3.6.4"):
            scores = [
                meteor_score.single_meteor_score(
                    word_tokenize(ref), word_tokenize(pred), alpha=alpha, beta=beta, gamma=gamma
                )
                for ref, pred in zip(references, predictions)
            ]
        else:
            scores = [
                meteor_score.single_meteor_score(ref, pred, alpha=alpha, beta=beta, gamma=gamma)
                for ref, pred in zip(references, predictions)
            ]

        return {"meteor": np.mean(scores)}

"""## Meteor Scores"""

M = Meteor()

#Calculate scores...

loop_sum_meteor = []
for index in range(50):
  score = M._compute(loop_sum[index],ref[index])
  loop_sum_meteor.append(score)
  #print(score)

match_sum_meteor = []
for index in range(50):
  score = M._compute(match_sum[index],ref[index])
  match_sum_meteor.append(score)
  #print(score)

pgen_meteor = []
for index in range(50):
  score = M._compute(pgen[index],ref[index])
  pgen_meteor.append(score)
  #print(score)

pnbert_meteor = []
for index in range(50):
  score = M._compute(pnbert[index],ref[index])
  pnbert_meteor.append(score)
  #print(score)