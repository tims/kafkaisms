Tweet the metamorphosis, by franz kafka.
tweets.py should be run every 30 minutes in a cron job.

To regen the tweets file, do the following:
cat metamorphosis.txt | python split.py | python group.py | python addtime.py > metamorphosis_tweets.txt

TODO:
deal with double tweets, ie different messages at the same timestamp
