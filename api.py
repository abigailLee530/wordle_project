import requests

url = "https://wordle-api.vercel.app/api/wordle"

def guess(word):
    data = {"guess": word}
    response = requests.post(url, json=data)
    return response.json()
    

def isCorrect(word):
    response_dict = guess(word)
    return response_dict.get("was_correct")

def formatResponse(response_dict):
    if response_dict.get("was_correct"):
        return None

    chars = response_dict.get("character_info")
    
    grey = []
    yellow = []
    green = []
    index = 0
    
    for item in chars:
        
        scores = item.get("scoring")
        
        if scores.get("in_word") == True and scores.get("correct_idx") == True:
            green.append(index)
        
        elif scores.get("in_word") == True and scores.get("correct_idx") == False:
            yellow.append(index)
        
        else:
            grey.append(index)
        
        index+=1
    return grey, yellow, green


#print(formatResponse(guess("words")))