def Composition(k, text):
	kmers = []
	for i in range(len(text)+1-k):
		kmers.append(text[i:i+k])
	return sorted(kmers)

def SuffixComposition(k, text, uniq=False):
	kmers = []
	for i in range(len(text)+1-k):
		kmers.append(text[i:i+k-1])
	if uniq:
		return sorted(list(kmers))
	else:
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

def Prefix(text):
	return text[0:-1]

def Overlap(patterns):
	kmers=sorted(patterns)
	adj_list = []
	for k1 in kmers:
		for k2 in kmers:
			if Suffix(k1) == Prefix(k2):
				adj_list.append((k1, k2))
	return adj_list

def deBrujin(k, text):
	kmers = SuffixComposition(k, text)
	overl = Overlap(kmers)
	adj_list = {}
	# Inicializo diccionario
	for kmer in kmers:
		adj_list[kmer]=[]
	for i in range(len(text)+1-k):
		adj_list[text[i:i+k-1]].append(text[i+1:i+k])
	return adj_list

def deBrujinGraphFromKmers(kmers_in):
	#print "Initialazing dictionary"
	kmers = []
	for kmer in kmers_in:
		kmers = kmers+SuffixComposition(len(kmer), kmer, uniq=True )
	kmers = set(kmers)
	adj_dict = {}
	for kmer1 in kmers:
		adj_dict[kmer1] = []
	for kmer in kmers_in:
		adj_dict[Prefix(kmer)].append(Suffix(kmer))
	return adj_dict



from sys import argv

kmer_file = open(argv[1], "r")
#kmer_file = open("input_deBrujinFrmKmers.txt", "r")
kmers =  []
for l in kmer_file:
	kmers.append(l.strip())
adj_dict =  deBrujinGraphFromKmers(kmers)
for k in sorted(adj_dict.keys()):
	print "%s -> %s" % (k, ",".join(adj_dict[k]))

"""

#adj_dict = deBrujin(12, "CTGAAGACCTCTCCACATTACTACGATATAAATCATTTCAGCCTCTAGATACGCCTTGGTGGGTGGGGTTGGCAATTTACGATATGTCCGAATGATTTGACACCAAATACCTTAGCTAGCCCCAAGGAAAATTCTGGGCTTTACGTTGGCCGAGCCACATTACTACAGTAAGGTTAAGCAACCAGCCAGTCGCTCATAAGGACTCCACGCCTCCCGTTACTGACTTCCAACAACAATGTGACAGTAGACTGGAACCTGGGAGGACATTATTGATTCGCCGCGAATCTTCTAAGGTATTTTACCCCCACTGGTCACCTTAACCATTAAGACCTCGAAGTGACACCTAGCCTCTTAACACCCAACTCCACCGACAATACCTATTCGCTGACAAGCGGGACATCCGATCGCCCCTGACTCGAGGTGTCTACCGTCCATCGATTGCTAAACTTTGTTAGGAGTCTAAGCGAACCATGGGAAGGGGGCGGCAGTCAACGTGCTCCTTTAGTGAGGTACCATATTCTTACAGCATGTGGAGCGCAGCAAACTAGCGACCGGGAGTACTCCCACAACCCTGGGTACGTACTGCACTTTTTTCAAGAGCCAGGGTCATTTAAATAGCATCTTTGCTCTTTCTGATAAGGGGGCGACCATCTCCGAATTGAGCCAAACGCTGGTATAAGACTCGTCTCATGACTCCCTAGCCATTTGTATGTTGTCATTTCTGATTTTAGCAGGTAAAACGTAAGGCCTGCTAAAGAATCACGCGGGGAGGCCTTAAATTTCGTCATGGAGCAATCGTCCTAGATTGCTGTGAAGGTTCGTACCAGTAGAGTCTAATGTGCGTAAATGTTAACTGGCCGTATATTCTCTGGTGAGCTGAAACAGAAAGCTGGCAGAAAGCCACTCTTGCTGTTTCGTGTGTACGGACATCGGGATAGTACCAAAAAGCATGTTCTTCATCTGGCGATGCTTGATGTCTACCGTAGACACCTTCATACGT")
# Input for generate de brujin from text
k = int(raw_input())
text = str(raw_input())
adj_dict = deBrujin(k, text)
for k in sorted(adj_dict.keys()):
	print "%s -> %s" % (k, ",".join(adj_dict[k]))



# Overlap input
from sys import argv
#kmers = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"] 
kmer_file = open(argv[1], "r")
kmers =  []
for l in kmer_file:
	kmers.append(l.strip())
pairs = Overlap(kmers)
for p in pairs:
	print " -> ".join(p)
	

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