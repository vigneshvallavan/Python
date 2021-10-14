from prsaw import RandomStuffV2

rs = RandomStuffV2() 

while True:
    user_text = input("You: ")
    response = rs.get_ai_response(user_text)  # result will be in dict type -->  {'message': 'Wassup man, how you doing.'}
    print("Bot:",response['message'])

rs.close()