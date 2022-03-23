from fileinput import filename
from msilib.schema import Class
import gspread


class CheetAPI:

    def __init__(self, cheetsheet_name, worksheet_name, filename = None, ):
        """ 
        cheetsheet_name: Google cheetsheet filename
        worksheetname: worksheet name in defined cheetsheetname
        filename: If you want to store the credentials file somewhere else, specify the path to service_account.json:
        """

        self.cheetsheet_name = cheetsheet_name
        self.worksheet_name = worksheet_name
        self.filename = filename
        
        if self.filename is None:
            self.sa = gspread.service_account()
        else:
            self.sa = gspread.service_account(filename= self.filename)

        self.sh = self.sa.open(self.cheetsheet_name)

        self.wks = self.sh.worksheet(self.worksheet_name)

    def single_row_update(self, start_row_name, row_range, data):
        if row_range != len(data):
            raise Exception(f'Row range and length of data must be same! row range/data length: {row_range}/{len(data)}') 
        else:
            self.wks.update(f'{start_row_name.upper()}{row_range}', [data])

"""
Example:

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

"""