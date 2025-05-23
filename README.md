# [**Curso em Video**](https://www.cursoemvideo.com/) - Curso de Python 3 :v:

## **Mundo 1 [40 Horas]**

----

### Curso Python #01 - Seja um Programador.

*Este curso introdutório prepara o palco para sua jornada na programação. Ele cobre os conceitos fundamentais do que é programação e o que significa ser um programador.*

----

### Curso Python #02 - Para que serve o Python ?.

*Descubra a versatilidade do Python! Este curso explora a vasta gama de aplicações do Python, desde desenvolvimento web e análise de dados até inteligência artificial e automação.*

----

### Curso Python #03 - Instalando o Python3 e o IDLE.

*Prepare-se para programar! Este curso guia você pelo processo de instalação do Python 3 e seu Ambiente de Desenvolvimento Integrado (IDLE) padrão.*

----

### Curso Python #04 - Primeiros comandos em Python3.

*Hora de escrever suas primeiras linhas de código Python! Este curso apresenta comandos básicos e sintaxe, permitindo que você interaja com o interpretador Python.*

----

### Curso Python #05 - Instalado o PyCharm e o QPython3.

*Explore ambientes de desenvolvimento mais poderosos! Este curso demonstra como instalar e configurar o PyCharm (uma IDE profissional popular) e o QPython3 (para desenvolvimento mobile).*

----

### **EXE_01: Olá, Mundo!**

> Crie um programa que escreva "olá mundo!" na tela.

#### Conceitos-chave:
*   **`função print()`:** Usada para exibir dados na console.

#### Solução:
```python
print('Olá, Mundo!')
```

#### Explicação:

A função `print()` é uma função embutida do Python que recebe um ou mais argumentos e os exibe na tela. Neste caso, passamos a string `'Olá, Mundo!'` como argumento para a função `print()`.

#### Saída Esperada:

Running this code will display:
```
Olá, Mundo!
```

----

### **EXE_02: Mensagem de Boas-Vindas Personalizada**

> Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

#### Conceitos-chave:
*   **`função input()`:** Usada para receber dados do usuário.
*   **`função print()`:** Usada para exibir dados.
*   **Concatenação de strings ou f-strings:** Para combinar texto com variáveis.

#### Solução:
```python
nome = input('Digite seu nome: ')
print(f'Olá, {nome}! Bem-vindo!')
```

#### Explicação:

1.  A função `input('Digite seu nome: ')` solicita que o usuário digite seu nome e armazena o valor digitado na variável `nome`.
2.  A função `print(f'Olá, {nome}! Bem-vindo!')` então exibe uma mensagem de boas-vindas.
    *   O `f` antes da string indica uma "f-string" (literal de string formatada).
    *   `{nome}` dentro da f-string é um marcador de posição que é substituído pelo valor da variável `nome`.

#### Exemplo de Uso:

If the user types 'Maria' when prompted, the output will be:
```
Olá, Maria! Bem-vindo!
```

----

### Curso Python #06 - Tipos Primitivos e Saída de Dados.

---- 

### **EXE_03: Soma de Dois Números**

> Crie um programa que leia dois números e mostre a soma entre eles.

#### Conceitos-chave:
*   Função `input()` para ler dados do usuário.
*   Função `int()` ou `float()` para converter o texto lido para número.
*   Operadores aritméticos (adição `+`).
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 03.py correspondente.
```

#### Explicação:

O programa solicitará ao usuário que digite dois números. Esses números serão lidos como texto, convertidos para o tipo numérico apropriado (inteiro ou decimal) e, em seguida, somados. O resultado da soma será exibido na tela.

#### Exemplo de Uso:
```
Digite o primeiro número: 10
Digite o segundo número: 5
A soma entre 10 e 5 é: 15
```

----

### **EXE_04: Analisando Tipos Primitivos**

> Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possiveis sobre ele.

#### Conceitos-chave:
*   Função `input()` para ler dados do usuário.
*   Função `type()` para verificar o tipo de dado.
*   Métodos de string como `isnumeric()`, `isalpha()`, `isalnum()`, `isupper()`, `islower()`, `isspace()`.
*   Função `print()` para exibir as informações.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 04.py correspondente.
```

#### Explicação:

O programa lerá uma entrada do teclado. Em seguida, utilizará a função `type()` para mostrar o tipo primitivo do dado lido. Adicionalmente, explorará diversos métodos de string para verificar características como: se é numérico, alfabético, alfanumérico, se está em maiúsculas, minúsculas, ou se é composto apenas por espaços.

#### Exemplo de Uso:
```
Digite algo: Python3
Tipo primitivo: <class 'str'>
É numérico? False
É alfabético? False
É alfanumérico? True
Está em maiúsculas? False
Está em minúsculas? False
É espaço? False
```

----

### Curso Python #07 - Operadores Aritméticos

----

### **EXE_05: Antecessor e Sucessor**

> Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

#### Conceitos-chave:
*   Função `input()` para ler o número.
*   Função `int()` para converter o texto para inteiro.
*   Operadores aritméticos (subtração `-` e adição `+`).
*   Função `print()` para exibir os resultados.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 05.py correspondente.
```

#### Explicação:

O programa lerá um número inteiro fornecido pelo usuário. Em seguida, calculará o antecessor subtraindo 1 do número e o sucessor adicionando 1 ao número. Ambos os resultados serão exibidos.

#### Exemplo de Uso:
```
Digite um número inteiro: 25
O antecessor de 25 é 24.
O sucessor de 25 é 26.
```

----

### **EXE_06: Dobro, Triplo e Raiz Quadrada**

> Crie um algoritmo que leia um número e mostre o seu dobro, triplo e rais quadrada.

#### Conceitos-chave:
*   Função `input()` para ler o número.
*   Função `float()` ou `int()` para conversão.
*   Operadores aritméticos (multiplicação `*`).
*   Função `pow()` ou operador `**` para calcular a raiz quadrada (ex: `n ** (1/2)`).
*   Função `print()` para exibir os resultados.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 06.py correspondente.
```

#### Explicação:

O programa lerá um número. Depois, calculará o dobro (número * 2), o triplo (número * 3) e a raiz quadrada (número elevado a 0.5 ou usando `pow(numero, 1/2)`). Os três resultados serão mostrados na tela.

#### Exemplo de Uso:
```
Digite um número: 16
Dobro: 32
Triplo: 48
Raiz Quadrada: 4.0
```

----

### **EXE_07: Média Aritmética**

> Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#### Conceitos-chave:
*   Função `input()` para ler as notas.
*   Função `float()` para converter as notas para números decimais.
*   Operadores aritméticos (adição `+` e divisão `/`).
*   Função `print()` para exibir a média.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 07.py correspondente.
```

#### Explicação:

O programa solicitará ao aluno que digite suas duas notas. As notas serão convertidas para números decimais, somadas, e o resultado será dividido por 2 para calcular a média. A média final será exibida.

#### Exemplo de Uso:
```
Digite a primeira nota: 7.5
Digite a segunda nota: 8.5
A média do aluno é: 8.0
```

----

### Curso Python #08 - Utilizando Módulos

----

### **EXE_08: Conversor de Medidas**

> Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

#### Conceitos-chave:
*   Função `input()` para ler o valor em metros.
*   Função `float()` para conversão.
*   Operadores aritméticos (multiplicação `*`).
*   Função `print()` para exibir as conversões.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 08.py correspondente.
```

#### Explicação:

O programa lerá um valor em metros. Para converter para centímetros, o valor será multiplicado por 100. Para converter para milímetros, o valor em metros será multiplicado por 1000. Os resultados das conversões serão exibidos.

#### Exemplo de Uso:
```
Digite um valor em metros: 2.5
2.5 metros equivalem a:
250.0 centímetros
2500.0 milímetros
```

----

### **EXE_09: Tabuada**

> Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

#### Conceitos-chave:
*   Função `input()` para ler o número inteiro.
*   Função `int()` para conversão.
*   Laço de repetição `for` (ex: `for i in range(1, 11):`).
*   Operadores aritméticos (multiplicação `*`).
*   Função `print()` para exibir cada item da tabuada.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 09.py correspondente.
```

#### Explicação:

O programa lerá um número inteiro. Em seguida, usará um laço `for` para iterar de 1 a 10. Em cada iteração, multiplicará o número lido pelo iterador atual e exibirá o resultado no formato "numero X iterador = resultado".

#### Exemplo de Uso:
```
Digite um número inteiro para ver sua tabuada: 7
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
```

----

### **EXE_10: Conversor de Moedas (Real para Dólar)**

> Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. **Considere US$1.00 = R$3,27**

#### Conceitos-chave:
*   Função `input()` para ler o valor em Reais.
*   Função `float()` para conversão.
*   Operadores aritméticos (divisão `/`).
*   Função `print()` para exibir o resultado da conversão.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 10.py correspondente.
```

#### Explicação:

O programa lerá a quantidade de dinheiro em Reais que uma pessoa possui. Considerando a taxa de câmbio fixa de R$3,27 por US$1,00, o valor em Reais será dividido pela taxa de câmbio para determinar quantos Dólares a pessoa pode comprar.

#### Exemplo de Uso:
```
Quanto dinheiro você tem na carteira? R$100.00
Com R$100.00 você pode comprar US$30.58
```

----

### **EXE_11: Cálculo de Tinta para Parede**

> Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².

#### Conceitos-chave:
*   Função `input()` para ler largura e altura.
*   Função `float()` para conversão.
*   Operadores aritméticos (multiplicação `*`, divisão `/`).
*   Função `print()` para exibir a área e a quantidade de tinta.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 11.py correspondente.
```

#### Explicação:

O programa lerá a largura e a altura de uma parede. Calculará a área multiplicando a largura pela altura. Em seguida, dividirá a área por 2 (rendimento da tinta) para determinar a quantidade de litros de tinta necessários.

#### Exemplo de Uso:
```
Digite a largura da parede (metros): 5
Digite a altura da parede (metros): 3
A área da parede é: 15.0 m²
Quantidade de tinta necessária: 7.5 litros
```

----

### **EXE_12: Calculando Descontos**

> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#### Conceitos-chave:
*   Função `input()` para ler o preço.
*   Função `float()` para conversão.
*   Operadores aritméticos (multiplicação `*`, subtração `-`).
*   Cálculo de porcentagem.
*   Função `print()` para exibir o novo preço.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 12.py correspondente.
```

#### Explicação:

O programa lerá o preço original de um produto. Calculará o valor do desconto (preço * 5 / 100). Em seguida, subtrairá o valor do desconto do preço original para obter o novo preço com desconto.

#### Exemplo de Uso:
```
Digite o preço do produto: R$120.00
O preço com 5% de desconto é: R$114.00
```

----

### **EXE_13: Aumento Salarial**

> Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

#### Conceitos-chave:
*   Função `input()` para ler o salário.
*   Função `float()` para conversão.
*   Operadores aritméticos (multiplicação `*`, adição `+`).
*   Cálculo de porcentagem.
*   Função `print()` para exibir o novo salário.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 13.py correspondente.
```

#### Explicação:

O programa lerá o salário atual de um funcionário. Calculará o valor do aumento (salário * 15 / 100). Em seguida, adicionará o valor do aumento ao salário original para obter o novo salário.

#### Exemplo de Uso:
```
Digite o salário do funcionário: R$2500.00
O novo salário com 15% de aumento é: R$2875.00
```

----

### **EXE_14: Conversor de Temperaturas (ºC para ºF)**

> Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

#### Conceitos-chave:
*   Função `input()` para ler a temperatura em Celsius.
*   Função `float()` para conversão.
*   Fórmula de conversão: `F = C * 9/5 + 32`.
*   Operadores aritméticos.
*   Função `print()` para exibir a temperatura em Fahrenheit.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 14.py correspondente.
```

#### Explicação:

O programa lerá uma temperatura em graus Celsius. Aplicará a fórmula de conversão `F = (C * 9/5) + 32` para calcular a temperatura equivalente em graus Fahrenheit.

#### Exemplo de Uso:
```
Digite a temperatura em °C: 30
A temperatura de 30.0°C corresponde a 86.0°F.
```

----

### **EXE_15: Aluguel de Carros**

> Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de dias pelas quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa **R$60** por dia e **R$0,15** por Km rodado.

#### Conceitos-chave:
*   Função `input()` para ler km e dias.
*   Funções `float()` e `int()` para conversões.
*   Operadores aritméticos (multiplicação `*`, adição `+`).
*   Função `print()` para exibir o preço total.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 15.py correspondente.
```

#### Explicação:

O programa solicitará a quantidade de dias que o carro foi alugado e a quantidade de quilômetros rodados. Calculará o custo dos dias (dias * R$60) e o custo dos quilômetros (km * R$0,15). O preço total será a soma desses dois custos.

#### Exemplo de Uso:
```
Por quantos dias o carro foi alugado? 5
Quantos Km foram percorridos? 350
O preço total a pagar é: R$352.50
```

----

### **EXE_16: Quebrando um Número Real**

> Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. **EX:Digite um número:6.127. O número 6.127 tem a parte interia 6.**

#### Conceitos-chave:
*   Função `input()` para ler o número real.
*   Função `float()` para conversão.
*   Módulo `math` e função `trunc()` (ou função `int()` para conversão direta).
*   Função `print()` para exibir a porção inteira.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 16.py correspondente.
```

#### Explicação:

O programa lerá um número real. Para obter a porção inteira, pode-se usar a função `trunc()` do módulo `math`, que remove a parte decimal, ou simplesmente converter o número para `int()`.

#### Exemplo de Uso:
```
Digite um número Real: 6.127
O número 6.127 tem a parte inteira 6.
```

----

### **EXE_17: Catetos e Hipotenusa**

> Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

#### Conceitos-chave:
*   Função `input()` para ler os catetos.
*   Função `float()` para conversão.
*   Módulo `math` e função `hypot()` ou `sqrt()` e `pow()`.
*   Teorema de Pitágoras: `hipotenusa² = cateto_oposto² + cateto_adjacente²`.
*   Função `print()` para exibir a hipotenusa.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 17.py correspondente.
```

#### Explicação:

O programa lerá os comprimentos dos dois catetos de um triângulo retângulo. Para calcular a hipotenusa, pode-se usar a função `math.hypot(cat_oposto, cat_adjacente)` ou aplicar o Teorema de Pitágoras: `hipotenusa = math.sqrt(math.pow(cat_oposto, 2) + math.pow(cat_adjacente, 2))`.

#### Exemplo de Uso:
```
Digite o comprimento do cateto oposto: 3.0
Digite o comprimento do cateto adjacente: 4.0
A hipotenusa vai medir: 5.0
```

----

### **EXE_18: Seno, Cosseno e Tangente**

> Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, casseno e tangente desse ângulo.

#### Conceitos-chave:
*   Função `input()` para ler o ângulo em graus.
*   Função `float()` para conversão.
*   Módulo `math` e funções `radians()`, `sin()`, `cos()`, `tan()`.
*   Função `print()` para exibir os resultados.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 18.py correspondente.
```

