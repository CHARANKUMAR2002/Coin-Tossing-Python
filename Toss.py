import random
import playsound
from gtts import gTTS


def tossing_coin():
    coin =["Its Heads", "Its Tails"]
    toss = random.choice(coin)
    playsound.playsound("Coin.mp3")
    text = toss
    language = 'en'
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("toss.mp3")
    playsound.playsound("toss.mp3")
tossing_coin()
