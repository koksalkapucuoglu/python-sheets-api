from fileinput import filename
import gspread

# sa = gspread.service_account(filename="C:/Users/<your_user_directory>/.config/gspread/service_account.json")
# sh = sa.open("CheetSheetName")

# wks = sh.worksheet("Worksheet 1")

# print('Rows: ', wks.row_count)
# print('Cols: ', wks.col_count)

# print(wks.acell('B2').value)

# wks.update('B2', 'updated_value')
# wks.update('A2:K2', [
#     [1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     10,
#     11]
# ])

# update_row=3
# wks.update(f'A{update_row}', [
#     [21,
#     22,
#     23,
#     24,
#     25,
#     26,
#     27,
#     28,
#     29,
#     20,
#     21]
# ])

from cheetsheet import CheetAPI 

cheetapi = CheetAPI(filename="C:/Users/<your_user_directory>/.config/gspread/service_account.json", cheetsheet_name = "CheetSheetName", worksheet_name = "Worksheet 1" )
data = [21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    20,
    21]


cheetapi.single_row_update('d', 11, data)