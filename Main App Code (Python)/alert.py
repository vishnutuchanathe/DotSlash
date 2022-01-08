from twilio.rest import TwilioRestClient as Call

From_Number = ""
To_Number = ""
Src_Path = ""

def call():
    client = Call("","")
    print('Call initiated')
    client.calls.create(to=To_Number, from_=From_Number, url=Src_Path, method = 'Get')
    print('Call has been triggered successfully')
