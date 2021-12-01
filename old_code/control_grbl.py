import requests
resultFilename = 'grbl_test.gcode' #+ '.nc'   # Filename on disk
url = "https://mymachine.openbuilds.com:3001/upload"

with open(resultFilename, 'r') as f2:
    data = f2.read() # Data = the GCODE to send
    print(data)

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\".nc\"\r\nContent-Type: false\r\n\r\n"+ data +"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'Postman-Token': "79eeb4b2-5e96-4c84-b04f-8aabda9d47b0"
    }

response = requests.request("POST", url, data=payload, headers=headers)

if response:
    print(response.text)