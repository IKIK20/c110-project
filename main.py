import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go
import random

df= pd.read_csv("data.csv")
data= df["reading_time"].tolist()

mean= st.mean(data)

print(mean)



def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean1 = st.mean(dataset)
    return mean1


def show_fig(mean_list):
    fig= ff.create_distplot([mean_list],["reading_time"], show_hist= False)
    fig.show()


def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    mean2 = st.mean(mean_list)
    print(mean2)
    show_fig(mean_list)

setup()