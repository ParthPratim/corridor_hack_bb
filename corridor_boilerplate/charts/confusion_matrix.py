from charts.base import ModelPlot
import pandas as pd
import math, numpy
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn


class ConfusionMatrix(ModelPlot):

    def generate(self):
        csv_data = pd.read_csv(self.file) 
        output = csv_data['model_output']
        target = csv_data['model_target']
        for i in range(len(output)):
            if output[i] > 0.5 :
                output[i] = 1
            else :
                output[i] = 0

        classes = [0,1]
        cfm = confusion_matrix(target , output)
        df_cfm = pd.DataFrame(cfm, index = classes, columns = classes)
        plt.title("Confusion Matrix")
        plt.figure(figsize = (10,7))

        cfm_plot = sn.heatmap(df_cfm, annot=True)

        store_f = "./temp/%s_cfm.pdf" % (self.doc_id)
        
        cfm_plot.figure.savefig(store_f)
        return store_f
