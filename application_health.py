import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "up", "Application is functioning correctly"
        else:
            return "down", f"Application is down. HTTP status code: {response.status_code}"
    except requests.RequestException as e:
        return "down", f"Failed to connect to the application: {str(e)}"

def main():
    application_url = 'http://madhan.com/'  # Change this to your application URL
    status, message = check_application_status(application_url)
    print(f"Application status: {status}")
    print('message',message)

if __name__ == "__main__":
    main()
