
def speech_to_text(key_azure, region_azure, lang):
    import azure.cognitiveservices.speech as speechsdk
    from sys import exit

    speech_config = speechsdk.SpeechConfig(subscription=key_azure,
                                           region=region_azure)

    if lang == "en":
        speech_config.speech_recognition_language = "en-US"
    elif lang == "de":
        speech_config.speech_recognition_language = "de-DE"
    elif lang == "de-CH":
        speech_config.speech_recognition_language = "de-DE"
    else:
        print("[ERROR] Language not supported.")
        exit()

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return speech_recognition_result.text.replace("enemy", "anime").replace("enemies", "animes").replace("Enemy", "Anime").replace("Enemies", "Animes")
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")