import re
link = "/rc/clk?jk=20a30344f3ebc4db&fccid=abd185ea16d56fc8&vjs=3"
clickable_link = "https://www.indeed.com/viewjob?jk=20a30344f3ebc4db&from=serp&vjs=3"

new = link.replace("/rc/clk","https://www.indeed.com/viewjob")
result = re.sub('&[^>]+&', '&from=serp&', new)
print(clickable_link)
print(result)
