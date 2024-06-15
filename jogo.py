# SOLUCIONADO PÓS-OBI

def checa_celula(celula, qtdViz):
  if celula == "0": # celula morta
    if qtdViz == 3: 
      return "1"; 
    else:
      return "0";
  elif celula == "1": # célula viva
    if qtdViz > 3:
      return "0";
    elif qtdViz < 2:
      return "0";
    else:
      return "1";

N, Q = map(int, input().split());
matriz = [];

for _ in range(N):
  linha = input();
  matriz.append(linha);

vetorNovo = "";
for _ in range(Q): # Q-ésimo estado do jogo
  newMatriz = [];
  for i in range(N):
    res = "";
    for j in range(N):
      cc = 0;
      if i == 0: # Primeira linha
        if j == 0: # Primeira coluna
          if matriz[i][j+1] == "1": cc += 1;
          if matriz[i+1][j] == "1": cc += 1;
          if matriz[i+1][j+1] == "1": cc += 1;
          
          res += checa_celula(matriz[i][j], cc);
        elif j == N-1: # Última coluna
          if matriz[i][j-1] == "1": cc += 1;
          if matriz[i+1][j] == "1": cc += 1;
          if matriz[i+1][j-1] == "1": cc += 1;
          
          res += checa_celula(matriz[i][j], cc);
        else: # Colunas do meio
          if matriz[i][j+1] == "1": cc += 1;
          if matriz[i][j-1] == "1": cc += 1;
          if matriz[i+1][j] == "1": cc += 1;
          if matriz[i+1][j+1] == "1": cc += 1;
          if matriz[i+1][j-1] == "1": cc += 1;
          
          res += checa_celula(matriz[i][j], cc);
      elif i == N-1: # Última linha
        if j == 0:
          if matriz[i][j+1] == "1": cc += 1;
          if matriz[i-1][j] == "1": cc += 1;
          if matriz[i-1][j+1] == "1": cc += 1;

          res += checa_celula(matriz[i][j], cc);
        elif j == N-1:
          if matriz[i][j-1] == "1": cc += 1;
          if matriz[i-1][j] == "1": cc += 1;
          if matriz[i-1][j-1] == "1": cc += 1;

          res += checa_celula(matriz[i][j], cc);
        else:
          if matriz[i][j+1] == "1": cc += 1;
          if matriz[i][j-1] == "1": cc += 1;
          if matriz[i-1][j] == "1": cc += 1;
          if matriz[i-1][j+1] == "1": cc += 1;
          if matriz[i-1][j-1] == "1": cc += 1;
          
          res += checa_celula(matriz[i][j], cc);
      else: # Linhas do meio
        if j == 0:
          if matriz[i-1][j] == "1": cc += 1;
          if matriz[i][j+1] == "1": cc += 1;
          if matriz[i+1][j] == "1": cc += 1;
          if matriz[i+1][j+1] == "1": cc += 1;
          if matriz[i-1][j+1] == "1": cc += 1;
        
          res += checa_celula(matriz[i][j], cc);
        elif j == N-1:
          if matriz[i+1][j] == "1": cc += 1;
          if matriz[i-1][j] == "1": cc += 1;
          if matriz[i][j-1] == "1": cc += 1;
          if matriz[i-1][j-1] == "1": cc += 1;
          if matriz[i+1][j-1] == "1": cc += 1;
        
          res += checa_celula(matriz[i][j], cc);
        else:
          if matriz[i][j-1] == "1": cc += 1;
          if matriz[i][j+1] == "1": cc += 1;
          if matriz[i-1][j] == "1": cc += 1;
          if matriz[i-1][j+1] == "1": cc += 1;
          if matriz[i-1][j-1] == "1": cc += 1;
          if matriz[i+1][j] == "1": cc += 1;
          if matriz[i+1][j+1] == "1": cc += 1;
          if matriz[i+1][j-1] == "1": cc += 1;

          res += checa_celula(matriz[i][j], cc);
    newMatriz.append(res);
  matriz = newMatriz[0:N];

for linha in matriz:
  print(linha);
