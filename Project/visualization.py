import matplotlib.pyplot as plt
#import seaborn as sb
import test_create
import pandas as pd


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
    r = dict_to_dframe(rest_dict)
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
    


x,y = seq_dependence(test_create.result, 'mrna')
plt.plot(x,y)
plt.show()
