# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19oLSBEhOG6nriHybRVx0CnomFEI6CQQs
"""

!pip install wmd
!pip install summ-eval
!pip install bert_score
!pip install sacrebleu
!pip install wmd
!pip install sentencepiece
!pip install .nmt_bleu
!pip install datasets
!pip install nltk

"""# Bleu Metric"""

from multiprocessing import Pool
import gin
import sacrebleu
from summ_eval.metric import Metric

_DESCRIPTION = """\
BLEU (bilingual evaluation understudy) is an algorithm for evaluating the quality of text which has been machine-translated from one natural language to another.
Quality is considered to be the correspondence between a machine's output and that of a human: "the closer a machine translation is to a professional human translation,
the better it is" – this is the central idea behind BLEU. BLEU was one of the first metrics to claim a high correlation with human judgements of quality, and
remains one of the most popular automated and inexpensive metrics.
Scores are calculated for individual translated segments—generally sentences—by comparing them with a set of good quality reference translations.
Those scores are then averaged over the whole corpus to reach an estimate of the translation's overall quality. Intelligibility or grammatical correctness
are not taken into account[citation needed].
BLEU's output is always a number between 0 and 1. This value indicates how similar the candidate text is to the reference texts, with values closer to 1
representing more similar texts. Few human translations will attain a score of 1, since this would indicate that the candidate is identical to one of the
reference translations. For this reason, it is not necessary to attain a score of 1. Because there are more opportunities to match, adding additional
reference translations will increase the BLEU score.
"""

_KWARGS_DESCRIPTION = """
Computes BLEU score of translated segments against one or more references.
Args:
    predictions: list of translations to score.
        Each translation should be tokenized into a list of tokens.
    references: list of lists of references for each translation.
        Each reference should be tokenized into a list of tokens.
    max_order: Maximum n-gram order to use when computing BLEU score.
    smooth: Whether or not to apply Lin et al. 2004 smoothing.
Returns:
    'bleu': bleu score,
    'precisions': geometric mean of n-gram precisions,
    'brevity_penalty': brevity penalty,
    'length_ratio': ratio of lengths,
    'translation_length': translation_length,
    'reference_length': reference_length
Examples:
    >>> predictions = [
    ...     ["hello", "there", "general", "kenobi"],                             # tokenized prediction of the first sample
    ...     ["foo", "bar", "foobar"]                                             # tokenized prediction of the second sample
    ... ]
    >>> references = [
    ...     [["hello", "there", "general", "kenobi"], ["hello", "there", "!"]],  # tokenized references for the first sample (2 references)
    ...     [["foo", "bar", "foobar"]]                                           # tokenized references for the second sample (1 reference)
    ... ]
    >>> bleu = datasets.load_metric("bleu")
    >>> results = bleu.compute(predictions=predictions, references=references)
    >>> print(results["bleu"])
    1.0
"""

#@gin.configurable
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
        #print("BLEU is intended as a corpus-level metric. Be careful!")
        if isinstance(reference, str):
            reference = [reference]
        score = sacrebleu.sentence_bleu(summary, reference, smooth_method=self.sent_smooth_method, \
             smooth_value=self.sent_smooth_value, use_effective_order=self.sent_use_effective_order)
        score_dict = {"bleu" : score.score}
        #return score_dict
        #print(score.score)
        return score.score

    # def evaluate_batch(self, summaries, references, aggregate=True):
    #     if aggregate:
    #         if isinstance(references[0], str):
    #             references = [references]
    #         score = sacrebleu.corpus_bleu(summaries, references, smooth_method=self.smooth_method, \
    #            smooth_value=self.smooth_value, force=self.force, lowercase=self.lowercase, \
    #            use_effective_order=self.use_effective_order)
    #         score_dict = {"bleu": score.score}
    #     else:
    #         p = Pool(processes=self.n_workers)
    #         score_dict = p.starmap(self.evaluate_example, zip(summaries, references))
    #         p.close()
    #     return score_dict

    # property
    # def supports_multi_ref(self):
    #     return True

