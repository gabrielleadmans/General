#script that takes a sequence as input and outputs all peptides of length 20 aas with a step of 10 aas
# requires a -s argument with sequence to be cut up

import sys
import argparse
import math

#this part stores the "seqence" argument into a variable.
print 'Argument List:', str(sys.argv)

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--sequence", help="sequence to be split into peptides")

args = argParser.parse_args()
#print("args=%s" % args)
#print("args.sequence=%s" % args.sequence)
sequence = args.sequence
print (sequence)

print ("length",len(sequence))
nb_whole_peptides=math.trunc((len(sequence))/10-1)
print (nb_whole_peptides)

peptides=[]

i=1
while i <= nb_whole_peptides:
    print "> peptide",(i-1)*10+1,"-",(i-1)*10+20+1
    print (sequence [(i-1)*10:(i-1)*10+20])
    
    peptides.append("> peptide"+str((i-1)*10+1)+"-"+str((i-1)*10+20+1))

    peptides.append (sequence [(i-1)*10:(i-1)*10+20])
    i=i+1


peptides.append(sequence[-20:])

print "> peptide",len(sequence)-19,"-",len(sequence)
print (sequence[-20:])

print "all peptides",peptides 
print "number of peptides:", len(peptides)


