#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv, json
import pandas as pd
import numpy  as np
import matplotlib.pyplot as pt
import requests


url = requests.get('https://api.covid19india.org/raw_data.json')
json_file = open('D:\\python dataset\\raw_data.json','w')
json_file.write(str(url.text))
json_file.close()

#to load json file into variable
data = json.load(open('D:\\python dataset\\raw_data.json'))


#writing into cvs file
output = csv.writer(open('D:\\python dataset\\covid19.csv','w'))
output.writerow(data['raw_data'][0].keys())
for row in data['raw_data']:
    output.writerow(row.values())
    
#converting cvs file to excel
read_file = pd.read_csv (r'D:\\python dataset\\covid19.csv',encoding="cp1252")
read_file.to_excel (r'D:\\python dataset\\raw_data_csv.xlsx', index = None, header=True)

print('covid data is READY TO USE :')
print()

#read excel file and show it in graph
file=pd.read_excel('D:\\python dataset\\raw_data_csv.xlsx')
file.fillna("undefined", inplace = True) 
#line graph
print('In this line graph the gender is represented:')
f=0
m=0
ud=0
for i in file['gender']:
    if(i=='M'):m=m+1
    elif(i=='F'):f=f+1
    else:ud=ud+1
print("-----> male :",m)
print("-----> female :",f)
print("-----> undefined :",ud)

gender=["Male","Female","Undefined"]
value=[m,f,ud]
pt.title("COVID_19 DATA")
pt.xlabel("Gender")
pt.ylabel("Total number of people")
pt.plot(gender,value,color="red")
pt.grid(True)
pt.show()


# In[2]:


import csv, json
import pandas as pd
import numpy  as np
import matplotlib.pyplot as pt
import requests


url = requests.get('https://api.covid19india.org/raw_data.json')
json_file = open('D:\\python dataset\\raw_data.json','w')
json_file.write(str(url.text))
json_file.close()

#to load json file into variable
data = json.load(open('D:\\python dataset\\raw_data.json'))


#writing into cvs file
output = csv.writer(open('D:\\python dataset\\covid19.csv','w'))
output.writerow(data['raw_data'][0].keys())
for row in data['raw_data']:
    output.writerow(row.values())
    
#converting cvs file to excel
read_file = pd.read_csv (r'D:\\python dataset\\covid19.csv',encoding="cp1252")
read_file.to_excel (r'D:\\python dataset\\raw_data_csv.xlsx', index = None, header=True)

#read excel file and show it in graph
file=pd.read_excel('D:\\python dataset\\raw_data_csv.xlsx')
file.fillna("undefined", inplace = True) 

#bar graph
print('In this bar graph the current status is represented:')
rec=0
hop=0
dea=0
mig=0
uda=0
for i in file['currentstatus']:
    if(i=='Recovered'):rec=rec+1
    elif(i=='Hospitalized'):hop=hop+1
    elif(i=='Deceased'):dea=dea+1
    elif(i=='Migrated'):mig=mig+1
    else:uda+=1
print("-----> Recovered :",rec)
print("-----> Hospitalized :",hop)
print("-----> Deceased :",dea)
print("-----> Migrated :",mig)
print("-----> Undefined :",uda)

pt.title("COVID_19 DATA")
ob=("Recovered","Hospitalized","Deceased","Migrated","Undefined")
z=np.arange(len(ob))
val=[rec,hop,dea,mig,uda]
pt.xlabel("Current Status")
pt.ylabel("Total number of people")
toplabel=pt.bar(z,val,color=['green', 'orange', 'black', 'red', 'blue'])
pt.xticks(z,ob)
pt.grid(True)
for i in toplabel:
    height = i.get_height()
    pt.text(i.get_x() + i.get_width()/2, 1*height,height,ha='center', va='bottom')
pt.show()


# In[5]:


import csv, json
import pandas as pd
import numpy  as np
import matplotlib.pyplot as pt
import requests


url = requests.get('https://api.covid19india.org/raw_data.json')
json_file = open('D:\\python dataset\\raw_data.json','w')
json_file.write(str(url.text))
json_file.close()

#to load json file into variable
data = json.load(open('D:\\python dataset\\raw_data.json'))


#writing into cvs file
output = csv.writer(open('D:\\python dataset\\covid19.csv','w'))
output.writerow(data['raw_data'][0].keys())
for row in data['raw_data']:
    output.writerow(row.values())
    
#converting cvs file to excel
read_file = pd.read_csv (r'D:\\python dataset\\covid19.csv',encoding="cp1252")
read_file.to_excel (r'D:\\python dataset\\raw_data_csv.xlsx', index = None, header=True)

#read excel file and show it in graph
file=pd.read_excel('D:\\python dataset\\raw_data_csv.xlsx')
file.fillna("undefined", inplace = True) 

#pie chart
print('In this pie chart the age is represented:')
un=0
a1=0
a2=0
a3=0
a4=0
a5=0
for i in file['agebracket']:
    if(i>='0' and i<='20'):a1+=1
    elif(i>='21' and i<='40'):a2+=1
    elif(i>='41' and i<='60'):a3+=1
    elif(i>='61' and i<='80'):a4+=1
    elif(i>='81' and i<='100'):a5+=1
    else:un+=1
print("-----> 0-20 :",a1)
print("-----> 21-40 :",a2)
print("-----> 41-60 :",a3)
print("-----> 61-80 :",a4)
print("-----> 81-100 :",a5)
print("-----> Undefined :",un)
fig = pt.figure()
ax = fig.add_axes([0,0,1,1])
lab = ['0-20', '21-40', '41-60', '61-80', '81-100','Undefined']
coviddata = [a1,a2,a3,a4,a5,un]
pt.title("COVID_19 DATA")
pt.xlabel("Age Bracket")
pt.ylabel("Total number of people")
pt.grid(True)
ax.pie(coviddata, labels = lab,autopct='%1.2f%%')
pt.show()


# In[ ]:




