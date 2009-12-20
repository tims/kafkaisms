Tweet the metamorphosis, by Franz Kafka.
tweets.py should be run every 30 minutes in a cron job.
See http://twitter.com/kafkaisms

To regen the tweets file, do the following:
cat metamorphosis.txt | python split.py | python group.py | python addtime.py > metamorphosis_tweets.txt


