import yaml
import twitter
import datetime
#api = twitter.Api()
#print api.GetUserTimeline('roserpens')

status = yaml.load(open('status.yaml'))
if status == None:
    status = {}
lasttweet = status.get('lasttweet', {})
lastdate = lasttweet.get('date', datetime.datetime.fromtimestamp(0))
lasttext = lasttweet.get('text')

print "lasttweet:",lastdate,lasttext

tweetsfile = open('metamorphosis_tweets.txt')
for line in tweetsfile:
    parts = line.strip().split('\t')
    dt = datetime.datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S')
    if dt > lastdate and len(parts) > 1:
        text = parts[1]
        break

print "nexttweet:",dt,text

# do post to twitter

status['lasttweet'] = {'date':dt, 'text':text}
yaml.dump(status, stream=open('status.yaml','w'))





