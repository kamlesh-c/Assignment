#! /usr/bin/python
import re
import requests
req = requests.get("https://security.gentoo.org/glsa/202008-20")
data = req.text
search = "Affected package."
searchresult = re.findall(search,data)
print (format(searchresult[0]))
#regex = "Affected versions.+(\n.+)([0-9]\.[0-9].)"
regex = "Affected versions.+(\n.+)([0-9]\.[0-9][0-9])"
version = re. findall(regex,data)
print ("Affected version :{}".format(version[0][-1]))
