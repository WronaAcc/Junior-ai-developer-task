from openai import OpenAI
import os

client = OpenAI(api_key="Twój klucz API :)")

def load_article(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        article = file.read()
    return article

def save_html(content, file_path="artykul.html"):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Plik HTML został zapisany jako {file_path}")

def process_article_with_openai(article):
    prompt = (
        "Przekształć poniższy artykuł na strukturę HTML bez tagów <html>, <head> ani <body>. "
        "Użyj odpowiednich tagów HTML do strukturyzacji treści, takich jak <h1>, <h2>, <p>, <img> oraz <figcaption>. "
        "Wstaw miejsca na obrazy z tagiem <img src='image_placeholder.jpg'> i dodaj opis obrazka w atrybucie alt, "
        "np. 'Asystent głosowy wspomaga codzienne czynności'. Umieść podpisy pod grafikami, używając tagu <figcaption>."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem, który przekształca artykuły na HTML."},
            {"role": "user", "content": f"{prompt}\n\nArtykuł:\n{article}"}
        ],
        max_tokens=2048
    )

    html_content = response.choices[0].message.content.strip()
    return html_content

def main():
    article_file_path = "artykul.txt"

    article = load_article(article_file_path)

    html_content = process_article_with_openai(article)

    save_html(html_content)

if __name__ == "__main__":
    main()