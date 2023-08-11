import requests
import json
import dewiki
import sys

def request_wikipedia(page: str):
    URL = "https://en.wikipedia.org/w/api.php"

#Parâmetros da solicitação à API
    PARAMS = {
        "action"    : "parse",
        "page"      : page,
        "prop"      : "wikitext",
        "format"    : "json",
        "redirects" : "true"
    }

    try:
        res = requests.get(url=URL, params=PARAMS)
        res.raise_for_status()
    except requests.HTTPError as e:
        raise e
#Conteúdo da resposta é decodificado usando o módulo json.
    try:
        data = json.loads(res.text)
        return data["parse"]["wikitext"]["*"]
    except json.decoder.JSONDecodeError as e:
        raise e

def my_program():
#Verifica se o número de argumentos é válido
    if len(sys.argv) != 2:
        print("ATTENTION: Only one argument is needed!")
        sys.exit(1)

#Obtém a consulta a partir dos argumentos da linha de comando
    query = sys.argv[1]
    
#Verifica se o parâmetro é válido
    if not query.strip():
        print("ATTENTION: invalid parameter.")
        sys.exit(1)

#Obtém o conteúdo da página da Wikipedia
    content = request_wikipedia(query)
    if content is None:
        return

#Remove formatação Wiki do conteúdo
    clean_text = dewiki.from_string(content)

#Cria e escreve o conteúdo no arquivo .wiki
    try:
        filename = f"{query.replace(' ', '_')}.wiki"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(clean_text)
        print(f"Result saved in {filename}")
    except IOError as e:
        print(f"Error creating .wiki file: {e}")

if __name__ == '__main__':
    my_program()