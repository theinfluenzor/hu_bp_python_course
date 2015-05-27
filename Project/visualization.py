import matplotlib.pyplot as plt
#import seaborn as sb
import test_create
import pandas as pd
import test_model
import numpy as np
import pickle as p

output = {}
with open('output.p', 'rb') as f:
    output = p.load(f)

def dict_to_dframe(res_dict):
    """ Takes result dict and return a DataFrame with timecourses for each model species."""
    s = pd.DataFrame()
    key_list = []

    for i, key in enumerate(res_dict):
        s[i] = pd.DataFrame(res_dict[key]['timecourse'], columns = [key])
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
            last_conc.append(res_dict[key]['timecourse'][-1])
        else:
            continue
    return seq_lengths, last_conc



def mean_timecourse(res_dict, keywords):
    """ Calculates mean timecourse with standard deviation for each element in keywords.
        e.g.: If 'mrna' is an element keywords mean_timecourse returns mean timecourse for all mRNAs + std. """
    all_mean_time_courses = {}
    all_std_time_courses = {}
    for kw in keywords:
        print kw
        all_mean_time_courses[kw] = timecourse_by_column(res_dict, [kw]).mean(axis = 1)
        all_std_time_courses[kw] = timecourse_by_column(res_dict, [kw]).std(axis = 1)
    all_mean_df = pd.DataFrame(all_mean_time_courses)
    all_std_df = pd.DataFrame(all_std_time_courses)
    return all_mean_df, all_std_df  
    #return all_mean_time_courses
    
def mean_species_mass(res_dict, keywords):
    mean_mass_dict = {}
    kw_count = {}
    for kw in keywords:
        print kw
        mean_mass_dict[kw] = 0
        kw_count[kw] = 0
        for key in res_dict.keys():
            if kw in key:
                print key
                mean_mass_dict[kw] += res_dict[key]['mass']
                kw_count[kw] += 1
    
    for key in mean_mass_dict.keys():
        mean_mass_dict[key] = mean_mass_dict[key]/kw_count[key]

    return mean_mass_dict



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
    elif plotword == 'species_mean':
        a, b = mean_timecourse(res_dict,keywords) #be careful with keywords
        a.plot(subplots=False, yerr=b, cmap = 'coolwarm') 
        plt.show()
      
    #elif plotword == 'mass_distribution':
     #   mass_dict = mean_species_mass(res_dict,keywords)


s = mean_species_mass(test_model.test_dict, ['MRNA', 'Protein'])
#mighty_plot(output, 'species_mean', ['Ribosomes', 'Protein'])