#### Explicação:

O programa lerá um ângulo em graus. Como as funções trigonométricas do módulo `math` esperam o ângulo em radianos, primeiro converteremos o ângulo de graus para radianos usando `math.radians()`. Em seguida, calcularemos o seno, cosseno e tangente usando `math.sin()`, `math.cos()` e `math.tan()`, respectivamente.

#### Exemplo de Uso:
```
Digite o ângulo (em graus): 30
Seno: 0.50
Cosseno: 0.87
Tangente: 0.58
(Valores aproximados)
```

----

### **EXE_19: Sorteando um Item na Lista**

> Um profressor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.

#### Conceitos-chave:
*   Função `input()` para ler os nomes dos alunos.
*   Listas para armazenar os nomes.
*   Módulo `random` e função `choice()`.
*   Função `print()` para exibir o nome sorteado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 19.py correspondente.
```

#### Explicação:

O programa solicitará o nome de quatro alunos. Esses nomes serão armazenados em uma lista. A função `random.choice()` será usada para selecionar aleatoriamente um nome da lista.

#### Exemplo de Uso:
```
Digite o nome do primeiro aluno: Ana
Digite o nome do segundo aluno: Bruno
Digite o nome do terceiro aluno: Carlos
Digite o nome do quarto aluno: Daniela
O aluno escolhido foi: Bruno 
(O resultado pode variar)
```

----

### **EXE_20: Sorteando uma Ordem na Lista**

> O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#### Conceitos-chave:
*   Função `input()` para ler os nomes.
*   Listas para armazenar os nomes.
*   Módulo `random` e função `shuffle()`.
*   Função `print()` para exibir a lista ordenada.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 20.py correspondente.
```

#### Explicação:

Similar ao exercício anterior, o programa lerá o nome dos quatro alunos e os armazenará em uma lista. A função `random.shuffle()` será usada para embaralhar a ordem dos elementos dentro da lista. A lista com a nova ordem será então exibida.

#### Exemplo de Uso:
```
Digite o nome do primeiro aluno: Ana
Digite o nome do segundo aluno: Bruno
Digite o nome do terceiro aluno: Carlos
Digite o nome do quarto aluno: Daniela
A ordem de apresentação será:
['Carlos', 'Ana', 'Daniela', 'Bruno']
(O resultado pode variar)
```

----

### **EXE_21: Tocando um MP3**

> Faça um programa em Python que abre e reproduza o áudio de um arquivo **MP3**.

#### Conceitos-chave:
*   Biblioteca `pygame` (ou outra biblioteca de áudio como `playsound`).
*   Inicialização do mixer do `pygame`.
*   Carregamento do arquivo MP3.
*   Comandos para tocar e esperar a música terminar.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 21.py correspondente.
# Exemplo usando pygame:
# import pygame
# pygame.init()
# pygame.mixer.music.load('nome_do_arquivo.mp3')
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#    pygame.time.Clock().tick(10)
```

#### Explicação:

Este programa requer uma biblioteca externa para manipulação de áudio, como o `pygame`. Primeiro, o `pygame` é inicializado. Em seguida, o mixer de música é usado para carregar o arquivo MP3 especificado. O comando `play()` inicia a reprodução, e um loop pode ser usado para manter o programa rodando enquanto a música toca.

#### Saída Esperada:

O programa irá reproduzir o som do arquivo MP3 especificado. Não haverá saída de texto, a menos que mensagens de status sejam adicionadas.

----

### Curso Python #09 - Manipulando Texto

----

### **EXE_22: Analisador de Textos**

> Crie um programa que leia o nome completo de uma pessoa e mostre:
>- O nome com todas as letras maiúsculas e minúsculas.
>- Quantas letras ao todo(sem considerar espaços).
>- Quantas letras tem o primeiro nome.

#### Conceitos-chave:
*   Função `input()` para ler o nome.
*   Métodos de string: `upper()`, `lower()`, `strip()`, `split()`.
*   Função `len()` para contar caracteres.
*   Função `print()` para exibir os resultados.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 22.py correspondente.
```

#### Explicação:

O programa lerá o nome completo. Para mostrar em maiúsculas e minúsculas, usará `nome.upper()` e `nome.lower()`. Para contar as letras sem espaços, pode-se remover os espaços e usar `len()` ou somar o `len()` de cada parte do nome. Para contar as letras do primeiro nome, usará `nome.split()` para dividir o nome em partes e pegará o `len()` da primeira parte.

#### Exemplo de Uso:
```
Digite seu nome completo: Ana Maria de Souza
Nome em maiúsculas: ANA MARIA DE SOUZA
Nome em minúsculas: ana maria de souza
Total de letras (sem espaços): 15
Letras no primeiro nome: 3
```

----

### **EXE_23: Separando Dígitos de um Número**

> Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. Ex: Digite um número:1834. unidade: 4 dezena: 3 centena: 8 milhar: 1

