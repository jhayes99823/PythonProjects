import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp = "hosts_temp"
redirect = "127.0.0.1"
website_block_list = [
    "www.facebook.com",
    "facebook.com",
    "www.twitter.com",
    "twitter.com"
]

# runs forever
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 2) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 3):
        print("Working Hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in website_block_list:
                if site in content:
                    pass
                else:
                    file.write("\n" + redirect+ " " + site + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()  
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_block_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours")

    time.sleep(5)