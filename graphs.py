import os
import sys
import datetime

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
                data[challenge] = data.get(challenge, {})
                if date in data[challenge]:
                    data[challenge][date].append(float(x.split(',')[-1].strip()))
                else:
                    data[challenge][date] = [float(x.split(',')[-1].strip())]
        f.close()
print(data)

# print(len(f.readlines()))
# f = open('ValTargetSwitch - Challenge - 2020.11.01-15.54.11 Stats.csv', 'r')
# s = 'ValTargetSwitch - Challenge - 2020.11.01-15.54.11 Stats.csv'
# print('-'.join(s.split('-')[:-2]))
