import requests
import json

# Get information from CTAN api for babel-ukrainian package
apiurl = "https://www.ctan.org/json/2.0/pkg/babel-ukrainian"
response = requests.get(apiurl)

# Save data from CTAN api for babel-ukrainian package to .json
response_dict = response.json()

with open("data.json", "w") as file:
    json.dump(response_dict, file, indent=4)

# Get url of doc file of babel-ukrainian package
docurl = response_dict["documentation"][0]["href"]

# Repalace abstract "ctan:" to specified mirror url
docurl_mirror = docurl.replace("ctan:", "https://mirrors.ctan.org/")

# Request from mirror url
doc_file_url = requests.get(docurl_mirror)

# Save file from mirror url to local folder
open("ukraineb.pdf", "wb").write(doc_file_url.content)
