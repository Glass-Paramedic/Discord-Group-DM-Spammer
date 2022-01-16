# Cat Mafia go brrrrrr 
import requests, json, time, random

recipients = []
token = input("Input ur token fam..")

print("Input the ID's of the users you want to spam, one by one, pressing [ENTER] after each ID. (NO more than 8 IDs and no less than 2) DO NOT INPUT YOUR OWN ID ")
while True:
    ide = input("Input user ID or type 'done' when ur finished fam:")
    if "done" in ide.lower():
        break
    else:
        recipients.append(ide)

header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0", "Content-Type": "application/json", "Authorization": token
}

url = "https://discord.com/api/v9/users/@me/channels"
data = {"recipients":recipients}
data = json.dumps(data)
gc_created = []

def msg(channel, auth):
    try:
        n = hash(time.time())
        data = '{"content":"@everyone","nonce":' + str(n) + ',"tts":false}'
        response = requests.post(f'https://discord.com/api/v9/channels/{channel}/messages', headers=auth, data=data)
    except:
        time.sleep(3)

for i in range(0,1000):
    try:
        time.sleep(0.3)
        response = requests.post(url, data=data, headers=header)
        resp = response.json()
        if response.status_code == 200:
            gc_created.append(resp["id"])
            continue
        else:
            ratelimit = int(resp["retry_after"]) + random.randint(0,6)
            if ratelimit > 100:
                if len(gc_created) > 2:
                    for channel in gc_created:
                        msg(channel, header)
                        time.sleep(random.random())        
            time.sleep(ratelimit)
    except Exception as e:
        print("Stopped spamming groupchats")
        print(e)
