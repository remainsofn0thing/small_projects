import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[lat]': response.get('lat'),
            '[lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} :  {v}')
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("city")}_{response.get("query")}.html')
    except requests.exceptions.ConnectionError:
        print('[!] Please check ur connection!')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('SOME TEXT'))
    ip = input('Enter some target ip: ')
    get_info_by_ip(ip=ip)


if __name__ == "__main__":
    main()
