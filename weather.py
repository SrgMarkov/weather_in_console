import requests


def check_weather(loc):
    url_template = 'https://wttr.in/{}'
    display_properties = {'n': '', 'q': '', 'M': '', 'm': '', 'T': '', 'lang': 'ru'}
    url = url_template.format(loc)
    response = requests.get(url, params=display_properties)
    if response.ok:
        return response.text
    else:
        return response.raise_for_status


def main():
    location_list = ['London', 'cvo', 'Череповец']
    for location in location_list:
        print(check_weather(location))


if __name__ == '__main__':
    main()
