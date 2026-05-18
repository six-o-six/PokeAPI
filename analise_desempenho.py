import os
import pandas as pd

CSV_PATH = "resultados.csv"

def carregar_dados() -> pd.DataFrame:
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(
            f"Arquivo '{CSV_PATH}' não encontrado. "
            "Execute o projeto primeiro para gerar os dados."
        )
    df = pd.read_csv(CSV_PATH, parse_dates=["timestamp"], encoding="latin1")
    df["cpus"]      = df["cpus"].astype(int)
    df["downloads"] = df["downloads"].astype(int)
    df["iteracao"]  = df["iteracao"].astype(int)
    df["tempo_s"]   = df["tempo_s"].astype(float)
    return df

def resumo_geral(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa por método + cpus + downloads e calcula as principais
    estatísticas de tempo por iteração.
    """
    return (
        df.groupby(["metodo", "cpus", "downloads"])["tempo_s"]
        .agg(
            media         = "mean",
            mediana       = "median",
            minimo        = "min",
            maximo        = "max",
            desvio_padrao = "std",
            n_execucoes   = "count",
        )
        .round(4)
        .reset_index()
        .sort_values(["downloads", "media"])
    )

def ranking_por_downloads(df: pd.DataFrame) -> pd.DataFrame:
    """
    Classifica as configurações da mais rápida para a mais lenta
    dentro de cada quantidade de downloads.
    """
    resumo = resumo_geral(df)
    resumo["rank"] = (
        resumo.groupby("downloads")["media"]
        .rank(method="min")
        .astype(int)
    )
    return resumo.sort_values(["downloads", "rank"])[
        ["downloads", "rank", "metodo", "cpus", "media", "mediana", "desvio_padrao"]
    ]

def speedup_vs_sequencial(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula quantas vezes cada configuração é mais rápida que o Sequencial.
    speedup = tempo_sequencial / tempo_configuracao
    speedup > 1 → mais rápido | speedup < 1 → mais lento
    """
    resumo = resumo_geral(df)

    baseline = (
        resumo[resumo["metodo"] == "Sequencial"][["downloads", "media"]]
        .rename(columns={"media": "tempo_sequencial"})
    )

    merged = resumo.merge(baseline, on="downloads", how="left")
    merged["speedup"] = (merged["tempo_sequencial"] / merged["media"]).round(4)

    return (
        merged[["metodo", "cpus", "downloads", "media", "tempo_sequencial", "speedup"]]
        .sort_values(["downloads", "speedup"], ascending=[True, False])
    )

def impacto_cpus(df: pd.DataFrame) -> pd.DataFrame:
    """
    Para cada método paralelo, mostra como o tempo médio varia conforme
    o número de CPUs aumenta e qual o percentual de melhora em relação
    à configuração anterior de CPUs.
    """
    paralelos = df[df["metodo"] != "Sequencial"]

    resumo = (
        paralelos.groupby(["metodo", "downloads", "cpus"])["tempo_s"]
        .mean()
        .round(4)
        .reset_index()
        .rename(columns={"tempo_s": "media"})
        .sort_values(["metodo", "downloads", "cpus"])
    )

    resumo["melhora_pct"] = (
        resumo.groupby(["metodo", "downloads"])["media"]
        .pct_change() * -100
    ).round(2)

    return resumo

def consistencia(df: pd.DataFrame) -> pd.DataFrame:
    """
    Coeficiente de variação (CV) = desvio_padrao / media * 100
    CV baixo  → execuções estáveis e previsíveis
    CV alto   → resultados instáveis (possível ruído de rede ou concorrência)
    """
    resumo = resumo_geral(df)
    resumo["cv_pct"] = (
        (resumo["desvio_padrao"] / resumo["media"]) * 100
    ).round(2)

    return (
        resumo[["metodo", "cpus", "downloads", "media", "desvio_padrao", "cv_pct"]]
        .sort_values("cv_pct")
    )

def evolucao_por_iteracao(df: pd.DataFrame) -> pd.DataFrame:
    """
    Média do tempo por iteração (1 a 10) agrupada por método, cpus e downloads.
    """
    return (
        df.groupby(["metodo", "cpus", "downloads", "iteracao"])["tempo_s"]
        .mean()
        .round(4)
        .reset_index()
        .sort_values(["metodo", "downloads", "cpus", "iteracao"])
    )

def melhor_configuracao(df: pd.DataFrame) -> pd.DataFrame:
    """
    Para cada quantidade de downloads, retorna a configuração
    (método + cpus) com o menor tempo médio.
    """
    resumo = resumo_geral(df)
    idx = resumo.groupby("downloads")["media"].idxmin()
    return (
        resumo.loc[idx][["downloads", "metodo", "cpus", "media", "mediana", "desvio_padrao"]]
        .reset_index(drop=True)
    )

def imprimir_separador(titulo: str):
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)

def executar_analise():
    df = carregar_dados()

    imprimir_separador("1. RESUMO GERAL")
    print(resumo_geral(df).to_string(index=False))

    imprimir_separador("2. RANKING POR QUANTIDADE DE DOWNLOADS")
    print(ranking_por_downloads(df).to_string(index=False))

    imprimir_separador("3. SPEEDUP VS SEQUENCIAL")
    print(speedup_vs_sequencial(df).to_string(index=False))

    imprimir_separador("4. IMPACTO DO Nº DE CPUs")
    print(impacto_cpus(df).to_string(index=False))

    imprimir_separador("5. CONSISTÊNCIA DAS EXECUÇÕES (CV%)")
    print(consistencia(df).to_string(index=False))

    imprimir_separador("6. EVOLUÇÃO POR ITERAÇÃO")
    print(evolucao_por_iteracao(df).to_string(index=False))

    imprimir_separador("7. MELHOR CONFIGURAÇÃO POR DOWNLOADS")
    print(melhor_configuracao(df).to_string(index=False))

if __name__ == "__main__":
    executar_analise()