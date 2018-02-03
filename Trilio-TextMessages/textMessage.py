# (312) 313-6417

from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "ACaa6bc6f9092a843c7c156d72aac33f73"
# Your Auth Token from twilio.com/console
auth_token  = "ce9bfabc63eed5dceed0bf6d2fc680a2"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(

    to="+1 312-532-7290",
    from_="+1 312-313-6417",
    body="Hello from the other side!")

print(message.sid)




#
#
# from twilio.rest import Client
#
# # Your Account SID from twilio.com/console
# account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# # Your Auth Token from twilio.com/console
# auth_token  = "your_auth_token"
#
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     to="+15558675309",
#     from_="+15017250604",
#     body="Hello from Python!")
#
# print(message.sid)
#
