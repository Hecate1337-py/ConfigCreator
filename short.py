import requests
import configparser

def fetch_pages_data(user_access_token):
    url = f"https://graph.facebook.com/me/accounts"
    params = {
        'access_token': user_access_token
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Error fetching pages data: {response.status_code}")
        return []

def create_config_from_facebook(file_name, user_access_token):
    pages_data = fetch_pages_data(user_access_token)

    if not pages_data:
        print("No pages found or invalid access token.")
        return

    config = configparser.ConfigParser()

    for i, page in enumerate(pages_data[:4], start=1):
        config[f'PAGE_{i:02}'] = {
            'page_name': page.get('name', ''),
            'page_id': page.get('id', ''),
            'access_token': page.get('access_token', '')
        }

    config['DETAILS'] = {
        'video_path': 'vid',
        'hashtags': '#viral #epic #reels #fyp #respect'
    }

    config['REPLY_TEMPLATES'] = {
        'default_reply': 'Thanks for watching, dont forget to like, comment, follow, and share <3.'
    }

    with open(file_name, 'w') as configfile:
        config.write(configfile)

    print(f"Config file '{file_name}' berhasil dibuat dengan data halaman Facebook.")

user_access_token = input("Masukkan User Access Token: ")
create_config_from_facebook('config.ini', user_access_token)
