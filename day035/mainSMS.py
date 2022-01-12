from twilio.rest import Client

account_sid = "******************************"
auth_token = "******************************"

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Just a test.",
                     from_= '+************',
                     to= '+************'
                 )
print(message.status)
