#!/usr/bin/env python

from better_profanity import profanity
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def censor(word):
    return profanity.censor(word)

sc = SparkContext("local[*]", "Censor")
sc.setLogLevel('ERROR')

ssc = StreamingContext(sc, 1)

lines = ssc.socketTextStream("localhost",9999)

words = lines.map(lambda line: censor(line))

# Print the first ten elements of each RDD generated in this DStream to the console
words.pprint()
ssc.start()
ssc.awaitTermination()

