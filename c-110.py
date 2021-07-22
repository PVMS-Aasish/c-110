import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random 

df=pd.read_csv("TEMP.csv")
TEMP_list=df["temp"].tolist()

#fig=ff.create_distplot([TEMP_list],["temp"],show_hist=False)
#fig.show()

mean=statistics.mean(TEMP_list)
std_deviation=statistics.stdev(TEMP_list)
print("mean:- "+str(mean))
print("stdev:- "+str(std_deviation))

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([TEMP_list],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))    
    fig.show()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(TEMP_list)-1)
        value=TEMP_list[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)


setup()

def std_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)


std_deviation() 
