from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9c2811c53b17867fa8d9d68834fd43a0"
# Your Auth Token from twilio.com/console
auth_token  = "27c326ee4125e451e5923c57c0454b60"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918603689070", 
    from_="+15106940328",
    body="Hello from Ujjwal!")

print(message.sid)