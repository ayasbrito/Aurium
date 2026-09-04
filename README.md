Aurium | Simulador de Rede Social em Terminal (CLI)

O **Aurium** é um sistema de rede social desenvolvido em Python focado na simulação de conexões entre usuários, relacionamentos de amizade, gamificação via pontuação de Aura e recomendação de conexões baseada em grafos relacionais.

-----
Tecnologias e Conceitos de Engenharia de Software
- **Linguagem:** Python 3.10+
- **Estruturas de Dados:** Implementação de `dataclasses`, manipulação de listas dinâmicas e verificação manual de ponteiros/índices.
- **Algoritmos de Ordenação:** Algoritmo de ordenação personalizada (*Selection Sort*) para cálculo de rankings com critério de desempate por ordem alfabética.
- **Modelagem de Grafos Relacionais:** Representação da rede social onde os usuários funcionam como nós e as amizades estabelecem as arestas do grafo.
- **Qualidade & Validação:** Tipagem estática (`typing`), tratamento de exceções de leitura (`try/except`) e testes integrados via *Doctests*.
-----
[Funcionalidades Principais
1. **Importação de Amizades via Arquivo:** Leitura e interpretação de arquivos `.txt` externos contendo grafos de conexões pré-existentes.
2. **Gestão de Amizades & Reciprocidade:** Mapeamento de novas amizades com verificação dinâmica para garantir a correspondência mútua na rede.
3. **Sistema de Gamificação (Aura):** Cálculo automático do nível de reputação (Aura) dos usuários, que aumenta ou diminui conforme suas interações (amizades, depoimentos e remoção de conexões).
4. **Algoritmo de Recomendação:** Sugestão inteligente de novas conexões baseada em conexões de 2º grau (*amigos de amigos*).
5. **Ranking Global:** Exibição ordenada dos usuários com maior nível de Aura na plataforma.
-----
Estrutura de Arquivos

```text
├── Aurium.py  # Código-fonte principal com lógica e CLI
├── amizades.txt                   # Arquivo de exemplo de dados de entrada de exemplo
└── README.md                      # Documentação do projeto
