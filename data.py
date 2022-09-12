import pandas
import json

excel_data_df = pandas.read_excel('tarot_sheet.xlsx', sheet_name = 'Sheet1')

thisisjson = excel_data_df.to_json(orient='records')

print('Excel sheet to JSON:\n', thisisjson)

thisisjson_dict = json.loads(thisisjson)

with open('tarot_sheet.json', 'w') as json_file:
    json.dump(thisisjson_dict, json_file)