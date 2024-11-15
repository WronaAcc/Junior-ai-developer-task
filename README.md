# Projekt: Junior AI Developer Task

## Zawartość projektu

- `main.py` - Skrypt Pythona odpowiedzialny za odczyt pliku tekstowego, wysyłanie treści do OpenAI API oraz zapisanie wygenerowanego HTML.
- `artykul.txt` - Przykładowy plik tekstowy z artykułem używany jako dane wejściowe.
- `artykul.html` - Wygenerowany plik HTML zawierający przetworzoną treść artykułu, gotowy do wyświetlenia w przeglądarce.
- `szablon.html` - Opcjonalny szablon HTML do wizualizacji artykułu, zawierający podstawowe style CSS i strukturyzację.
- `podglad.html` - Opcjonalny plik z pełnym podglądem artykułu, bazujący na szablonie HTML.

## Wymagania

- Python 3.7 lub nowszy
- Biblioteka `openai` (można ją zainstalować za pomocą `pip`)

## Instrukcja uruchomienia

1. Sklonuj repozytorium na swój komputer:

   ```bash
   git clone https://github.com/WronaAcc/Junior-ai-developer-task.git
   cd Junior-ai-developer-task

2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install openai

3. Dodaj swój klucz API OpenAi:
   
   W pliku main.py zastąp "Twój klucz API :)" swoim kluczem API OpenAi.
   ```bash
   client = OpenAi(api_keys="sk...Twój_klucz_API")

4. Uruchom skrypt:
   ```bash
   python main.py
   ```
   Skrypt odczyta zawartość pliku artykul.txt, przetworzy go za pomocą OpenAi API i zapisze wynik w pliku artykul.html

## Działanie aplikacji

- Odczyt artykułu - Skrypt odczytuje treść artykułu z pliku artykul.txt.
- Przetwarzanie za pomocą OpenAI API - Tekst artykułu, wraz z promptem, jest wysyłany do modelu OpenAI, który generuje odpowiednio sformatowany kod HTML.
- Zapis wyniku - Otrzymany kod HTML jest zapisywany w pliku artykul.html. Plik ten zawiera tylko sekcję <body> i jest gotowy do wyświetlenia w przeglądarce w połączeniu z szablonem.

## Opcjonalne pliki

- szablon.html - Możesz użyć tego szablonu do wizualizacji artykułu. Zawiera podstawowe style i kod JavaScript, który poprawia wygląd treści.
- podglad.html - Ten plik zawiera pełny podgląd artykułu, gotowy do wyświetlenia w przeglądarce.

## Uwagi

- Upewnij się, że masz aktywne połączenie internetowe, aby aplikacja mogła połączyć się z OpenAI API.
- Pamiętaj, że użycie OpenAI API jest płatne, jeśli nie masz darmowego klucza API.

# Projekt ten został stworzony wyłącznie na potrzeby rekrutacji i nie jest przeznaczony do komercyjnego użytku!
