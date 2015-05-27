import matplotlib.pyplot as plt
#import seaborn as sb
import test_create
import pandas as pd
import test_model
import numpy as np


def dict_to_dframe(res_dict):
    """ Takes result dict and return a DataFrame with timecourses for each model species."""
    s = pd.DataFrame()
    key_list = []

    for i, key in enumerate(res_dict):
        s[i] = pd.DataFrame(res_dict[key]['time_course'], columns = [key])
        key_list.append(key)

    s.columns = key_list
    return s

def timecourse_by_column(res_dict, keywords):
    """ Takes result dictionary and list of keywords(strings), which define the model species which should be plottet.
        e.g.: keywords = ['MRNA', 'Protein'], stores timecourses of all mRNAs and all Proteins in a DataFrame, which is returned.
    """
    r = dict_to_dframe(res_dict)
    wished_cols = []
    for kw in keywords:
        wished_cols += [x for x in r.columns if kw in x]

    r_mod = r[wished_cols]
    return r_mod
    

def seq_dependence(res_dict, keyword):
    """ Takes result dictionary and returns species sequence lengths as well as each final concentration. """
    seq_lengths = []
    last_conc = []
    for key in res_dict.keys():
        if keyword in key:
            seq_lengths.append(len(res_dict[key]['sequence']))
            last_conc.append(res_dict[key]['time_course'][-1])
        else:
            continue
    return seq_lengths, last_conc
    
def mighty_plot(res_dict, plotword, keywords):
    """ Plots as desired. """
    if plotword == 'time_course':
        p = timecourse_by_column(res_dict, keywords) #p is DataFrame
        plt.plot(p)
        plt.show()
    elif plotword == 'sequence_dependency':
        if len(keywords) > 1:
            print 'If you want to plot sequence length dependent concentrations, keywords has to have only one element.'
        else:
            x,y = seq_dependence(res_dict, str(keywords))
            plt.plot(x,y)
            plt.show()
    elif plotword == 'correlation':
        c_df = timecourse_by_column(res_dict,keywords)
        c = c_df.corr()
        plt.pcolor(c, cmap = 'Blues')
        plt.yticks(np.arange(0.5,len(c.index),1), c.index)
        plt.xticks(np.arange(0.5,len(c.columns),1), c.columns, rotation = 'vertical')
        plt.colorbar()
        plt.show()


mighty_plot(test_model.test_dict, 'correlation', [''])

