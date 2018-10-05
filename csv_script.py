import csv
import pandas as pd
target = '/home/mmursaleen/Desktop/codebase/honeywell-new/honeywell-ma/data/task_TSM.csv'
data = pd.read_csv(target)
print(data[['TaskTextString', 'TaskTopicType']])
useful_columns = ['TaskKey', 'TaskTopicType', 'SubTaskLabel', 'TaskTextString',
                 'PacketType', 'PacketId', 'SubTaskTitle','SubTaskId',]

data[useful_columns].to_csv('ts_csv.csv', index=False)
print(data)