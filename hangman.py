import os
import sys
import re

ref = [0] * 26
k=0
for letter1 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
	ref[k]=letter1
	k+=1

sum=0;
f = open("hw1_word_counts_05.txt")
fp = open("hw1_word_counts_05_calculated.txt", "w")
for line in f:
	w=line.split(' ',1)[1]
	sum=sum+int(w)
f.seek(0)
sum_initial=float(sum)
print sum_initial
pwf_sum=float(0)
for line in f:
	pre_w=line.split(' ',1)[0]
	w=line.split(' ',1)[1]
	iw=int(w)
	pw=float(iw)/float(sum)
	pwf = "%.10f" % pw
	pwf_sum+=float(pwf)
	fp.write(pre_w)
	fp.write(" ")
	fp.write(str(iw))
	fp.write(" ")
	fp.write(str(pwf))
	fp.write("\n")
f.close()
fp.close()

name = raw_input("Enter correctly guessed word (size 5): ")
l=list(name)
flag_s=0
s=""
for letter in name:
        if letter.isalpha():
                flag_s=1
                s+=str(letter)
if flag_s==1:
        s = "[^" + s + "]"
        name=name.replace('.',s)

fp = open("hw1_word_counts_05_calculated.txt", "r")
fpmatch = open("hw1_matched.txt", "w")
for line in fp:
	wd = line.split(' ')[0]
	count = line.split(' ')[1]
	prob = line.split(' ')[2]
	prob="%.10f" % float(prob)
	matchobj = re.match (name,wd)
	if matchobj:
		fpmatch.write(wd)
		fpmatch.write(" ")
		fpmatch.write(str(count))
		fpmatch.write(" ")
		fpmatch.write(str(prob))
		fpmatch.write("\n")
fpmatch.close()	
fp.close()


incorrect = raw_input("Enter incorrectly guessed letters: ")
fpexact = open("hw1_exact.txt", "w")
fpmatch = open("hw1_matched.txt", "r")
for line in fpmatch:
	wd = line.split(' ')[0]
	flag = 0
	count = line.split(' ')[1]
	prob = line.split(' ')[2]
	prob="%.10f" % float(prob)
	for letter in incorrect:
		if letter in wd:
			flag = 1
	if flag == 0: 
		fpexact.write(wd)
		fpexact.write(" ")
		fpexact.write(str(count))
		fpexact.write(" ")
		fpexact.write(str(prob))
		fpexact.write("\n")

fpexact.close()
fpmatch.close()

fp = open("hw1_exact.txt", "r")
fp_new = open("hw1_exact_new.txt", "w")
sum_new=float(0)
for line in fp:
	count=line.split(' ')[1]
	count=float(count)
	sum_new+=count
fp.seek(0)
print sum_new
prob_new=sum_new/sum_initial
for line in fp:
	wd=line.split(' ')[0]
	count=line.split(' ')[1]
	prob=line.split(' ')[2]
	prob=float(prob)
	prob="%.10f" % prob
	fp_new.write(wd)
	fp_new.write(" ")
	fp_new.write(str(count))
	fp_new.write(" ")
	fp_new.write(str(prob))
	fp_new.write("\n")
fp.close()
fp_new.close()

fp = open("hw1_exact_new.txt", "r")
alpha_prob = [0] * 26
i=-1
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        i+=1
	if letter in name or letter in incorrect:
		continue
        fp.seek(0)
        for line in fp:
                wd = line.split(' ')[0]
                prob=line.split(' ')[2]
                prob=float(prob)
                if letter in wd:
                        alpha_prob[i]+=prob
for j in range(0,26):
	alpha_prob[j]/=prob_new
	print alpha_prob[j]

max_index=alpha_prob.index(max(alpha_prob))
print "Best next guess is %c with P(Li) = %.4f" % (ref[max_index], max(alpha_prob))
fp.close()
	
