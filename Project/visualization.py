import matplotlib as plt
import test_create
import pandas as pd


def dict_to_dframe(res_dict):
    """ Takes result dict and return a DataFrame with timecourses for each model species. """
    s = pd.DataFrame()
    key_list = []

    for i, key in enumerate(res_dict):
        s[i] = pd.DataFrame(res_dict[key]['time_course'], columns = [key])
        key_list.append(key)

    s.columns = key_list
    return s

r = dict_to_dframe(test_create.result)

#figure
#plt.plot(r)