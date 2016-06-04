import sys
import nltk

def tweetline(filename):
  f = open(filename, 'rU')
  tweets = []
  outf = open('politics-tweet.txt', 'w')
  for line in f:
    loc,tweet = line.split('\t\t\t')
    tweets.append(tweet)
    outf.write(tweet)
    outf.write('\n')
  return tweets

def tag_tweet(filename):
  tweets = tweetline(filename)
  tag_list = []
  f = open('politics-tweet2.txt', 'rU')
  outf = open('tagged-tweet.txt', 'w')
  for line in f:
    text = nltk.word_tokenize(line)
    tag_list == []
    tag_list = nltk.pos_tag(text)
    for word in tag_list:
      outf.write(str(word[0]+'_'+word[1]))
      outf.write(' ')
    outf.write('\n')
    
  
def main():
  tag_tweet(sys.argv[1])

if __name__ == '__main__':
  main()
