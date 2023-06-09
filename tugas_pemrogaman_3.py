# -*- coding: utf-8 -*-
"""Tugas Pemrogaman 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ETGu-9C1OI3Of8vOHU_NYnSg6TQBOMYc

# **Ramadhan Aditya Ibrahim - 1301200240**
# **Ryan Chandra Hadi - 1301204125**

# **Data Set**
"""

import pandas as pd
import math

df = pd.read_excel("https://raw.githubusercontent.com/bloodsking/Learning-AI/main/traintest_.xlsx", "train")
df

df1= pd.read_excel("https://raw.githubusercontent.com/bloodsking/Learning-AI/main/traintest_.xlsx", "test")
df1

x1 = df['x1']
x2 = df['x2']
x3 = df['x3']
x4 = df['id']
x5 = df['y']
x6 = x1.tail(80).tolist()
x7 = x2.tail(80).tolist()
x8 = x3.tail(80).tolist()
x9 = x1.head(216).tolist()
x10 = x2.head(216).tolist()
x11 = x3.head(216).tolist()
x12 = x5.tail(80).tolist()
y1 = df1['x1']
y2 = df1['x2']
y3 = df1['x3']

"""# **Rumus**"""

def euclideanA(data1, data2, data3, data4, data5, data6, i, index):
  dataD = []
  for j in range(index):
    rumus1 = ((data1[i] - data2[j])**2 + (data3[i] - data4[j])**2 + (data5[i] - data6[j])**2)**0.5
    dataD.append(((rumus1, j, x5[j])))

  return dataD

"""# **Validation Data**"""

for zz in range(1, 40, 2):
  z = []
  temp = 0
  for i in range(len(x6)):

    final = 0
    final1 = 0
  
    jarak = euclideanA(x6, x9, x7, x10, x8, x11, i, len(x10))
    jarak.sort()
    jarak = jarak[:zz]
    for k in range(zz):
      if(jarak[k][2]) ==1:
        final1 += 1
      else:
        final += 1
    
    if(final < final1):
      z.append(1)
    else:
      z.append(0)
  print(z)
  print(x12)
  for j in range(len(x12)):
    if z[j] == x12[j]:
      temp += 1
  persen = temp/len(x12) * 100    
  print("hasil validasi dari K: ", zz, "sebesar :",persen, "%\n")

"""# **Test Data**

"""

z = []
zz = 21
for i in range(len(df1)):
  final = 0
  final1 = 0
  jarak = euclideanA(y1,x1,y2,x2,y3,x3,i,len(df))
  jarak.sort()
  jarak = jarak[:zz]
  for k in range(zz):
    if(jarak[k][2]) ==1:
      final1 += 1
    else:
      final += 1
    
  if(final < final1):
    z.append(1)
  else:
    z.append(0)
print(z)
z1 = pd.DataFrame(z)
z1.columns = ['y']
z1['x1'] = y1
z1['x2'] = y2
z1['x3'] = y3
print(z1)

#membuat file excel
file = pd.ExcelWriter('hasil akhir.xlsx')

#memindahkan data1 ke excel
z1.to_excel(file)

#menyimpan hasil file yang sudah di export
file.save()
print("Data biner sudah ditambahkan ke data tes")

