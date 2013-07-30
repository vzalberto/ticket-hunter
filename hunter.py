import twitter

execfile('keys.py')

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)
statuses = api.GetSearch(term='boletos gratis')
url = 'http://twitter.com/'
i = 0

api.PostUpdate('Statuses count='+str(len(statuses)))
for s in statuses:
    i = i + 1
    print i
    Turl = url+s.user.screen_name+'/status/'+str(s.id)
    rt = s.text.find('RT ')
    if rt < 0:		
        api.PostUpdate(Turl)
    else:
        log = open('log.txt', 'a')
        log.write(Turl+'\n')
        log.close()



