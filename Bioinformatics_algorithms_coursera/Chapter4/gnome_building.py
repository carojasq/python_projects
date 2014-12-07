def Composition(k, text):
	kmers = []
	for i in range(len(text)+1-k):
		kmers.append(text[i:i+k])
	return sorted(kmers)


def GenomePathProblem(kmers):
	genome = ""
	kmer_length=len(kmers[0])
	for kmer in kmers:
		genome+=kmer[0]
	genome+=kmer[1:]
	return genome


def Suffix(text):
	return text[1:]

def Prefix(text)
	return text[0:-1]
"""


#Genome Path Problem
from sys import argv
kmer_file = open(argv[1], "r")
kmers =  []
for l in kmer_file:
	kmers.append(l.strip())
print GenomePathProblem(kmers)


# Composition input
k = int(raw_input())
text = str(raw_input())
print "\n".join(Composition(k, text))
"""