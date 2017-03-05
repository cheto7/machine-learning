import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('census.csv')
'''
Function to show the sum of records of each classification by each value of the feature
'''
def show_sum_val(data, features):
    for ftr in features:
        distinct = data[ftr].unique()

        pos = list()
        neg = list()
        
        for val in distinct:
            pos.append(len(data[(data[ftr] == val) & (data['income'] == '>50K')]))
            neg.append(len(data[(data[ftr] == val) & (data['income'] == '<=50K')]))
            
        
        fig, ax = plt.subplots()
        ind = np.arange(len(distinct))
        width = 0.35
        
        rects1 = ax.bar(ind, pos, width, color='g')
        
        rects2 = ax.bar(ind + width, neg, width, color='r')
        
        ax.set_ylabel('Times')
        ax.set_title('Values of '+ftr)
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(distinct)
        
        """
        Attach a text label above each bar displaying its height
        """
        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                        '%d' % int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)
    
    plt.show()
    
show_sum_val(data, ['occupation','sex','race','education_level','relationship','native-country', 'workclass', 'marital-status','hours-per-week', 'age'])
    