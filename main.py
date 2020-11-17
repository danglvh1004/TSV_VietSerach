import gspread

gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key('1jxtRxaA5-UG9Lynl5SHfZx_gSoSEKBKgZ76ArhPRB60')
vinh = sh.sheet1
valueOfSheet1 = vinh.get_all_records()
print(valueOfSheet1)

