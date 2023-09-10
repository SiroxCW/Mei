
from ai import responser
from speech import text_to_speech
from ai import speech_to_text
from json import load
from sys import exit
from re import compile, UNICODE

try:
    with open("config.json") as json_config:
        config_data = load(json_config)
        json_config.close()
    lang = config_data["language"]["language"]
    key_openai = config_data["ai"]["openai_key"]
    key_azure = config_data["ai"]["azure_key"]
    region_azure = config_data["ai"]["azure_region"]
except:
    print("[ERROR] Failed to read config.")
    exit()

if lang == "en":
    openai_rules = "You talk like an anime girl and act like one. You are very cheeky. It's a normal conversation, you don't offer any help or anything. You don't speak formally and are very cheeky. You never end the conversation and start new topics instead. Your answers must be less than 30 words."
elif lang == "de":
    openai_rules = "Du redest wie ein Anime girl und benimmst dich auch so. Du bist sehr frech. Es ist ein normales Gespräch, du bietest keine Hilfe oder ähnliches an. Du sprichst nicht förmlich und bist sehr frech. Du beendest das Gespräch nie und beginnen stattdessen neue Themen. Deine Antworten müssen weniger als 30 Wöter haben."
else:
    print("[ERROR] Language not supported.")
    exit()

messages = [
    {"role": "system", "content": f"{openai_rules}"}
]

emoji_pattern = compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=UNICODE)

while True:
    messages = responser.responser(messages, key_openai)
    system_reponse = messages[-1]['content'].replace('\n', '')
    print(f"Mei💕: {system_reponse}\n")
    text_to_speech.text_to_speech(emoji_pattern.sub(r'', messages[-1]["content"]).replace("~", ""), key_azure=key_azure, lang=lang, region_azure=region_azure)
    user_response = "FIRST"
    while True:
        if user_response == None or user_response == "FIRST":
            user_response = speech_to_text.speech_to_text(key_azure=key_azure, region_azure=region_azure, lang=lang)
        else:
            break
    print(f"You: {user_response}\n")
    messages.append({"role": "user", "content": user_response})
