arquivo = open("teste.txt", "w") # Abre o arquivo "teste.txt" para escrita (cria o arquivo se não existir)
arquivo.write("Olá, este é um teste de escrita em arquivo.\n") # Escreve uma linha de texto no arquivo
arquivo.close() # Fecha o arquivo para garantir que os dados sejam salvos corretamente

arquivo = open("teste.txt", "r") # Abre o arquivo "teste.txt" para leitura, o r é utilizado para mostrar que o arquivo será aberto para leitura
conteudo = arquivo.read() # Lê o conteúdo do arquivo e armazena na variável
print(conteudo) # Imprime o conteúdo do arquivo
arquivo.close() # Fecha o arquivo após a leitura