## Description
Mycroft TTS plugin for [Softcatala TTS](https://github.com/Softcatala/tts-service)

## Install

Build and run the [docker image from softcatala](https://github.com/Softcatala/tts-service)

`pip install ovos-tts-plugin-softcatala`

## Configuration

```json
  "tts": {
    "module": "ovos-tts-plugin-softcatala",
    "ovos-tts-plugin-softcatala": {
      "url": "http://localhost:8100/speak/"
    }
  }
 
```
