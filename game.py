# -*- coding: utf-8 -*-
# this is console traditional russian game visilitsa
# i guess one word from list and you shoul guess it
# if you dont guess letter  you lose 1 life from 6
# if you lose all your life ypu will be hanged

import random
def game():
    # next line is image of visilitsa
    vis=['','','','','','','','']
    vis[6]='''
      _____ 
     |     |
     |    _0_  
     |     |
     |    / \\
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
    dict_of_words=['absolute', 'abstract', 'academic', 'accepted', 'accident', 'accuracy', 'accurate', 'achieved', 'acquired', 'activity', 'actually',
                   'addition', 'adequate', 'adjacent', 'adjusted', 'advanced', 'advisory', 'advocate', 'affected', 'aircraft', 'alliance', 'although',
                   'aluminum', 'analysis', 'announce', 'anything', 'anywhere', 'apparent', 'appendix', 'approach', 'approval', 'argument', 'artistic',
                   'assembly', 'assuming', 'athletic', 'attached', 'attitude', 'attorney', 'audience', 'autonomy', 'aviation', 'bachelor', 'bacteria',
                   'baseball', 'bathroom', 'becoming', 'benjamin', 'birthday', 'boundary', 'breaking', 'breeding', 'building', 'bulletin', 'business',
                   'calendar', 'campaign', 'capacity', 'casualty', 'catching', 'category', 'Catholic', 'cautious', 'cellular', 'ceremony', 'chairman',
                   'champion', 'chemical', 'children', 'circular', 'civilian', 'clearing', 'clinical', 'clothing', 'collapse', 'colonial', 'colorful',
                   'commence', 'commerce', 'complain', 'complete', 'composed', 'compound', 'comprise', 'computer', 'conclude', 'concrete', 'conflict',
                   'confused', 'congress', 'consider', 'constant', 'consumer', 'continue', 'contract', 'contrary', 'contrast', 'convince', 'corridor',
                   'coverage', 'covering', 'creation', 'creative', 'criminal', 'critical', 'crossing', 'cultural', 'currency', 'customer', 'database',
                   'daughter', 'daylight', 'deadline', 'deciding', 'decision', 'decrease', 'deferred', 'definite', 'delicate', 'delivery', 'describe',
                   'designer', 'detailed', 'diabetes', 'dialogue', 'diameter', 'directly', 'director', 'disabled', 'disaster', 'disclose', 'discount',
                   'discover', 'disorder', 'disposal', 'distance', 'distinct', 'district', 'dividend', 'division', 'doctrine', 'document', 'domestic',
                   'dominant', 'dominate', 'doubtful', 'dramatic', 'dressing', 'dropping', 'duration', 'dynamics', 'earnings', 'economic', 'educated',
                   'efficacy', 'eighteen', 'election', 'electric', 'eligible', 'emerging', 'emphasis', 'employee', 'endeavor', 'engaging', 'engineer',
                   'enormous', 'entirely', 'entrance', 'envelope', 'equality', 'equation', 'estimate', 'evaluate', 'eventual', 'everyday', 'everyone',
                   'evidence', 'exchange', 'exciting', 'exercise', 'explicit', 'exposure', 'extended', 'external', 'facility', 'familiar', 'featured',
                   'feedback', 'festival', 'finished', 'firewall', 'flagship', 'flexible', 'floating', 'football', 'foothill', 'forecast', 'foremost',
                   'formerly', 'fourteen', 'fraction', 'franklin', 'frequent', 'friendly', 'frontier', 'function', 'generate', 'generous', 'genomics',
                   'goodwill', 'governor', 'graduate', 'graphics', 'grateful', 'guardian', 'guidance', 'handling', 'hardware', 'heritage', 'highland',
                   'historic', 'homeless', 'homepage', 'hospital', 'humanity', 'identify', 'identity', 'ideology', 'imperial', 'incident', 'included',
                   'increase', 'indicate', 'indirect', 'industry', 'informal', 'informed', 'inherent', 'initiate', 'innocent', 'inspired', 'instance',
                   'integral', 'intended', 'interact', 'interest', 'interior', 'internal', 'interval', 'intimate', 'intranet', 'invasion', 'involved',
                   'isolated', 'judgment', 'judicial', 'junction', 'keyboard', 'landlord', 'language', 'laughter', 'learning', 'leverage', 'lifetime',
                   'lighting', 'likewise', 'limiting', 'literary', 'location', 'magazine', 'magnetic', 'maintain', 'majority', 'marginal', 'marriage',
                   'material', 'maturity', 'maximize', 'meantime', 'measured', 'medicine', 'medieval', 'memorial', 'merchant', 'midnight', 'military',
                   'minimize', 'minister', 'ministry', 'minority', 'mobility', 'modeling', 'moderate', 'momentum', 'monetary', 'moreover', 'mortgage',
                   'mountain', 'mounting', 'movement', 'multiple', 'national', 'negative', 'nineteen', 'northern', 'notebook', 'numerous', 'observer',
                   'occasion', 'offering', 'official', 'offshore', 'operator', 'opponent', 'opposite', 'optimism', 'optional', 'ordinary', 'organize',
                   'original', 'overcome', 'overhead', 'overseas', 'overview', 'painting', 'parallel', 'parental', 'patented', 'patience', 'peaceful',
                   'periodic', 'personal', 'persuade', 'petition', 'physical', 'pipeline', 'platform', 'pleasant', 'pleasure', 'politics', 'portable',
                   'portrait', 'position', 'positive', 'possible', 'powerful', 'practice', 'precious', 'pregnant', 'presence', 'preserve', 'pressing',
                   'pressure', 'previous', 'princess', 'printing', 'priority', 'probable', 'probably', 'producer', 'profound', 'progress', 'property',
                   'proposal', 'prospect', 'protocol', 'provided', 'provider', 'province', 'publicly', 'purchase', 'pursuant', 'quantity', 'question',
                   'rational', 'reaction', 'received', 'receiver', 'recovery', 'regional', 'register', 'relation', 'relative', 'relevant', 'reliable',
                   'reliance', 'religion', 'remember', 'renowned', 'repeated', 'reporter', 'republic', 'required', 'research', 'reserved', 'resident',
                   'resigned', 'resource', 'response', 'restrict', 'revision', 'rigorous', 'romantic', 'sampling', 'scenario', 'schedule', 'scrutiny',
                   'seasonal', 'secondly', 'security', 'sensible', 'sentence', 'separate', 'sequence', 'sergeant', 'shipping', 'shortage', 'shoulder',
                   'simplify', 'situated', 'slightly', 'software', 'solution', 'somebody', 'somewhat', 'southern', 'speaking', 'specific', 'spectrum',
                   'sporting', 'standard', 'standing', 'standout', 'sterling', 'straight', 'strategy', 'strength', 'striking', 'struggle', 'stunning',
                   'suburban', 'suitable', 'superior', 'supposed', 'surgical', 'surprise', 'survival', 'sweeping', 'swimming', 'symbolic', 'sympathy',
                   'syndrome', 'tactical', 'tailored', 'takeover', 'tangible', 'taxation', 'taxpayer', 'teaching', 'tendency', 'terminal', 'terrible',
                   'thinking', 'thirteen', 'thorough', 'thousand', 'together', 'tomorrow', 'touching', 'tracking', 'training', 'transfer', 'traveled',
                   'treasury', 'triangle', 'tropical', 'turnover', 'ultimate', 'umbrella', 'universe', 'unlawful', 'unlikely', 'valuable', 'variable',
                   'vertical', 'victoria', 'violence', 'volatile', 'warranty', 'weakness', 'weighted', 'whatever', 'whenever', 'wherever', 'wildlife',
                   'wireless', 'withdraw', 'woodland', 'workshop', 'yoursel']


    dict_of_words+=['ability', 'absence', 'academy', 'account', 'accused', 'achieve', 'acquire', 'address', 'advance',
                    'adverse', 'advised', 'adviser', 'against', 'airline', 'airport', 'alcohol', 'alleged', 'already', 'analyst',
                    'ancient', 'another', 'anxiety', 'anxious', 'anybody', 'applied', 'arrange', 'arrival', 'article', 'assault',
                    'assumed', 'assured', 'attempt', 'attract', 'auction', 'average', 'backing', 'balance', 'banking', 'barrier',
                    'battery', 'bearing', 'beating', 'because', 'bedroom', 'believe', 'beneath', 'benefit', 'besides', 'between',
                    'billion', 'binding', 'brother', 'brought', 'burning', 'cabinet', 'caliber', 'calling', 'capable', 'capital',
                    'captain', 'caption', 'capture', 'careful', 'carrier', 'caution', 'ceiling', 'central', 'centric', 'century',
                    'certain', 'chamber', 'channel', 'chapter', 'charity', 'charlie', 'charter', 'checked', 'chicken', 'chronic',
                    'circuit', 'classes', 'classic', 'climate', 'closing', 'closure', 'clothes', 'collect', 'college', 'combine',
                    'comfort', 'command', 'comment', 'compact', 'company', 'compare', 'compete', 'complex', 'concept', 'concern', 'concert']

    # dict of 600 7 and 8 letters words

    rnumb=random.randint(0,100)

    rword=dict_of_words[rnumb]

    word=[]
    for i in range(len(rword)):
        word.append(rword[i])


    counts=0
    b = '''choose letter'''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lenth = len(word)
    wordgues = ['_']*lenth

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
                    print('you already chose this letter or letter wrong, try another!')

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
while(True):
    print('1- Play game')
    print('2 - Exit')
    chose=input()
    if chose=='1':
        game()
    elif chose=='2':
        exit()
    else:
        continue