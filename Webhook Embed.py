import requests
url = input("Webhook URL: ")
embed = {}
embedtitle = input("Embed title: ")
embed["title"] = embedtitle
embeddesc = input("Embed description: ")
embed["description"] = embeddesc
while True: #Thumbnail (optional)
    thumbnailornot = input("Add a thumbnail? (Yes/no): ")
    if thumbnailornot.lower() == 'yes':
        embedthumbnailurl = input("Enter a thumbnail URL: ")
        embed['thumbnail'] = {"url": embedthumbnailurl}
        break
    elif thumbnailornot.lower() == 'no':
        break
    else:
        print("Please enter either 'yes' or 'no' (without quotes).")
embedfieldnum = input("How many fields in the embed? (Enter a number, 0 for none): ")
try: embedfieldnum = int(embedfieldnum)
except: print("You were supposed to enter a number - we'll assume you meant 0.")
if embedfieldnum is not 0:
    embed['fields'] = []
    for fieldnum in range(embedfieldnum):
        fieldtitle = input("Field {} Title: ".format(fieldnum+1))
        fieldtext = input("Field {} Content: ".format(fieldnum+1))
        embed['fields'].append({"name":fieldtitle,"value":fieldtext})
embedcolor = input("Embed Hex Color (6 Digit Hex): ")
embedcolor = int(embedcolor, 16)
embed["color"] = embedcolor
print(embed)
data = {"embeds": [embed]}
requests.post(url,json=data)
