# скачать файл с данными можно по этой ссылке - http://bit.ly/2dgWaBp
#• Какие три страны завоевали больше всех медалей на летних играх?

# • Какие три страны завоевали больше всех медалей на зимних играх?

#• Сколько медалей завоевывал в среднем за одни игры Советский союз (с разбивкой на летние и зимние игры)?

#• Сколько медалей в среднем за игры выигрывали страны, которые раньше входили в Советский союз (с разбивкой на летние и зимние игры)?

import xlrd
import unidecode
import copy
book= xlrd.open_workbook('olympicsalltime.xls')
sheet = book.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
len1=len(vals)
len2=len(vals[0])
print('Первое задание')
a=[]
for i in range(len1):
    b = []
    for j in range(len2):
        if j==0:
            b.append(unidecode.unidecode(sheet.cell_value(i,j)))
        else:
            if i>0:
                b.append(int(sheet.cell_value(i,j)))
            else:
                b.append(sheet.cell_value(i, j))
    a.append(b)
sum_summer=[]
for i in range(len1-1):
    if i ==0:
        continue
    else:
        sum_summer.append(a[i][2]+a[i][3]+a[i][4])
sum_summer1=copy.copy(sum_summer)
sum_summer1.sort()
w=[]
for i in range(len(a)):
    if sum_summer[i]==sum_summer1[-1]:
        w.append(i)
        break
for i in range(len(a)):
    if sum_summer[i]==sum_summer1[-2]:
        w.append(i)
        break
for i in range(len(a)):
    if sum_summer[i]==sum_summer1[-3]:
        w.append(i)
        break
print(a[w[0]+1][0], "-",a[w[0]+1][2]+a[w[0]+1][3]+a[w[0]+1][4])
print(a[w[1]+1][0], "-",a[w[1]+1][2]+a[w[1]+1][3]+a[w[1]+1][4])
print(a[w[2]+1][0], "-",a[w[2]+1][2]+a[w[2]+1][3]+a[w[2]+1][4])
print()
print("Второе задание")
sum_winter=[]
for i in range(len1-1):
    if i ==0:
        continue
    else:
        sum_winter.append(a[i][6]+a[i][7]+a[i][8])
sum_winter1=copy.copy(sum_winter)
sum_winter1.sort()
w_1=[]
for i in range(len(a)):
    if sum_winter[i]==sum_winter1[-1]:
        w_1.append(i)
        break
for i in range(len(a)):
    if sum_winter[i]==sum_winter1[-2]:
        w_1.append(i)
        break
for i in range(len(a)):
    if sum_winter[i]==sum_winter1[-3]:
        w_1.append(i)
        break
print(a[w_1[0]+1][0], "-",a[w_1[0]+1][6]+a[w_1[0]+1][7]+a[w_1[0]+1][8])
print(a[w_1[1]+1][0], "-",a[w_1[1]+1][6]+a[w_1[1]+1][7]+a[w_1[1]+1][8])
print(a[w_1[2]+1][0], "-",a[w_1[2]+1][6]+a[w_1[2]+1][7]+a[w_1[2]+1][8])
print()
print("Третье задание")
print("В среднем за одни летние игры Советкий союз зарабатывал:", (a[108][2]+a[108][3]+a[108][4])/a[108][1], "медалей")
print("В среднем за одни зимние игры Советкий союз зарабатывал:", (a[108][6]+a[108][7]+a[108][8])/a[108][5], "медалей")
print()
print('Четвертое задание')
ip=[106,135,12,68,139,44,4,75,8,39,78,84,74,126]
for i in ip:
    if a[i][1] != 0:
        print('В среднем',a[i][0], 'за летние игры выигрывал(а) -', (a[i][2]+a[i][3]+a[i][4])/a[i][1], 'медалей')
    else:
        print(a[i][0], 'не участвовал на летней олимпиаде')
    if a[i][5]!=0:
        print('В среднем ', a[i][0], 'за зимние игры выигрывал(а) -', (a[i][6] + a[i][5] + a[i][4]) / a[i][5], 'медалей')
    else:
        print(a[i][0], 'не участвовал на зимней олимпиаде')

