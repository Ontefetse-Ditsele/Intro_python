#Tech Support
#

from random import randint
global responses
responses = {"crashed":"Are the drivers up to date",
             "blue":"Ah, the blue screen of death. And then what happend?",
             "hacked":"You should consider installing anti-virus software",
             "bluetooth":"Have you tried mouthwash?",
             "windows":"Ah,I think i see your problem",
             "apple":"You do mean the computer kind?",
             "spam": "You should see if your mail client can filter messages",
             "connection":"Contact Telkom"
             }

def techsupport(query):
    global responses
    
    if query in responses:
        return responses[query]
    else: 
        return False
    
def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')

def get_input():
    global responses
    
    answer = input().lower()
    answer = answer.split()
    
    for query in answer:
        if query in responses: return query
    
    return answer[0]

def main():

    welcome()    
    query = get_input()
    
    while (not query=='quit'):
        
        if not techsupport(query):
            print("Curious, tell me more")
        else:
            print(techsupport(query))
        
        query = get_input()    
          
if __name__ == '__main__': main()