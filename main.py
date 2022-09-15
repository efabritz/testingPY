import requests

yatoken = 'AQAAAABesRe7AADLW9k_fNfHvkzUgfj6Ku8y1VE'
url = 'https://cloud-api.yandex.net/v1/disk/resources'

def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(yatoken)
    }

def read_token(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def yandex_disc_request(path):
    headers = get_headers()
    params = {'path': path}
    path_request = requests.put(url=url, params=params, headers=headers)
    print(path_request.status_code)
    return path_request.status_code

def get_request(path):
    headers = get_headers()
    params = {"url": url, "path": path}
    response = requests.get(url, headers=headers, params=params)
    return response.status_code

# if __name__ == '__main__':
#     yandex_disc_request('testdir')
#     get_request('test_cat')

