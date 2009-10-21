import sys
from datetime import datetime, timedelta

paragraph = []

halfHour = timedelta(0, 1800)
delta = timedelta(0)

startdate = datetime(datetime.now().year, datetime.now().month, datetime.now().day)
daydelta = timedelta(1)
hourdelta = timedelta(0,60*60*11)
delta = daydelta + hourdelta

lasttime = startdate

""" Print tweets with a timestamp """
def echoTweets(tweets, delta):
    dt = startdate + delta
    for tweet in tweets:
        if dt < lasttime:
            raise "Cannot tweet in the past!"
        print "\t".join([dt.strftime("%s"),tweet])
        lasttimee = dt
        dt = dt + halfHour
    return dt

for line in sys.stdin:
    line = line.strip()
    if line:
        paragraph.append(line)
    else:
        dt = echoTweets(paragraph, delta)
        paragraph = []
        daydelta = daydelta + timedelta(1)
        hourdelta = timedelta(0,60*60*11)
        delta = daydelta + hourdelta

if paragraph:
    echoTweets(paragraph, delta)