#### Conceitos-chave:
*   Função `input()` para ler o número como string ou int.
*   Operadores aritméticos (divisão inteira `//` e módulo `%`) se lido como int.
*   Indexação de string se lido como string.
*   Função `print()` para exibir os dígitos.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 23.py correspondente.
```

#### Explicação:

Se o número for lido como inteiro:
- Unidade: `numero % 10`
- Dezena: `(numero // 10) % 10`
- Centena: `(numero // 100) % 10`
- Milhar: `(numero // 1000) % 10`
Se lido como string (após garantir que tem 4 dígitos, preenchendo com zeros à esquerda se necessário):
- Unidade: `numero_str[3]`
- Dezena: `numero_str[2]`
- Centena: `numero_str[1]`
- Milhar: `numero_str[0]`

#### Exemplo de Uso:
```
Digite um número (0-9999): 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
```

----

### **EXE_24: Verificando as Primeiras Letras de um Texto**

> Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome **"SANTO"**.

#### Conceitos-chave:
*   Função `input()` para ler o nome da cidade.
*   Métodos de string: `strip()` para remover espaços extras, `upper()` para padronizar a caixa, `startswith()`.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 24.py correspondente.
```

#### Explicação:

O programa lerá o nome da cidade. Para fazer a verificação de forma robusta, é bom remover espaços no início e fim (`strip()`) e converter o nome da cidade para maiúsculas (`upper()`). Então, o método `startswith('SANTO')` verificará se a cidade começa com "SANTO".

#### Exemplo de Uso:
```
Digite o nome da cidade: Santo André
A cidade começa com "SANTO"? True

Digite o nome da cidade: São Paulo
A cidade começa com "SANTO"? False
```

----

### **EXE_25: Procurando uma String Dentro de Outra**

> Crie um programa que leia um nome de uma pessoa e diga se ela tem **"SILVA"** no nome.

#### Conceitos-chave:
*   Função `input()` para ler o nome.
*   Métodos de string: `upper()` para padronizar a caixa.
*   Operador `in` para verificar a existência de uma substring.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 25.py correspondente.
```

#### Explicação:

O programa lerá o nome de uma pessoa. Para tornar a busca insensível a maiúsculas/minúsculas, o nome lido pode ser convertido para maiúsculas (`nome.upper()`). Então, o operador `in` é usado para verificar se "SILVA" está contido no nome (`'SILVA' in nome.upper()`).

#### Exemplo de Uso:
```
Digite seu nome completo: João da Silva
Seu nome tem "SILVA"? True

Digite seu nome completo: Maria Oliveira
Seu nome tem "SILVA"? False
```

----

### **EXE_26: Primeira e Última Ocorrência de uma String**

> Faça um programa que leia uma frase pelo teclado e mostre:
>- Quantas vezes aparece a letra "A".
>- Em que posição ela aparece a primeira vez.
>- Em que posição aparece a última vez.

#### Conceitos-chave:
*   Função `input()` para ler a frase.
*   Métodos de string: `upper()` ou `lower()` para padronizar, `count()`, `find()`, `rfind()`.
*   Função `print()` para exibir os resultados.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 26.py correspondente.
```

#### Explicação:

O programa lerá uma frase. É recomendável converter a frase para maiúsculas ou minúsculas para a contagem e busca.
- `frase.upper().count('A')` contará as ocorrências de "A".
- `frase.upper().find('A')` encontrará a posição da primeira ocorrência (retorna -1 se não encontrar).
- `frase.upper().rfind('A')` encontrará a posição da última ocorrência (retorna -1 se não encontrar).

#### Exemplo de Uso:
```
Digite uma frase: Arara Azulada
A letra 'A' aparece 5 vezes.
A primeira ocorrência de 'A' está na posição: 0.
A última ocorrência de 'A' está na posição: 11.
```

----

### **EXE_27: Primeiro e Último Nome de uma Pessoa**

> Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza >- primeiro = Ana >- último = Souza

#### Conceitos-chave:
*   Função `input()` para ler o nome completo.
*   Métodos de string: `strip()`, `split()`.
*   Indexação de listas.
*   Função `print()` para exibir os nomes.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 27.py correspondente.
```

#### Explicação:

O programa lerá o nome completo. O método `strip()` pode ser usado para remover espaços extras nas extremidades. O método `split()` dividirá o nome em uma lista de palavras. O primeiro nome será o elemento no índice 0 da lista (`lista_nomes[0]`). O último nome será o elemento no último índice da lista (`lista_nomes[-1]` ou `lista_nomes[len(lista_nomes)-1]`).

#### Exemplo de Uso:
```
Digite seu nome completo: Ana Maria de Souza
Primeiro nome: Ana
Último nome: Souza
```

----

### Curso Python #10 - Condições (Parte 1)

----

### **EXE_28: Jogo da Adivinhação v.1.0**

> Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar desconbrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

#### Conceitos-chave:
*   Módulo `random` e função `randint()`.
*   Função `input()` para ler o palpite do usuário.
*   Função `int()` para converter o palpite.
*   Estrutura condicional `if/else`.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 28.py correspondente.
```

#### Explicação:

O computador escolherá um número aleatório entre 0 e 5 usando `random.randint(0, 5)`. O programa solicitará ao usuário um palpite. Se o palpite do usuário for igual ao número escolhido pelo computador, o usuário vence; caso contrário, perde.

#### Exemplo de Uso:
```
Vou pensar em um número entre 0 e 5. Tente adivinhar...
Qual é o seu palpite? 3
Pensei no número 3. Parabéns, você venceu! 
(Ou: Pensei no número X. Que pena, você perdeu!)
```

----

### **EXE_29: Radar Eletrônico**

> Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ela foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

#### Conceitos-chave:
*   Função `input()` para ler a velocidade.
*   Função `float()` ou `int()` para conversão.
*   Estrutura condicional `if`.
*   Operadores aritméticos para calcular a multa.
*   Função `print()` para exibir a mensagem e a multa, se houver.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 29.py correspondente.
```

#### Explicação:

O programa lerá a velocidade de um carro. Se a velocidade for maior que 80 Km/h, calculará o excesso de velocidade (velocidade - 80) e a multa (excesso * 7). Em seguida, exibirá uma mensagem informando que o motorista foi multado e o valor da multa.

#### Exemplo de Uso:
```
Digite a velocidade do carro (Km/h): 100
Você foi multado! Excedeu o limite de 80Km/h.
Valor da multa: R$140.00

Digite a velocidade do carro (Km/h): 70
Velocidade dentro do limite.
```

----

### **EXE_30: Par ou Ímpar?**

> Crie um programa que leia um número inteiro e mostre na tela se ela é **PAR** ou **INPAR**.

#### Conceitos-chave:
*   Função `input()` para ler o número.
*   Função `int()` para conversão.
*   Operador módulo `%`.
*   Estrutura condicional `if/else`.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 30.py correspondente.
```

#### Explicação:

O programa lerá um número inteiro. Para verificar se é par ou ímpar, usará o operador módulo (`%`). Se o resto da divisão do número por 2 for 0 (`numero % 2 == 0`), o número é par; caso contrário, é ímpar.

#### Exemplo de Uso:
```
Digite um número inteiro: 24
O número 24 é PAR.

Digite um número inteiro: 17
O número 17 é ÍMPAR.
```

----

### **EXE_31: Custo da Viagem**

> Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

#### Conceitos-chave:
*   Função `input()` para ler a distância.
*   Função `float()` para conversão.
*   Estrutura condicional `if/else`.
*   Operadores aritméticos.
*   Função `print()` para exibir o preço.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 31.py correspondente.
```

#### Explicação:

O programa lerá a distância da viagem. Se a distância for até 200 Km, o preço será `distancia * 0.50`. Se for maior que 200 Km, o preço será `distancia * 0.45`.

#### Exemplo de Uso:
```
Digite a distância da viagem (Km): 150
O preço da passagem é: R$75.00

Digite a distância da viagem (Km): 300
O preço da passagem é: R$135.00
```

----

### **EXE_32: Ano Bissexto**

> Faça um programa que leia um ano qualquer e mostre se ele é **BISSEXTO**.

#### Conceitos-chave:
*   Função `input()` para ler o ano.
*   Função `int()` para conversão.
*   Operador módulo `%`.
*   Estruturas condicionais aninhadas ou operadores lógicos (`and`, `or`).
*   Regras do ano bissexto: divisível por 4, mas não por 100, a menos que seja divisível por 400.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 32.py correspondente.
```

#### Explicação:

O programa lerá um ano. Para verificar se é bissexto, aplicará as seguintes regras:
1. É divisível por 4 E (não é divisível por 100 OU é divisível por 400).
   `(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)`

#### Exemplo de Uso:
```
Digite um ano: 2024
O ano 2024 é BISSEXTO.

Digite um ano: 1900
O ano 1900 NÃO é BISSEXTO.

Digite um ano: 2000
O ano 2000 é BISSEXTO.
```

----

### **EXE_33: Maior e Menor Valores**

> Faça um programa que leia três número e mostre qual é o maior e qual é o menor.

#### Conceitos-chave:
*   Função `input()` para ler os três números.
*   Função `int()` ou `float()` para conversão.
*   Estruturas condicionais `if/elif/else`.
*   Função `print()` para exibir o maior e o menor.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 33.py correspondente.
```

#### Explicação:

O programa lerá três números. Uma forma de resolver é assumir que o primeiro número é o maior e o menor inicialmente. Depois, comparar com o segundo número e atualizar o maior e o menor se necessário. Repetir o processo para o terceiro número. Alternativamente, usar uma série de `if` e `elif` para todas as comparações possíveis.

#### Exemplo de Uso:
```
Digite o primeiro número: 15
Digite o segundo número: 7
Digite o terceiro número: 22
Maior número: 22
Menor número: 7
```

----

### **EXE_34: Aumentos Múltiplos**

> Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00 , calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#### Conceitos-chave:
*   Função `input()` para ler o salário.
*   Função `float()` para conversão.
*   Estrutura condicional `if/else`.
*   Cálculo de porcentagem e operadores aritméticos.
*   Função `print()` para exibir o novo salário.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 34.py correspondente.
```

#### Explicação:

O programa lerá o salário do funcionário. Se o salário for maior que R$1250,00, o aumento será de 10% (`salario * 10 / 100`). Caso contrário (salário menor ou igual a R$1250,00), o aumento será de 15% (`salario * 15 / 100`). O novo salário será o salário original mais o aumento calculado.

#### Exemplo de Uso:
```
Digite o salário do funcionário: R$1500.00
Seu novo salário com 10% de aumento é: R$1650.00

Digite o salário do funcionário: R$1000.00
Seu novo salário com 15% de aumento é: R$1150.00
```

----

### **EXE_35: Analisando Triângulo v1.0**

> Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#### Conceitos-chave:
*   Função `input()` para ler os comprimentos das retas.
*   Função `float()` para conversão.
*   Desigualdade triangular: a soma de quaisquer dois lados deve ser maior que o terceiro lado.
*   Estrutura condicional `if/else` e operadores lógicos `and`.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 35.py correspondente.
```

#### Explicação:

O programa lerá o comprimento de três retas (r1, r2, r3). Para que formem um triângulo, a seguinte condição deve ser verdadeira (desigualdade triangular):
(r1 + r2 > r3) E (r1 + r3 > r2) E (r2 + r3 > r1).
Se a condição for atendida, as retas podem formar um triângulo; caso contrário, não.

#### Exemplo de Uso:
```
Digite o comprimento da primeira reta: 7
Digite o comprimento da segunda reta: 10
Digite o comprimento da terceira reta: 5
As retas PODEM FORMAR um triângulo.

Digite o comprimento da primeira reta: 12
Digite o comprimento da segunda reta: 3
Digite o comprimento da terceira reta: 8
As retas NÃO PODEM FORMAR um triângulo.
```

----

### Curso Python #011 - Cores no Terminal

----

## **Mundo 2 [40 Horas]**

----

### Curso Python #012 - Condições Aninhadas 

----

### **EXE_36: Aprovando Empréstimo Bancário**

> Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode execeder 30% do salário ou então o empréstimo será negado.

#### Conceitos-chave:
*   Função `input()` para ler valor da casa, salário e anos.
*   Funções `float()` e `int()` para conversões.
*   Cálculo da prestação mensal: `valor_casa / (anos * 12)`.
*   Cálculo do limite da prestação: `salario * 30 / 100`.
*   Estrutura condicional `if/else`.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 36.py correspondente.
```

#### Explicação:

O programa coleta o valor da casa, o salário do comprador e o número de anos para pagamento. Calcula o valor da prestação mensal. Verifica se essa prestação excede 30% do salário do comprador. Se não exceder, o empréstimo é aprovado; caso contrário, é negado.

#### Exemplo de Uso:
```
Valor da casa: R$120000
Salário do comprador: R$3000
Anos para pagar: 10
Prestação mensal: R$1000.00
Limite da prestação (30% do salário): R$900.00
Empréstimo NEGADO.

Valor da casa: R$100000
Salário do comprador: R$4000
Anos para pagar: 10
Prestação mensal: R$833.33
Limite da prestação (30% do salário): R$1200.00
Empréstimo APROVADO.
```

----

### **EXE_37: Conversor de Bases Numéricas**

> Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal.

#### Conceitos-chave:
*   Função `input()` para ler o número e a opção de conversão.
*   Função `int()` para conversões.
*   Funções `bin()`, `oct()`, `hex()` para conversão de bases.
*   Fatiamento de strings para remover prefixos (ex: `[2:]`).
*   Estrutura condicional `if/elif/else`.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 37.py correspondente.
```

#### Explicação:

O programa lê um número inteiro e a base de conversão desejada. Utiliza as funções `bin()`, `oct()` ou `hex()` conforme a escolha do usuário. O resultado dessas funções inclui um prefixo ("0b", "0o", "0x") que geralmente é removido usando fatiamento de string antes da exibição.

#### Exemplo de Uso:
```
Digite um número inteiro: 255
Escolha a base de conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
Sua opção: 1
255 em Binário é: 11111111
```

----

### **EXE_38: Comparando Números**

> Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior, O segundo valor é maior, Não existe valor maior, os dois são iguais.

#### Conceitos-chave:
*   Função `input()` para ler os dois números.
*   Função `int()` para conversão.
*   Estrutura condicional `if/elif/else`.
*   Operadores relacionais (`>`, `<`, `==`).
*   Função `print()` para exibir a comparação.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 38.py correspondente.
```

#### Explicação:

O programa lê dois números inteiros. Compara-os usando operadores relacionais para determinar se o primeiro é maior, se o segundo é maior, ou se são iguais, e exibe a mensagem correspondente.

#### Exemplo de Uso:
```
Digite o primeiro número: 10
Digite o segundo número: 5
O primeiro valor é maior.

Digite o primeiro número: 7
Digite o segundo número: 7
Não existe valor maior, os dois são iguais.
```

----

### **EXE_39: Alistamento Militar**

> Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistare ao seviço militar. Seu programa também deverá mostra o tempo que falta ou que passou do prazo.

#### Conceitos-chave:
*   Função `input()` para ler o ano de nascimento.
*   Módulo `datetime` para obter o ano atual (`datetime.date.today().year`).
*   Cálculo da idade.
*   Estrutura condicional `if/elif/else`.
*   Função `print()` para exibir a situação do alistamento.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 39.py correspondente.
```

#### Explicação:

O programa lê o ano de nascimento do jovem e calcula sua idade com base no ano atual. Se a idade for menor que 18, informa quanto tempo falta para o alistamento. Se a idade for 18, informa que é hora de se alistar. Se for maior que 18, informa quanto tempo passou do prazo de alistamento.

#### Exemplo de Uso:
```
Ano de nascimento: 2006
Idade: 18 anos em AAAA (ano atual)
É hora de se alistar!

Ano de nascimento: 2008
Idade: 16 anos em AAAA (ano atual)
Ainda faltam 2 anos para o alistamento.

Ano de nascimento: 2000
Idade: 24 anos em AAAA (ano atual)
Você já deveria ter se alistado há 6 anos.
```

----

### **EXE_40: Média com Status**

> Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atigida: Média abaixo de 5.0: REPROVADO, Média entre 5.0 e 6.9: RECUPERAÇÃO, Média 7.0 ou superior: APROVADO.

#### Conceitos-chave:
*   Função `input()` para ler as notas.
*   Função `float()` para conversão.
*   Cálculo da média.
*   Estrutura condicional `if/elif/else`.
*   Função `print()` para exibir a média e o status.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 40.py correspondente.
```

#### Explicação:

O programa lê duas notas, calcula a média e, com base na média, classifica o aluno como REPROVADO, EM RECUPERAÇÃO ou APROVADO.

#### Exemplo de Uso:
```
Primeira nota: 4.5
Segunda nota: 5.0
Média: 4.75
Status: REPROVADO
```

----

### **EXE_41: Classificando Atletas**

> A Confederação Nacional de Notação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: Até 9 anos: MIRIN, Até 14 anos: INFANTIL, Até 19 anos: JUNIOR, Até 25 anos: SÉNIOR, Acima: MASTER.

#### Conceitos-chave:
*   Função `input()` para ler o ano de nascimento.
*   Módulo `datetime` para obter o ano atual.
*   Cálculo da idade.
*   Estrutura condicional `if/elif/else` aninhada ou sequencial.
*   Função `print()` para exibir a categoria.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 41.py correspondente.
```

#### Explicação:

O programa calcula a idade do atleta e o classifica em uma categoria (MIRIM, INFANTIL, JUNIOR, SÊNIOR, MASTER) com base em faixas etárias definidas.

#### Exemplo de Uso:
```
Ano de nascimento do atleta: 2010
Idade: 14 anos em AAAA (ano atual)
Categoria: INFANTIL
```

----

### **EXE_42: Analisando Triângulos v2.0**

> Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, ESCALENO: todos os lados diferentes.

#### Conceitos-chave:
*   Reutilização da lógica do EXE_35 (verificar se forma triângulo).
*   Estrutura condicional `if/elif/else` para classificar o tipo de triângulo.
*   Comparação dos lados para determinar o tipo.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 42.py correspondente.
```

#### Explicação:

Primeiro, o programa verifica se os três lados informados podem formar um triângulo (usando a desigualdade triangular do EXE_35). Se puderem, ele então compara os lados para determinar se o triângulo é EQUILÁTERO (todos os lados iguais), ISÓSCELES (dois lados iguais) ou ESCALENO (todos os lados diferentes).

#### Exemplo de Uso:
```
Digite o comprimento da primeira reta: 7
Digite o comprimento da segunda reta: 7
Digite o comprimento da terceira reta: 10
As retas PODEM FORMAR um triângulo ISÓSCELES.
```

----

### **EXE_43: Cálculo de IMC**

> Desenvolva uma lógico que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5:Abaixo do peso, Entre 18.5 e 25:Peso ideal, 25 até 30:Sobrepeso, 30 até 40:Obesidade, Acima de 40:Obesidade mórbida.

#### Conceitos-chave:
*   Função `input()` para ler peso e altura.
*   Função `float()` para conversão.
*   Fórmula do IMC: `peso / (altura ** 2)`.
*   Estrutura condicional `if/elif/else`.
*   Função `print()` para exibir o IMC e o status.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 43.py correspondente.
```

#### Explicação:

O programa calcula o Índice de Massa Corporal (IMC) a partir do peso e altura fornecidos. Em seguida, classifica o status da pessoa com base em faixas de IMC.

#### Exemplo de Uso:
```
Digite seu peso (Kg): 70
Digite sua altura (m): 1.75
Seu IMC é: 22.86
Status: Peso ideal
```

----

### **EXE_44: Gerenciador de Pagamentos**

> Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: Á vista dinheiro/cheque: 10% de desconto, Á vista no cartão: 5% de desconto, Em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.

#### Conceitos-chave:
*   Função `input()` para ler o preço e a condição de pagamento.
*   Estrutura condicional `if/elif/else`.
*   Cálculo de descontos e juros.
*   Função `print()` para exibir o valor final.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 44.py correspondente.
```

#### Explicação:

O programa lê o preço do produto e a opção de pagamento. Aplica descontos ou juros conforme a opção escolhida e calcula o valor final a ser pago.

#### Exemplo de Uso:
```
Preço do produto: R$100.00
Opções de pagamento:
1 - À vista dinheiro/cheque (10% desconto)
2 - À vista cartão (5% desconto)
3 - Em até 2x no cartão (preço normal)
4 - 3x ou mais no cartão (20% juros)
Escolha a opção: 1
Valor a pagar: R$90.00
```

----

### **EXE_45: Jokenpô (Pedra, Papel e Tesoura)**

> Crie um programa que façã o computador jogar Jokenpô com você.

#### Conceitos-chave:
*   Módulo `random` (função `choice()` ou `randint()`).
*   Função `input()` para a jogada do usuário.
*   Representação das jogadas (ex: 0 para Pedra, 1 para Papel, 2 para Tesoura).
*   Lógica de vitória/derrota/empate no Jokenpô.
*   Estruturas condicionais.
*   Função `print()` para exibir as jogadas e o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 45.py correspondente.
```

#### Explicação:

O computador escolhe aleatoriamente entre Pedra, Papel e Tesoura. O usuário insere sua jogada. O programa compara as jogadas para determinar o vencedor com base nas regras do Jokenpô.

#### Exemplo de Uso:
```
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? 0
Computador jogou PAPEL.
Você PERDEU! Papel embrulha Pedra.
```

----

### Curso Python #13 - Estrutura de repetição for

----

### **EXE_46: Contagem Regressiva**

> Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#### Conceitos-chave:
*   Laço `for` com `range()` (ex: `range(10, -1, -1)`).
*   Módulo `time` e função `sleep(1)`.
*   Função `print()` para mostrar os números e a mensagem final.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 46.py correspondente.
```

#### Explicação:

O programa usa um laço `for` para contar de 10 até 0. A cada número, ele o exibe na tela e pausa por 1 segundo usando `time.sleep(1)`. Ao final da contagem, exibe uma mensagem indicando o estouro dos fogos.

#### Saída Esperada:
```
10
9
8
7
6
5
4
3
2
1
0
BUM! POW! ESTOURO!
```

----

### **EXE_47: Contagem de Pares**

> Crie uma programa que mostre ma tela todos os números pares que estão no intervalo entre 1 e 50.

#### Conceitos-chave:
*   Laço `for` com `range()`.
*   Operador módulo `%` para verificar se é par (`numero % 2 == 0`).
*   Função `print()` para exibir os números pares.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 47.py correspondente.
# Alternativa: for i in range(2, 51, 2): print(i)
```

#### Explicação:

O programa itera pelos números no intervalo de 1 a 50. Para cada número, verifica se ele é par (resto da divisão por 2 é igual a 0). Se for par, o número é exibido. Uma forma mais eficiente é usar `range(2, 51, 2)` para iterar diretamente pelos pares.

#### Saída Esperada:
```
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 
```

----

### **EXE_48: Soma Ímpares Múltiplos de Três**

> Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#### Conceitos-chave:
*   Laço `for` com `range()`.
*   Operador módulo `%` para verificar se é ímpar e se é múltiplo de três.
*   Variável acumuladora para a soma.
*   Função `print()` para exibir a soma.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 48.py correspondente.
```

#### Explicação:

O programa itera de 1 a 500. Para cada número, verifica se é ímpar (`numero % 2 != 0`) E se é múltiplo de três (`numero % 3 == 0`). Se ambas as condições forem verdadeiras, o número é adicionado a uma variável que acumula a soma.

#### Saída Esperada:
```
A soma de todos os números ímpares múltiplos de três entre 1 e 500 é: XXXXX
(O valor XXXXX será o resultado da soma)
```

----

### **EXE_49: Tabuada v.2.0**

> Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#### Conceitos-chave:
*   Função `input()` para ler o número.
*   Laço `for` com `range(1, 11)`.
*   Função `print()` para formatar a saída da tabuada.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 49.py correspondente.
```

#### Explicação:

Este é uma variação do EXE_09, mas a ênfase é no uso do laço `for`. O programa lê um número e usa um `for` para iterar de 1 a 10, exibindo a multiplicação do número pelo iterador em cada passo.

#### Exemplo de Uso:
```
Digite um número para ver sua tabuada: 5
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
```

----

### **EXE_50: Soma dos Pares**

> Desenvolva um programa que leia seis números inteiros e mostrea soma apenas daqueles que foram pares. Se o valor digitado for impar, desconsidere-o.

#### Conceitos-chave:
*   Laço `for` para ler os seis números (ex: `for _ in range(6):`).
*   Função `input()` dentro do laço.
*   Operador módulo `%` para verificar se é par.
*   Variável acumuladora para a soma dos pares.
*   Função `print()` para exibir a soma.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 50.py correspondente.
```

#### Explicação:

O programa usa um laço para solicitar seis números inteiros. Dentro do laço, cada número lido é verificado. Se for par, é adicionado a uma soma acumulada. Números ímpares são ignorados.

#### Exemplo de Uso:
```
Digite o 1º número: 3
Digite o 2º número: 4
Digite o 3º número: 5
Digite o 4º número: 6
Digite o 5º número: 7
Digite o 6º número: 8
A soma dos números pares digitados é: 18 (4 + 6 + 8)
```

----

### **EXE_51: Progressão Aritmética v1.0**

> Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#### Conceitos-chave:
*   Função `input()` para ler o primeiro termo e a razão.
*   Laço `for` com `range(10)` para gerar os 10 termos.
*   Fórmula do termo geral da PA: `termo_n = primeiro_termo + (n-1) * razao`.
*   Função `print()` para exibir os termos.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 51.py correspondente.
```

#### Explicação:

O programa lê o primeiro termo (a1) e a razão (r) de uma Progressão Aritmética. Em seguida, usa um laço `for` para calcular e exibir os 10 primeiros termos. O n-ésimo termo pode ser calculado como `a1 + (i) * r` onde `i` vai de 0 a 9.

#### Exemplo de Uso:
```
Primeiro termo da PA: 2
Razão da PA: 3
Os 10 primeiros termos da PA são:
2 5 8 11 14 17 20 23 26 29 
```

----

### **EXE_52: Números Primos**

> Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#### Conceitos-chave:
*   Função `input()` para ler o número.
*   Laço `for` para testar divisores (de 2 até a raiz quadrada do número, ou até `numero - 1`).
*   Operador módulo `%` para verificar divisibilidade.
*   Contador de divisores ou uma flag booleana.
*   Condições para ser primo (divisível apenas por 1 e por ele mesmo).
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 52.py correspondente.
```

#### Explicação:

O programa lê um número inteiro. Para verificar se é primo, conta quantos divisores ele tem no intervalo de 1 até o próprio número. Um número primo tem exatamente dois divisores (1 e ele mesmo). Casos especiais como 0, 1 devem ser tratados. Uma otimização é testar divisores apenas até a raiz quadrada do número.

#### Exemplo de Uso:
```
Digite um número inteiro: 7
O número 7 É PRIMO.

Digite um número inteiro: 10
O número 10 NÃO É PRIMO.
```

----

### **EXE_53: Detector de Palíndromo**

> Crie um programa que leia uma frase qualquer e diga se ela é um **polindromo, desconsiderando os espaços.

#### Conceitos-chave:
*   Função `input()` para ler a frase.
*   Métodos de string: `replace(" ", "")` para remover espaços, `lower()` ou `upper()` para padronizar.
*   Fatiamento de string para inverter a frase (ex: `frase_invertida = frase_sem_espacos[::-1]`).
*   Comparação da string original (tratada) com sua versão invertida.
*   Função `print()` para exibir o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 53.py correspondente.
```

#### Explicação:

O programa lê uma frase. Remove os espaços e converte para uma única caixa (maiúscula ou minúscula). Em seguida, compara a frase tratada com sua versão invertida. Se forem iguais, é um palíndromo.

#### Exemplo de Uso:
```
Digite uma frase: APOS A SOPA
A frase É UM PALÍNDROMO.

Digite uma frase: ANA
A frase É UM PALÍNDROMO.

Digite uma frase: PYTHON
A frase NÃO É UM PALÍNDROMO.
```

----

### **EXE_54: Grupo da Maioridade**

> Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#### Conceitos-chave:
*   Laço `for` para ler os sete anos de nascimento.
*   Módulo `datetime` para obter o ano atual.
*   Cálculo da idade.
*   Contadores para maiores e menores de idade (considerando 18 anos como maioridade).
*   Função `print()` para exibir os totais.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 54.py correspondente.
```

#### Explicação:

O programa lê o ano de nascimento de sete pessoas. Para cada pessoa, calcula a idade. Mantém dois contadores: um para os que têm 18 anos ou mais (maiores) e outro para os menores de 18 anos.

#### Exemplo de Uso:
```
Digite o ano de nascimento da 1ª pessoa: 2000
Digite o ano de nascimento da 2ª pessoa: 2010
... (até a 7ª pessoa)
Total de pessoas maiores de idade: X
Total de pessoas menores de idade: Y
```

----

### **EXE_55: Maior e Menor da Sequência**

> Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior peso lido. (O enunciado original pede apenas o maior, mas é comum pedir maior e menor).

#### Conceitos-chave:
*   Laço `for` para ler os cinco pesos.
*   Variáveis para armazenar o maior e o menor peso lidos até o momento.
*   Inicialização adequada dessas variáveis (ex: com o primeiro peso lido, ou com valores extremos).
*   Função `print()` para exibir o maior (e menor) peso.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 55.py correspondente.
```

#### Explicação:

O programa lê o peso de cinco pessoas. Durante a leitura, compara cada peso com o maior e o menor peso registrados até então, atualizando-os se necessário. O primeiro peso lido pode inicializar ambas as variáveis (maior e menor).

#### Exemplo de Uso:
```
Digite o peso da 1ª pessoa (Kg): 75.5
Digite o peso da 2ª pessoa (Kg): 60.2
Digite o peso da 3ª pessoa (Kg): 88.0
Digite o peso da 4ª pessoa (Kg): 55.9
Digite o peso da 5ª pessoa (Kg): 70.1
Maior peso lido: 88.0 Kg
Menor peso lido: 55.9 Kg
```

----

### **EXE_56: Analisador Completo**

> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo, Qual é o nome do homen mais velho, Quantas mulheres têm menos de 20 anos.

#### Conceitos-chave:
*   Laço `for` para ler os dados das 4 pessoas.
*   Variáveis para acumular a soma das idades, armazenar o nome e idade do homem mais velho, e contar mulheres com menos de 20 anos.
*   Estruturas condicionais para as verificações.
*   Função `print()` para exibir os resultados.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 56.py correspondente.
```

#### Explicação:

O programa coleta nome, idade e sexo de 4 pessoas. Calcula a média de idade. Identifica o homem mais velho e seu nome. Conta quantas mulheres têm menos de 20 anos.

#### Exemplo de Uso:
```
---- 1ª PESSOA ----
Nome: Ana
Idade: 22
Sexo [M/F]: F
---- 2ª PESSOA ----
Nome: Bruno
Idade: 30
Sexo [M/F]: M
... (até a 4ª pessoa)
A média de idade do grupo é de XX.X anos.
O homem mais velho tem YY anos e se chama ZZZZ.
Ao todo são WW mulheres com menos de 20 anos.
```

----

### Curso Python #14 - Estrutura de repetição while

----

### **EXE_57: Validação de Dados**

> Faça um programa que leia o sexo de uma pessoam, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor corrento.

#### Conceitos-chave:
*   Laço `while` para repetição até entrada válida.
*   Função `input()` para ler o sexo.
*   Métodos de string `upper()`, `strip()`.
*   Condição de parada do laço.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 57.py correspondente.
```

#### Explicação:

O programa solicita a entrada do sexo (M/F). Um laço `while` continua pedindo a entrada enquanto o valor digitado não for 'M' ou 'F' (após tratamento como `upper()` e `strip()`).

#### Exemplo de Uso:
```
Digite seu sexo [M/F]: G
Dado inválido. Digite novamente: M
Sexo M registrado com sucesso.
```

----

### **EXE_58: Jogo da Adivinhação v.2.0**

> Melhore o jogo do **DESAFIO 028** onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jagador vai tentar adivinhar até acertar, mostrando no final quando palpites foram necessário para vencer.

#### Conceitos-chave:
*   Módulo `random` (`randint()`).
*   Laço `while` para continuar até o jogador acertar.
*   Contador de palpites.
*   Condicionais para dar dicas (maior/menor) são opcionais mas melhoram o jogo.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 58.py correspondente.
```

#### Explicação:

O computador escolhe um número entre 0 e 10. O jogador tenta adivinhar. O laço `while` continua até o palpite ser correto. Um contador registra o número de tentativas.

#### Exemplo de Uso:
```
Pensei em um número entre 0 e 10. Tente adivinhar!
Qual seu palpite? 5
Errou! Tente um número maior.
Qual seu palpite? 8
Acertou! Você precisou de 2 palpites.
```

----

### **EXE_59: Menu de Opções**

> Crie um programa que leia dois valores e mostre um menu como o abaixo: Seu programa deverá realizar a operação solicitada em cada caso. >- [ 1 ] Somar >- [ 2 ] Multiplicar >- [ 3 ] Maior >- [ 4 ] Novos númeos >- [ 5 ] Sair do programa

#### Conceitos-chave:
*   Laço `while` para manter o menu ativo até a opção de sair.
*   Função `input()` para ler os números e a opção do menu.
*   Estruturas condicionais `if/elif/else` para tratar as opções.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 59.py correspondente.
```

#### Explicação:

O programa lê dois valores. Entra em um laço `while` que exibe um menu de operações. Conforme a opção escolhida pelo usuário, realiza a operação (somar, multiplicar, identificar o maior, permitir novos números ou sair). O laço termina quando a opção "sair" é escolhida.

#### Exemplo de Uso:
```
Digite o primeiro valor: 10
Digite o segundo valor: 5
--- MENU ---
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Sua opção: 1
A soma é 15.
--- MENU ---
...
Sua opção: 5
Saindo...
```

----

### **EXE_60: Cálculo do Fatorial**

> Faça um programa que leia número qualquer e mostre o seu fatorial. Ex: 5!=5x4x3x2x1 = 120

#### Conceitos-chave:
*   Função `input()` para ler o número.
*   Laço `while` (ou `for`) para calcular o fatorial.
*   Variável acumuladora para o resultado do fatorial.
*   Módulo `math` e função `factorial()` como alternativa.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 60.py correspondente.
```

#### Explicação:

O programa lê um número. Para calcular o fatorial, multiplica o número por todos os seus antecessores positivos até 1. (Ex: 5! = 5 * 4 * 3 * 2 * 1). Isso pode ser feito com um laço `while` ou `for` decrementando.

#### Exemplo de Uso:
```
Digite um número para calcular seu fatorial: 5
Calculando 5! = 5 x 4 x 3 x 2 x 1 = 120
```

----

### **EXE_61: Progressão Aritmética v2.0**

> Refaça o **Desafio 051**, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#### Conceitos-chave:
*   Função `input()` para ler o primeiro termo e a razão.
*   Laço `while` para gerar os termos.
*   Variável para controlar o termo atual e um contador para os 10 termos.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 61.py correspondente.
```

#### Explicação:

Similar ao EXE_51, mas usando `while`. O programa lê o primeiro termo e a razão. Um laço `while` é usado para calcular e exibir os 10 primeiros termos, atualizando o termo atual somando a razão a cada passo, e usando um contador para controlar o número de termos exibidos.

#### Exemplo de Uso:
```
Primeiro termo da PA: 2
Razão da PA: 3
Os 10 primeiros termos da PA são:
2 -> 5 -> 8 -> 11 -> 14 -> 17 -> 20 -> 23 -> 26 -> 29 -> FIM
```

----

### **EXE_62: Super Progressão Aritmética v3.0**

> Melhore o **Desafio 061**, perguntando para o suruário se ele quer mostrer mais alguns termos. O programa encerra quando ele disser que quer mostrar O termos.

#### Conceitos-chave:
*   Reutilização da lógica do EXE_61.
*   Laço `while` aninhado ou modificado para perguntar por mais termos.
*   Entrada do usuário para decidir quantos termos a mais ou se quer sair (0 termos).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 62.py correspondente.
```

#### Explicação:

Baseado no EXE_61, após mostrar os 10 primeiros termos (ou a quantidade solicitada), o programa pergunta ao usuário quantos termos adicionais ele deseja ver. Se o usuário digitar um número maior que 0, mais termos são mostrados. Se digitar 0, o programa encerra.

#### Exemplo de Uso:
```
Primeiro termo da PA: 2
Razão da PA: 3
2 -> 5 -> 8 -> 11 -> 14 -> 17 -> 20 -> 23 -> 26 -> 29 -> PAUSA
Quantos termos você quer mostrar a mais? 3
32 -> 35 -> 38 -> PAUSA
Quantos termos você quer mostrar a mais? 0
Progressão finalizada com X termos mostrados.
```

----

### **EXE_63: Sequência de Fibonacci v1.0**

> Escreva um programa que leia um número **n** inteiro qualquer e mostre na tela os **n** primeiros elementos de uma sequência de Fibonacci. Ex 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

#### Conceitos-chave:
*   Função `input()` para ler `n`.
*   Laço `while` (ou `for`) para gerar `n` termos.
*   Variáveis para armazenar os dois últimos termos da sequência para calcular o próximo.
*   Lógica da Sequência de Fibonacci: o próximo termo é a soma dos dois anteriores.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 63.py correspondente.
```

#### Explicação:

O programa lê `n`. Inicia a sequência com os dois primeiros termos (0 e 1). Em um laço, calcula o próximo termo somando os dois anteriores, exibe o termo, e atualiza as variáveis que guardam os dois últimos termos. Repete até `n` termos serem mostrados.

#### Exemplo de Uso:
```
Quantos termos da sequência de Fibonacci você quer mostrar? 7
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 
```

----

### **EXE_64: Tratando Vários Valores v1.0**

> Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parado. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando flag).

