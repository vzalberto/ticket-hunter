import twitter
from twilio.rest import TwilioRestClient

execfile('keys.py')
execfile('twilio_auth.py')

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)
statuses = api.GetSearch(term='boletos gratis')
url = 'http://twitter.com/'
print str(len(statuses))+" nuevos tuits"

client = TwilioRestClient(account_sid, auth_token)

for s in statuses:
    Turl = url+s.user.screen_name+'/status/'+str(s.id)
    smsBody = "@"+s.user.screen_name+" "+s.text
    rt = s.text.find('RT ')
    if rt < 0:		
        api.PostUpdate("@sereunespejo "+Turl)
	message = client.sms.messages.create(body=smsBody, to=dest_number, from_=tw_number)
    else:
        log = open('log.txt', 'a')
        log.write(Turl+'\n')
        log.close()



