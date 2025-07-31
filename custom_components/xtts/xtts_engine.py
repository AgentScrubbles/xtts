import requests

class XTTSEngine:

    def __init__(self, voice: str, url: str, model: str):
        self._voice = voice
        self._url = url
        self._model = model

    def get_tts(self, text: str):
        """ Makes request to OpenAI TTS engine to convert text into audio"""

        self.switch_model(self._model)

        headers: dict = {}
        data: dict = {"text": text, "speaker_wav": self._voice, "language": "en"}
        url = '{}/tts_to_audio/'.format(self._url)
        print('[XTTS][VOICE={}][URL={}]'.format(url, self._voice))
        return requests.post(url, headers=headers, json=data)
        
    def handle_response(self, response):
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            raise Exception(f"Request failed, status code: {response.status_code}")

    def switch_model(self, model_name):
        data = {
            "model_name": model_name
        }
        response = requests.post(url=f'{self._url}/switch_model', json=data)
        
        if response.status_code == 400:
            detail = response.json()['detail']
            if 'already loaded' in detail:
                return
        return self.handle_response(response) 

    @staticmethod
    def get_supported_langs() -> list:
        """Returns list of supported languages. Note: the model determines the provides language automatically."""
        return ["af", "ar", "hy", "az", "be", "bs", "bg", "ca", "zh", "hr", "cs", "da", "nl", "en", "et", "fi", "fr", "gl", "de", "el", "he", "hi", "hu", "is", "id", "it", "ja", "kn", "kk", "ko", "lv", "lt", "mk", "ms", "mr", "mi", "ne", "no", "fa", "pl", "pt", "ro", "ru", "sr", "sk", "sl", "es", "sw", "sv", "tl", "ta", "th", "tr", "uk", "ur", "vi", "cy"]


