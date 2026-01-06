import requests
from bs4 import BeautifulSoup
import time

#Configurações
CIDADES_INTERESSE = ["Tramandaí", "Imbé", "Osório", "Xangrila", "Xangri-lá", "Cidreira"]
URL_FUNDATEC = "https://www.fundatec.org.br/portal/concursos/"

def monitorar_concursos():
    print(f"[{time.strftime('%H:%M:%S')}] Verificando novos concursos...")

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(URL_FUNDATEC, timeout=15, headers=headers)
        response.encoding = 'iso-8859-1'

        soup = BeautifulSoup(response.text, 'html.parser')

        concursos_abertos = soup.find_all('div', class_='box-inscricoes-abertas')
        concursos_em_andamento = soup.find_all('div', class_='box-inscricoes-andamento')

        todos_concursos = concursos_abertos + concursos_em_andamento

        concursos_encontrados = []

        for concursos in todos_concursos:
            titulo_div = concursos.find('div', class_='box-title')
            if not titulo_div:
                continue

            nome_concurso = titulo_div.get_text(strip=True)

            link_tag = concursos.find('a')
            link_completo = "https://www.fundatec.org.br/portal/concursos/" + link_tag['href'] if link_tag else "Link não disponível"

            for cidade in CIDADES_INTERESSE:
                if cidade.lower() in nome_concurso.lower():
                    concursos_encontrados.append({
                        "cidade": cidade,
                        "nome": nome_concurso,
                        "link": link_completo
                    })

        if concursos_encontrados:
            print(f"Foram encontrados {len(concursos_encontrados)} editais para suas cidades:\n")
            for conc in concursos_encontrados:
                print(f"📍 Cidade: {conc['cidade']}")
                print(f"🏢 Órgão: {conc['nome']}")
                print(f"🔗 Link: {conc['link']}")
                print("-" * 50)
        else:
            print("Nenhum concurso novo para as cidades selecionadas.")

    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    while True:
        monitorar_concursos()
        print(f"\nAguardando 1 hora para a próxima verificação...\n")
        time.sleep(3600)
