# coding:utf-8
'''
Created on 2016年12月30日

@author: Administrator
'''

import xlwt,xlrd

'''
:写入excle
'''

file = xlwt.Workbook()
table = file.add_sheet("sheetname",cell_overwrite_ok=True)  # 允许重复写入
table.write(0,0,'test')
table.write(0,0,'test1')
file.save("demo.xlsx")

'''
:读取excle
'''

data = xlrd.open_workbook('D:/Eclipseworkspace/AutoTest/src/Data-Driven/demo.xlsx')
tabel1 = data.sheet_by_index(0)
cell_A1 = tabel1.cell(0,0).value
print cell_A1
print tabel1.name

