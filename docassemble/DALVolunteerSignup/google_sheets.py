import gspread
import json
from docassemble.base.util import get_config
from oauth2client.service_account import ServiceAccountCredentials
credential_info = json.loads(get_config('google').get('suffolklitlab@gmail.com service account credentials'), strict=False)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
__all__ = ['append_to_sheet']

def append_to_sheet(sheet_name, vals, worksheet_index=0):
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credential_info, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    sheet.append_row(vals)