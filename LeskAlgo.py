import string
import sys
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from itertools import chain


port = PorterStemmer()

def simplelesk(context, ambword, position=None, stem=True,hyperhyponym= True ):
    maxoverlap = 0;
    bestsense = None
    context = context.split()
    if not wn.synsets(ambword): 
         return None 
    for sentsense in wn.synsets(ambword):
        if position and sentsense.position is not position:
            continue
        ldic = []
        ldic+= sentsense.definition().split()
        for i in sentsense.examples():
            ldic+= i.split()

        ldic+= sentsense.lemma_names()

        if hyperhyponym == True:
            ldic+= list(chain(*[i.lemma_names() for i in sentsense.hypernyms()+sentsense.hyponyms()]))       

        if stem == True: 
            ldic = [port.stem(j) for j in ldic]
            context = [port.stem(k) for k in context] 
        soverlaps = set(ldic).intersection(context)
        #print ('%d' %(len(soverlaps)))
        #print ('%s: %s' % (sentsense.name(), sentsense.definition()))
        #print ('Examples')
        #for i in sentsense.examples():
            #print ('%s' %(i))
        #print('\n')
        if len(soverlaps) > maxoverlap:
            bestsense = sentsense
            maxoverlap = len(soverlaps)
    return bestsense

#print("All senses of word 'Bank' with overlap counts")
#print('\n')
def leskcomp(filename1, filename2):
    f1 = open(filename1, 'rU')
    f2 = open(filename2, 'rU')
    outf = open('lesk-output.txt', 'w')
    for line1,line2 in zip(f1,f2):
        sen = []
        words = line1.split()
        sen.append(line2)
        for word in words:
            ans2 = simplelesk(sen[0], word)
            #print ("Context Sentense:", sen[0])
            #outf.write("Context Sentense:"+ sen[0])
            #print (word)
            #outf.write(word)
            #outf.write('\n')
            #print ("Best Sense:")
            #outf.write("Best Sense:")
            #outf.write('\n')
            if ans2:
                #print ("WordNet Definition:",ans2.definition())
                outf.write(ans2.definition())
            #print ('\n')
        outf.write('\n')

#sent = ['The bank can guarantee deposits will eventually cover future tuition costs because it invests in adjustable-rate mortgage securities.']
#ans2 = simplelesk(sent[0],'bank')
#print ("Context Sentense:", sent[0])
#print ('\n')
#print ("Best Sense:")
#print ("WordNet Definition:",ans2.definition())
#print
def main():
    leskcomp(sys.argv[1], sys.argv[2])
if __name__ == '__main__':
  main()


