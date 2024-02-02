import requests

#token_request = requests.get("https://opentdb.com/api_token.php?command=request")
#token = token_request.json()
#print(token)

def get_questions():
    amount = 10
    difficulty = '' #'easy' | 'medium' | 'hard'

    url = f"https://opentdb.com/api.php"
    params = {
        'type': 'boolean',
        'amount': amount,
        'category': 18
    }

    if difficulty:
        params['difficulty'] = difficulty

    r = requests.get(url, params=params)

    response = r.json()
    response_code = response['response_code']

    if response_code > 0:
        print(response_code)

    return response['results']
