N, K = map(int, input().split());
lista = list(map(int, input().split()));
lista.sort();
print(lista[N-K]);