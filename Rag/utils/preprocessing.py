import re

def preprocessing(test:str) ->str:
    text = text.replace("\n"," ")
    text = re.sub(r"\s+"," ",text)
    text = text.strip() #It removes whitespaces at the start and end of the word

    return text