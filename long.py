import requests
import configparser

def fetch_pages_data(long_lived_token):
    url = f"https://graph.facebook.com/me/accounts"
    params = {
        'access_token': long_lived_token
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Error fetching pages data: {response.status_code}")
        return []

def exchange_for_long_lived_token(app_id, app_secret, short_lived_token):
    url = f"https://graph.facebook.com/v17.0/oauth/access_token"
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': app_id,
        'client_secret': app_secret,
        'fb_exchange_token': short_lived_token
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('access_token')
    else:
        print(f"Error exchanging token: {response.status_code}, {response.text}")
        return None

def create_config_from_facebook(file_name, long_lived_token):
    pages_data = fetch_pages_data(long_lived_token)

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

short_lived_token = input("Masukkan Short-Lived Access Token: ")
app_id = input("Masukkan Facebook App ID: ")
app_secret = input("Masukkan Facebook App Secret: ")

long_lived_token = exchange_for_long_lived_token(app_id, app_secret, short_lived_token)

if long_lived_token:
    print(f"Long-Lived Access Token: {long_lived_token}")
    create_config_from_facebook('config.ini', long_lived_token)
else:
    print("Gagal mendapatkan Long-Lived Access Token.")
