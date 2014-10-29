#!/usr/bin/python2

#Solution for http://rosalind.info/problems/revc/ 
in_seq = raw_input()
out = ""
for i in in_seq:
    if i=="A":
	out += "T"
    elif i=="T":   
        out += "A"
    elif i=="G":   
        out += "C"
    elif i=="C":   
        out += "G"
print out[::-1]

