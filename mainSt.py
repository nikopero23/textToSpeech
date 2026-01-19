import streamlit as st
from googletrans import Translator
from gtts import gTTS

LINGUE = {
    'it': 'Italiano',
    'en': 'Inglese',
    'es': 'Spagnolo',
    'fr': 'Francese',
    'de': 'Tedesco',
    'pt': 'Portoghese',
    'ru': 'Russo',
    'ja': 'Giapponese',
    'ko': 'Coreano',
    'zh-cn': 'Cinese Semplificato',
}

st.title("🌍 Traduttore con MP3")

frase = st.text_input("Scrivi la frase da tradurre")

lingua_dest = st.selectbox(
    "Seleziona la lingua di destinazione",
    options=list(LINGUE.keys()),
    format_func=lambda x: LINGUE[x]
)

if st.button("Traduci"):
    if not frase:
        st.error("Scrivi una frase!")
    else:
        translator = Translator()
        risultato = translator.translate(frase, dest=lingua_dest)
        testo_tradotto = risultato.text

        st.success("Traduzione completata")
        st.write("**Testo tradotto:**", testo_tradotto)

        tts = gTTS(text=testo_tradotto, lang=lingua_dest)
        mp3_file = "traduzione.mp3"
        tts.save(mp3_file)

        st.audio(mp3_file, format="audio/mp3")
