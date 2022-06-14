'''
Program finds the Min, Max, Mean, Median, and Mode from 
an unlimited amount of input, after sorting the intergers
from said input.
'''





import sys

intake = sys.stdin.readlines()

sorted_intake = []

x = iter(intake)
count_int = 0
minimum = sys.maxsize
maximum = 0
average = 0
sum = 0
while True:
    try:
        xx = next(x)
    except StopIteration:
        break
    try:
        i = int(xx)
        count_int += 1
        if(i > maximum):
            maximum = i
        if (i < minimum ):
            minimum = i
        
        
        average = average + i

        sum += i
        sorted_intake.append(i)

    except: 
        continue

sorted_intake_final = sorted(sorted_intake)


print('Count:  ' , count_int)    
print('Minimum:' , minimum)
print('Maximum:' , maximum)
print('Mean:   ' ,sum/count_int)
if (count_int % 2 == 0):
    v = int(count_int / 2)
    print(
        'Median: ' ,
        (sorted_intake_final[v-1] + sorted_intake_final[v]) / 2
        )


else:
    print('Median: ', sorted_intake_final[int((count_int+1)/2)])

z = iter(sorted_intake_final)
lastvalue = 0
lvcount = 0
mv = 0
mvcount = 0

while True:
    try:
        i = next(z)
    except:
        break
    if (mvcount == 0):
        mv = i
        mvcount = 1
    else:
        if (i == mv):
            mvcount += 1
        else: 
            lvcount += 1
            lastvalue = i
    if (lvcount > mvcount):
        mvcount = lvcount
        mv = lastvalue
        lvcount = 0

print('Mode:   ' , mv)
