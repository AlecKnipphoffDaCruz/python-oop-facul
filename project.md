# Briefing — App "Monte seu Carro" (OOP em Python)

## Contexto

Atividade acadêmica de Python na UNISC chamada "Hora do Discovery". Cada grupo escolhe um tema, pesquisa e monta uma oficina interativa para apresentar à turma. Nosso tema é **Orientação a Objetos em Python**.

O app será usado como **experimento com a turma** durante a apresentação de 10 minutos — projetado na tela enquanto um integrante do grupo interage ao vivo.

---

## Story Telling

A ideia é ensinar OOP sem parecer uma aula. Em vez de explicar "o que é uma classe", o usuário simplesmente **monta um carro** — escolhendo chassi, motor, rodas e cor — e enquanto faz isso, o código Python aparece sendo construído ao vivo na tela.

No final, ele olha pro lado e percebe que acabou de instanciar um objeto, definir atributos e chamar métodos, sem perceber.

O mapeamento conceitual é direto:

| Ação do usuário | Conceito de OOP |
|---|---|
| Escolher o chassi, motor, rodas, cor | Atributos da classe `Carro` |
| Adicionar uma peça | Método sendo chamado |
| O carro sendo construído | Instanciação de um objeto |
| Peças agrupadas num carro | Encapsulamento |

---

## Layout

A tela é dividida em **3 colunas**:

### Coluna esquerda — Painel de opções
- Título: "Monte seu Carro dos Sonhos!"
- Seletores para cada parte do carro:
  - **Chassi** (ex: Esportivo, SUV, Sedã)
  - **Motor** (ex: 1.0, 2.0, Elétrico)
  - **Rodas** (ex: Aro 15, Aro 17, Aro 19)
  - **Cor** (ex: Vermelho, Preto, Branco, Azul)
- Botão: "Montar Carro"

### Coluna central — Visualização do carro
- Ilustração SVG do carro sendo montado em tempo real
- Cada escolha altera visualmente o carro (cor, rodas, etc.)

### Coluna direita — Código Python gerado
- Bloco de código que aparece e atualiza conforme o usuário escolhe as peças
- Mostra a classe sendo construída, os atributos sendo definidos e o objeto sendo instanciado
- Exemplo do output esperado:

```python
class Carro:
    def __init__(self):
        self.chassi = "Esportivo"
        self.motor = "2.0"
        self.rodas = "Aro 17"
        self.cor = "Vermelho"

meu_carro = Carro()
```

---

## Requisitos técnicos

- **Tecnologia:** HTML + CSS + JavaScript puro (single file, sem dependências externas)
- **Uso:** Projetado na tela durante a apresentação — não precisa funcionar no celular
- **Estilo visual:** Limpo, moderno, cores vibrantes — tom de app/ferramenta didática
- **Carro:** Ilustração SVG simples e estilizada, não realista
- **Código:** Syntax highlight simples na coluna direita (pode ser feito com CSS puro)

---

## O que NÃO precisa

- Responsividade mobile
- Backend ou servidor
- Salvar estado
- Múltiplos carros simultâneos

---

## Entregável esperado

Um único arquivo `index.html` que roda direto no navegador, com as 3 colunas funcionando — seleções à esquerda atualizam o carro no centro e o código à direita em tempo real.