import pandas as pd
import csv
import statistics
import random
import plotly.figure_factory as ff

read_csv = pd.read_csv("medium_data.csv")

data = read_csv["reading_time"].tolist()

mean_list = []

def randomMeans():
    setOfMeans = []
    for i in range(0 , 30):
        index = random.randint(0 , len(data))
        value = data[index]
        setOfMeans.append(value)
    samplingMean = statistics.mean(setOfMeans)
    return samplingMean

def setup():
    for j in range(0 , 100):
        randMeans = randomMeans()
        mean_list.append(randMeans)

setup()

sampling_mean = statistics.mean(mean_list)
population_mean = statistics.mean(data)

sampling_stdev = statistics.stdev(mean_list)
population_stdev = statistics.stdev(data)

print(f"The mean of the sample is {sampling_mean} and mean of population is {population_mean}")
print(f"The Standard Deviation of the sample is {sampling_stdev} and Standard Deviation of population is {population_stdev}")

graph = ff.create_distplot([mean_list] , ["Claps"] , show_hist = False)

graph.show()