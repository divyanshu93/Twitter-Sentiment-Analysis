import sys
import re

def unicode_cov(filename):
  
  f = open(filename)
  outf = open('politics-tweet2.txt', 'w')
  for line in f:
    #line = str(line)
    line2 = line.replace('\u2019', '.')
    print (line2)
    #line2 = line2.replace("\u2026", ":")
    #outf.write(line2)
    
def main():
  unicode_cov(sys.argv[1])

if __name__ == '__main__':
  main()
