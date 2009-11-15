import yaml
import twitter
import datetime
import sys

config = yaml.load(open('config.yaml'))
username = config['username']
password = config['password']

status = yaml.load(open('status.yaml'))
if status == None:
    status = {}

api = twitter.Api(username=username, password=password)

bla = api.GetUserTimeline('kafkaisms', count=1)
if len(bla) > 0:
    livetweet = [long(bla[0].id), datetime.datetime.strptime(bla[0].created_at, "%a %b %d %H:%M:%S +0000 %Y"), bla[0].text]
else:
    livetweet = [None, None, None]
liveid, livedate, livetext = livetweet

lasttweet = status.get('lasttweet', {})
lastid = lasttweet.get('id',0)
lastdate = lasttweet.get('date', datetime.datetime.fromtimestamp(0))
lasttext = lasttweet.get('text')

print "livetweet:",liveid, livedate, livetext
print "lasttweet:",lastid, lastdate, lasttext

if lastid > 0:
    if lastid != liveid:
        raise Exception("live id and last id don't match!")
    if lasttext != livetext:
        raise Exception("live text and last text don't match!")

tweetsfile = open('metamorphosis_tweets.txt')
for line in tweetsfile:
    parts = line.strip().split('\t')
    dt = datetime.datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S')
    if dt > lastdate and len(parts) > 1:
        text = parts[1]
        break

print "nexttweet:",dt,text

if dt < datetime.datetime.now():
    print "past publish time, publishing"
else:
    print "not yet publish time."
    sys.exit()

# do post to twitter
poststatus = api.PostUpdate(text)
print poststatus
id = long(poststatus.id)

status['lasttweet'] = {'id':id, 'date':dt, 'text':text}
yaml.dump(status, stream=open('status.yaml','w'))





