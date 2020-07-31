#Support.py
#

from random import randint

def support(query):
    responses = {"crashed":"Are the drivers up to date",
                 "blue":"Ah, the blue screen of death. And then what happend?",
                 "hacked":"You should consider installing anti-virus software",
                 "bluetooth":"Have you tried mouthwash?",
                 "windows":"Ah,I think i see your problem",
                 "apple":"You do mean the computer kind?",
                 "spam": "You should see if your mail client can filter messages",
                 "connection":"Contact Telkom"
                 }
    if query in responses:
        return responses[query]
    else: 
        return "Curious, tell me more"
    
def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')

def get_input():
    return input().lower()


def main():

    welcome()    
    query = get_input()
    
    while (not query=='quit'):
        
        print(support(query))
        
        query = get_input()    
         
 
if __name__ == '__main__': main()
