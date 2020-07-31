from urllib.request import urlopen
import json


EMOJI_JSON_URL = 'https://raw.githubusercontent.com/joypixels/emojione/master/emoji.json'


def get_bash_hex_value(emoji_json):
    hex_value = ''
    for char in emoji_json['code_points']['output'].split('-'):
        hex_value += '\\U' + char
    return hex_value


def print_emoji(emoji_json):
    hex_value = get_bash_hex_value(emoji_json)
    print('["{0}"]="{1}"'.format(emoji_json['shortname'], hex_value))


if __name__ == '__main__':
    with urlopen(EMOJI_JSON_URL) as conn:
        emojis_json = json.loads(conn.read().decode('utf-8'))
        for emoji_code in emojis_json:
            emoji_json = emojis_json[emoji_code]
            print_emoji(emoji_json)
