import sys
from datetime import datetime, timedelta

paragraph = []

halfhour = timedelta(0, 1800)
delta = timedelta(0)

startdate = datetime(datetime.now().year, datetime.now().month, datetime.now().day + 1, 9)
oneday = timedelta(1)

dt = startdate
for line in sys.stdin:
    line = line.strip()
    
    if line:
        dt += halfhour
    else:
        dt += oneday
        dt = dt.replace(hour=9, minute=0)
    
    if '\x01' in line:
        l1,l2 = line.split('\x01')
        print "%s\t%s" % (dt, l1)
        print "%s\t%s" % (dt, l2)
    else:
        print "%s\t%s" % (dt, line)

sys.exit()
""" Print tweets with a timestamp """
def echoTweets(tweets, delta, kafkaid):
    #print lasttime
    dt = startdate + delta
    for tweet in tweets:
        if dt < lasttime:
            raise "Cannot tweet in the past!"
        if '\x01' in tweet:
            tweet1, tweet2 = tweet.split('\x01')
            print "\t".join([kafkaid, dt.strftime("%s"),tweet1])
            kafkaid += 1
            print "\t".join([kafkaid, dt.strftime("%s"),tweet2])
        else:
            print "\t".join([kafkaid, dt.strftime("%s"),tweet])
        lasttime = dt
        dt = dt + halfHour
    return kafkaid,dt

for line in sys.stdin:
    kafkaid += 1
    line = line.strip()
    if line:
        paragraph.append(line)
    else:
        kafkaid,dt = echoTweets(paragraph, delta,kafkaid)
        paragraph = []
        daydelta = daydelta + timedelta(1)
        hourdelta = timedelta(0,60*60*11)
        delta = daydelta + hourdelta

if paragraph:
    echoTweets(paragraph, delta)




