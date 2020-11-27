## Description
Mycroft TTS plugin for [Softcatala TTS](https://github.com/Softcatala/tts-service)

The "plugins" are pip install-able modules presenting one or more entrypoints with a entrypoint group defined in setup.py

more info in the [original PR](https://github.com/MycroftAI/mycroft-core/pull/2594)

## Install

Build and run the [docker image from softcatala](https://github.com/Softcatala/tts-service)

`mycroft-pip install git+https://github.com/OpenJarbas/mycroft-tts-plugin-softcatala`

## Configuration

```json
  "tts": {
    "module": "softcatala_tts_plug",
    "softcatala_tts_plug": {
      "url": "http://localhost:8100/speak/"
    }
 
```
