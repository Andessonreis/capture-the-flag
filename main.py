#!/usr/bin/env python3

import urllib.parse

def main():
    print("||| BEM-VINDO AO MINI-CTF SUPER SECRETO |||")
    print("Responda às perguntas com atenção e veja o resultado no final!")
    print("Boa sorte!\n")

    # Lista de perguntas com dicas para cada uma
    perguntas = [
        {"pergunta": "Qual sua cor favorita?", "dica": "Exemplo: azul, verde, vermelho."},
        {"pergunta": "Qual ano você nasceu?", "dica": "Responda com um número, como 2000."},
        {"pergunta": "Escolha um número de 1 a 10:", "dica": "Qualquer número entre 1 e 10."},
    ]

    respostas = []

    # Loop para fazer perguntas ao usuário
    for i, q in enumerate(perguntas):
        print(f"Pergunta {i + 1}: {q['pergunta']}")
        print(f"Dica: {q['dica']}")
        resposta = input(">> ").strip()
        
        # Armazenando a resposta
        respostas.append(resposta)
        print("Resposta registrada!\n")

    print("Parabéns! Você completou o desafio. Gerando resultado...\n")

    # Gerando um link de resultado
    params = {
        "resposta1": respostas[0],
        "resposta2": respostas[1],
        "resposta3": respostas[2],
    }
    base_url = "https://meuctf.supersecreto.net/result"
    query_string = urllib.parse.urlencode(params)
    resultado = f"{base_url}?{query_string}"
    
    print(f"Acesse o resultado aqui: {resultado}")

if __name__ == "__main__":
    main()
