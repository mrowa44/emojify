from urllib.request import urlopen
import json


EMOJI_JSON_URL = 'https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json'


def get_bash_hex_value(emoji_json):
    hex_value = ''
    for char in emoji_json['emoji']:
        hex_value += hex(ord(char)).replace('0x', '\\U')
    return hex_value


def print_emoji(emoji_json):
    for alias in emoji_json['aliases']:
        hex_value = get_bash_hex_value(emoji_json)
        print('[":{0}:"]="{1}"'.format(alias, hex_value))


if __name__ == '__main__':
    with urlopen(EMOJI_JSON_URL) as conn:
        emojis_json = json.loads(conn.read().decode('utf-8'))
        for emoji_json in emojis_json:
            print_emoji(emoji_json)
