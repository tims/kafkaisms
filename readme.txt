Tweet the metamorphosis, by franz kafka.
tweets.py should be run every 30 minutes in a cron job.

To regen the tweets file, do the following:
cat metamorphosis.txt | py split.py | py group.py | py addtime.py > metamorphosis_tweets.txt
