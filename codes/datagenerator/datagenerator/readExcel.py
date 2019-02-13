import xlrd

ExcelFileName= 'C:\CODE\dataGeneration\codes\syndatagenerator\codes\datagenerator\datagenerator\Data.xlsx'
workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_name("Sheet1") # We need to read the data 
#from the Excel sheet named "Sheet1"

num_rows = worksheet.nrows #Number of Rows
num_cols = worksheet.ncols #Number of Columns

result_data =[]
for curr_row in range(0, num_rows, 1):
    row_data = []
    for curr_col in range(0, num_cols, 1):
        data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
        print(data)
        row_data.append(data)
        result_data.append(row_data)