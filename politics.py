import sys
import re

def dict_file():
  afinnfile = open("AFINN-111.txt")
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)  # Convert the score to an integer.

  return scores

def politic(filename):
  tweets = {}
  pollist = []
  c = 0
  f = open(filename,'rU')
  poldict = open('POLITICSDICT.txt','rU')
  #pollist = poldict.split('\n')
  for line in poldict:
    line = line.lower()
    line,blank = line.split('\n')
    pollist.append(line)
  for line in f:
    loc, tweet = line.split('\t\t\t')
    tweetlist = tweet.split()
    for word in tweetlist:
     word = word.lower()
     for pol in pollist:
       if pol == word:
         tweets[tweet] = loc
  #print c
  outf = open('politics.txt', 'w')
  for tweet in tweets.items():
    outf.write(tweet[1]+'\t\t\t'+tweet[0])
    #outf.write('\n')
  
  return tweets

def tweet_sentiment(filename):
  value = 0
  i = 0
  common = {}
  new = {}
  outf = open("final.txt", 'w')
  scores = dict_file()
  common = politic(filename)
  for tweet in common.items():
    value = 0
    for score in scores.items():
      if score[0] in tweet[0]:
        value += score[1]
    outf.write(str(value) + '\t' + tweet[0])
    new[tweet[0]] = value
    outf.write('\n')
  outf.close()
  return new
  

def new(filename):
  new = tweet_sentiment(filename)
  value = 0
  n_count = 0
  p_count = 0
  t_count = 0
  total = 0
  n_prop = 0
  p_porp = 0 
  t_prop = 0
  n_count = float(n_count)
  for line in new.items():
    value = line[1]
    if(value < 0):
      n_count +=1
    elif(value > 0):
      p_count +=1
    else:
      t_count +=1
  total = n_count + p_count + t_count
  n_prop = (float(n_count/total))*100
  p_prop = (float(p_count/total))*100
  t_prop = (float(t_count/total))*100
  print ('Proportion of negative sentiment tweets:',n_prop,'%')
  print ('Proportion of positive sentiment tweets:',p_prop,'%')
  print ('Proportion of neutral sentiment tweets:',t_prop,'%')
    

def main():
  new(sys.argv[1])

if __name__ == '__main__':
  main()
