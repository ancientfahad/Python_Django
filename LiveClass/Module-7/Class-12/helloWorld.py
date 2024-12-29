import requests
import datetime

# *** Read *** #

# URL = 'http://164.68.107.70:6060/api/v1/ReadProduct'

# response = requests.get(URL)

# code = response.status_code
# jsonData = response.json()
# headers = response.headers

# print(code)
# print(jsonData)
# print(headers)

# *** Create *** #

# URL = 'http://164.68.107.70:6060/api/v1/CreateProduct'

# PAYLOAD = {
#     "ProductName": "Fahad",
#     "ProductCode": "122112",
#     "Img": '',
#     "UnitPrice": "122112",
#     "Qty": "1",
#     "TotalPrice": "122112",
# }

# HEADER = {
#     "Content-Type": "application/json"
# }

# # requests.post(URL, PAYLOAD, HEADER)
# response = requests.post(url = URL, json = PAYLOAD, headers = HEADER)

# code = response.status_code
# jsonData = response.json()
# headers = response.headers

# print(code)
# print(jsonData)
# print(headers)

current = datetime.datetime.now()

print(current.year)
print(current.month)
print(current.hour)
print(current.time())
print(current.second)
print(current.microsecond)
print(current.weekday())

formatCurrent = current.strftime("%d/%m/%Y")

print(formatCurrent)

startDate = datetime.datetime(1994, 7, 13)
endDate = datetime.datetime(2024, 9, 30)

difference = (endDate - startDate)/365

print(difference)

addition = endDate + datetime.timedelta(days=100)

print(addition)


