# IS_Med

Gerador De mensagens:
    Gera X mensagens e coloca na worklist


Gera Bloco:
    Recebe lista de mensagens e concatena com ‘!’ no fim de cada mensagem
    devolve bloco


Gerador ACK’s:
    recebe bloco e gera ACK’s


Servidor PC1:
    vai á work list pega em X mensagens
    gera Bloco
    gera ACK’s
    envia Bloco
    regista timestamp e ack’s
    espera resposta
    imprime tempo que demorou.
    se não receber resposta em 1 min reenvia bloco


Cliente PC2:
    recebe mensagens
    gera ACK’s
    envia ack’s em bloco






Servidor PC2: Não é necessário para este teste de tempos
Cliente PC1: Não é necessário para este teste de tempos
Gerador de Relatórios: Não é necessário para este teste de tempos
