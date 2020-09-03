import requests
import schedule
import time

oldIp = "not the same"
# job function which will send the get request to dynv6 server with new ip address
def job():
    global oldIp
    currentIp = requests.get('https://api6.ipify.org')
    print("Your current IP Address: ",currentIp.content)
    if(currentIp.content == oldIp):
        print('The Ipv6 are the same !')
    else:
        oldIp = currentIp.content
        response = requests.get('https://ipv6.dynv6.com/api/update?ipv6=auto&token=8pkxzMqsyj8Ev4f2nFct5yHL61hzja&zone=beserver.dynv6.net')
        print("Ipv6 updated !")


schedule.every(10).seconds.do(job)

while 1:
    schedule.run_pending()
    # time.sleep(1)