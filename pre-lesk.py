import sys

def prelesk(filename):
  c = 0
  tagdict = {}
  i = 1
  f = open(filename, 'rU')
  outf = open('lesk-input.txt', 'w')
  for line in f:
    sen = line.split()
    for tagword in sen:
      if c == 0:
        #tagdict = str('tagdict')
        #tagdict = tagdict+str(i)
        word, tag = tagword.split('_')
        tagdict[word] = tag
        c = 1
      else:
        c = 0
    d = 0
    for item in tagdict.items():
      if item[1] == 'VB':
        outf.write(item[0])
        outf.write(' ')
        d = 1
    #outf.write('\n')
    if d == 0:
      for item in tagdict.items():
        if item[1] == 'NNP':
          outf.write(item[0])
          outf.write(' ')
      #outf.write('\n')
    tagdict = {}
    outf.write('\n')
    
          

def main():
  prelesk(sys.argv[1])

if __name__ == '__main__':
  main()
