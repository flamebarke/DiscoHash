```
    ____                    __  __           __  
   / __ \(⌐■_■)__________  / / / /___ ______/ /_ 
  / / / / / ___/ ___/ __ \/ /_/ / __ `/ ___/ __ \
 / /_/ / (__  ) /__/ /_/ / __  / /_/ (__  ) / / /
/_____/_/____/\___/\____/_/ /_/\__,_/____/_/ /_/  
```

`>: (◕‿‿◕) What does this plugin do?`

DiscoHash is a [Pwnagotchi](https://pwnagotchi.ai/) plugin that converts pcaps captured by Pwnagotchi to a hashcat compatible hash (EAPOL/PMKID: mode 22000) and posts them to Discord using a web hook.

`>: (♥‿‿♥) Installation:`

- [ ] After you have your Pwnagotchi up and running, download, compile and install [hxctools](https://github.com/ZerBea/hcxtools).
```
git clone https://github.com/ZerBea/hcxtools.git
cd hcxtools
make
sudo make install
```

- [ ] Create a new Discord server and set up a new [web hook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
- [ ] Copy discohash.py from this repo to /usr/local/share/pwnagotchi/installed-plugins/
```
cd /usr/local/share/pwnagotchi/installed-plugins
sudo wget https://raw.githubusercontent.com/flamebarke/DiscoHash/main/discohash.py
```
- [ ] Set the following options within /etc/pwnagotchi/config.toml
```
main.plugins.discohash.enabled = true
main.plugins.discohash.web_hook = [YOUR WEB HOOK URL]
```



