import requests


class GetProxy:

    @staticmethod
    def gen_proxy():
        curl = requests.get(
            'https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true').text
        if 'limit' in curl:
            return None
        return {"http": curl, "https": curl}
