import requests, re, urllib, os, html, shutil, sys, datetime

# get the path to the directory that this script resides in
script_dir = os.path.dirname(os.path.abspath(__file__))

# output file name
output_filename = 'stats_' + datetime.date.today().strftime('%#m-%#d-%Y') + '.txt'
output_filepath = script_dir + '\\' + output_filename

# delete output file if it exists
if os.path.exists(output_filepath):
    os.remove(output_filepath)

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
        'https://www.youtube.com/@AkiRosenthal',
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
        'https://www.youtube.com/@TsunomakiWatame',
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
        'https://www.youtube.com/@NinomaeInanis',
        'https://www.youtube.com/@GawrGura',
        'https://www.youtube.com/@WatsonAmelia',
        'https://www.youtube.com/@IRyS',
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
        'https://www.youtube.com/@YukokuRoberu',
        'https://www.youtube.com/@KageyamaShien',
        'https://www.youtube.com/@AragamiOga',
        'https://www.youtube.com/@YatogamiFuma',
        'https://www.youtube.com/@UtsugiUyu',
        'https://www.youtube.com/@HizakiGamma',
        'https://www.youtube.com/@MinaseRio',
        'https://www.youtube.com/@RegisAltare',
        'https://www.youtube.com/@MagniDezmond',
        'https://www.youtube.com/@AxelSyrios',
        'https://www.youtube.com/@NoirVesper',
        'https://www.youtube.com/@GavisBettel',
        'https://www.youtube.com/@MachinaXFlayon',
        'https://www.youtube.com/@BanzoinHakka',
        'https://www.youtube.com/@JosuijiShinri'
    ],
    'virtuareal' : [

    ],
    'nijisanji main branch' : [
        https://www.youtube.com/@TsukinoMito
        https://www.youtube.com/@YukiChihiro
        https://www.youtube.com/@ShizukaRin
        https://www.youtube.com/@ShibuyaHajime
        https://www.youtube.com/@Moira
        https://www.youtube.com/@HiguchiKaede
        https://www.youtube.com/@Elu
        https://www.youtube.com/@Suzuya_Aki
        https://www.youtube.com/@MononobeAlice
        https://www.youtube.com/@KenmochiToya
        https://www.youtube.com/@IenagaMugi
        https://www.youtube.com/@MorinakaKazaki
        https://www.youtube.com/@FushimiGaku
        https://www.youtube.com/@GilzarenIII
        https://www.youtube.com/@FuminoTamaki
        https://www.youtube.com/@UshimiIchigo
        https://www.youtube.com/@SuzukaUtako
        https://www.youtube.com/@YuhiRiri
        https://www.youtube.com/@Kanae
        https://www.youtube.com/@AkabaneYouko
        https://www.youtube.com/@Dola
        https://www.youtube.com/@HanabatakeChaika
        https://www.youtube.com/@AzuchiMomo
        https://www.youtube.com/@Ryushen
        https://www.youtube.com/@Sister_Claire
        https://www.youtube.com/@SuzukiMasaru
        https://www.youtube.com/@TodorokiKyoko
        https://www.youtube.com/@UzukiKou
        https://www.youtube.com/@HarusakiAir
        https://www.youtube.com/@YashiroKizuku
        https://www.youtube.com/@NaruseNaru
        https://www.youtube.com/@SasakiSaku
        https://www.youtube.com/@HonmaHimawari
        https://www.youtube.com/@MakainoRirimu
        https://www.youtube.com/@Kuzuha
        https://www.youtube.com/@ShiinaYuika
        https://www.youtube.com/@KandaShoichi
        https://www.youtube.com/@AmemoriSayo
        https://www.youtube.com/@TakamiyaRion
        https://www.youtube.com/@AsukaHina
        https://www.youtube.com/@MaimotoKeisuke
        https://www.youtube.com/@DebidebiDebiru
        https://www.youtube.com/@RindouMikoto
        https://www.youtube.com/@JoeRikiichi
        https://www.youtube.com/@MachitaChima
        https://www.youtube.com/@SakuraRitsuki
        https://www.youtube.com/@BelmondBanderas
        https://www.youtube.com/@YagurumaRine
        https://www.youtube.com/@YumeoiKakeru
        https://www.youtube.com/@KuroiShiba
        https://www.youtube.com/@YuzukiRoa
        https://www.youtube.com/@OnomachiHaruka
        https://www.youtube.com/@user-hk5qj2kc4x
        https://www.youtube.com/@SetoMiyako
        https://www.youtube.com/@InuiToko
        https://www.youtube.com/@AngeKatrina
        https://www.youtube.com/@LizeHelesta
        https://www.youtube.com/@AizonoManami
        https://www.youtube.com/@SaegusaAkina
        https://www.youtube.com/@YukishiroMahiro
        https://www.youtube.com/@ExAlbio
        https://www.youtube.com/@LeviElipha
        https://www.youtube.com/@HayamaMarin
        https://www.youtube.com/@HakaseFuyuki
        https://www.youtube.com/@NuiSociere
        https://www.youtube.com/@YorumiRena
        https://www.youtube.com/@KagamiHayato
        https://www.youtube.com/@AibaUiha
        https://www.youtube.com/@ArsAlmal
        https://www.youtube.com/@AmamiyaKokoro
        https://www.youtube.com/@RatnaPetit
        https://www.youtube.com/@EliConifer
        https://www.youtube.com/@HanaMacchia
        https://www.youtube.com/@SukoyaKana
        https://www.youtube.com/@HayaseSou
        https://www.youtube.com/@ShellinBurgundy
        https://www.youtube.com/@Fumi
        https://www.youtube.com/@YamagamiKaruta
        https://www.youtube.com/@HoshikawaSara
        https://www.youtube.com/@EmmaAugust
        https://www.youtube.com/@LuisCammy
        https://www.youtube.com/@MatsukaiMao
        https://www.youtube.com/@GweluOsGar
        https://www.youtube.com/@ShirayukiTomoe
        https://www.youtube.com/@FuwaMinato
        https://www.youtube.com/@RaiGalilei
        https://www.youtube.com/@AmiciaMichella
        https://www.youtube.com/@RiksaDhirendra
        https://www.youtube.com/@KurusuNatsume
        https://www.youtube.com/@Naraka_nijisanji
        https://www.youtube.com/@MashiroMeme
        https://www.youtube.com/@MinSuha
        https://www.youtube.com/@FurenELustario
        https://www.youtube.com/@Ibrahim
        https://www.youtube.com/@Gaon
        https://www.youtube.com/@AzuraCecillia
        https://www.youtube.com/@LaylaAlstroemeria
        https://www.youtube.com/@NaraHaramaung
        https://www.youtube.com/@GenzukiTojiro
        https://www.youtube.com/@NagaoKei
        https://www.youtube.com/@KaidaHaru
        https://www.youtube.com/@SoNagi
        https://www.youtube.com/@SorahoshiKirame
        https://www.youtube.com/@SuoSango
        https://www.youtube.com/@KitakojiHisui
        https://www.youtube.com/@TodoKohaku
        https://www.youtube.com/@NishizonoChigusa
        https://www.youtube.com/@LeeRoha
        https://www.youtube.com/@AkiraRay
        https://www.youtube.com/@EtnaCrimson
        https://www.youtube.com/@BonnivierPranaja
        https://www.youtube.com/@YangNari
        https://www.youtube.com/@RyuHari
        https://www.youtube.com/@OhJiyu
        https://www.youtube.com/@NagisaArcinia
        https://www.youtube.com/@DeremKado
    ],
    'nijisanji en' : [
        https://www.youtube.com/@FinanaRyugu
        https://www.youtube.com/@SonnyBrisko
        https://www.youtube.com/@SelenTatsuki
        https://www.youtube.com/@MillieParfait
        https://www.youtube.com/@Rosemi_Lovelock
        https://www.youtube.com/@EliraPendora
        https://www.youtube.com/@UkiVioleta
        https://www.youtube.com/@NinaKosaka
        https://www.youtube.com/@EnnaAlouette
        https://www.youtube.com/@petragurin
        https://www.youtube.com/@MystaRias
        https://www.youtube.com/@PomuRainpuff
        https://www.youtube.com/@AlbanKnox
        https://www.youtube.com/@MariaMarionette
        https://www.youtube.com/@ShuYamino
        https://www.youtube.com/@VoxAkuma
        https://www.youtube.com/@IkeEveland
        https://www.youtube.com/@LucaKaneshiro
        https://www.youtube.com/@KyoKaneko
        https://www.youtube.com/@FulgurOvid
        https://www.youtube.com/@AiaAmare
        https://www.youtube.com/@ScarleYonaguni
        https://www.youtube.com/@AsterArcadia
        https://www.youtube.com/@RenZotto
        https://www.youtube.com/@HexHaywire
        https://www.youtube.com/@KotokaTorahime
        https://www.youtube.com/@VerVermillion
        https://www.youtube.com/@VezaliusBandage
        https://www.youtube.com/@VantacrowBringer
        https://www.youtube.com/@YuQ.Wilson
        https://www.youtube.com/@YugoAsuma
        https://www.youtube.com/@ZaionLanZa
        https://www.youtube.com/@MelocoKyoran
        https://www.youtube.com/@DoppioDropscythe
        https://www.youtube.com/@ReimuEndou
    ]
}

def print_to_file(input_data):
    with open(output_filepath, 'a') as file:
        file.write('{}\n'.format(input_data))


# debug dump html data to a target directory
def debug_print(html_data, dir_path, file_name):

    with open(dir_path + '/' + file_name, 'w', encoding='utf-8') as debug_file:
        debug_file.write(html_data)

def find_expr_in_html(expr, html):
    return re.findall(expr, html, re.S)



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

    print_to_file(subscriber_text)

    subscriber_tokens = subscriber_text.split()

    print_to_file(subscriber_tokens)

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
        print_to_file(url)

        r = requests.get(url)

        username = get_username_from_url(url)

        # debug_print(r.text, script_dir, '{}_dump.txt'.format(username))

        sub_count = get_subscirber_numbers(r.text, username)

        print_to_file('username: {}'.format(username))
        print_to_file('sub_count: {}'.format(sub_count))
        print_to_file('')

        data.append([sub_count, username, org.upper()])



sorted_data = sorted(data, key=lambda x: x[0], reverse=True)

ranking = 0

for sub_count, username, org in sorted_data:
    ranking += 1
    formatted_sub_count = '{:,.0f}'.format(sub_count)
    print_to_file('{} {} {} {}'.format(ranking, org, username, formatted_sub_count))
