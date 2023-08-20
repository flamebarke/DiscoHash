import discord

from os import remove

TOKEN = "<TOKEN>"
CHANNEL_ID = <CHANNEL_ID_INT>
CHANNEL_NAME = "<CHANNEL_NAME>"


def handle_response(message)->str:
    p_message = message.lower()
    if p_message == 'hello dumphash' or p_message == '!dumphash' or p_message == '!help dumphash' or p_message == '!helpdumphash':
        return f"`Hi Im your HASH DUMPER Bot for using me please go to {CHANNEL_NAME} channel and write !dumphash`"

async def send_message(message,user_message,is_private):
    try:
        response = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception:
        pass


def run_discord_bot():
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    client = discord.Client(intents=intents)
    @client.event
    async def on_ready():
        print(f'{client.user} is now ready!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} Said: '{user_message}' on channel:'{channel}'.")

        if user_message == '!dumphash' and channel == CHANNEL_NAME:
            with open('hashes.22000', 'w') as f:
                o_cahnnel = client.get_channel(int())
                messages = o_cahnnel.history(limit=100)
                async for i in messages: 
                    try:
                        hash_dict = i.embeds[0].to_dict() 
                        hash = hash_dict['fields'][0]['value']
                        f.write(hash[1:-1])
                    except:
                        pass
            with open('hashes.22000', 'r') as f:
                await message.channel.send(file=discord.File(f, 'hashcat.22000.txt'))
                print('send file!')
            remove("hashes.22000")

        elif user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message=message,user_message=user_message, is_private=True)
        else:
            await send_message(message=message,user_message=user_message, is_private=False)
    client.run(TOKEN)


if __name__ == '__main__':
    run_discord_bot()
