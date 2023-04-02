#  ________  _______   ________  ___          ________  ________  ________   
# |\   __  \|\  ___ \ |\_____  \|\  \        |\   __  \|\   __  \|\   __  \  
# \ \  \|\  \ \   __/| \|___/  /\ \  \       \ \  \|\  \ \  \|\ /\ \  \|\  \ 
#  \ \   _  _\ \  \_|/__   /  / /\ \  \       \ \   ____\ \   __  \ \   ____\
#   \ \  \\  \\ \  \_|\ \ /  /_/__\ \  \       \ \  \___|\ \  \|\  \ \  \___|
#    \ \__\\ _\\ \_______\\________\ \__\       \ \__\    \ \_______\ \__\   
#     \|__|\|__|\|_______|\|_______|\|__|        \|__|     \|_______|\|__|   
#
# ============================================================================
# 
# A tool to get data from Rezi and use it on PBP to download games. The code
# is available on Github, if you've paid for this then you've been scammed!
# This has been written with Python3 and VSCodium
# 
# ============================================================================
# 
# Please note that the code provided here is licensed under the GNU General 
# Public License Version 3.0 (GPL-3.0). This means that you are free to use, 
# modify, and distribute the code under the terms of the GPL-3.0, but please 
# be aware of the license requirements and restrictions outlined in the 
# GPL-3.0.
# 
# ============================================================================ 

# Imports
import pandas as pd
import json
import requests
import re
import sys

# Defines the data to where will it get the rezi.csv file
owner = "Brisolo32"
repo = "rezi-backend"
tag = "rezi"
filename = "rezi.csv"

# URL from where to download
url = f'https://github.com/{owner}/{repo}/releases/download/{tag}/{filename}'

if len(sys.argv) != 3:
    print("Usage: pbp-rezi [query] [cache location]")
    exit()

# Arguments to be passed on
query = sys.argv[1].lower()
cache_location = sys.argv[2]

print(f"Query: {query}")
print(f"Cache Location: {cache_location}")

# Sends a request to the URL variable and writes it to an rezi.csv file
response = requests.get(url)
file = open(f'./{filename}', 'wb')
file.write(response.content)
file.close()

df = pd.read_csv("./rezi.csv")
out: list[int] = []

# Goes through every value on the list and gets
# those who contain the query string
for index, values in enumerate(df["title"]):
    value_lower: str = values.lower()

    if query in value_lower:
        out.append(index)

# Loops over out and gets the row equal to the value
print(f"Length: {len(out)}")
res_value: dict[str, any] = {'response': []}
if len(out) != 0:
    for index, value in enumerate(out):
        row = df.iloc[value]

        title: str = re.sub(r"\.(zip|7z|rar)$", "", row["title"])
        url: str = row["link"]
        platform: str = row["icon"]

        data = {
            'title': f"{title} ({platform})",
            "urls": [
                url
            ]
        }

        res_value["response"].append(data)
else:
    exit()

# Writes the data to an file with the name in cache_location
encoded_json = json.dumps(res_value)

with open(f"{cache_location}", "w") as cache_file:
    cache_file.write(encoded_json)
    cache_file.close()

with open(cache_location, 'r') as f:
    data = f.read()
    print(f"Data written to file: {data}")