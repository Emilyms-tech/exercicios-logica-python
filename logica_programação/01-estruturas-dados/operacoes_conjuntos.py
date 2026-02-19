lista = {"maçã", "banana", "laranja"} # Cria um conjunto (set) com frutas, os conjuntos são coleções não ordenadas e sem elementos duplicados
print(lista) # Imprime o conjunto, a ordem dos elementos pode variar a cada execução
lista.add("uva") # Adiciona o elemento "uva" ao conjunto
print(lista) # Imprime o conjunto atualizado, agora incluindo "uva"
lista.remove("banana") # Remove o elemento "banana" do conjunto
print(lista) # Imprime o conjunto atualizado, agora sem "banana"

lista2 = {"maçã", "pera", "uva"} # Cria outro conjunto com algumas frutas, incluindo "maçã" e "uva" que estão no primeiro conjunto
intersecao = lista.intersection(lista2) # Calcula a interseção dos dois conjuntos, ou seja, os elementos que estão em ambos os conjuntos
print(intersecao) # Imprime a interseção, que deve conter "maçã" e "uva" se ambos os conjuntos tiverem esses elementos

uniao = lista.union(lista2) # Calcula a união dos dois conjuntos, ou seja, todos os elementos que estão em pelo menos um dos conjuntos
print(uniao) # Imprime a união, que deve conter "maçã", "laranja", "uva", e "pera" sem duplicatas

diferenca = lista.difference(lista2) # Calcula a diferença entre os conjuntos, ou seja, os elementos que estão no primeiro conjunto mas não no segundo
print(diferenca) # Imprime a diferença, que deve conter "laranja" se

lista.update(lista2) # Atualiza o primeiro conjunto com os elementos do segundo conjunto, adicionando "pera" e mantendo "maçã" e "uva"
print(lista) # Imprime o conjunto atualizado, que agora deve conter "maçã",