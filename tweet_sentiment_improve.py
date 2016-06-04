import sys

def dict_file():
  afinnfile = open("AFINN-111.txt")
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)  # Convert the score to an integer.

  return scores


def tweet_sentiment():
  scores = dict_file()
  c = 0
  sentiment_score = {}
  poltweetfile = open("politics-tweet2.txt", 'rU')
  leskoutputfile = open("lesk-output.txt", 'rU')
  outf = open("sentiment-score.txt", "w")
  for line1, line2 in zip(poltweetfile, leskoutputfile):
    wordlist = []
    value = 0
    words = line1.split()
    defs = line2.split()
    for word in words:
      wordlist.append(word)
    for def1 in defs:
      wordlist.append(def1)
    for word in wordlist:
      for score in scores.items():
        if score[0] == word:
          value += score[1]
    if c == 0:
      outf.write(str(value)+'\t'+line1)
      sentiment_score[line1] = value
      outf.write('\n')
      c = 1
    else:
      c = 0
  return sentiment_score

def print_output():
  output = tweet_sentiment()
  value = 0
  n_count = 0
  p_count = 0
  t_count = 0
  total = 0
  n_prop = 0
  p_porp = 0 
  t_prop = 0
  n_count = float(n_count)
  for item in output.items():
    value = item[1]
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
  print_output()

if __name__ == '__main__':
  main()
