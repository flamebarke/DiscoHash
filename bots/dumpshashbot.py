import discord

from os import remove

TOKEN = "<TOKEN>"
CHANNEL_ID = <CHANNEL_ID_INT>
CHANNEL_NAME = "<CHANNEL_NAME>"
WEBHOOK_NAME = "<WEBHOOK_NAME_FOR_FILTERING>"
DEFAULT_MESSAGES_LIMIT = 100



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

        if '!dumphash' in user_message and channel == CHANNEL_NAME:
            try:
                limit_messages = int(user_message.split(' ')[1])
            except:
                limit_messages = DEFAULT_MESSAGES_LIMIT
            with open('hashes.22000', 'w') as f:
                o_cahnnel = client.get_channel(int(CHANNEL_ID))
                if limit_messages > DEFAULT_MESSAGES_LIMIT:
                    limit = limit_messages*2
                else:
                    limit = DEFAULT_MESSAGES_LIMIT
                messages = o_cahnnel.history(limit=limit)
                count = 0
                async for i in messages:
                    if WEBHOOK_NAME in str(i):
                        count +=1
                        try:
                            hash_dict = i.embeds[0].to_dict() 
                            hash = hash_dict['fields'][0]['value']
                            f.write(hash[1:-1])
                            if count == limit_messages:
                                break
                        except:
                            pass
            with open('hashes.22000', 'r') as f:
                await message.channel.send(f'''Gathering up to last {limit_messages} hashes.\n\nWPA\WPA2 is minimum 8 chars. \nFor BruteForce from 8 to 11 digits use this: \n  hashcat -m 22000 -a 3 hashcat.22000.txt ?d?d?d?d?d?d?d?d?d?d?d -i --increment-min=8 \n\nFor BruteForce from 8 to 11 chars use this: \n  hashcat -m 22000 -a 3 hashcat.22000.txt ?a?a?a?a?a?a?a?a?a?a?a -i --increment-min=8 \n\n'''
                                           ,file=discord.File(f, 'hashcat.22000.txt'))
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
