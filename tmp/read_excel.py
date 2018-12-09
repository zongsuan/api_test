#导入xlrd
import xlrd

#打开Excel（work-book）
excel = xlrd.open_workbook("../data/data.xlsx")

#指定工作表

sheet =excel.sheet_by_name("登录")
sheet =excel.sheet_by_index(0)             #这个也是登录  1是注册

#读取信息
print(sheet.nrows)
print(sheet.ncols)
print(sheet.row_values(0))         #打印第一行数据
print(sheet.row_values(1))         #打印第二行数据
print(sheet.cell(0,0).value)       #打印指定单元格数据


#练习1：打印所有注册模块的用例，不要标题行

sheet =excel.sheet_by_name("注册")
for i in range(1,sheet.nrows):
    print(sheet.row_values(i))