# for index in range(50):
#     # Absolute path of a file
#     old_name = str(index)+".dec"
#     new_name = "pnbert_"+str(index)+".dec"
#     # Renaming the file
#     os.rename(old_name, new_name)

"""## Bleu Scores"""

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
  #print(score)

"""# Chrf(++) metric


"""

# coding=utf-8
# Copyright 2021 The HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Chrf(++) metric as available in sacrebleu. """
import sacrebleu as scb
from packaging import version
from sacrebleu import CHRF

import datasets

_CITATION = """\
@inproceedings{popovic-2015-chrf,
    title = "chr{F}: character n-gram {F}-score for automatic {MT} evaluation",
    author = "Popovi{\'c}, Maja",
    booktitle = "Proceedings of the Tenth Workshop on Statistical Machine Translation",
    month = sep,
    year = "2015",
    address = "Lisbon, Portugal",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W15-3049",
    doi = "10.18653/v1/W15-3049",
    pages = "392--395",
}
@inproceedings{popovic-2017-chrf,
    title = "chr{F}++: words helping character n-grams",
    author = "Popovi{\'c}, Maja",
    booktitle = "Proceedings of the Second Conference on Machine Translation",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W17-4770",
    doi = "10.18653/v1/W17-4770",
    pages = "612--618",
}
@inproceedings{post-2018-call,
    title = "A Call for Clarity in Reporting {BLEU} Scores",
    author = "Post, Matt",
    booktitle = "Proceedings of the Third Conference on Machine Translation: Research Papers",
    month = oct,
    year = "2018",
    address = "Belgium, Brussels",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W18-6319",
    pages = "186--191",
}
"""

_DESCRIPTION = """
ChrF and ChrF++ are two MT evaluation metrics. They both use the F-score statistic for character n-gram matches,
and ChrF++ adds word n-grams as well which correlates more strongly with direct assessment. 
"""

_KWARGS_DESCRIPTION = """
Produces ChrF(++) scores for hypotheses given reference translations.
Args:
    predictions: The system stream (a sequence of segments).
    references: A list of one or more reference streams (each a sequence of segments).
    char_order: Character n-gram order.
    word_order: Word n-gram order. If equals to 2, the metric is referred to as chrF++.
    beta: Determine the importance of recall w.r.t precision.
    lowercase: Enable case-insensitivity.
    whitespace: If `True`, include whitespaces when extracting character n-grams.
    eps_smoothing: If `True`, applies epsilon smoothing similar
    to reference chrF++.py, NLTK and Moses implementations. Otherwise,
    it takes into account effective match order similar to sacreBLEU < 2.0.0.
Returns:
    'score': The chrF (chrF++) score,
    'char_order': The character n-gram order,
    'word_order': The word n-gram order. If equals to 2, the metric is referred to as chrF++,
    'beta': Determine the importance of recall w.r.t precision
Examples:
    >>> prediction = ["The relationship between Obama and Netanyahu is not exactly friendly."]
    >>> reference = [["The ties between Obama and Netanyahu are not particularly friendly."]]
    >>> chrf = datasets.load_metric("chrf")
    >>> results = chrf.compute(predictions=prediction, references=reference)
    >>> print(results)
    {'score': 61.576379378113785, 'char_order': 6, 'word_order': 0, 'beta': 2}
"""


@datasets.utils.file_utils.add_start_docstrings(_DESCRIPTION, _KWARGS_DESCRIPTION)
class ChrF(datasets.Metric):
    def _info(self):
        if version.parse(scb.__version__) < version.parse("1.4.12"):
            raise ImportWarning(
                "To use `sacrebleu`, the module `sacrebleu>=1.4.12` is required, and the current version of `sacrebleu` doesn't match this condition.\n"
                'You can install it with `pip install "sacrebleu>=1.4.12"`.'
            )
        return datasets.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            homepage="https://github.com/mjpost/sacreBLEU#chrf--chrf",
            inputs_description=_KWARGS_DESCRIPTION,
            features=datasets.Features(
                {
                    "predictions": datasets.Value("string", id="sequence"),
                    "references": datasets.Sequence(datasets.Value("string", id="sequence"), id="references"),
                }
            ),
            codebase_urls=["https://github.com/mjpost/sacreBLEU#chrf--chrf"],
            reference_urls=[
                "https://github.com/m-popovic/chrF",
            ],
        )

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

        # return {
        #     "score": output.score,
        #     "char_order": output.char_order,
        #     "word_order": output.word_order,
        #     "beta": output.beta,
        # }

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

