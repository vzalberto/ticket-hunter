import twitter

execfile('keys.py')

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)
statuses = api.GetSearch(term='regalaremos boletos ceremonia')
url = 'http://twitter.com/'

for s in statuses:
	Turl = url+s.user.screen_name+'/status/'+s.id
	rt = s.text.find('RT ')
	if rt < 0:		
		api.PostUpdate(Turl)
	else:
		log = open('log.txt', 'a')
		log.write(url+'\n')
		log.close()

