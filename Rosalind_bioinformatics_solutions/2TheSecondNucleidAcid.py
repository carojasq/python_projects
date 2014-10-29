#!/usr/bin/python2

#Solution for http://rosalind.info/problems/rna/
rna_string = raw_input()
print "".join(["U" if i=="T" else i for i in rna_string ])
