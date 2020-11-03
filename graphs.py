import os
import sys
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
import seaborn as sns

#
# if len(sys.argv) != 2:
#     sys.exit('Please provide start date')
# start_date = sys.argv[1].split('/')
# start_date = datetime.datetime(int(start_date[2], start_date[0], start_date[1]))
start_date = datetime.datetime(2020, 10, 1)

data = {}
os.chdir("C:\Program Files (x86)\Steam\steamapps\common\FPSAimTrainer\FPSAimTrainer\stats")
for filename in os.listdir():
    challenge = '-'.join(filename.split('-')[:-2])
    date = (filename.split('-')[-2].split('.'))
    date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
    if date >= start_date:
        f = open(filename, 'r')
        for x in f.readlines():
            if x[:5] == 'Score':
                # data[challenge] = data.get(challenge, {})
                # if date in data[challenge]:
                #     data[challenge][date].append(float(x.split(',')[-1].strip()))
                # else:
                #     data[challenge][date] = [float(x.split(',')[-1].strip())]
                data[challenge] = data.get(challenge, [[], []])
                data[challenge][0].append(date)
                data[challenge][1].append(float(x.split(',')[-1].strip()))
        f.close()

print(data)
dates = matplotlib.dates.date2num(data["Micro Flick - Challenge "][0])

sns.regplot(dates, data["Micro Flick - Challenge "][1])
plt.title("Micro Flick - Challenge ")
plt.plot_date(dates, data["Micro Flick - Challenge "][1], color = '#1f77b4')
plt.show()

# coef = np.polyfit(dates, data["1 Wall 6 targets Adjust - Challenge "][1], 1)
# poly = np.poly1d(coef)
# plt.plot(dates, data["1 Wall 6 targets Adjust - Challenge "][1], 'yo', dates, poly(dates),'--k')
# # plt.plot_date(dates, data["1 Wall 6 targets Adjust - Challenge "][1])
# plt.title("1 Wall 6 targets Adjust - Challenge ")
# plt.show()

# print(len(f.readlines()))
# f = open('ValTargetSwitch - Challenge - 2020.11.01-15.54.11 Stats.csv', 'r')
# s = 'ValTargetSwitch - Challenge - 2020.11.01-15.54.11 Stats.csv'
# print('-'.join(s.split('-')[:-2]))
