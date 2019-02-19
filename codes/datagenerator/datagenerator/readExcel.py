import xlrd

ExcelFileName= 'C:\CODE\dataGeneration\codes\syndatagenerator\codes\datagenerator\datagenerator\Data.xlsx'
workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_name("Sheet1") # We need to read the data 
#from the Excel sheet named "Sheet1"

num_rows = worksheet.nrows #Number of Rows
num_cols = worksheet.ncols #Number of Columns

result_dict =[]
header_row_data = []

for curr_col in range(0, num_cols, 1):
    data = worksheet.cell_value(0, curr_col) # Read the data in the current cell
    header_row_data.append(data)

for curr_row in range(1, num_rows, 1):
    row_data = []
    print(curr_row)
    for curr_col in range(0, num_cols, 1):
        data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
        row_data.append(data)
    result_dict.append(dict(zip(header_row_data, row_data)))

print (result_dict)