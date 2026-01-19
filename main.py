import asyncio
from googletrans import Translator
from gtts import gTTS
import os

# Lingue disponibili
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

async def main():
    print("=== TRADUTTORE CON MP3 ===\n")
    
    # Input della frase
    frase = input("Scrivi la frase da tradurre: ").strip()
    if not frase:
        print("Errore: devi scrivere una frase!")
        return
    
    # Selezione della lingua
    print("\nLingue disponibili:")
    for codice, nome in LINGUE.items():
        print(f"  {codice}: {nome}")
    
    lingua_dest = input("\nSeleziona la lingua di destinazione (es. it, en, es): ").strip().lower()
    if lingua_dest not in LINGUE:
        print("Errore: lingua non disponibile!")
        return
    
    # Traduzione
    print("\nTraduzione in corso...")
    translator = Translator()
    risultato = await translator.translate(frase, dest=lingua_dest)
    testo_tradotto = risultato.text
    
    # Stampa il risultato
    print(f"\n Testo originale: {frase}")
    print(f"Lingua: {LINGUE[lingua_dest]}")
    print(f"Traduzione: {testo_tradotto}\n")
    
    # Generazione MP3
    print("Generazione file MP3 in corso...")
    try:
        tts = gTTS(text=testo_tradotto, lang=lingua_dest, slow=False)
        nomefile = f"traduzione_{lingua_dest}.mp3"
        tts.save(nomefile)
        print(f"File MP3 salvato: {nomefile}")
        
        # Apri il file MP3
        if os.name == 'nt':  # Windows
            os.startfile(nomefile)
            print(f"Riproduzione in corso...")
    except Exception as e:
        print(f"Errore nella generazione MP3: {e}")

asyncio.run(main())