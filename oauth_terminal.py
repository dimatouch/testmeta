from google_auth_oauthlib.flow import InstalledAppFlow

# Вкажіть шлях до вашого client_secret.json
CLIENT_SECRETS_FILE = "client_secret.json"

# Дозволи, які ви хочете запитувати (наприклад, доступ до email)
SCOPES = ['https://www.googleapis.com/auth/userinfo.email']

def authenticate_google():
    # Ініціалізація потоку авторизації
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    
    # Запуск авторизації через локальний сервер
    credentials = flow.run_local_server(port=0)
    
    # Отримання токена доступу
    print("Access Token:", credentials.token)
    return credentials.token

if __name__ == "__main__":
    token = authenticate_google()
    print("\nВаш токен доступу:")
    print(token)
