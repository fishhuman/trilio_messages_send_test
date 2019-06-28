from twilio.rest import Client

account_sid = "ACb3dde628af2aba151f4832de389bb688"

autn_token = "996c50d579137ee9a338b796341ba689"

client = Client(account_sid, autn_token)

message = client.messages.create(
    to = "+886975395993",
    from_ = "+12054306356",
    body = "你好，請好好堅持下去")


