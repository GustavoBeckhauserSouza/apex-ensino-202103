# Exercícios

1. Escreva uma função que indique se um número está dentro de um intervalo

```
func(numero, inicio_intervalo, fim_intervalo)
func(1, 4, 7) # False
func(4, 3, 9) # True
```

2. Escreva um programa em Python que converta uma temperatura de Celsius para Fahrenheit, e vice versa. Crie 2 funções para isso.
```
C -> F: (C × 9/5) + 32 = 32°F
F -> C: (F − 32) × 5/9 = -17,78 °C
```

3. Escreva uma função que receba uma string e calcule a quantidade de letras maiúsculas e minúsculas essa string tem

```
func("hUadhHIqpO")
{"maiusculas": 4, "minusculas": 6}
```

Para isso utilize os métodos `isupper()` e `islower()`

4. Escreva uma função em Python que recebe uma lista e retorne uma nova lista sem números repetidos
```
func([1, 2, 2, 4, 4, 5, 6, 7, 7, 7, 8, 9, 9, 9, 9])
[1, 2, 4, 5, 6, 7, 8, 9]
```

5. Escreva uma função em Python que receba uma lista de números, e retorne uma outra
lista apenas com os números pares.

```
func([1, 2, 3, 6, 7, 10, 34, 35, 91])
[2, 6, 10, 34]
```