import wikipedia as wp
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def search_wiki():
    wp.lang("es")
    talk("Qué desea buscar?")
    busqueda = input("Buscar: ")
    resultado = wp.summary(busqueda)
    talk(resultado)    
    
search_wiki()
