from collections import OrderedDict
#Solution for 	http://rosalind.info/problems/dna/

in_seq = raw_input()
ns = {'A': 0, 'C': 0, 'G': 0, 'T': 0} #nucleotides
for n in in_seq: ns[n]+=1
print "%i %i %i %i" % (ns['A'], ns['C'], ns['G'], ns['T'])

