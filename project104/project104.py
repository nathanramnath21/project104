import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
        reader=csv.reader(f)
        file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
        n_numb=file_data[i][1]
        new_data.append(float(n_numb))
n=len(new_data)
total=0
for x in new_data:
        total+=x
mean=total/n
print("Mean is: "+ str(mean))

with open('SOCR-HeightWeight.csv', newline='') as f:
        reader=csv.reader(f)
        file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
        n_numb=file_data[i][1]
        new_data.append(float(n_numb))
n=len(new_data)
new_data.sort()
if n%2==0:
    meadian1=float(new_data[n//2])
    meadian2=float(new_data[n//2-1])
    meadian=(meadian1+meadian2)/2
else:
    meadian=new_data[n//2]
    print(n)
print("Median is: "+str(meadian))

with open('SOCR-HeightWeight.csv', newline='') as f:
        reader=csv.reader(f)
        file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
        n_numb=file_data[i][1]
        new_data.append(float(n_numb))
data=Counter(new_data)
moded_data_more_mode_range={"50-60":0, "60-70":0, "70-80":0}
for height, occurrence in data.items():
    if 50<float(height)<60:
        moded_data_more_mode_range["50-60"]+=occurrence
    elif 60<float(height)<70:
        moded_data_more_mode_range["60-70"]+=occurrence
    elif 70<float(height)<80:
        moded_data_more_mode_range["70-80"]+=occurrence
mode_range, mode_occurrence=0,0
for range, occurrence in moded_data_more_mode_range.items():
    if occurrence>mode_occurrence:
        mode_range, mode_occurrence=[int(range.split("-")[0]), int(range.split("-")[1])], occurrence
mode = float((mode_range[0] + mode_range[1]) / 2) 
print(f"Mode is -> {mode:2f}")
