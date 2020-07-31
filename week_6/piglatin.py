#piglatin
#

def to_pig_latin(sentence):
    """Translate the user sentence to pig latin by calling translate"""   
    
    def translate(user_input): 
        """helper function to to_pig_latin to translate words in the sentence"""
        first = user_input[0]
        if first in ["a","e","i","o","u"]: 
            user_input = user_input.lower()
            user_input += "way" 
            return user_input
        else: 
            user_input = user_input.lower()
            user_input = user_input[1:]+first+"ay" 
            return user_input 
    sente = sentence.split()
    piglatin_sen = ""
    for index in sente:
        piglatin_sen = translate(sente[index])
    
    return piglatin_sen
    
def to_english(sentence):
    pass

inp = "The little brown fox was an ox"

print(to_pig_latin(inp))