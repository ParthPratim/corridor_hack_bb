from charts.base import ModelPlot
import matplotlib.pyplot as plt
import pandas as pd

class SalaryUtilization(ModelPlot):

    def generate(self, x , y):
        plt.clf()
        csv_data = pd.read_csv(self.file) 
        salary = csv_data[x]
        utilization = csv_data[y]

        plt.plot(salary,utilization,  marker="o",  linestyle='None')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(x + " Vs " + y)

        store_f = "./temp/%s_%s_vs_%s.pdf" % (self.doc_id, x, y)
        plt.savefig(store_f)
        return store_f
