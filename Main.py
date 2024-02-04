import os
try:
    import requests 
    import ctypes 
    import time
    from datetime import datetime
    import uuid
    import json
except:
    print("Installing libs pls wait")
    libs = [
        "requests",
        "ctypes",
        "datetime",
        "uuid"
    ]
    for lib in libs:
        os.system(f"pip install -q {lib}")
    import requests 
    import ctypes 
    import time
    from datetime import datetime
    import uuid
    import json
    print("finished")

if not os.path.exists("config.json"):
    open("config.json", "w")

    data = {
        "NOTE": "To use replace the first GUILDID1 with the id of the guild u want to bump then in CHANNELID FOR GUILDID1 put the channel id wheare u want the command to be ran (the channelid obv must be from the guild)",
        "IMPORTANT": "4 is the max bc of the 30 min coldown (2h for the same guild 30min for diffrent guild)",
        "GUILDID EXAMPLE": "1157405821450338334",
        "CHANNELID EXAMPLE": "1197292049167290410",
        "GuildIDS": [
            "GUILDID1",
            "GUILDID2",
            "GUILDID3",
            "GUILDID4"
        ],
        "ChannelIDS": [
            "CHANNELID FOR GUILDID1",
            "CHANNELID FOR GUILDID2",        
            "CHANNELID FOR GUILDID3",
            "CHANNELID FOR GUILDID4"
        ],
        "Token": "Put the token of your account here so it can send the bump command",
        "Hide": False
    }

    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)
    input("Config written please fill it out with the info needed")
    os.startfile("config.json")
    exit()

with open("config.json", "r") as f:
    data = json.load(f)
    guild_ids = data["GuildIDS"]
    channel_ids = data["ChannelIDS"]
    token = data["Token"]
    hide_s = data["Hide"]

def send(token, channel_id, guild_id):
    try:
        r = requests.post(
            "https://discord.com/api/v9/interactions",
            headers={
                "Authorization": token,
                "Content-Type": "application/json",
            },
            json={
                "type": 2,
                "application_id": "302050872383242240",
                "guild_id": guild_id,
                "channel_id": channel_id,
                "data": {
                    "type": 1,
                    "name": "bump"
                }
            }
        )
        return r.status_code, r.text
    except Exception as e:
        return "???", e


def get_time():
    return datetime.now().strftime("%d/%m %H:%M:%S")


def hide():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 0)

def main():
    if None in (guild_ids, channel_ids, token):
        print("Error reading configuration. Exiting.")
        return

    i = 0
    if hide_s:
        hide()

    while True:
        for channel_id, guild_id in zip(channel_ids, guild_ids):
            i += 1
            status_code, response = send(token, channel_id, guild_id)
            print(f"{get_time()} | {i} | {status_code} | {response} | Waiting 2100s")
            time.sleep(2100)
        i = 0

if __name__ == "__main__":
    main()
