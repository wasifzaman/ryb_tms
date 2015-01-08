from datetime import datetime


x = [datetime.strptime('1/7/2015', '%m/%d/%Y')]
y = [datetime.strptime('1/31/2015', '%m/%d/%Y')]
z = [datetime.strptime('1/7/2014', '%m/%d/%Y')]

d = [y, x, z]
d.sort()

print(d)