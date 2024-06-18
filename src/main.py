import numpy as np
import pandas as pd

FILE_PATH = '../data/goalscorers.csv'


def main():
    dados_gols = pd.read_csv('../data/goalscorers.csv')
    dados_resultados = pd.read_csv('../data/results.csv')

    dados_completos = pd.merge(dados_gols, dados_resultados, on=['date', 'home_team', 'away_team'])

    condicoes = [
        (dados_completos['home_score'] > dados_completos['away_score']),
        (dados_completos['home_score'] < dados_completos['away_score']),
        (dados_completos['home_score'] == dados_completos['away_score'])
    ]
    escolhas = ['vitória_casa', 'vitória_fora', 'empate']
    dados_completos['resultado_jogo'] = np.select(condicoes, escolhas, default='indeterminado')

    primeiro_gol = dados_completos[
        dados_completos['minute'] == dados_completos.groupby('date')['minute'].transform('min')]


    vitorias_primeiro_gol = primeiro_gol[primeiro_gol['resultado_jogo'].isin(['vitória_casa', 'vitória_fora'])]


    contagem_vitorias = vitorias_primeiro_gol['team'].value_counts()
    print(f'Numero de vitorias que o time possui fazendo o primeiro gol da partida:')
    print(contagem_vitorias)
    print(f'---------------------------------------')


    vitorias_home_team = dados_completos[(dados_completos['resultado_jogo'] == 'vitória_casa') & (
            dados_completos['team'] == dados_completos['home_team'])]
    porcentagem_vitorias_home_team = (len(vitorias_home_team) / len(
        dados_completos[dados_completos['team'] == dados_completos['home_team']])) * 100


    vitorias_away_team = dados_completos[(dados_completos['resultado_jogo'] == 'vitória_fora') & (
            dados_completos['team'] == dados_completos['away_team'])]
    porcentagem_vitorias_away_team = (len(vitorias_away_team) / len(
        dados_completos[dados_completos['team'] == dados_completos['away_team']])) * 100
    print(f"Porcentagem de vitórias do time da casa: {porcentagem_vitorias_home_team:.2f}%")
    print(f"Porcentagem de vitórias do time visitante: {porcentagem_vitorias_away_team:.2f}%")
    print("_______________")

    gols_primeiro_tempo = dados_gols[dados_gols['minute'] <= 45]
    gols_segundo_tempo = dados_gols[dados_gols['minute'] > 45]

    numero_gols_primeiro_tempo = len(gols_primeiro_tempo)
    numero_gols_segundo_tempo = len(gols_segundo_tempo)

    total_gols = numero_gols_primeiro_tempo + numero_gols_segundo_tempo
    porcentagem_primeiro_tempo = (numero_gols_primeiro_tempo / total_gols) * 100
    porcentagem_segundo_tempo = (numero_gols_segundo_tempo / total_gols) * 100

    print(f"Porcentagem de gols no primeiro tempo: {porcentagem_primeiro_tempo:.2f}%")
    print(f"Porcentagem de gols no segundo tempo: {porcentagem_segundo_tempo:.2f}%")
    print("_______________")


main()
