```
    ____                    __  __           __  
   / __ \(⌐■_■)__________  / / / /___ ______/ /_ 
  / / / / / ___/ ___/ __ \/ /_/ / __ `/ ___/ __ \
 / /_/ / (__  ) /__/ /_/ / __  / /_/ (__  ) / / /
/_____/_/____/\___/\____/_/ /_/\__,_/____/_/ /_/  
```

### >: What does this plugin do (◕‿‿◕)?

DiscoHash is a [Pwnagotchi](https://pwnagotchi.ai/) plugin that converts pcaps captured by Pwnagotchi to a hashcat compatible hash (EAPOL/PMKID: mode 22000) and posts them to Discord along with any GPS location data (from USB dongle or net-pos plugin) using a web hook.

To avoid reinventing the wheel DiscoHash reuses a couple of functions from the [hashie](https://github.com/evilsocket/pwnagotchi-plugins-contrib/blob/master/hashie.py) and [discord](https://github.com/evilsocket/pwnagotchi-plugins-contrib/blob/master/discord.py) plugins.

Within the bot folder there is a Discord Bot that will scrape all captured hashes from the discord server and return them in a text file. This is not required for the plugin, but it makes it easier to pull large amounts of hashes quickly. You can modify the discord bot to only pull hashes from within a certain date range etc.

Example Output:

![DiscoHash Discord message](/discohash.png)

![Hashbot](/hashbot.png)

ps. can you crack my AP? (⌐■_■)


### >: Installation:

- [X] After you have Pwnagotchi up and running, download, compile and install [hxctools](https://salsa.debian.org/pkg-security-team/hcxtools).
```
sudo su
apt-get update
apt-get install libcurl4-openssl-dev libssl-dev zlib1g-dev
cd /opt
git clone https://github.com/ZerBea/hcxtools.git
cd hcxtools
make
make install
```
- [X] Create a new Discord server and set up a new [web hook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
- [X] Copy discohash.py from this repo to /usr/local/share/pwnagotchi/installed-plugins/ (if the directory doesn't exist create it)
```
cd /usr/local/share/pwnagotchi/installed-plugins
sudo wget https://raw.githubusercontent.com/flamebarke/DiscoHash/main/discohash.py
```
- [X] Set the following options within /etc/pwnagotchi/config.toml
```
main.plugins.discohash.enabled = true
main.plugins.discohash.webhook_url = "YOUR WEB HOOK URL"
```


### >: Usage:

Simply reboot Pwnagotchi make sure it has internet access (bluetooth pairing) and watch those hashes roll in!


### >: Notes (◕‿‿◕):

If you have a custom handshake directory then you will need to modify line 32 of discohash.py to your custom handshake directory.

DiscoHash checks for new pcap files at the end of each epoch so they will come fairly frequently. To reduce this interval modify the code to use a different callback. 

To check out how to make plugins for Pwnagotchi check the docs [here](https://pwnagotchi.ai/plugins/#developing-your-own-plugin).

You can contact me by sending my Pwnagotchi some PwnMail at:

`f033aa5cd581f67ac5f88838de002fc240aadc74ee2025b0135e5fff4e4b5a4a`


### >: To Do:

- [X] Parse lat/long from GPS and add to message
- [ ] Add one liner for cracking the hash with hashcat
