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
    primeiro_gol_resultado = primeiro_gol.groupby('team')['resultado_jogo'].value_counts(normalize=True)

    vitoria_casa = dados_completos[dados_completos['resultado_jogo'] == 'vitória_casa']['team'].value_counts(
        normalize=True)
    vitoria_fora = dados_completos[dados_completos['resultado_jogo'] == 'vitória_fora']['team'].value_counts(
        normalize=True)

    gols_primeiro_tempo = dados_completos[dados_completos['minute'] <= 45]['team'].value_counts(normalize=True)
    gols_segundo_tempo = dados_completos[dados_completos['minute'] > 45]['team'].value_counts(normalize=True)

    print(primeiro_gol_resultado)
    print("_______________")
    print(f"Vitórias em casa: {vitoria_casa}")
    print(f"Vitórias fora: {vitoria_fora}")
    print("_______________")
    print(f"Gols no primeiro tempo: {gols_primeiro_tempo}")
    print(f"Gols no segundo tempo: {gols_segundo_tempo}")
    print("_______________")


main()
