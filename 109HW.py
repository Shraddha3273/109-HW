import plotly.figure_factory as ff
import csv
import statistics
import pandas as pd

file1 = pd.read_csv("StudentsPerformance.csv")
rs = file1["reading score"].to_list()
ws = file1["writing score"].to_list()

rMean = statistics.mean(rs)
wMean = statistics.mean(ws)

rMedian = statistics.median(rs)
wMedian = statistics.median(ws)

rMode = statistics.mode(rs)
wMode = statistics.mode(ws)

print("Mean, Median and Mode of the Reading Scores is {},{},{}".format(rMean, rMedian, rMode))

figure = ff.create_distplot([rs],["result"], show_hist = False)
figure.show()

rsd = statistics.stdev(rs)
rsd = statistics.stdev(ws)

rsd_start = rMean-rsd
rsd_end = rMean+rsd

rs_1_stdev = [result for result in rs if result > rsd_start and result < rsd_end]

print("{}% of Reading Scores of Students lies within 1st standard deviation ".format(len(rs_1_stdev)*100.0/len(rs)))

rsd_2_stdev = 2*rsd
rsd_2_start = rMean-rsd_2_stdev
rsd_2_end = rMean+rsd_2_stdev

rl_2_stdev = [result for result in rs if result > rsd_2_start and result < rsd_2_end]
print("{}% of Reading Scores of Students lies within 2nd standard deviation ".format(len(rl_2_stdev)*100.0/len(rs)))

rsd_3_stdev = 3*rsd
rsd_3_start = rMean-rsd_3_stdev
rsd_3_end = rMean+rsd_3_stdev

rs_3_stdev = [result for result in rs if result > rsd_3_start and result < rsd_3_end]
print("{}% of Reading Scores of Students lies within 3rd standard deviation ".format(len(rs_3_stdev)*100.0/len(rs)))