from twilio.rest import TwilioRestClient

execfile('twilio_auth.py')

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body="2 nuevos tuits", to=dest_number, from_=tw_number)
print message.sid

