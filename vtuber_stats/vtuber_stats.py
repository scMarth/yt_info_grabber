import requests, re, urllib, os, html, shutil, sys

accounts = {
    'hololive' : [
        'https://www.youtube.com/@TokinoSora',
        'https://www.youtube.com/@Robocosan',
        'https://www.youtube.com/@SakuraMiko',
        'https://www.youtube.com/@HoshimachiSuisei',
        'https://www.youtube.com/@AZKi',
        'https://www.youtube.com/@YozoraMel',
        'https://www.youtube.com/@ShirakamiFubuki',
        'https://www.youtube.com/@NatsuiroMatsuri',
        'https://www.youtube.com/@AkaiHaato',
        'https://www.youtube.com/@AkiRosenthal', # wrong
        'https://www.youtube.com/@MinatoAqua',
        'https://www.youtube.com/@MurasakiShion',
        'https://www.youtube.com/@NakiriAyame',
        'https://www.youtube.com/@YuzukiChoco',
        'https://www.youtube.com/@OozoraSubaru',
        'https://www.youtube.com/@OokamiMio',
        'https://www.youtube.com/@NekomataOkayu',
        'https://www.youtube.com/@InugamiKorone',
        'https://www.youtube.com/@usadapekora',
        'https://www.youtube.com/@ShiranuiFlare',
        'https://www.youtube.com/@ShiroganeNoel',
        'https://www.youtube.com/@HoushouMarine',
        'https://www.youtube.com/@AmaneKanata',
        'https://www.youtube.com/@TsunomakiWatame', # wrong
        'https://www.youtube.com/@TokoyamiTowa',
        'https://www.youtube.com/@HimemoriLuna',
        'https://www.youtube.com/@KiryuCoco',
        'https://www.youtube.com/@YukihanaLamy',
        'https://www.youtube.com/@MomosuzuNene',
        'https://www.youtube.com/@ShishiroBotan',
        'https://www.youtube.com/@OmaruPolka',
        'https://www.youtube.com/@LaplusDarknesss',
        'https://www.youtube.com/@TakaneLui',
        'https://www.youtube.com/@HakuiKoyori',
        'https://www.youtube.com/@SakamataChloe',
        'https://www.youtube.com/@kazamairoha',
        'https://www.youtube.com/@AyundaRisu',
        'https://www.youtube.com/@MoonaHoshinova',
        'https://www.youtube.com/@AiraniIofifteen',
        'https://www.youtube.com/@KureijiOllie',
        'https://www.youtube.com/@AnyaMelfissa',
        'https://www.youtube.com/@PavoliaReine',
        'https://www.youtube.com/@VestiaZeta',
        'https://www.youtube.com/@KaelaKovalskia',
        'https://www.youtube.com/@KoboKanaeru',
        'https://www.youtube.com/@MoriCalliope',
        'https://www.youtube.com/@TakanashiKiara',
        'https://www.youtube.com/@NinomaeInanis', # wrong
        'https://www.youtube.com/@GawrGura',
        'https://www.youtube.com/@WatsonAmelia',
        'https://www.youtube.com/@IRyS', # wrong
        'https://www.youtube.com/@CeresFauna',
        'https://www.youtube.com/@OuroKronii',
        'https://www.youtube.com/@NanashiMumei',
        'https://www.youtube.com/@HakosBaelz',
        'https://www.youtube.com/@TsukumoSana'
    ],
    'holostars' : [
        'https://www.youtube.com/@HanasakiMiyabi',
        'https://www.youtube.com/@KanadeIzuru',
        'https://www.youtube.com/@Arurandeisu',
        'https://www.youtube.com/@rikka',
        'https://www.youtube.com/@AstelLeda',
        'https://www.youtube.com/@KishidoTemma',
        'https://www.youtube.com/@YukokuRoberu' # roberu wrong
    ]
}

# debug dump html data to a target directory
def debug_print(html_data, dir_path, file_name):

    with open(dir_path + '/' + file_name, 'w', encoding='utf-8') as debug_file:
        debug_file.write(html_data)

def find_expr_in_html(expr, html):
    return re.findall(expr, html, re.S)

# get the path to the directory that this script resides in
script_dir = os.path.dirname(os.path.abspath(__file__))

def is_decimal_number(string):
    try:
        float(string)  # Try converting the string to a float
        return True  # If successful, it's a valid decimal number
    except ValueError:
        return False  # If ValueError occurs, it's not a valid decimal number

def get_subscirber_numbers(html_data, username):
    subscriber_text = find_expr_in_html(
        # r'subscriberCountText":{"accessibility":{"accessibilityData":{"label":"([^"]*subscribers)"}},"simpleText":"[^"]*"},"tvBanner":{',
        r'subscriberCountText":{"accessibility":{"accessibilityData":{"label":"([^"]*subscribers)"}},"simpleText":"[^"]*"},"tvBanner":',
        html_data
    )

    if not subscriber_text:
        subscriber_text = find_expr_in_html(
            # r'subscriberCountText":{"accessibility":{"accessibilityData":{"label":"([^"]*subscribers)"}},"simpleText":"[^"]*"},"tvBanner":{',
            r'subscriberCountText":{"accessibility":{"accessibilityData":{"label":"([^"]*subscribers)"}},"simpleText":"[^"]*"},"trackingParams":"',
            html_data
        )

    subscriber_text = subscriber_text[0]

    subscriber_text = subscriber_text.split(' subscribers')[0]

    print(subscriber_text)

    subscriber_tokens = subscriber_text.split()

    print(subscriber_tokens)

    sub_count = None
    for token in subscriber_tokens:
        if token[-1] == 'K':
            rest_of_token = token[0:len(token) - 1]
            if is_decimal_number(rest_of_token):
                sub_count = float(rest_of_token) * 1000
        elif is_decimal_number(token):
            sub_count = float(token)
        else:
            if token == 'million':
                sub_count *= 1000000

    return sub_count

def get_username_from_url(url):
    return url.split('/@')[1]

data = []

for org in accounts:
    for url in accounts[org]:
        print(url)

        r = requests.get(url)

        username = get_username_from_url(url)

        debug_print(r.text, script_dir, '{}_dump.txt'.format(username))

        sub_count = get_subscirber_numbers(r.text, username)

        print('username: {}'.format(username))
        print('sub_count: {}'.format(sub_count))
        print('')

        data.append([sub_count, username, org.upper()])



sorted_data = sorted(data, key=lambda x: x[0], reverse=True)

ranking = 0

for sub_count, username, org in sorted_data:
    ranking += 1
    formatted_sub_count = '{:,.0f}'.format(sub_count)
    print('{} {} {} {}'.format(ranking, org, username, formatted_sub_count))
