import csv
import pandas as pd
target = '/home/mmursaleen/Desktop/codebase/honeywell-new/honeywell-ma/data/task_TSM.csv'
data = pd.read_csv(target)
#select only one column by pd
print(data.TaskTextString)
#select multiple columns by pd
print(data[['TaskTextString', 'TaskTopicType']])
#select rows by pd
print(data.iloc[2])
#selct multiple rows
print(data.iloc[3:5])
#selecting rows with logic
print(data[(data.TaskTextString == 'repair with wiring')|(data.TaskKey == 'EN303000001000')])
print(data.reset_index(inplace=True, drop=True))
useful_columns = ['TaskKey', 'TaskTopicType', 'SubTaskLabel', 'TaskTextString',
                 'PacketType', 'PacketId', 'SubTaskTitle','SubTaskId',]

data[useful_columns].to_csv('ts_csv.csv', index=False)
print(data)


