import webbrowser
from datetime import datetime
def url_open(url):
    webbrowser.open(url, new=1)
    return 0

datetime_str = '8/26/22 20:48:00'
datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

url = "https://i.hzmbus.com/webhtml/ticket_details?xlmc_1=%E9%A6%99%E6%B8%AF&xlmc_2=%E7%8F%A0%E6%B5%B7&xllb=1&xldm=HKGZHO&code_1=HKG&code_2=ZHO"

print (datetime.now(),datetime_object)

while 0 == 0:
    now = datetime.now()
    print (datetime_object, now)
    if now > datetime_object:
        url_open (url)
        print (datetime_object, now)
        raise Exception("Done")

