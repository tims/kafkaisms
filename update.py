from datetime import datetime

def getTimeTweet(line):
    timestr, tweet = line.split('\t')
    timestamp = datetime.fromtimestamp(int(timestr))

def getLastTweet():
    f = open('lasttweet.txt')
    print "opened lasttweet.txt"
    last = f.next()
    f.close()
    if last:
        timestamp, tweet = getTimeTweet(line)
        print "Last tweet was at:", timestamp
        print "Tweet text:", tweet
        return timestamp, tweet
    else:
        return None, None
    
lasttime, lasttweet = getLastTweet()

f = open('metamorphosis_tweets.txt')
for line in f:
    timestr, tweet = line.split('\t')
    if



