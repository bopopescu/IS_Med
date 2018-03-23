# IS_Med


Gerador De mensagens:
    Gera X mensagens e coloca na worklist


Servidor PC1:
    vai á work list pega na messagem .. envia .. e preenche o timestamp e ack


Cliente PC1:
    recebe ACK’s
    preenche na worklist timestamp e ack recebido


Servidor PC2:
    envia ACk’s
    envia relatórios se já estiverem preenchidos


Cliente PC2:
    recebe mensagens
    guarda na worklist



Gerador de Relatórios:
    Mostra informações ao Utilizador e pede relatório
    preenche a BD





BD1:
    Worklist:
        Novos Campos:
                timestamp enviado (sentTime)
                timestamp receção (recTime)
                ACK (ack)
    Pedido:
        Novo Campo:
            Relatório (rel)

BD2:
    Worklist:
        Novos Campos:
            ACK (ack)
            ack enviado (ackSent)
            relatório (rel)
            relatório enviado (relSent)
