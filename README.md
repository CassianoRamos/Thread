# Thread
Exemplo simples do uso de Thread para a matéria de SO

Esse é um código bem básico que simula o uso de threads para realizar múltiplos downloads simultaneamente.
Temos nas funções a indicação do inicio do download, um tempo decorrido, que simula o tempo de download e após a indicação do fim do mesmo.
Para fazer com que essas funções operem de forma simultanea e paralela, fazemos a chamada da thread e a alocamos para que seja realizada a função downloadUM() e logo após chamamos de forma direta a função downloadDois(), desta forma os dois downloads serão feitos juntos, mas em threads diferentes, otimizando o tempo de transferencia dos mesmos.
