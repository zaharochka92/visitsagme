# -*- coding: utf-8 -*-
# this is console traditional russian game visilitsa
# i guess one word from list and you shoul guess it
# if you dont guess letter  you lose 1 life from 6
# if you lose all your life ypu will be hanged

import random
# next line is image of visilitsa
vis=['','','','','','','','']
vis[6]='''
  _____ 
 |     |
 |    _0_  
 |    / \\
 |   
/ \\
'''

vis[5]='''
  _____ 
 |     |
 |      
 |    
 |   
/ \\
'''

vis[4]='''
  _____ 
 |     
 |     
 |    
 |   
/ \\
'''

vis[3]='''
  
 |     
 |     
 |    
 |   
/ \\
'''

vis[2] = '''     
 |    
 |   
/ \\
'''

vis[1] = '''     
/ \\
'''

vis[0]= '''     
/ 
'''
dict_of_words=['ability', 'academy', 'account', 'achieve', 'actions', 'address', 'advance', 'affairs', 'against', 'airport', 'alcohol', 'allowed', 'already', 'amazing', 'amounts', 'ancient', 'android', 'animals', 'another', 'answers', 'anxiety', 'anymore', 'appears', 'applied', 'applies', 'arrived', 'article', 'artists', 'aspects', 'attacks', 'attempt', 'authors', 'average', 'awarded', 'awesome', 'balance', 'banking', 'battery', 'because', 'becomes', 'bedroom', 'believe', 'benefit', 'between', 'biggest', 'billion', 'brother', 'brought', 'browser', 'buttons', 'calling', 'cameras', 'capable', 'capital', 'captain', 'capture', 'careful', 'carried', 'causing', 'centers', 'central', 'century', 'certain', 'chances', 'changed', 'changes', 'channel', 'chapter', 'charged', 'charges', 'charity', 'cheaper', 'checked', 'chicken', 'choices', 'circuit', 'claimed', 'classes', 'classic', 'clearly', 'clients', 'climate', 'closely', 'clothes']
rnumb=random.randint(0,100)

rword=dict_of_words[rnumb]

word=[]
for i in range(len(rword)):
    word.append(rword[i])


counts=0
b='''choose letter'''
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lenth=len(word)
wordgues=['_']*lenth

print('i make up a word')
print(f'you shoul guess a word of {lenth} letters')
print(wordgues)
while(True):
    if counts<7 and lenth>0:
        print(b,letters)

        while(True):
            leter = input()
            if letters.count(leter)!=0:
                letters.remove(leter)
                break
            else:
                print('you already chose this letter, try another!')

        if word.count(leter)==0:
            print('no such letter')
            print(vis[counts])
            counts+=1

        else:
            lenth-=word.count(leter)
            for i in range(len(word)):
                if word[i]==leter:
                    wordgues[i]=leter
        if counts<7 and lenth>0:
            print('your should guess word')
            print(wordgues)
    elif counts==7:
        print('you lose')
        print('word was', word)
        break
    elif counts<7 and lenth==0:
        print('You win')
        print('your word was')
        print(word)

        break
