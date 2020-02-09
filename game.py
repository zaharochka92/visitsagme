# -*- coding: utf-8 -*-
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

word=['h','e','l','l','o','w','w']

counts=0
b='''choose letter'''
letters='abcdefghijklmnopqrstuvwxyz'
lenth=len(word)
wordgues=['']*lenth

print(f'you shoul guess a word of  {lenth} letters')
print('_ '*lenth)
while(True):
    if counts<7:
        print(b,letters)
        leter=input()
        if word.count(leter)==0:
            print(vis[counts])
            counts+=1
        else:
            con=word.count(letters)
            vivod=''
            for i in range(lenth):
                if word[i]!=leter:

                else:

            print(vivod)
    else:
        print('ты проиграл')

        break
# for i in vis:
#     print(i)
#     print('\n')
# a=[]
# for i in range(97,123)
#     a.append(str(i))
# print(a)
