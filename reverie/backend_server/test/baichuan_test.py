import requests
import time
import os
url = "http://10.112.189.233:5001/baichuan2/chat"

def baichuan_request(prompt):
    os.environ["HTTP_PROXY"] = ""
    os.environ["HTTPS_PROXY"] = ""
    # time1 = time.time()
    return requests.post(url, data={"content": prompt}).text
    # print(f"baichuan time cost:{time.time() - time2}")

# with open("content.txt", 'r', encoding='utf-8') as f:
#     prompt = f.read()
# baichuan_res = baichuan_request(prompt)
# print("\nbaichuan_res111:\n",baichuan_res)