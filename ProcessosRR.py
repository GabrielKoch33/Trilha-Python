import time
tempo_max_processo = 0
i = 0
finished = False

# EXEMPLO DE PREEMPÇÃO COM ROUND ROBIN

while tempo_max_processo < 15:

    # Processo 1, Este processo está como prioridade enquanto outro processo mais importante não esteja ocorrendo, e leva aprox. 10 segundos
    for i in range(i,11):
        
        if i == 0:
            print(f'Processo Nº 1 | Estado: PRONTO...AGUARDANDO INICIALIZAÇÃO')

        else:
            print(f'Executando processo Nº 1 | PID: 1125 | Estado: Em Execução | Tempo do Processo: {i} segundos', flush=True)
            time.sleep(1) 
            tempo_max_processo += 1

            if tempo_max_processo == 5:
                time.sleep(1)
                print(f'Processo Nº 1 | Estado: BLOQUEADO...AGUARDANDO O NOVO PROCESSO DE MAIS PRIORIDADE E MENOS TEMPO ACABAR', flush=True)
                i += 1
                break
    
    print()
    while finished == False:

        print(f'Processo Nº 2 | Estado: PRONTO...AGUARDANDO INICIALIZAÇÃO', flush=True)
        time.sleep(1)

        for j in range(1,6):
            print(f'Executando processo Nº 2 | PID: 1126 | Estado: Em Execução | Tempo do Processo: {j} segundos', flush=True)
            time.sleep(1)
            tempo_max_processo += 1

        finished = True
        print(f'Processo Nº 2 | Estado: FINALIZADO...LIBERANDO MEMÓRIA', flush=True)
        print()