"""# Meteor Metric"""

# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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


_CITATION = """\
@inproceedings{banarjee2005,
  title     = {{METEOR}: An Automatic Metric for {MT} Evaluation with Improved Correlation with Human Judgments},
  author    = {Banerjee, Satanjeev  and Lavie, Alon},
  booktitle = {Proceedings of the {ACL} Workshop on Intrinsic and Extrinsic Evaluation Measures for Machine Translation and/or Summarization},
  month     = jun,
  year      = {2005},
  address   = {Ann Arbor, Michigan},
  publisher = {Association for Computational Linguistics},
  url       = {https://www.aclweb.org/anthology/W05-0909},
  pages     = {65--72},
}
"""

_DESCRIPTION = """\
METEOR, an automatic metric for machine translation evaluation
that is based on a generalized concept of unigram matching between the
machine-produced translation and human-produced reference translations.
Unigrams can be matched based on their surface forms, stemmed forms,
and meanings; furthermore, METEOR can be easily extended to include more
advanced matching strategies. Once all generalized unigram matches
between the two strings have been found, METEOR computes a score for
this matching using a combination of unigram-precision, unigram-recall, and
a measure of fragmentation that is designed to directly capture how
well-ordered the matched words in the machine translation are in relation
to the reference.
METEOR gets an R correlation value of 0.347 with human evaluation on the Arabic
data and 0.331 on the Chinese data. This is shown to be an improvement on
using simply unigram-precision, unigram-recall and their harmonic F1
combination.
"""

_KWARGS_DESCRIPTION = """
Computes METEOR score of translated segments against one or more references.
Args:
    predictions: list of predictions to score. Each prediction
        should be a string with tokens separated by spaces.
    references: list of reference for each prediction. Each
        reference should be a string with tokens separated by spaces.
    alpha: Parameter for controlling relative weights of precision and recall. default: 0.9
    beta: Parameter for controlling shape of penalty as a function of fragmentation. default: 3
    gamma: Relative weight assigned to fragmentation penalty. default: 0.5
Returns:
    'meteor': meteor score.
Examples:
    >>> meteor = datasets.load_metric('meteor')
    >>> predictions = ["It is a guide to action which ensures that the military always obeys the commands of the party"]
    >>> references = ["It is a guide to action that ensures that the military will forever heed Party commands"]
    >>> results = meteor.compute(predictions=predictions, references=references)
    >>> print(round(results["meteor"], 4))
    0.6944
"""


@datasets.utils.file_utils.add_start_docstrings(_DESCRIPTION, _KWARGS_DESCRIPTION)
class Meteor(datasets.Metric):
    def _info(self):
        return datasets.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=datasets.Features(
                {
                    "predictions": datasets.Value("string", id="sequence"),
                    "references": datasets.Value("string", id="sequence"),
                }
            ),
            codebase_urls=["https://github.com/nltk/nltk/blob/develop/nltk/translate/meteor_score.py"],
            reference_urls=[
                "https://www.nltk.org/api/nltk.translate.html#module-nltk.translate.meteor_score",
                "https://en.wikipedia.org/wiki/METEOR",
            ],
        )

    def _download_and_prepare(self, dl_manager):
        import nltk

        nltk.download("wordnet")
        if NLTK_VERSION >= version.Version("3.6.4"):
            nltk.download("punkt")

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
#M._compute("How do you feedsadwd eweweqw wq ewql dsad","How do you feel")

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