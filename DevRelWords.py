#making derivationally related word dictionary for improving the word alignment.
import os
import re

#files on which we are reading
n_data = open('DerivationallyRelatedWords/data.noun','r').readlines()
v_ind = open('DerivationallyRelatedWords/index.verb','r').readlines()
a_ind = open('DerivationallyRelatedWords/index.adj','r').readlines()
ad_ind = open('DerivationallyRelatedWords/index.adv','r').readlines()

#file in which the final output is stored
dev_wd = open('DerivationallyRelatedWords/Dev_Words.dic','w')
#other temporary variables used are:
    # i, i1, i2, i3 - iterators
    # verbs_sub, adj_sub, adv_sub - to hold results from regex findall operations
    # t - temporary split operation result holder


for i in range(0,len(n_data)):
    temp = n_data[i].split('|')
    #nouns or proper nouns.......
    nouns = re.findall('[a-z][a-z]*\-[A-Za-z0-9][\_\-\.A-Za-z0-9]*|[A-Z][a-z]*\-[A-Za-z0-9][\_\-\.A-Za-z0-9]*|[a-z][a-z]*\_[A-Za-z0-9][\_\-\.A-Za-z0-9]*|[A-Z][a-z]*\_[A-Za-z0-9][\_\-\.A-Za-z0-9]*|[a-z][a-z]*\-[a-z]*|[a-z][a-z][a-z]*|[A-Z][A-Z]*[a-z]*',temp[0])
    print(i,nouns)
    if len(nouns)>0:
        if not nouns[0].isupper() and not nouns[0].islower():
            #print('\nproper-nouns:', end = ' ')
            dev_wd.write('\nproper-nouns: ')
        else:
            #print('\nnouns:', end = ' ')
            dev_wd.write('\nnouns: ')
        for i1 in nouns:
            #print(i1.replace('_',' '), end = '; ')
            dev_wd.write(i1.replace('_',' ') + '; ')
        #verbs........
        verbs_sub = re.findall('\+ [0-9]* v',temp[0])
        if(verbs_sub):
            #print('\nverbs:', end = ' ')
            dev_wd.write('\nverbs:' + ' ')
            for i2 in range(0,len(verbs_sub)):
                for i3 in v_ind:
                    if verbs_sub[i2][2:10] in i3:
                        t = i3.split(' ')
                        #print(t[0].replace('_',' '), end = '; ')
                        dev_wd.write(t[0].replace('_',' ') + '; ')
        #adjectives........
        adj_sub = re.findall('\+ [0-9]* a',temp[0])
        if(adj_sub):
            #print('\nadjectives:', end = ' ')
            dev_wd.write('\nadjectives: ')
            for i2 in range(0,len(adj_sub)):
                for i3 in a_ind:
                    if adj_sub[i2][2:10] in i3:
                        t = i3.split(' ')
                        #print(t[0].replace('_',' '), end = '; ')
                        dev_wd.write(t[0].replace('_',' ') + '; ')
        #adverbs........
        adv_sub = re.findall('\+ [0-9]* r',temp[0])
        if(adv_sub):
            #print('\nadverbs:', end = ' ')
            dev_wd.write('\nadverbs: ')
            for i2 in range(0,len(adv_sub)):
                for i3 in ad_ind:
                    if adv_sub[i2][2:10] in i3:
                        t = i3.split(' ')
                        #print(t[0].replace('_',' '), end = '; ')
                        dev_wd.write(t[0].replace('_',' ') + '; ')
        #print('\ngloss:',re.sub(r'\".*\"','',temp[1].lstrip()))
        dev_wd.write('\ngloss:' + re.sub(r'\".*\"','',temp[1].lstrip()))
    #print('\n----------------------------------------------------------------------------------------------------')
dev_wd.close()