#### Conceitos-chave:
*   Laço `while True` com `break`.
*   Função `input()` dentro do laço.
*   Condição de parada (número == 999).
*   Contador para a quantidade de números e acumulador para a soma.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 64.py correspondente.
```

#### Explicação:

O programa entra em um laço infinito que lê números inteiros. Se o número digitado for 999 (flag de parada), o laço é interrompido. Caso contrário, o número é somado a um acumulador e um contador de números é incrementado. No final, exibe a quantidade de números digitados e a soma total.

#### Exemplo de Uso:
```
Digite um número [999 para parar]: 5
Digite um número [999 para parar]: 10
Digite um número [999 para parar]: 3
Digite um número [999 para parar]: 999
Foram digitados 3 números.
A soma entre eles é 18.
```

----

### **EXE_65: Maior e Menor Valores com Continuação**

> Crie um programa que leia vários números inteiros pelo teclado. No final de execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

#### Conceitos-chave:
*   Laço `while` controlado por uma flag de continuação (ex: `while continuar == 'S':`).
*   Variáveis para maior, menor, soma e contador.
*   `input()` para ler os números e a opção de continuar.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 65.py correspondente.
```

#### Explicação:

O programa lê números inteiros em um laço. A cada número, atualiza o maior, o menor, a soma e o contador. Após cada número, pergunta ao usuário se deseja continuar. Quando o usuário decide parar, o programa calcula e exibe a média, o maior e o menor valor.

