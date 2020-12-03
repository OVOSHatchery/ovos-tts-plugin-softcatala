## Description
Mycroft TTS plugin for [Softcatala TTS](https://github.com/Softcatala/tts-service)

The "plugins" are pip install-able modules that provide new TTS engines for mycroft

more info in the [docs](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/plugins)

## Install

Build and run the [docker image from softcatala](https://github.com/Softcatala/tts-service)

`mycroft-pip install jarbas-tts-plugin-softcatala`

## Configuration

```json
  "tts": {
    "module": "softcatala_tts_plug",
    "softcatala_tts_plug": {
      "url": "http://localhost:8100/speak/"
    }
 
```
