
def text_to_speech(text, key_azure, region_azure, lang):
    import azure.cognitiveservices.speech as speechsdk
    from sys import exit

    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=key_azure, region=region_azure)
    audio_config = speechsdk.audio.AudioOutputConfig(filename="speech/voiceline.wav")


    # The language of the voice that speaks.
    if lang == "en":
        speech_config.speech_synthesis_voice_name = 'en-US-AmberNeural'
    elif lang == "de":
        speech_config.speech_synthesis_voice_name = 'de-DE-KatjaNeural'
    elif lang == "de-CH":
        speech_config.speech_synthesis_voice_name = 'de-CH-LeniNeural'
    else:
        print("[ERROR] Language not supported.")
        exit()

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")