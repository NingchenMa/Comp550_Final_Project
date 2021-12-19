from abc import abstractmethod, ABCMeta
from rouge_score import rouge_scorer
from os import listdir
import csv

class evaluator(object, metaclass=ABCMeta):
    @abstractmethod
    def evaluate(self, summary, ref, input):
        pass

    @abstractmethod
    def name(self):
        pass

class rougeN(evaluator):

    def __init__(self, N):
        self.N = N

    def name(self):
        return 'rougeL' if self.N == 0 else 'rouge{0}'.format(self.N)

    def evaluate(self, summary, ref, input):
        scorer = rouge_scorer.RougeScorer([self.name()], use_stemmer=True)
        return scorer.score(summary, ref)[self.name()].recall


def getScores(evaluators, outputs, refs, inputs):
    inputs = inputs if not inputs is None else [None for i in range(len(outputs))]
    scores = {}
    for eval in evaluators:
        scores[eval.name()] = []
        for i in range(len(outputs)):
            scores[eval.name()].append(eval.evaluate(outputs[i], refs[i], inputs[i]))
    return scores

if __name__ == '__main__':

    models = ['MatchSum', 'PNBERT', 'PGen', 'LoopSum']

    ms = sorted(listdir('./dec/MatchSum/'), key=lambda f: int(f.split(".")[0]))
    pn = sorted(listdir('./dec/PNBERT/'), key=lambda f: int(f.split(".")[0]))
    pg = sorted(listdir('./dec/PGen/'), key=lambda f: int(f.split(".")[0]))
    ls = sorted(listdir('./dec/LoopSum/'), key=lambda f: int(f.split(".")[0]))
    rf = sorted(listdir('./ref/'), key=lambda f: int(f.split(".")[0]))
    inputs = sorted(listdir('./in/'), key=lambda f: int(f.split(".")[0]))

    data = { model : [] for model in models}
    ins = []
    refs = []

    for i in range(50):

        for model in models:
            with open('./dec/{0}/'.format(model) + ms[i], "r") as _file:
                data[model].append(_file.read().replace('\n', ''))

        with open('./ref/' + rf[i], "r") as _file:
            refs.append(_file.read().replace('\n', ''))
        with open('./in/' + inputs[i], "r") as _file:
            ins.append(_file.read().replace('\n', ''))

    rougeL = rougeN(0)
    rouge1 = rougeN(1)
    rouge2 = rougeN(2)
    rouge3 = rougeN(3)
    rouge4 = rougeN(4)

    evaluators = [rouge1, rouge2, rouge3, rouge4, rougeL]

    for model, outputs in data.items():
        scores = getScores(evaluators, outputs, refs, ins)

        csv_columns = [evaluator.name() for evaluator in evaluators]
        csv_scores = [{ evaluator: scores[evaluator][i] for evaluator in csv_columns} for i in range(len(scores[csv_columns[0]]))]

        with open(model + '-rouge.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in csv_scores:
                writer.writerow(data)

        #print(model)
        #print(getScores(evaluators, data[model], refs, ins))






