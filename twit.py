import twitter

auth_file = "auth.txt"
with open(auth_file) as f:
	auth_list = f.readlines()

consumer_key = auth_list[0].strip('\n')
consumer_secret = auth_list[1].strip('\n')
access_token_key = auth_list[2].strip('\n')
access_token_secret = auth_list[3].strip('\n')

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

print(api.VerifyCredentials())