#### Exemplo de Uso:
```
Digite um número: 10
Quer continuar? [S/N] S
Digite um número: 5
Quer continuar? [S/N] S
Digite um número: 15
Quer continuar? [S/N] N
Você digitou 3 números.
Média: 10.0
Maior valor: 15
Menor valor: 5
```

----

### Curso Python #15 - Interrompendo repetições while

----

### **EXE_66: Vários Números com Flag (Interrupção)**

>  Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condiçõe de parada. No final, mostre quantos números foram digitado e qual foi a soma entre eles(desconsiderando o flag).

#### Conceitos-chave:
*   Laço `while True`.
*   `input()` para ler o número.
*   Condicional `if numero == 999: break`.
*   Acumulador para soma e contador para quantidade (fora do `if` do break).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 66.py correspondente.
```

#### Explicação:

Este exercício é muito similar ao EXE_64, mas a ênfase é no uso do `break` para interromper um laço `while True` quando a flag (999) é digitada. A soma e a contagem ocorrem antes da verificação da flag.

#### Exemplo de Uso:
```
Digite um valor (999 para parar): 8
Digite um valor (999 para parar): 2
Digite um valor (999 para parar): 5
Digite um valor (999 para parar): 999
Foram digitados 3 valores. A soma é 15.
```

----

### **EXE_67: Tabuada v.3.0 (Interrupção Negativa)**

> Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

#### Conceitos-chave:
*   Laço `while True`.
*   `input()` para ler o número para a tabuada.
*   Condicional `if numero < 0: break`.
*   Laço `for` aninhado para gerar a tabuada do número (de 1 a 10).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 67.py correspondente.
```

#### Explicação:

O programa entra em um laço infinito, solicitando um número ao usuário. Se o número for negativo, o laço é interrompido. Caso contrário, a tabuada desse número (de 1 a 10) é exibida usando um laço `for` interno.

#### Exemplo de Uso:
```
Quer ver a tabuada de qual valor? 7
7 x 1 = 7
...
7 x 10 = 70
Quer ver a tabuada de qual valor? 3
3 x 1 = 3
...
3 x 10 = 30
Quer ver a tabuada de qual valor? -1
PROGRAMA TABUADA ENCERRADO. Volte sempre!
```

----

### **EXE_68: Jogo do Par ou Ímpar**

> Faça um programa que jogue **par ou impar** com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#### Conceitos-chave:
*   Laço `while True`.
*   `random.randint()` para a escolha do computador.
*   `input()` para a escolha do jogador (número e 'P' ou 'I').
*   Lógica para determinar se a soma é par ou ímpar.
*   Condicional para verificar se o jogador ganhou ou perdeu.
*   Contador de vitórias consecutivas.
*   `break` quando o jogador perde.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 68.py correspondente.
```

#### Explicação:

Em um laço, o jogador escolhe um número e se aposta em Par ou Ímpar. O computador escolhe um número. A soma é calculada. Verifica-se se o resultado é par ou ímpar e compara com a aposta do jogador. Se o jogador acertar, o contador de vitórias aumenta e o jogo continua. Se errar, o jogo é interrompido e o total de vitórias é mostrado.

#### Exemplo de Uso:
```
Vamos jogar PAR ou ÍMPAR!
Digite um valor: 3
Par ou Ímpar? [P/I] P
Você jogou 3 e o computador 2. Total 5 (ÍMPAR).
Você PERDEU!
GAME OVER! Você venceu 0 vezes.

(Se o jogador ganhar algumas vezes)
...
Você jogou X e o computador Y. Total Z (PAR/ÍMPAR).
Você VENCEU!
Vamos jogar novamente...
...
GAME OVER! Você venceu K vezes.
```

----

### **EXE_69: Análise de Dados do Grupo**

> Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A ) Quantoas pessoas tem mais de 18 anos. B ) Quantos homens foram cadastrados. C ) Quantas mulheres tem menos de 20 anos.

#### Conceitos-chave:
*   Laço `while True` ou `while continuar == 'S'`.
*   `input()` para ler idade, sexo e a opção de continuar.
*   Contadores para: pessoas > 18 anos, homens, mulheres < 20 anos.
*   Validação da entrada de sexo e da opção de continuar.
*   `break` ou controle de flag para encerrar o laço principal.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 69.py correspondente.
```

#### Explicação:

O programa cadastra idade e sexo de várias pessoas. Para cada pessoa, atualiza os contadores:
- Pessoas com mais de 18 anos.
- Homens cadastrados.
- Mulheres com menos de 20 anos.
Após cada cadastro, pergunta se o usuário quer continuar. Ao encerrar, exibe os totais.

#### Exemplo de Uso:
```
--- CADASTRE UMA PESSOA ---
Idade: 25
Sexo [M/F]: M
Quer continuar? [S/N] S
--- CADASTRE UMA PESSOA ---
Idade: 17
Sexo [M/F]: F
Quer continuar? [S/N] S
--- CADASTRE UMA PESSOA ---
Idade: 30
Sexo [M/F]: F
Quer continuar? [S/N] N
--- RESULTADOS ---
Total de pessoas com mais de 18 anos: X
Total de homens cadastrados: Y
Total de mulheres com menos de 20 anos: Z
```

----

### **EXE_70: Estatísticas de Produtos**

> Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A ) Qual é o total gasto na compra B ) Quantos produtos custam mais de R$1000 (o original diz R$10.000, mas R$1000 é mais comum para exemplos) C ) Qual é o nome do produto mais barato

#### Conceitos-chave:
*   Laço `while True` ou `while continuar == 'S'`.
*   `input()` para nome, preço e opção de continuar.
*   Acumulador para total gasto.
*   Contador para produtos > R$1000.
*   Variáveis para armazenar o nome e preço do produto mais barato (e lógica para atualização).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 70.py correspondente.
```

#### Explicação:

O programa lê nome e preço de vários produtos. Calcula o total gasto. Conta quantos produtos custam mais de R$1000. Identifica o nome do produto mais barato (comparando o preço de cada produto com o menor preço registrado até então). Pergunta se o usuário quer continuar após cada produto.

#### Exemplo de Uso:
```
--- CADASTRO DE PRODUTO ---
Nome do produto: Notebook
Preço: R$3500.00
Quer continuar? [S/N] S
--- CADASTRO DE PRODUTO ---
Nome do produto: Mouse
Preço: R$50.00
Quer continuar? [S/N] N
--- FIM DA COMPRA ---
Total gasto: R$3550.00
Produtos custando mais de R$1000: 1
Produto mais barato: Mouse (R$50.00)
```

----

### **EXE_71: Simulador de Caixa Eletrônico**

> Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Considere cédulas de R$50, R$20, R$10, R$1.

#### Conceitos-chave:
*   `input()` para ler o valor do saque.
*   Divisão inteira `//` e operador módulo `%` para calcular a quantidade de cada cédula.
*   Laço `while` para processar o valor enquanto houver saldo a sacar.
*   Estrutura condicional para verificar se há necessidade de uma cédula específica.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 71.py correspondente.
```

#### Explicação:

O programa lê o valor que o usuário deseja sacar. Começando pela cédula de maior valor (R$50), calcula quantas cédulas são necessárias usando divisão inteira. O restante do valor é calculado usando o operador módulo. Esse processo é repetido para as cédulas de R$20, R$10 e R$1, até que o valor total do saque seja coberto.

#### Exemplo de Uso:
```
Que valor você quer sacar? R$138
Total de X cédulas de R$50
Total de Y cédulas de R$20
Total de Z cédulas de R$10
Total de W cédulas de R$1
(Ex: Para R$138: 2 de R$50, 1 de R$20, 1 de R$10, 3 de R$1)
```

----

## **Mundo 3 [40 Horas]**

----

### Curso Python #16 - Tupla

----

### **EXE_72: Número por Extenso**

> Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#### Conceitos-chave:
*   Tuplas para armazenar os números por extenso.
*   Função `input()` para ler o número.
*   Função `int()` para converter a entrada.
*   Validação da entrada para garantir que está entre 0 e 20.
*   Indexação de tupla para acessar o nome do número.
*   Laço `while` para garantir entrada válida.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 72.py correspondente.
```

#### Explicação:

O programa define uma tupla com os nomes dos números de zero a vinte. Solicita ao usuário um número entre 0 e 20, validando a entrada. Em seguida, usa o número digitado como índice para acessar e exibir o nome correspondente na tupla.

#### Exemplo de Uso:
```
Digite um número entre 0 e 20: 15
Você digitou o número quinze.
```

----

### **EXE_73: Tuplas com Times de Futebol**

> Crie uma lista preenchida com os 20 primeiros colocados da Tabela do **Compeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: A ) Os 5 primeiros B ) Os últimos 4 colocados C ) Time em ordem alfabética. D ) Em que posição está o time da Chapecoense

#### Conceitos-chave:
*   Tuplas para armazenar a lista de times.
*   Fatiamento de tuplas (slicing) para mostrar os primeiros e últimos.
*   Função `sorted()` para ordenar a tupla alfabeticamente.
*   Método `index()` para encontrar a posição de um item.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 73.py correspondente.
```

#### Explicação:

O programa armazena os 20 primeiros times em uma tupla.
A) Usa fatiamento `times[:5]` para os 5 primeiros.
B) Usa fatiamento `times[-4:]` para os 4 últimos.
C) Usa `sorted(times)` para a ordem alfabética.
D) Usa `times.index('Chapecoense') + 1` para a posição (somando 1 pois o índice é baseado em zero).

#### Exemplo de Uso:
```
Lista de times: (Time1, Time2, ..., Time20)
Os 5 primeiros são: (Time1, Time2, Time3, Time4, Time5)
Os 4 últimos são: (Time17, Time18, Time19, Time20)
Times em ordem alfabética: [..., Chapecoense, ...]
O time Chapecoense está na Xª posição.
```

----

### **EXE_74: Maior e Menor Valores em Tupla**

> Crie um programa que vai gerar cinco números aleatórios e colocar em tupla. Depois disse, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

#### Conceitos-chave:
*   Módulo `random` e função `randint()`.
*   Tuplas para armazenar os números.
*   Laço `for` para gerar os números.
*   Funções `max()` e `min()` para encontrar o maior e menor valor na tupla.
*   Função `print()` para exibir os resultados.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 74.py correspondente.
```

#### Explicação:

O programa gera cinco números aleatórios (por exemplo, entre 1 e 10) e os armazena em uma tupla. Em seguida, exibe a tupla completa e utiliza as funções `max()` e `min()` para mostrar o maior e o menor valor gerado.

#### Exemplo de Uso:
```
Os números sorteados foram: (3, 7, 1, 9, 5)
O maior valor sorteado foi: 9
O menor valor sorteado foi: 1
```

----

### **EXE_74 (Duplicado): Maior e Menor Valores em Tupla**

> Crie um programa que vai gerar cinco números aleatório e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

#### Conceitos-chave:
*   Módulo `random` e função `randint()`.
*   Tuplas para armazenar os números.
*   Laço `for` para gerar os números.
*   Funções `max()` e `min()` para encontrar o maior e menor valor na tupla.
*   Função `print()` para exibir os resultados.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 74.py correspondente. 
# (Este é um exercício duplicado no original)
```

#### Explicação:

Este exercício é idêntico ao anterior. O programa gera cinco números aleatórios, armazena-os em uma tupla, exibe a tupla e, em seguida, mostra o maior e o menor valor usando `max()` e `min()`.

#### Exemplo de Uso:
```
Os números sorteados foram: (8, 2, 6, 4, 10)
O maior valor sorteado foi: 10
O menor valor sorteado foi: 2
```

----

### **EXE_75: Análise de Dados em uma Tupla**

> Desenvolva um programa que leia quatro valores pelo teclado e quarde-os em uma tupla. No final. mostre: A ) Quantas vezes apareceu o valor 9. B ) Em que posição foi digitado o primeiro valor 3. C ) Quais foram os números pares.

#### Conceitos-chave:
*   Função `input()` para ler os valores.
*   Construção de tupla com os valores lidos.
*   Método `count()` para contar ocorrências.
*   Método `index()` para encontrar a posição (com tratamento de erro se o valor não existir).
*   Laço `for` e operador módulo `%` para identificar números pares.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 75.py correspondente.
```

#### Explicação:

O programa lê quatro números e os armazena em uma tupla.
A) Usa `tupla.count(9)` para contar quantas vezes o 9 aparece.
B) Usa `tupla.index(3)` para encontrar a posição do primeiro 3 (se existir).
C) Itera pela tupla e verifica quais números são pares.

#### Exemplo de Uso:
```
Digite um número: 9
Digite outro número: 3
Digite mais um número: 5
Digite o último número: 9
Você digitou os valores (9, 3, 5, 9)
O valor 9 apareceu 2 vezes.
O valor 3 apareceu na 2ª posição.
Os valores pares digitados foram: Nenhum (ou listar os pares)
```

----

### **EXE_76: Lista de Preços com Tupla**

> Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#### Conceitos-chave:
*   Tupla única contendo nomes e preços intercalados.
*   Laço `for` com `range()` e passo 2 para iterar pela tupla.
*   Formatação de strings (`f-strings`) para exibir os dados em formato tabular.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 76.py correspondente.
```

#### Explicação:

O programa define uma tupla com produtos e seus preços (ex: `('Lápis', 1.75, 'Borracha', 2.00, ...)`). Em seguida, usa um laço `for` para percorrer a tupla de dois em dois elementos, exibindo o nome do produto e seu preço formatado.

#### Exemplo de Uso:
```
LISTAGEM DE PREÇOS
-------------------------
Lápis........... R$   1.75
Borracha........ R$   2.00
Caderno......... R$  15.90
...
-------------------------
```

----

### **EXE_77: Contando Vogais em Tupla**

> Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostra, para cada palavra, quais são as suas vogais.

#### Conceitos-chave:
*   Tupla de palavras.
*   Laço `for` para iterar sobre as palavras da tupla.
*   Laço `for` aninhado para iterar sobre as letras de cada palavra.
*   Verificação se uma letra é vogal (ex: `if letra.lower() in 'aeiou'`).
*   Função `print()` para exibir as vogais de cada palavra.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 77.py correspondente.
```

#### Explicação:

O programa tem uma tupla com palavras. Para cada palavra na tupla, ele percorre suas letras. Se uma letra for uma vogal (comparando em minúsculas), ela é exibida.

#### Exemplo de Uso:
```
Na palavra APRENDER temos as vogais: a e e
Na palavra PROGRAMAR temos as vogais: o a a
...
```

----

### Curso Python #17 - Lista(Parte1)

----

### **EXE_78: Maior e Menor Valores na Lista**

> Faça um programa que leia 5 valores numéricos e quarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

#### Conceitos-chave:
*   Listas para armazenar os valores.
*   Laço `for` para ler os valores.
*   Funções `max()` e `min()` para encontrar maior e menor valor.
*   Método `index()` ou laço com `enumerate()` para encontrar as posições.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 78.py correspondente.
```

#### Explicação:

O programa lê 5 números e os armazena em uma lista. Encontra o maior e o menor valor usando `max()` e `min()`. Depois, itera pela lista usando `enumerate()` para encontrar e exibir as posições (índices) onde o maior e o menor valor aparecem.

#### Exemplo de Uso:
```
Digite um valor para a Posição 0: 3
Digite um valor para a Posição 1: 7
Digite um valor para a Posição 2: 2
Digite um valor para a Posição 3: 7
Digite um valor para a Posição 4: 5
Você digitou os valores [3, 7, 2, 7, 5]
O maior valor digitado foi 7 nas posições 1, 3.
O menor valor digitado foi 2 na posição 2.
```

----

### **EXE_79: Valores Únicos em uma Lista**

> Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já existe lá dentro, ele não será adicionado. No final, serão exibidos todos os valore únicos digitados, em ordem crescente.

#### Conceitos-chave:
*   Listas.
*   Laço `while` para permitir múltiplas entradas.
*   Verificação `if valor not in lista`.
*   Método `append()` para adicionar à lista.
*   Método `sort()` para ordenar a lista.
*   Opção para o usuário parar de digitar.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 79.py correspondente.
```

#### Explicação:

O programa permite que o usuário digite vários números. Cada número é adicionado a uma lista somente se ainda não estiver presente. O processo continua até que o usuário decida parar. No final, a lista de valores únicos é exibida em ordem crescente.

#### Exemplo de Uso:
```
Digite um valor: 5
Valor adicionado com sucesso...
Quer continuar? [S/N] S
Digite um valor: 3
Valor adicionado com sucesso...
Quer continuar? [S/N] S
Digite um valor: 5
Valor duplicado! Não vou adicionar...
Quer continuar? [S/N] N
Você digitou os valores: [3, 5]
```

----

### **EXE_80: Lista Ordenada sem Repetições**

> Crie um programa onde o usuário posso digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usor o sort()). No final, mostre a lista ordenada na tela.

#### Conceitos-chave:
*   Listas.
*   Laço `for` para ler os cinco valores.
*   Lógica de inserção ordenada: percorrer a lista existente para encontrar a posição correta de inserção do novo valor.
*   Método `insert()` para adicionar o valor na posição correta.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 80.py correspondente.
```

#### Explicação:

O programa lê cinco números. Para cada número, ele é inserido na lista de forma que a lista permaneça ordenada. Isso é feito encontrando a posição correta na lista (onde o novo número é maior que os anteriores e menor que os seguintes) e usando `lista.insert(posicao, valor)`.

#### Exemplo de Uso:
```
Digite um valor: 8
Adicionado ao final da lista...
Digite um valor: 3
Adicionado na posição 0 da lista...
Digite um valor: 5
Adicionado na posição 1 da lista...
...
Os valores digitados em ordem foram: [3, 5, ..., 8]
```

----

### **EXE_81: Extraindo Dados de uma Lista**

> Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

#### Conceitos-chave:
*   Listas.
*   Laço `while` para múltiplas entradas.
*   Função `len()` para contar elementos.
*   Método `sort(reverse=True)` para ordenar em forma decrescente.
*   Operador `in` para verificar a existência do valor 5.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 81.py correspondente.
```

#### Explicação:

O programa lê vários números e os armazena em uma lista até que o usuário decida parar.
A) Exibe o total de números usando `len(lista)`.
B) Ordena a lista em ordem decrescente usando `lista.sort(reverse=True)` e a exibe.
C) Verifica se o número 5 está na lista usando `5 in lista` e informa o usuário.

#### Exemplo de Uso:
```
Digite um valor: 7
Quer continuar? [S/N] S
Digite um valor: 5
Quer continuar? [S/N] S
Digite um valor: 10
Quer continuar? [S/N] N
Foram digitados 3 números.
Lista em ordem decrescente: [10, 7, 5]
O valor 5 faz parte da lista! (ou: O valor 5 NÃO foi encontrado na lista!)
```

----

### **EXE_82: Dividindo Valores em Várias Listas**

> Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas lista extras que vão conter apenas os valores pares e os valores impares digitados, respectivamento. Ao final, mostre o conteúdo das três listas geradas.

#### Conceitos-chave:
*   Listas (principal, pares, ímpares).
*   Laço `while` para múltiplas entradas.
*   Operador módulo `%` para verificar se é par ou ímpar.
*   Método `append()` para adicionar às listas correspondentes.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 82.py correspondente.
```

#### Explicação:

O programa lê vários números e os armazena em uma lista principal. Em seguida, itera por esta lista; se um número for par, ele é adicionado a uma lista de pares; se for ímpar, a uma lista de ímpares. No final, as três listas são exibidas.

#### Exemplo de Uso:
```
Digite um valor: 4
Quer continuar? [S/N] S
Digite um valor: 7
Quer continuar? [S/N] S
Digite um valor: 2
Quer continuar? [S/N] N
Lista completa: [4, 7, 2]
Lista de pares: [4, 2]
Lista de ímpares: [7]
```

----

### **EXE_83: Validando Expressões Matemáticas**

> Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#### Conceitos-chave:
*   Listas usadas como pilha.
*   Laço `for` para percorrer a expressão.
*   Verificação de parênteses: se abrir '(', adiciona à pilha; se fechar ')', tenta remover da pilha.
*   Condições de erro: fechar parêntese sem ter um aberto na pilha, ou sobrar parênteses abertos na pilha ao final.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 83.py correspondente.
```

#### Explicação:

O programa analisa uma expressão matemática para verificar se os parênteses estão balanceados. Ele usa uma lista como uma pilha: ao encontrar um '(', empilha; ao encontrar um ')', desempilha se a pilha não estiver vazia. Se tentar desempilhar de uma pilha vazia ou se a pilha não estiver vazia no final, a expressão é inválida.

#### Exemplo de Uso:
```
Digite a expressão: (a + b) * (c - (d + e))
Sua expressão está válida!

Digite a expressão: ((a + b)
Sua expressão está inválida!
```

----

### Curso Python #17 - Listas (Parte 2)

----

### **EXE_84: Lista Composta e Análise de Dados**

> Faça um proframa que leia nome e peso de vários pessosas, quardando tudo em uma lista. No final, mostre: A ) Quantas pessosas foram cadastradas. B ) Uma listagem com os pessoas mais pesadas. C ) Uma listagem com as pessoas mais leves.

#### Conceitos-chave:
*   Listas compostas (lista de listas, onde cada sublista tem nome e peso).
*   Laço `while` para múltiplas entradas.
*   Função `len()` para contar pessoas.
*   Identificação do maior e menor peso.
*   Laços `for` para encontrar todas as pessoas com o maior/menor peso.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 84.py correspondente.
```

#### Explicação:

O programa lê nome e peso de várias pessoas, armazenando cada par [nome, peso] em uma lista principal.
A) Conta o número de sublistas (pessoas).
B) Encontra o maior peso e depois lista todas as pessoas com esse peso.
C) Encontra o menor peso e depois lista todas as pessoas com esse peso.

#### Exemplo de Uso:
```
Nome: Ana
Peso: 55
Quer continuar? [S/N] S
Nome: Bruno
Peso: 80
Quer continuar? [S/N] S
Nome: Carla
Peso: 55
Quer continuar? [S/N] N
Foram cadastradas 3 pessoas.
Maior peso foi 80.0Kg. Peso de: [Bruno]
Menor peso foi 55.0Kg. Peso de: [Ana, Carla]
```

----

### **EXE_85: Listas com Pares e Ímpares**
> Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crecentre.

#### Conceitos-chave:
*   Lista única composta por duas sublistas: uma para pares e uma para ímpares (ex: `numeros = [[], []]`).
*   Laço `for` para ler os sete valores.
*   Operador módulo `%` para verificar paridade.
*   Método `append()` para adicionar às sublistas corretas.
*   Método `sort()` para ordenar as sublistas.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 85.py correspondente.
```

#### Explicação:

O programa usa uma lista principal contendo duas sublistas: `numeros[0]` para pares e `numeros[1]` para ímpares. Lê sete números. Se um número for par, é adicionado a `numeros[0]`; se for ímpar, a `numeros[1]`. No final, ambas as sublistas são ordenadas e exibidas.

#### Exemplo de Uso:
```
Digite o 1º valor: 4
Digite o 2º valor: 7
...
Digite o 7º valor: 1
Os valores pares digitados foram: [2, 4, 8] (exemplo)
Os valores ímpares digitados foram: [1, 5, 7] (exemplo)
```

----

### **EXE_86: Matriz em Python**

> Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

#### Conceitos-chave:
*   Listas aninhadas para representar a matriz.
*   Laços `for` aninhados para preencher e exibir a matriz.
*   Função `input()` para ler os valores.
*   Formatação de `print()` para exibir a matriz.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 86.py correspondente.
```

#### Explicação:

O programa cria uma matriz 3x3 (uma lista de 3 listas, cada uma com 3 elementos). Usa laços `for` aninhados para solicitar ao usuário que digite um valor para cada posição da matriz. Depois, usa outros laços `for` aninhados para exibir a matriz formatada.

#### Exemplo de Uso:
```
Digite um valor para [0, 0]: 1
Digite um valor para [0, 1]: 2
...
Digite um valor para [2, 2]: 9
[ 1 ] [ 2 ] [ 3 ]
[ 4 ] [ 5 ] [ 6 ]
[ 7 ] [ 8 ] [ 9 ]
```

----

![Matriz 3x3](img/3x3.png)

----

### **EXE_87: Mais Sobre Matriz em Python**

> Aprimore o desafio anterior, mostrando no final: A ) A soma de todos os valores pares digitados. B ) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

#### Conceitos-chave:
*   Reutilização da lógica do EXE_86 para criar e preencher a matriz.
*   Laços `for` aninhados para percorrer a matriz.
*   Condicionais para somar pares, somar elementos da terceira coluna e encontrar o maior da segunda linha.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 87.py correspondente.
```

#### Explicação:

Após preencher a matriz como no EXE_86:
A) Percorre todos os elementos, somando os que são pares.
B) Percorre os elementos onde o índice da coluna é 2 (terceira coluna) e os soma.
C) Encontra o maior valor entre os elementos da segunda linha (índice de linha 1).

#### Exemplo de Uso:
(Após preencher a matriz como no EXE_86)
```
A soma dos valores pares é: X.
A soma dos valores da terceira coluna é: Y.
O maior valor da segunda linha é: Z.
```

---

![Matriz 3x3](img/3x3.png)

----

### **EXE_88: Palpites para a Mega Sena**

> Faça um programa que ajude um jogador da **Mega Sena** a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

#### Conceitos-chave:
*   Módulo `random` e função `sample()` (ou `randint()` com verificação de duplicidade).
*   Listas compostas para armazenar os jogos.
*   Laço `for` para gerar a quantidade de jogos solicitada.
*   Laço `while` ou `sample()` para gerar 6 números únicos por jogo.
*   Módulo `time` e função `sleep()` para pausar entre a exibição dos jogos (opcional).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 88.py correspondente.
```

#### Explicação:

O programa pergunta quantos jogos o usuário quer gerar. Para cada jogo, sorteia 6 números distintos entre 1 e 60 (usar `random.sample(range(1, 61), 6)` é uma boa forma). Armazena cada jogo (lista de 6 números) em uma lista principal. Exibe todos os jogos gerados.

#### Exemplo de Uso:
```
Quantos jogos você quer que eu sorteie? 3
Jogo 1: [4, 15, 22, 37, 48, 55]
Jogo 2: [8, 12, 29, 33, 41, 50]
Jogo 3: [5, 19, 25, 30, 45, 59]
```

----

### **EXE_89: Boletim com Listas Compostas**

> Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim mostrar as notas de cada aluno individualmente.

#### Conceitos-chave:
*   Listas compostas (ex: `[[nome, [nota1, nota2], media], ...]`).
*   Laço `while` para ler dados de vários alunos.
*   Cálculo da média.
*   Formatação da saída para exibir o boletim.
*   Opção para mostrar notas de um aluno específico.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 89.py correspondente.
```

#### Explicação:

O programa lê nome e duas notas de vários alunos, armazenando-os em uma lista composta (cada item pode ser uma lista com nome, outra lista com as notas, e a média). Exibe um boletim resumido (No., Nome, Média). Depois, permite ao usuário consultar as notas de um aluno específico pelo seu número.

#### Exemplo de Uso:
```
Nome: Ana
Nota 1: 7.0
Nota 2: 8.5
Quer continuar? [S/N] S
...
No. NOME      MÉDIA
---------------------
0   Ana       7.75
1   Bruno     6.50
...
---------------------
Mostrar notas de qual aluno? (999 interrompe): 0
Notas de Ana são [7.0, 8.5]
```

