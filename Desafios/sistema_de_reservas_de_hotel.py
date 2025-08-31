def processar_reservas():
    # Entrada dos quartos disponíveis (transforma em conjunto para busca rápida)
    quartos_disponiveis = set(map(int, input().split()))

    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    # Listas para armazenar os resultados
    confirmadas = []
    recusadas = []

    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos:
    # Processamento das reservas
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            confirmadas.append(reserva)
            quartos_disponiveis.remove(
                reserva
            )  # Remove para que não seja reservado duas vezes
        else:
            recusadas.append(reserva)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))


# Chamada da função principal
processar_reservas()
