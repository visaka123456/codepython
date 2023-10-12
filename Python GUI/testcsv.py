# # testcsv.py

# import csv
# from datetime import datetime

# def writetocsv(data):
#     with open('data.csv','a',newline='',encoding='utf-8') as file:  
#         fw = csv.writer(file) # fw = filw writer
#         fw.writerow(data)
# data = ['banana',40]
# writetocsv(data)


# a = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# print(a)

from datetime import datetime

dt = datetime.now()
year = dt.year + 543

stamp = dt.strftime('{}-%m-%d %H:%M:%S'.format(year))
print(stamp)