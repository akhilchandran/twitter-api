import urllib,json
a= urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?screen_name=pramode_ce&count=50")
a= a.read()
a= json.loads(a)
count = 0
for e in a:
  if e["text"][0] != 'R'and count<10:
    print e['text'] 
    print "\n"
    count +=1  