----

### Curso Python #19 - Dicionários

----

### **EXE_90: Dicionário em Python**

> Faça um programa que leia nom e média de um aluno, quardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

#### Conceitos-chave:
*   Dicionários para armazenar dados do aluno.
*   Leitura de nome e média.
*   Determinação da situação (Aprovado/Reprovado) com base na média.
*   Adição de chaves e valores ao dicionário.
*   Iteração sobre o dicionário (`items()`) para exibir seu conteúdo.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 90.py correspondente.
```

#### Explicação:

O programa lê o nome e a média de um aluno. Com base na média (ex: >= 7 Aprovado, < 7 Reprovado), define a situação. Armazena nome, média e situação em um dicionário. No final, exibe os dados do dicionário.

#### Exemplo de Uso:
```
Nome: Ana
Média: 7.5
Nome é igual a Ana
Média é igual a 7.5
Situação é igual a Aprovado
```

----

### **EXE_91: Jogo de Dados em Python**

> Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatório. Guarde esses resultados em um dicinário. No final, coloque esse docionário em ordem, sobendo que o vencedor tirou o maior números no dado.

#### Conceitos-chave:
*   Dicionários para armazenar resultados dos jogadores.
*   Módulo `random` e função `randint(1, 6)`.
*   Laço `for` para simular as jogadas.
*   Módulo `operator` e função `itemgetter` (ou `lambda`) para ordenar o dicionário pelos valores.
*   Função `sorted()` para ordenar.
*   Módulo `time` e função `sleep()` para pausas (opcional).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 91.py correspondente.
```

#### Explicação:

O programa simula 4 jogadores lançando um dado. Os resultados (nome do jogador e valor do dado) são armazenados em um dicionário. Depois, o dicionário é ordenado em ordem decrescente dos valores dos dados para determinar o ranking dos jogadores.

#### Exemplo de Uso:
```
Valores sorteados:
  jogador1 tirou 4 no dado.
  jogador2 tirou 6 no dado.
  jogador3 tirou 2 no dado.
  jogador4 tirou 4 no dado.
Ranking dos jogadores:
  1º lugar: jogador2 com 6.
  2º lugar: jogador1 com 4.
  3º lugar: jogador4 com 4.
  4º lugar: jogador3 com 2.
```

----

### **EXE_92: Cadastro de Trabalhador em Python**

> Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CRPS for diferente de Zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrecente, além da idade, com quantos anos a pessoa vai s aposentar. (Considere 35 anos de contribuição para aposentadoria)

#### Conceitos-chave:
*   Dicionários.
*   Módulo `datetime` para calcular a idade.
*   Entrada de dados e condicionais para CTPS.
*   Cálculo da idade de aposentadoria (idade_contratacao + 35 - (ano_atual - ano_contratacao)).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 92.py correspondente.
```

#### Explicação:

O programa coleta dados de um trabalhador: nome, ano de nascimento, CTPS. Calcula a idade. Se a CTPS for diferente de zero, coleta ano de contratação e salário. Calcula com quantos anos a pessoa se aposentará, considerando 35 anos de contribuição a partir do ano de contratação. Todos os dados são armazenados e exibidos a partir de um dicionário.

#### Exemplo de Uso:
```
Nome: Ana
Ano de Nascimento: 1985
Carteira de Trabalho (0 não tem): 12345
Ano de Contratação: 2005
Salário: R$3000.00
--- DADOS ---
Nome: Ana
Idade: 39 (em AAAA)
CTPS: 12345
Contratação: 2005
Salário: R$3000.00
Aposentadoria: 55 anos (em AAAA)
```

----

### **EXE_93: Cadastro de Jogador de Futebol**

>  Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#### Conceitos-chave:
*   Dicionários para armazenar dados do jogador.
*   Listas para armazenar os gols por partida.
*   Laço `for` para ler os gols de cada partida.
*   Função `sum()` para calcular o total de gols.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 93.py correspondente.
```

#### Explicação:

O programa lê o nome do jogador e o número de partidas. Em seguida, para cada partida, lê quantos gols foram feitos, armazenando-os em uma lista. Todos esses dados (nome, lista de gols, total de gols) são guardados em um dicionário e exibidos.

#### Exemplo de Uso:
```
Nome do Jogador: Romário
Quantas partidas jogou? 5
Quantos gols na partida 1? 2
Quantos gols na partida 2? 1
...
--- RESULTADO ---
{'nome': 'Romário', 'gols_por_partida': [2, 1, ...], 'total_gols': X}
O jogador Romário jogou 5 partidas.
  => Na partida 1, fez 2 gols.
  => Na partida 2, fez 1 gol.
  ...
Foi um total de X gols.
```

----

### **EXE_94: Unindo Dicionários e Listas**

> Crie um programa que leia nome, sexo e idade de várias ṕessoas, quardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A ) Quantas pessoas cadastradas. B ) A média de idade. C ) Uma lista com mulheres. D ) Uma lista com idade acima da média.

#### Conceitos-chave:
*   Lista de dicionários.
*   Laço `while` para cadastrar várias pessoas.
*   Cálculo de média.
*   Iteração pela lista de dicionários para filtrar dados (mulheres, idades acima da média).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 94.py correspondente.
```

#### Explicação:

O programa cadastra nome, sexo e idade de várias pessoas. Cada pessoa é um dicionário, e todos os dicionários são adicionados a uma lista.
A) Conta o número de dicionários na lista.
B) Calcula a média de idade.
C) Cria uma nova lista apenas com os dicionários de mulheres.
D) Cria uma nova lista com os dicionários de pessoas com idade acima da média.

#### Exemplo de Uso:
```
Nome: Ana
Sexo [M/F]: F
Idade: 22
Quer continuar? [S/N] S
...
A) Ao todo temos X pessoas cadastradas.
B) A média de idade é de YY.Y anos.
C) As mulheres cadastradas foram: [Ana, ...]
D) Lista das pessoas que estão acima da média: [Bruno (idade Z), ...]
```

----

### **EXE_95: Aprimorando os Dicionários**

> Aprimore o **Desafio093** para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamaneto de cada jogador.

#### Conceitos-chave:
*   Lista de dicionários (cada dicionário é um jogador, como no EXE_93).
*   Laço `while` para cadastrar vários jogadores.
*   Laço `while` para permitir a consulta do aproveitamento de jogadores específicos até que o usuário decida parar.
*   Validação da entrada do usuário para consulta.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 95.py correspondente.
```

#### Explicação:

O programa cadastra vários jogadores (nome, partidas, gols por partida), cada um como um dicionário em uma lista. Exibe uma tabela resumo (cód, nome, gols, total). Em seguida, permite ao usuário consultar o levantamento detalhado de um jogador específico pelo seu código, repetidamente, até que uma opção de parada seja digitada.

#### Exemplo de Uso:
(Após cadastrar jogadores)
```
cod nome      gols        total
---------------------------------
  0 Romário   [2, 1, ...] X
  1 Zico      [3, 0, ...] Y
---------------------------------
Levantamento de qual jogador? (999 para parar) 0
-- LEVANTAMENTO DO JOGADOR Romário:
No jogo 1 fez 2 gols.
No jogo 2 fez 1 gol.
...
```

----

### Curso Python #20 - Funções (Parte 1)

----

### **EXE_96: Função que Calcula Área**

> Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#### Conceitos-chave:
*   Definição de função `def area(largura, comprimento):`.
*   Parâmetros de função.
*   Cálculo da área dentro da função.
*   Função `print()` dentro ou fora da função para mostrar o resultado.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 96.py correspondente.
```

#### Explicação:

O programa define uma função `area()` que aceita dois parâmetros: largura e comprimento. Dentro da função, calcula a área (largura * comprimento) e a exibe. O programa principal então chama essa função com valores fornecidos pelo usuário.

#### Exemplo de Uso:
```
Controle de Terrenos
--------------------
Largura (m): 4.5
Comprimento (m): 8
A área de um terreno 4.5x8.0 é de 36.0m².
```

----

### **EXE_97: Um Print Especial**

> Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptáveis.

#### Conceitos-chave:
*   Definição de função `def escreva(texto):`.
*   Função `len()` para obter o tamanho do texto.
*   `print()` para desenhar linhas (ex: `~`) de tamanho adaptável ao texto.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 97.py correspondente.
```

#### Explicação:

A função `escreva()` recebe um texto. Calcula o comprimento do texto. Imprime uma linha de `~` com comprimento igual ao do texto mais uma margem. Imprime o texto. Imprime outra linha de `~`.

#### Exemplo de Uso:
```
escreva('Olá, Mundo!')
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
```

----

### **EXE_98: Função de Contador**

> Faça um programa que tenha uma função chamada contador(), que receba três parâmentro: inicio, fim e passo. Seu programa tem que realizar três contagens através da função criada: A ) De 1 até 10, de 1 em 1. B ) De 1o até 0, de 2 em 2. C ) Uma contagem pesonalizada.

#### Conceitos-chave:
*   Definição de função `def contador(inicio, fim, passo):`.
*   Laço `for` com `range()` usando os parâmetros.
*   Tratamento para passo 0 ou negativo (se necessário, para evitar loops infinitos ou comportamento inesperado).
*   Módulo `time` e `sleep()` para pausas.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 98.py correspondente.
```

#### Explicação:

A função `contador()` recebe início, fim e passo. Realiza a contagem progressiva ou regressiva conforme os valores, imprimindo cada número. O programa principal chama a função para as três contagens especificadas, incluindo uma personalizada com entrada do usuário.

#### Exemplo de Uso:
```
Contagem de 1 até 10 de 1 em 1:
1 2 3 4 5 6 7 8 9 10 FIM!
Contagem de 10 até 0 de 2 em 2:
10 8 6 4 2 0 FIM!
Agora é sua vez de personalizar a contagem!
Início: 5
Fim: 20
Passo: 3
Contagem de 5 até 20 de 3 em 3:
5 8 11 14 17 20 FIM!
```

----

### **EXE_99: Função que Descobre o Maior**

> Faça um programa que tenha uma função chamada maior(), que receba vários parâmentros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#### Conceitos-chave:
*   Definição de função com parâmetros variáveis (`*args` ou `*valores`).
*   Função `max()` para encontrar o maior valor em uma coleção de números.
*   Iteração sobre os parâmetros variáveis.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 99.py correspondente.
```

#### Explicação:

A função `maior()` é definida para aceitar um número arbitrário de argumentos (`*valores`). Dentro da função, ela analisa os valores recebidos (pode usar `max(valores)` se `valores` for uma tupla/lista, ou iterar e comparar manualmente) e informa quantos valores foram passados e qual foi o maior.

#### Exemplo de Uso:
```
Analisando os valores passados...
Foram informados X valores ao todo.
O maior valor informado foi Y.
```

----

### **EXE_100: Funções para Sortear e Somar**

> Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da listaa e a segunda função vai mostrar a soma entre todos os calores PARES sorteados pela função anterior.

#### Conceitos-chave:
*   Listas globais ou passadas como parâmetros.
*   Função `sorteia(lista)`: usa `random.randint()` para sortear 5 números e os adiciona à lista.
*   Função `somaPar(lista)`: itera pela lista, soma os valores pares.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 100.py correspondente.
```

#### Explicação:

Uma lista `numeros` é criada. A função `sorteia()` popula essa lista com 5 números aleatórios. A função `somaPar()` percorre a lista `numeros`, identifica os valores pares e calcula sua soma, exibindo o resultado.

#### Exemplo de Uso:
```
Sorteando 5 valores da lista: [X, Y, Z, W, K] PRONTO!
Somando os valores pares de [X, Y, Z, W, K], temos SOMA_PAR.
```

----

### Curso Python #21 - Funções (Parte 2)

----

### **EXE_101: Funções para Votação**

> Crie um programa que tenha uma função chamada voto() que vai rereber como parâmentros o ano de nascimento de uma pessoa, retornando um valor literal indicando uma pessoa tem voto **NEGADO**, **OPCIONAL** ou **OBRIGATÓRIO** nas eleições.

#### Conceitos-chave:
*   Definição de função `def voto(ano_nascimento):`.
*   Módulo `datetime` para obter o ano atual e calcular a idade.
*   Retorno de strings ("NEGADO", "OPCIONAL", "OBRIGATÓRIO") com base na idade.
*   Regras de votação: <16 (NEGADO), 16-17 ou >65 (OPCIONAL), 18-65 (OBRIGATÓRIO).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 101.py correspondente.
```

#### Explicação:

A função `voto()` calcula a idade da pessoa a partir do ano de nascimento e do ano atual. Com base na idade, retorna uma string indicando a situação eleitoral da pessoa.

#### Exemplo de Uso:
```
Ano de Nascimento: 2007
Com 17 anos: Voto OPCIONAL.
```

----

### **EXE_102: Função para Fatorial**

> Crie um programa que tenha uma função fatorial() que receba dois parâmentros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

#### Conceitos-chave:
*   Definição de função `def fatorial(n, show=False):`.
*   Parâmetro opcional `show`.
*   Cálculo do fatorial (iterativo ou recursivo).
*   Impressão condicional do processo de cálculo se `show` for `True`.
*   Retorno do valor do fatorial.
*   Docstrings.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 102.py correspondente.
```

#### Explicação:

A função `fatorial()` calcula o fatorial de `n`. Se o parâmetro opcional `show` for `True`, ela também imprime o processo de cálculo (ex: "5 x 4 x 3 x 2 x 1 = "). A função retorna o resultado do fatorial.

#### Exemplo de Uso:
```
print(fatorial(5, show=True))
# Saída: 5 x 4 x 3 x 2 x 1 = 120

print(fatorial(5))
# Saída: 120
```

----

### **EXE_103: Ficha do Jogador**

> Faça um programa que tenha uma função chamado ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

#### Conceitos-chave:
*   Definição de função `def ficha(nome='<desconhecido>', gols=0):`.
*   Parâmetros opcionais com valores padrão.
*   Validação ou tratamento de `gols` para garantir que seja numérico (ou padrão 0).

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 103.py correspondente.
```

#### Explicação:

A função `ficha()` aceita um nome e um número de gols como parâmetros opcionais. Se o nome não for fornecido, usa "<desconhecido>". Se os gols não forem fornecidos ou forem inválidos, considera 0. Exibe a ficha formatada.

#### Exemplo de Uso:
```
Nome do jogador: Romário
Número de gols: 1000
O jogador Romário fez 1000 gol(s) no campeonato.

Nome do jogador: 
Número de gols: 
O jogador <desconhecido> fez 0 gol(s) no campeonato.
```

