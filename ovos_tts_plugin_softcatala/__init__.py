# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from ovos_plugin_manager.templates.tts import TTS, TTSValidator
import requests
import hashlib


class SoftcatalaTTSPlugin(TTS):
    """Interface to softcala TTS."""
    def __init__(self, lang="es-ca", config=None):
        super(SoftcatalaTTSPlugin, self).__init__(
            lang, config, SoftcatalaTTSValidator(self), 'mp3')
        self.url = config.get("url", "http://localhost:8100/speak/")

    @staticmethod
    def getMD5(text):
        m = hashlib.md5()
        m.update(text.encode('utf-8'))
        s = m.hexdigest()[:8].lower()
        return s

    def get_tts(self, sentence, wav_file):
        """Fetch tts audio using softcatala docker file.

        Arguments:
            sentence (str): Sentence to generate audio for
            wav_file (str): output file path
        Returns:
            Tuple ((str) written file, None)
        """
        params = {"text": sentence, "token": self.getMD5(sentence)}
        audio_data = requests.get(self.url, params=params).content
        with open(wav_file, "wb") as f:
            f.write(audio_data)
        return (wav_file, None)  # No phonemes


class SoftcatalaTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(SoftcatalaTTSValidator, self).__init__(tts)

    def validate_lang(self):
        lang = self.tts.lang
        # TODO ensure lang code matches

    def validate_connection(self):
        # TODO ensure url is valid
        pass

    def get_tts_class(self):
        return SoftcatalaTTSPlugin
