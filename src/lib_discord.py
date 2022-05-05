from get_config import f_get_channel

async def permission_send_message(bot_member, channel):
    bot_permissions = channel.permissions_for(bot_member)
    if bot_permissions.send_messages:
        print("The bot has permissions to send messages within the channel!")
    if not bot_permissions.send_messages:
        await channel.set_permissions(bot_member, send_messages = True)

async def send_message(client, smiley:str, message:str):
    #check for use permission send message function here
    channel = client.get_channel(f_get_channel())
    await channel.send(smiley + message)
