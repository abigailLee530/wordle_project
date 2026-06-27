import requests

url = "https://wordle-api.vercel.app/api/wordle"

data = {
    "guess": "words"
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:")
#print(response.json())

def formatResponse(response_dict):
    if response_dict.get("was_correct") == True:
        return "complete"
    
    chars = response_dict.get("character_info")
    
    grey = []
    orange = []
    green = []
    
    for item in chars:
        
        scores = item.get("scoring")
        
        if scores.get("in_word") == True and scores.get("correct_idx") == True:
            green.append(item.get("char"))
        
        elif scores.get("in_word") == True and scores.get("correct_idx") == False:
            orange.append(item.get("char"))
        
        else:
            grey.append(item.get("char"))
 
    return grey, orange, green


print(formatResponse(response.json()))