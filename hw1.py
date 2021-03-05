# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061150.csv'
data = []
header = []
sum = [0, 0, 0, 0, 0]
station_num = [0, 0, 0, 0, 0]
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
      if(row['PRES'] == '-99.000'):
        row['PRES'] = ''
      elif(row['PRES'] == '-999.000'):
         row['PRES'] = ''

      elif(row['station_id'] == 'C0A880'):
         if(row['PRES'] != ''):
            sum[0] += float(row['PRES'])
            station_num[0] += 1
      elif(row['station_id'] == 'C0F9A0'):
          if(row['PRES'] != ''):
            sum[1] += float(row['PRES'])
            station_num[1] += 1
      elif(row['station_id'] == 'C0G640'):
          if(row['PRES'] != ''):
            sum[2] += float(row['PRES'])
            station_num[2] += 1
      elif(row['station_id'] == 'C0R190'):
          if(row['PRES'] != ''):
            sum[3] += float(row['PRES'])
            station_num[3] += 1 
      elif(row['station_id'] == 'C0X260'):
          if(row['PRES'] != ''):
            sum[4] += float(row['PRES'])
            station_num[4] += 1
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.


def count(station, sum, num):
      print("['", end ='')
      print(station, end = '')
      print("', ", end = '')
      if (num == 0):
         print("'None'", end = '')
      else:
         mean = sum / num
         print(round(mean, 2), end = '')
      print(']', end = '')
#=======================================

# Part. 4
#=======================================
# Print result
print("[", end = '')
count('C0A880', sum[0], station_num[0])
print(', ', end = '')
count('C0F9A0', sum[1], station_num[1])
print(', ', end = '')
count('C0G640', sum[2], station_num[2])
print(', ', end = '')
count('C0R190', sum[3], station_num[3])
print(', ', end = '')
count('C0X260', sum[4], station_num[4])
print(']')
#========================================