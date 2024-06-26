import requests

class XTTSEngine:

    def __init__(self, voice: str, url: str):
        self._voice = voice
        self._url = url

    def get_tts(self, text: str):
        """ Makes request to OpenAI TTS engine to convert text into audio"""
        headers: dict = {}
        data: dict = {"text": text, "speaker_wav": self._voice, "language": "en"}
        url = '{}/tts_to_audio/'.format(self._url)
        print('[XTTS][VOICE={}][URL={}]'.format(url, self._voice))
        return requests.post(url, headers=headers, json=data)

    @staticmethod
    def get_supported_langs() -> list:
        """Returns list of supported languages. Note: the model determines the provides language automatically."""
        return ["af", "ar", "hy", "az", "be", "bs", "bg", "ca", "zh", "hr", "cs", "da", "nl", "en", "et", "fi", "fr", "gl", "de", "el", "he", "hi", "hu", "is", "id", "it", "ja", "kn", "kk", "ko", "lv", "lt", "mk", "ms", "mr", "mi", "ne", "no", "fa", "pl", "pt", "ro", "ru", "sr", "sk", "sl", "es", "sw", "sv", "tl", "ta", "th", "tr", "uk", "ur", "vi", "cy"]


