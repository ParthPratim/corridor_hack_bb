from charts.base import ModelPlot
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import pandas as pd

class AUC_ROC_Score(ModelPlot):

    def generate(self):
        csv_data = pd.read_csv(self.file) 
        output = csv_data['model_output']
        target = csv_data['model_target']
        fpr, tpr, _ = roc_curve(target , output)
        plt.clf()
        plt.plot(fpr,tpr)
        plt.ylabel('True Positive Rate')
        plt.xlabel('False Positive Rate')
        store_f = "./temp/%s_roc.pdf" % (self.doc_id)
        plt.savefig(store_f)
        return store_f
