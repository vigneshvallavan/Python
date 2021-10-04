import pandas as pd
import datetime

dataFrame = pd.read_csv('C:\\Users\\US\\Desktop\\aws_usecase\\usecase_4.csv')

print("\n",dataFrame,"\n")

result = dataFrame

i = 0
for x in result['Key_col']:

    e = datetime.datetime.now() 
    current_date_time = e.strftime("%Y-%m-%d %H:%M:%S")

    dataFrame.loc[i,'Batch_date'] = current_date_time
    dataFrame.loc[i,'Batch_key'] = str(e.strftime("%Y%m%d%H%M%S"))
    i+=1
    
print(dataFrame)