----

### **EXE_104: Validando Entrada de Dados em Python**

> Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n')

#### Conceitos-chave:
*   Definição de função `def leiaInt(prompt):`.
*   Laço `while True` para repetição até entrada válida.
*   Uso de `input()` dentro da função.
*   Método `isnumeric()` ou `isdigit()` para verificar se a string pode ser convertida para inteiro.
*   Conversão para `int()` e retorno do valor.
*   Mensagem de erro para entrada inválida.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 104.py correspondente.
```

#### Explicação:

A função `leiaInt()` recebe uma mensagem (prompt). Ela solicita a entrada ao usuário repetidamente até que um valor que possa ser convertido para inteiro seja digitado. Se a entrada não for um número inteiro válido, exibe uma mensagem de erro e pede novamente.

#### Exemplo de Uso:
```
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
# Se o usuário digitar 'abc', a função pedirá novamente.
```

----

### **EXE_105: Analisando e Gerando Dicionários**

> Faça um programa que tenha uma função notas() que pode recebar vários notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas, A Maior nota, A Menor nota, A Média da turma, A Situação (opcional). Adicione também as docstrings.

#### Conceitos-chave:
*   Definição de função `def notas(*n, sit=False):`.
*   Parâmetros variáveis `*n` para receber as notas.
*   Parâmetro opcional `sit` para incluir a situação.
*   Funções `len()`, `max()`, `min()`, `sum()`.
*   Cálculo da média.
*   Condicional para determinar a situação (Boa, Razoável, Ruim) com base na média.
*   Retorno de um dicionário com os resultados.
*   Docstrings.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 105.py correspondente.
```

#### Explicação:

A função `notas()` aceita várias notas e um parâmetro opcional `sit`. Ela calcula a quantidade de notas, a maior, a menor e a média. Se `sit=True`, também determina a situação da turma (ex: Boa para média >= 7). Retorna um dicionário com todas essas informações.

#### Exemplo de Uso:
```
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
# Saída: {'total': 4, 'maior': 10, 'menor': 5.5, 'media': 7.875, 'situacao': 'BOA'}
```

----

### **EXE_106: Sistema Interativo de Ajuda em Python**

> Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digirar a palavra **"FIM"**, o programa se encerrará.

#### Conceitos-chave:
*   Laço `while True`.
*   Função `input()` para ler o comando ou função.
*   Função `help()` para exibir a documentação.
*   Condição de parada (entrada == "FIM").
*   Formatação da saída (cores, títulos) para melhorar a interface.

#### Solução:
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 106.py correspondente.
```

#### Explicação:

O programa entra em um loop, solicitando ao usuário o nome de uma função ou biblioteca Python sobre a qual deseja obter ajuda. Ele então usa a função `help()` para exibir a documentação correspondente. O loop continua até que o usuário digite "FIM".

#### Exemplo de Uso:
```
SISTEMA DE AJUDA PyHELP
Função ou Biblioteca > print
(Exibe a ajuda da função print)
Função ou Biblioteca > FIM
ATÉ LOGO!
```

----

### Curso Python #22 - Módulos e Pacotes

----

### **EXE_107: Exercitando Módulos em Python**

> Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

#### Conceitos-chave:
*   Criação de um arquivo `.py` (módulo `moeda.py`).
*   Definição de funções dentro do módulo (`aumentar`, `diminuir`, `dobro`, `metade`).
*   Criação de um programa principal que importa o módulo (`import moeda` ou `from moeda import ...`).
*   Chamada das funções do módulo no programa principal.

#### Solução:
```python
# No arquivo moeda.py:
# def aumentar(preco, taxa): return preco * (1 + taxa/100)
# def diminuir(preco, taxa): return preco * (1 - taxa/100)
# def dobro(preco): return preco * 2
# def metade(preco): return preco / 2

# No programa principal (EX - 107.py):
# import moeda
# preco = float(input('Digite o preço: R$'))
# print(f'A metade de {preco} é {moeda.metade(preco)}')
# ...
```

#### Explicação:

Cria-se um módulo `moeda.py` com funções para operações financeiras básicas. Um segundo script importa e utiliza essas funções para manipular um preço.

#### Exemplo de Uso:
(No programa principal)
```
Digite o preço: R$100.00
A metade de 100.0 é 50.0
O dobro de 100.0 é 200.0
Aumentando 10%, temos 110.0
Diminuindo 13%, temos 87.0
```

----

### **EXE_108: Formatando Moedas em Python**

> Adapte o código do **Desafio 107**, criando uma função adicional chamada moeda() que consiga os valores como um valor monetário formatado.

#### Conceitos-chave:
*   Modificação do módulo `moeda.py`.
*   Criação da função `moeda(preco, simbolo='R$')` que retorna uma string formatada (ex: "R$100,00").
*   Uso de f-strings para formatação (`f'{simbolo}{preco:.2f}'.replace('.', ',')`).
*   Aplicação da função `moeda()` nos prints do programa principal.

#### Solução:
```python
# No arquivo moeda.py (adicionar/modificar):
# def moeda(preco=0, simbolo='R$'):
#    return f'{simbolo}{preco:.2f}'.replace('.', ',')

# No programa principal (EX - 108.py):
# import moeda
# preco = float(input('Digite o preço: R$'))
# print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
# ...
```

#### Explicação:

A função `moeda()` é adicionada ao módulo `moeda.py` para formatar um número como valor monetário. O programa principal agora usa `moeda.moeda()` para exibir os preços formatados.

#### Exemplo de Uso:
(No programa principal)
```
Digite o preço: R$100.00
A metade de R$100,00 é R$50,00
O dobro de R$100,00 é R$200,00
Aumentando 10%, temos R$110,00
```

----

### **EXE_109: Formatando Moedas em Python (Avançado)**

> Modifique as funções que foram criadas no **Desafio 107** para que elas aceitem um parâmetro a mais, informoando se o valor retornado por elas vai ser ou não formatado pelo funções moeda(), desenvolvida no **Desafio 108**.

#### Conceitos-chave:
*   Modificação das funções `aumentar`, `diminuir`, `dobro`, `metade` no módulo `moeda.py`.
*   Adição de um parâmetro opcional `formatar=False` a essas funções.
*   Retorno condicional: se `formatar` for `True`, chama `moeda()` antes de retornar; senão, retorna o valor numérico.

#### Solução:
```python
# No arquivo moeda.py (modificar funções):
# def metade(preco=0, formatar=False):
#    res = preco / 2
#    return res if not formatar else moeda(res)
# (Similar para aumentar, diminuir, dobro)

# No programa principal (EX - 109.py):
# import moeda
# preco = float(input('Digite o preço: R$'))
# print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
# ...
```

#### Explicação:

As funções do módulo `moeda.py` são alteradas para incluir um parâmetro booleano `formatar`. Se `True`, as funções retornam o resultado já formatado pela função `moeda()`; caso contrário, retornam o valor numérico bruto.

#### Exemplo de Uso:
(No programa principal)
```
Digite o preço: R$100.00
A metade de R$100,00 é R$50,00
O dobro de R$100,00 (sem formatar) é 200.0
Aumentando 10% (formatado), temos R$110,00
```

----

### **EXE_110: Reduzindo Ainda Mais seu Programa**

> Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre ma tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

#### Conceitos-chave:
*   Criação da função `resumo(preco, taxa_aum, taxa_red)` no módulo `moeda.py`.
*   Chamada interna das outras funções (`aumentar`, `diminuir`, `dobro`, `metade`, `moeda`) dentro de `resumo()`.
*   Impressão formatada de um resumo das análises do preço.

#### Solução:
```python
# No arquivo moeda.py (adicionar):
# def resumo(preco=0, taxa_aum=10, taxa_red=5):
#    print('-'*30)
#    print('RESUMO DO VALOR'.center(30))
#    print('-'*30)
#    print(f'Preço analisado: \t{moeda(preco)}')
#    print(f'Dobro do preço: \t{dobro(preco, True)}')
#    print(f'Metade do preço: \t{metade(preco, True)}')
#    print(f'{taxa_aum}% de aumento: \t{aumentar(preco, taxa_aum, True)}')
#    print(f'{taxa_red}% de redução: \t{diminuir(preco, taxa_red, True)}')
#    print('-'*30)

# No programa principal (EX - 110.py):
# import moeda
# preco = float(input('Digite o preço: R$'))
# moeda.resumo(preco, 20, 12)
```

#### Explicação:

A função `resumo()` é adicionada a `moeda.py`. Ela recebe um preço e percentuais de aumento/redução, e imprime um relatório formatado com o preço original, seu dobro, metade, e os valores com aumento e redução aplicados, todos formatados como moeda.

#### Exemplo de Uso:
(No programa principal)
```
Digite o preço: R$100.00
------------------------------
        RESUMO DO VALOR       
------------------------------
Preço analisado:  R$100,00
Dobro do preço:   R$200,00
Metade do preço:  R$50,00
20% de aumento:   R$120,00
12% de redução:   R$88,00
------------------------------
```

----

### **EXE_111: Transformando Módulos em Pacotes**

> Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado. Tranasfira todas as funções utilizandos nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

#### Conceitos-chave:
*   Criação de diretório de pacote (`utilidadesCev`).
*   Criação de arquivo `__init__.py` dentro do pacote (pode estar vazio).
*   Criação dos módulos `moeda.py` e `dado.py` dentro do pacote.
*   Movimentação das funções relevantes para `utilidadesCev/moeda.py`.
*   Ajuste das importações no programa principal (ex: `from utilidadesCev import moeda`).

#### Solução:
Estrutura de arquivos:
```
utilidadesCev/
  __init__.py
  moeda.py      (contém aumentar, diminuir, dobro, metade, moeda, resumo)
  dado.py       (inicialmente vazio ou com funções futuras)
EX - 111.py     (programa principal)
```
```python
# No programa principal (EX - 111.py):
# from utilidadesCev import moeda
# preco = float(input('Digite o preço: R$'))
# moeda.resumo(preco, 20, 12)
```

#### Explicação:

As funções de `moeda.py` são movidas para um módulo dentro de um pacote `utilidadesCev`. O programa principal agora importa as funções desse pacote para utilizá-las. O módulo `dado.py` é criado para uso futuro.

#### Exemplo de Uso:
(Mesma saída do EXE_110, mas agora usando o pacote)
```
Digite o preço: R$100.00
------------------------------
        RESUMO DO VALOR       
------------------------------
...
------------------------------
```

----

### **EXE_112: Entrada de Dados Monetários**

> Dentro do pacote utilidadesCev que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

#### Conceitos-chave:
*   Criação da função `leiaDinheiro(prompt)` no módulo `utilidadesCev/dado.py`.
*   Validação de entrada: verificar se a string pode ser convertida para float (ex: substituindo vírgula por ponto, verificando se é numérico após remoção do símbolo).
*   Loop `while` para repetir a entrada até ser válida.
*   Retorno do valor como `float`.

#### Solução:
```python
# No arquivo utilidadesCev/dado.py:
# def leiaDinheiro(msg):
#     valido = False
#     while not valido:
#         entrada = str(input(msg)).replace(',', '.').strip()
#         if entrada.isalpha() or entrada == "":
#             print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
#         else:
#             valido = True
#             return float(entrada)

# No programa principal (EX - 112.py):
# from utilidadesCev import moeda, dado
# preco = dado.leiaDinheiro('Digite o preço: R$')
# moeda.resumo(preco, 35, 22)
```

#### Explicação:

A função `leiaDinheiro()` no módulo `dado.py` solicita uma entrada e a valida para garantir que é um valor monetário (pode conter ',', '.', e ser convertível para float). Se inválida, pede novamente. O programa principal usa esta função para ler o preço.

#### Exemplo de Uso:
(No programa principal)
```
Digite o preço: R$abc
ERRO: "abc" é um preço inválido!
Digite o preço: R$150.50
(Mostra o resumo do EXE_110 com o preço R$150,50)
```

----

### Curso Python #23 - Tratamento de Erros e Exeções

----

### **EXE_113: Funções Aprofundadas em Python**

> Reescreva a função leiaint() que fizemos no **Desafio 104**, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

#### Conceitos-chave:
*   Tratamento de exceções `try-except`.
*   `ValueError` para falha na conversão para `int` ou `float`.
*   `KeyboardInterrupt` para lidar com interrupção do usuário.
*   Laço `while True` para repetir até entrada válida.
*   Funções `leiaInt()` e `leiaFloat()`.

#### Solução:
```python
# def leiaInt(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except (ValueError, TypeError):
#             print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
#             continue
#         except KeyboardInterrupt:
#             print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
#             return 0
#         else:
#             return n
# (Similar para leiaFloat, usando float() e tratando ValueError)
```
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 113.py correspondente.
```

#### Explicação:

As funções `leiaInt()` e `leiaFloat()` são criadas para ler números inteiros e de ponto flutuante, respectivamente. Elas usam blocos `try-except` para capturar `ValueError` (se a conversão falhar) e `KeyboardInterrupt` (se o usuário interromper), exibindo mensagens apropriadas e continuando o loop ou retornando um valor padrão.

#### Exemplo de Uso:
```
n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
# Se o usuário digitar 'abc' para inteiro: ERRO: Por favor, digite um número inteiro válido.
```

----

### **EXE_114: Site está acessível?**

> Crie um código em Pytho que teste se o site **Pudim** está acessivel pelo computador usado.

#### Conceitos-chave:
*   Módulo `urllib` ou `requests`.
*   Submódulo `urllib.request` e função `urlopen()`.
*   Tratamento de exceções `try-except` (`urllib.error.URLError`).

#### Solução:
```python
# import urllib
# import urllib.request
# try:
#     site = urllib.request.urlopen('http://www.pudim.com.br')
# except urllib.error.URLError:
#     print('O site Pudim não está acessível no momento.')
# else:
#     print('Consegui acessar o site Pudim com sucesso!')
#     # print(site.read()) # Opcional para ler o conteúdo
```
```python
# O código da solução para este exercício pode ser encontrado no arquivo EX - 114.py correspondente.
```

#### Explicação:

O programa tenta abrir a URL do site "pudim.com.br" usando `urllib.request.urlopen()`. Se a conexão for bem-sucedida, informa que o site está acessível. Se ocorrer um `URLError` (indicando que o site não pôde ser alcançado), informa que não está acessível.

#### Saída Esperada:
```
Consegui acessar o site Pudim com sucesso!
```
ou
```
O site Pudim não está acessível no momento.
```

----
