```
    ____                    __  __           __  
   / __ \(⌐■_■)__________  / / / /___ ______/ /_ 
  / / / / / ___/ ___/ __ \/ /_/ / __ `/ ___/ __ \
 / /_/ / (__  ) /__/ /_/ / __  / /_/ (__  ) / / /
/_____/_/____/\___/\____/_/ /_/\__,_/____/_/ /_/  
```

### >: What does this plugin do (◕‿‿◕)?

DiscoHash is a [Pwnagotchi](https://pwnagotchi.ai/) plugin that converts pcaps captured by Pwnagotchi to a hashcat compatible hash (EAPOL/PMKID: mode 22000) and posts them to Discord using a web hook.

To avoid reinventing the wheel DiscoHash reuses some code taken from the [hashie](https://github.com/evilsocket/pwnagotchi-plugins-contrib/blob/master/hashie.py) and [discord](https://github.com/evilsocket/pwnagotchi-plugins-contrib/blob/master/discord.py) plugins.

Example Output:

![DiscoHash Discord message](/discohash.png)

ps. can you crack my AP? (⌐■_■)


### >: Installation:

- [X] After you have Pwnagotchi up and running, download, compile and install [hxctools](https://github.com/ZerBea/hcxtools).
```
sudo apt-get install libcurl4-openssl-dev libssl-dev zlib1g-dev
git clone https://github.com/ZerBea/hcxtools.git
cd hcxtools
make
sudo make install
```
- [X] Create a new Discord server and set up a new [web hook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
- [X] Copy discohash.py from this repo to /usr/local/share/pwnagotchi/installed-plugins/
```
cd /usr/local/share/pwnagotchi/installed-plugins
sudo wget https://raw.githubusercontent.com/flamebarke/DiscoHash/main/discohash.py
```
- [X] Set the following options within /etc/pwnagotchi/config.toml
```
main.plugins.discohash.enabled = true
main.plugins.discohash.webhook_url = "[YOUR WEB HOOK URL]"
```


### >: Usage:

Simply reboot Pwnagotchi make sure it has internet access (bluetooth pairing) and watch those hashes roll in!


### >: Notes (◕‿‿◕):

DiscoHash checks for new pcap files at the end of each epoch so they will come fairly frequently. To reduce this interval modify the code to use a different callback. 

To check out how to make plugins for Pwnagotchi check the docs [here](https://pwnagotchi.ai/plugins/#developing-your-own-plugin).

You can contact me by sending my Pwnagotchi some PwnMail at:

`53291d7013a14b08cd8c7fea3b5de0f60f5e391f5584ac8310af5cfd96a04a4a`


### >: To Do:

- [ ] Add WiGLE Wifi integration to search by SSID and return lat,long
