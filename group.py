import sys, re

headingpattern = re.compile('^(\w\s?)+$')
endpattern = re.compile('[.?!;]$')

class Tweet:
    def __init__(self):
        self.set('')
    
    def say(self):
        if self.tweet: print self.tweet
        self.set('')
    
    def set(self,tweet):
        self.tweet = tweet
    
    def add(self,tweet):
        if tweet:
            self.set(' '.join([self.tweet,tweet]))
        else:
            self.set(tweet)
    
    def get(self):
        return self.tweet

tweet = Tweet()
lastblank = True

for line in sys.stdin:
    line = line.strip()
    
    # Forcibly end the current tweet on certain punctuation at the end of a line
    if endpattern.search(tweet.get()):
        tweet.say()

    # Proceed to processing the current line
    
    # if there is a blank line we should print it
    if not line:
        if not lastblank:
            tweet.say()
            print line
            lastblank = True
        continue

    # if there is no punctuation after the splitting stage, then this must be a heading paragraph.
    if headingpattern.match(line) and lastblank:
        tweet.say()
        tweet.set('== %s ==' % line)
        tweet.say()
        lastblank = True # we want to skip blanks after a heading
        continue
   
    lastblank = False
    # if the tweet will be too long with the current line, end the tweet and start a new one.
    current = tweet.get()
    currlen = len(current)
    if currlen + len(line) + 1 > 140:
        if current:
            if currlen > 140:
                parts = current.split(' ')
                tweet1 = ' '.join(parts[:len(parts)/2])
                tweet2 = ' '.join(parts[len(parts)/2:])
                tweet.set('\x01'.join([tweet1,tweet2]))
        tweet.say()
        tweet.set(line)
    else:
        if current:
            tweet.add(line)
        else:
            tweet.say()
            tweet.set(line)


