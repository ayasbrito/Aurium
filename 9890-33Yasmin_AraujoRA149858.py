# YASMIN BRITO ARAUJO RA149858
import sys
from dataclasses import dataclass

@dataclass
class Depoimento:
    """
    Detalhes de um depoimento feito por um usuario para outro
    """
    de: str
    para: str
    texto: str

@dataclass
class Usuario:
    """
    Um usuario com amigos e aura.
    """
    apelido: str
    amigos: list[str]
    aura: int
    depoimentos: list[Depoimento]

def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é a
    lista de apelidos de uma linha (o primeiro é o da pessoa e os demais são os
    de seus amigos).
    Por exemplo, se o conteúdo do arquivo for
    Malbarbo Josiane Mauro Flavio
    Josiane Malbarbo
    a resposta produzida é
    [['Malbarbo', 'Josiane', 'Mauro', 'Flavio'], ['Josiane', 'Malbarbo']]
    '''
    try:
        with open(nome) as f:
            return [linha.split() for linha in f]
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)

def coloca_por_ultimo(lista: list[str], indice: int) -> list[str]:
    '''
    Coloca o amigo de usuario em ultimo em sua lista de *amigos_usuario* de acordo com seu *indice*, retornando a lista modificada.

    Exemplos:
    >>> coloca_por_ultimo(['Mateus', 'Pedro', 'Rafael', 'Lucas'], 1)
    ['Mateus', 'Lucas', 'Rafael', 'Pedro']

    >>> coloca_por_ultimo(['Lara', 'Natalia', 'Millena', 'Isa'], 0)
    ['Isa', 'Natalia', 'Millena', 'Lara']

    >>> coloca_por_ultimo(['Guilherme', 'Anna', 'Ana'], 2)
    ['Guilherme', 'Anna', 'Ana']
    '''
    aux = lista[len(lista)-1]
    lista[len(lista)-1] = lista[indice]
    lista[indice] = aux

    return lista
    
def agrupa_pessoas(lista: list[Usuario], i: int) -> list[str]:
    """
    Junta os apelidos de uma *lista* de Usuarios, retornando uma lista com os nomes.
    # decrementar
    Exemplos:
    >>> agrupa_pessoas(
    ...     [
    ...         Usuario(apelido='Yasmin', amigos=['Mateus'], aura=0, depoimentos=[]),
    ...         Usuario(apelido='Mateus', amigos=['Yasmin'], aura=0, depoimentos=[]),
    ...     ],
    ...     2,
    ... )
    ['Yasmin', 'Mateus']
    >>> agrupa_pessoas(
    ...     [
    ...         Usuario(apelido='Duda', amigos=[], aura=0, depoimentos=[]),
    ...         Usuario(apelido='Elise', amigos=[], aura=0, depoimentos=[]),
    ...         Usuario(apelido='Sergio', amigos=[], aura=0, depoimentos=[]),
    ...     ],
    ...     3,
    ... )
    ['Duda', 'Elise', 'Sergio']
    >>> agrupa_pessoas(
    ...     [
    ...         Usuario(
    ...             apelido='Pedro',
    ...             amigos=['Augusto', 'Mariana'],
    ...             aura=100,
    ...             depoimentos=[],
    ...         )
    ...     ],
    ...     1,
    ... )
    ['Pedro']

    # [lista[i - 1].apelido]
    """
    if i == 0:
        lista_nova = []
    else:
        lista_nova = agrupa_pessoas(lista, i - 1)
        lista_nova.append(lista[i - 1].apelido)

    return lista_nova

def ordena_decrescente(usuarios: list[Usuario]) -> None:
    """
    Ordena uma lista de *usuarios* pela sua aura e retorna ela ordenada.

    Exemplos:
    >>> ordena_crescente([Usuario(apelido='Yasmin', amigos=['Mateus'], aura=100, depoimentos=[]), Usuario(apelido='Mateus', amigos=['Yasmin'], aura=200, depoimentos=[])])
    
    >>> ordena_crescente([Usuario(apelido='Lara', amigos=[], aura=50, depoimentos=[]), Usuario(apelido='Natalia', amigos=[], aura=50, depoimentos=[]), Usuario(apelido='Isa', amigos=[], aura=100, depoimentos=[])])
    
    >>> ordena_crescente([Usuario(apelido='Guilherme', amigos=[], aura=0, depoimentos=[]), Usuario(apelido='Anna', amigos=[], aura=300, depoimentos=[]), Usuario(apelido='Ana', amigos=[], aura=300, depoimentos=[])])
    
    """
    for j in range(0, len(usuarios)):
        imax = j
        for i in range(j, len(usuarios)):
            if usuarios[imax].aura < usuarios[i].aura:
                imax = i
            if usuarios[imax].aura == usuarios[i].aura:
                if usuarios[imax].apelido > usuarios[i].apelido:
                    imax = i

        t = usuarios[imax]
        usuarios[imax] = usuarios[j]
        usuarios[j] = t

    return 

def verifica_lista(lista: list[str], pessoa: str, i: int) -> int:
    """
    Verifica a partir do indice *i*  de uma *lista* se uma *pessoa* esta presente nela. Retorna o indice dela na lista caso ela esteja presente ou -1, caso ela nao esteja na lista.

    Exemplos:
    >>> verifica_lista(['Yasmin', 'Mateus', 'Pedro', 'Rafael'], 'Pedro', 4)
    2
    >>> verifica_lista(['Lara', 'Natalia', 'Millena'], 'Gribeler', 3)
    -1
    >>> verifica_lista(['Duda', 'Elise', 'Sergio'], 'Duda', 3)
    0
    """
    
    if i == 0:
        indice = -1
    else:
        if lista[i - 1] == pessoa:
            indice = i - 1
        else:
            indice = verifica_lista(lista, pessoa, i - 1)

    return indice

def fazer_amizade(usuarios: list[Usuario], indice_usuario: int, indice_amigo: int) -> None:
    """
    Adiciona um amig com indice *indice_amigo* na lista de amigos de um dos *usuarios* com indice *indice_usuario*. Alem disso, a funcao atualiza a aura de ambos para +100.

    Exemplos:
    >>> fazer_amizade([Usuario(apelido='Yasmin', amigos=[], aura=0, depoimentos=[]), Usuario(apelido='Mateus', amigos=[], aura=0, depoimentos=[])], 0, 1)
    
    >>> fazer_amizade([Usuario(apelido='Duda', amigos=['Elise'], aura=100, depoimentos=[]), Usuario(apelido='Elise', amigos=['Duda'], aura=100, depoimentos=[]), Usuario(apelido='Sergio', amigos=[], aura=0, depoimentos=[])], 0, 2)
    
    >>> fazer_amizade([Usuario(apelido='Guilherme', amigos=[], aura=0, depoimentos=[]), Usuario(apelido='Anna', amigos=[], aura=0, depoimentos=[])], 0, 1)
    
    """
    usuarios[indice_usuario].amigos.append(usuarios[indice_amigo].apelido)
    usuarios[indice_usuario] = atualiza_aura(usuarios[indice_usuario], 100)

    usuarios[indice_amigo].amigos.append(usuarios[indice_usuario].apelido)
    usuarios[indice_amigo] = atualiza_aura(usuarios[indice_amigo], 100)

    return 

def desfazer_amizade(usuarios: list[Usuario], indice_usuario: int, indice_amigo: int) -> None:
    """
    Retira um amigo com indice *indice_amigo* da lista de amizade de um dos *usuarios* com indice *indice_usuario*. Alem disso, a funcao atualiza a aura de ambos para -150.

    Exemplos:
    >>> desfazer_amizade([Usuario(apelido='Yasmin', amigos=['Mateus', 'Pedro'], aura=200, depoimentos=[]), Usuario(apelido='Mateus', amigos=['Yasmin'], aura=100, depoimentos=[])], 0, 1)
    
    >>> desfazer_amizade([Usuario(apelido='Lara', amigos=['Natalia'], aura=100, depoimentos=[]), Usuario(apelido='Natalia', amigos=['Lara'], aura=100, depoimentos=[])], 0, 1)
    
    >>> desfazer_amizade([Usuario(apelido='Duda', amigos=['Elise', 'Sergio'], aura=300, depoimentos=[]), Usuario(apelido='Elise', amigos=['Duda'], aura=100, depoimentos=[]), Usuario(apelido='Sergio', amigos=['Duda'], aura=100, depoimentos=[])], 0, 2)
    
    """
    indice_lista_amigo_usuario = verifica_lista(usuarios[indice_usuario].amigos, usuarios[indice_amigo].apelido, len(usuarios[indice_usuario].amigos))
    indice_lista_amigo = verifica_lista(usuarios[indice_amigo].amigos, usuarios[indice_usuario].apelido, len(usuarios[indice_amigo].amigos))

    coloca_por_ultimo(usuarios[indice_usuario].amigos, indice_lista_amigo_usuario)
    usuarios[indice_usuario].amigos.pop()
    usuarios[indice_usuario] = atualiza_aura(usuarios[indice_usuario], -150)

    coloca_por_ultimo(usuarios[indice_amigo].amigos, indice_lista_amigo)
    usuarios[indice_amigo].amigos.pop()
    usuarios[indice_amigo] = atualiza_aura(usuarios[indice_amigo], -150)

    return 

def atualiza_aura(pessoa: Usuario, n: int) -> Usuario:
    """
    Soma uma quantidade *n* à aura de uma *pessoa*, retornando a aura desse usuario atualizada.

    Exemplos:
    >>> atualiza_aura(Usuario(apelido='Yasmin', amigos=['Mateus'], aura=0, depoimentos=[]), 100)
    Usuario(apelido='Yasmin', amigos=['Mateus'], aura=100, depoimentos=[])

    >>> atualiza_aura(Usuario(apelido='Lara', amigos=['Natalia'], aura=200, depoimentos=[]), -150)
    Usuario(apelido='Lara', amigos=['Natalia'], aura=50, depoimentos=[])

    >>> atualiza_aura(Usuario(apelido='Guilherme', amigos=[], aura=50, depoimentos=[]), 250)
    Usuario(apelido='Guilherme', amigos=[], aura=300, depoimentos=[])
    """
    aura_nova = pessoa.aura + n
    pessoa.aura = aura_nova

    return pessoa

def remove_espacos(texto: str) -> str:
    """
    Remove os espacos do comeco e do fim de um *texto* e retorna ele formatado.

    >>> remove_espacos('yas   ')
    'yas'
    >>> remove_espacos('   yas')
    'yas'
    >>> remove_espacos('   ')
    ''
    """
    inicio = 0
    while inicio < len(texto) and texto[inicio] == ' ':
        inicio += 1

    fim = len(texto) - 1
    while fim >= 0 and texto[fim] == ' ':
        fim -= 1

    if inicio > fim:
        texto_formatado = ''
    else:
        texto_formatado = texto[inicio : fim + 1]
 
    return texto_formatado

def procura_usuario(usuarios: list[Usuario], nome: str) -> int:
    """
    Procura um usuario com *nome* nos *usuarios* e retorna seu indice. Retorna -1 se ele nao estiver na lista ou, caso ele esteja presente na lista, ela retorna seu indice nessa lista.

    Exemplos:
    >>> procura_usuario([Usuario(apelido='Yasmin', amigos=['Rafael'], aura=0, depoimentos=[]), Usuario(apelido='Rafael', amigos=['Yasmin'], aura=0, depoimentos=[])], 'Yasmin')
    0
    >>> procura_usuario([Usuario(apelido='Lara', amigos=[], aura=0, depoimentos=[]), Usuario(apelido='Natalia', amigos=[], aura=0, depoimentos=[])], 'Natalia')
    1
    >>> procura_usuario([Usuario(apelido='Duda', amigos=[], aura=0, depoimentos=[]), Usuario(apelido='Elise', amigos=[], aura=0, depoimentos=[])], 'Sergio')
    -1
    """
    i = 0
    achou = False
    indice = -1
    while not achou and i < len(usuarios):
        if usuarios[i].apelido == nome:
            achou = True
            indice = i
        i = i + 1

    return indice

def verifica_reciprocidade(usuarios: list[Usuario]) -> None:
    """
    Verifica se a amizade entre os *usuarios* eh reciproca. Caso um usuario tenha outro como amigo mas nao seja correspondido, adiciona a reciprocidade.

    Exemplos:
    >>> verifica_reciprocidade([Usuario(apelido='Yasmin', amigos=['Diogo'], aura=0, depoimentos=[]), Usuario(apelido='Diogo', amigos=[], aura=0, depoimentos=[])])
    
    >>> verifica_reciprocidade([Usuario(apelido='Lara', amigos=['Natalia', 'Isa'], aura=0, depoimentos=[]), Usuario(apelido='Natalia', amigos=['Lara'], aura=0, depoimentos=[]), Usuario(apelido='Isa', amigos=[], aura=0, depoimentos=[])])
    
    >>> verifica_reciprocidade([Usuario(apelido='Duda', amigos=['Elise'], aura=0, depoimentos=[]), Usuario(apelido='Elise', amigos=['Duda'], aura=0, depoimentos=[])])
    
    """
    for usuario in usuarios:
        indice_usuario = procura_usuario(usuarios, usuario.apelido)
        amigos = usuarios[indice_usuario].amigos
        for i in range(len(amigos)):
            for j in range(len(usuarios)):
                if usuarios[j].apelido == amigos[i]:
                    indice = verifica_lista(usuarios[j].amigos, usuario.apelido, len(usuarios[j].amigos))
                    if indice == -1:
                        usuarios[j].amigos.append(usuario.apelido)
                        atualiza_aura(usuarios[j], 100)
                        atualiza_aura(usuarios[indice_usuario], 100)

    return 

def amigo_usuario(usuarios: list[Usuario], usuario: Usuario) -> None:
    """
    Cria o usuario do amigo de um *usuario*, caso ele nao exista em sua lista de amigos e o adiciona nos *usuarios*.

    Exemplos:
    >>> amigo_usuario([Usuario(apelido='Yasmin', amigos=['Mateus'], aura=0, depoimentos=[])], Usuario(apelido='Yasmin', amigos=['Mateus'], aura=0, depoimentos=[]))
    
    >>> amigo_usuario([Usuario(apelido='Duda', amigos=['Elise', 'Sergio'], aura=0, depoimentos=[])], Usuario(apelido='Duda', amigos=['Elise', 'Sergio'], aura=0, depoimentos=[]))
    
    >>> amigo_usuario([Usuario(apelido='Guilherme', amigos=['Anna'], aura=0, depoimentos=[]), Usuario(apelido='Anna', amigos=[], aura=0, depoimentos=[])], Usuario(apelido='Guilherme', amigos=['Anna'], aura=0, depoimentos=[]))
    
    """
    for amigo in usuario.amigos:
        indice = procura_usuario(usuarios, amigo)
        if indice == -1:
            cria_usuario(usuarios, amigo)
            
    return 

def cria_usuario(usuarios: list[Usuario], usuario: str) -> Usuario:
    """
    Cria um usuario com o nome de *usuario* desejado e adiciona ele na lista de *usuarios*.

    Exemplos:
    >>> cria_usuario([], 'Yasmin')
    [Usuario(apelido='Yasmin', amigos=[], aura=0, depoimentos=[])]
    >>> cria_usuario([Usuario(apelido='Lara', amigos=[], aura=0, depoimentos=[])], 'Natalia')
    [Usuario(apelido='Lara', amigos=[], aura=0, depoimentos=[]), Usuario(apelido='Natalia', amigos=[], aura=0, depoimentos=[])]
    >>> cria_usuario([], 'Duda')
    [Usuario(apelido='Duda', amigos=[], aura=0, depoimentos=[])]
    """  
    usuario_novo = Usuario(usuario, [], 0, [])
    usuarios.append(usuario_novo)

    return usuario_novo

def importa_amizades(usuarios: list[Usuario], arquivo: str) -> None:
    """
    Importa amizades de um *arquivo* para os *usuarios*

    >>> importa_amizades([], 'amizades.txt')

    """
    # pessoas = le_arquivo(arquivo)
    pessoas = le_arquivo(arquivo)

    for pessoa in pessoas:
        indice_usuario = procura_usuario(usuarios, pessoa[0])
        if indice_usuario == -1:
            usuario_novo = cria_usuario(usuarios, pessoa[0])
        else:
            usuario_novo = usuarios[indice_usuario]

        if len(pessoa) > 1:
            qtd_amigos = len(pessoa[1:])
            usuario_novo.amigos = pessoa[1:]
            atualiza_aura(usuario_novo, qtd_amigos * 100)
            amigo_usuario(usuarios, usuario_novo)
            
    verifica_reciprocidade(usuarios)

    return 

def depoimento(usuarios: list[Usuario], indice_usuario: int, indice_amigo: int, depoimento: str) -> None:
    """
    Coloca na lista de depoimentos de um amigo com indice *indice_amigo* um *depoimento* enviado por um usuario com indice *indice_usuario*, atualizando a aura do usuario para +50 e a do amigo que recebeu o depoimento para +200.

    Exemplos:
    >>> depoimento([Usuario(apelido='Yasmin', amigos=['Mateus'], aura=100, depoimentos=[]), Usuario(apelido='Mateus', amigos=['Yasmin'], aura=100, depoimentos=[])], 0, 1, 'Voce eh top')

    >>> depoimento([Usuario(apelido='Lara', amigos=['Natalia'], aura=50, depoimentos=[]), Usuario(apelido='Natalia', amigos=['Lara'], aura=50, depoimentos=[])], 0, 1, 'te amoo lindaa!')

    >>> depoimento([Usuario(apelido='Duda', amigos=['Elise'], aura=0, depoimentos=[]), Usuario(apelido='Elise', amigos=['Duda'], aura=0, depoimentos=[])], 0, 1, 'nao quero mais ser sua amiga')
    
    """
    depoimento_novo = Depoimento(usuarios[indice_usuario].apelido, usuarios[indice_amigo].apelido, depoimento)
    atualiza_aura(usuarios[indice_usuario], 50)
    atualiza_aura(usuarios[indice_amigo], 200)
    usuarios[indice_amigo].depoimentos.append(depoimento_novo)

    return 

def ranking_aura(usuarios: list[Usuario]) -> str:
    """
    Retorna uma mensagem de texto mostrando a classificacao dos *usuarios* com base na sua aura em ordem decrescente (do mais alto para o mais baixo). Em caso de empate, o criterio de desempate eh que apelido vem primeiro na ordem alfabetica.

    Exemplos:
    >>> ranking_aura([Usuario(apelido='Yasmin', amigos=[], aura=300, depoimentos=[]), Usuario(apelido='Mateus', amigos=[], aura=100, depoimentos=[]), Usuario(apelido='Pedro', amigos=[], aura=200, depoimentos=[])])
    '1lugar -> Yasmin\\n2lugar -> Pedro\\n3lugar -> Mateus\\n'

    >>> ranking_aura([Usuario(apelido='Lara', amigos=[], aura=50, depoimentos=[]), Usuario(apelido='Natalia', amigos=[], aura=50, depoimentos=[])])
    '1lugar -> Lara\\n2lugar -> Natalia\\n'

    >>> ranking_aura([Usuario(apelido='Guilherme', amigos=[], aura=0, depoimentos=[])])
    '1lugar -> Guilherme\\n'
    """
    ordena_decrescente(usuarios)
    texto = ''

    for i in range(len(usuarios)):
        texto = texto + str(i + 1) + 'o lugar -> '+ str(usuarios[i].apelido) + '\n'
        
    return texto

def recomendacao_amizade(usuarios: list[Usuario], indice_usuario: int) -> list[str]:
    """
    Faz uma recomendacao de amizade para um usuario dos *usuarios* e indice *indice_usuario*, criando uma lista de acordo com os amigos dos seus amigos, caso o usuario ainda nao seja amigo de algum deles.

    Exemplos:
    >>> recomendacao_amizade([Usuario(apelido='Yasmin', amigos=['Mateus'], aura=0, depoimentos=[]), Usuario(apelido='Mateus', amigos=['Yasmin', 'Pedro'], aura=0, depoimentos=[]), Usuario(apelido='Pedro', amigos=['Mateus'], aura=0, depoimentos=[])], 'Yasmin')
    ['Pedro']

    >>> recomendacao_amizade([Usuario(apelido='Lara', amigos=['Natalia'], aura=0, depoimentos=[]), Usuario(apelido='Natalia', amigos=['Lara', 'Isa'], aura=0, depoimentos=[]), Usuario(apelido='Isa', amigos=['Natalia'], aura=0, depoimentos=[])], 'Lara')
    ['Isa']

    >>> recomendacao_amizade([Usuario(apelido='Duda', amigos=['Elise'], aura=0, depoimentos=[]), Usuario(apelido='Elise', amigos=['Duda'], aura=0, depoimentos=[])], 'Duda')
    []
    """
    lista_recomendacao = []

    for amigo in usuarios[indice_usuario].amigos:
        indice_amigo = procura_usuario(usuarios, amigo)
        amigos = usuarios[indice_amigo].amigos
        if amigos != []:
            for amigo_amigo in amigos:
                indice_amigo_usuario = verifica_lista(usuarios[indice_usuario].amigos, amigo_amigo, len(usuarios[indice_usuario].amigos))
                if amigo_amigo != usuarios[indice_usuario].apelido and indice_amigo_usuario == -1:
                    lista_recomendacao.append(amigo_amigo)

    return lista_recomendacao

def main() -> int:
    usuarios = []
    opcoes_validas = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    modo = -1
    
    while modo != 0:
        print('------ Aurium ------')
        print('[1] Importar amizades')
        print('[2] Criar usuário')
        print('[3] Fazer amizade')
        print('[4] Desfazer amizade')
        print('[5] Mostrar detalhes de um usuario')
        print('[6] Fazer depoimento')
        print('[7] Recomendações de amizade')
        print('[8] Ranking dos usuários pela aura')
        print('[0] Sair\n')            

        opcao = input('Escolha uma opção entre 0 e 8: ')

        modo = -1

        for i in range(len(opcoes_validas)):
            if opcao == opcoes_validas[i]:
                modo = int(opcao)

        if modo == 1:
            # importar amizades
            arquivo = input('\nDigite o nome do arquivo que deseja importar: ')

            importa_amizades(usuarios, arquivo)
            
            if usuarios == [] or not arquivo:
                print('O arquivo que vc digitou eh invalido. Tente novamente \n')
            else:
                print('Usuarios importados com sucesso! Estes sao os usuarios da plataforma agora: ', usuarios)

        elif modo == 2:
            # criar usuario
            usuario = input('\nDigite o nome que deseja por em seu apelido: ')
            usuario_novo_formatado = remove_espacos(usuario)
            
            indice_usuario = procura_usuario(usuarios, usuario_novo_formatado)

            if indice_usuario == -1 and usuario_novo_formatado != '':
                usuario_novo = cria_usuario(usuarios, usuario_novo_formatado)
                print('\nUsuario foi criado com sucesso!: ', usuario_novo, '\nTente fazer uma amizade agora!!\n\nEstes sao todos os usuarios da plataforma agora: ', agrupa_pessoas(usuarios, len(usuarios)), '\n')
            else:
                print('Usuario incorreto ou ele ja existe! Tente novamente')

        elif modo == 3:
            # fazer amizades
            usuario = input('\nDigite o se nome de usuario: ')
            usuario_formatado = remove_espacos(usuario)
            
            indice_usuario = procura_usuario(usuarios, usuario_formatado)
            
            if indice_usuario != -1:
                print("\nEstes sao os seus amigos atualmente: ", usuarios[indice_usuario].amigos)

                amigo = input('\nDigite o nome de seu novo amigo: ')
                amigo_formatado = remove_espacos(amigo)

                indice_amigo = procura_usuario(usuarios, amigo_formatado)
                indice_lista_amizade = verifica_lista(usuarios[indice_usuario].amigos, usuarios[indice_amigo].apelido, len(usuarios[indice_usuario].amigos))

                if indice_lista_amizade == -1 and indice_amigo != -1:
                    fazer_amizade(usuarios, indice_usuario, indice_amigo)
                    print("Amizade adicionada com sucesso! Voce e seu amigo ganharam +100 de aura.\n", 'Estes sao seus amigos agora: ', usuarios[indice_usuario].amigos, '\n')
                else:
                    print('\nEste amigo ja existe na sua lista de amigos. Tente adicionar outra pessoa.\n')
            else:
                print('\nUsuario inexistente ou amigo nao exitente na plataforma. Tente novamente\n')

        elif modo == 4:
            # desfazer amizades:
            usuario = input('\nDigite o se nome de usuario: ')
            indice_usuario = procura_usuario(usuarios, usuario_formatado)
            amigo = input('\nDigite o nome do amigo que deseja remover: ')

            usuario_formatado = remove_espacos(usuario)
            amigo_formatado = remove_espacos(amigo)

            indice_amigo = procura_usuario(usuarios, amigo_formatado)

            if indice_usuario != -1:
                print("\nEstes sao os seus amigos atualmente: ", usuarios[indice_usuario].amigos)

                amigo = input('\nDigite o nome do amigo que deseja remover: ')
                amigo_formatado = remove_espacos(amigo)

                indice_amigo = procura_usuario(usuarios, amigo_formatado)
                indice_lista_amizade = verifica_lista(usuarios[indice_usuario].amigos, usuarios[indice_amigo].apelido, len(usuarios[indice_usuario].amigos))
                
                if indice_lista_amizade != -1 and indice_amigo != -1:
                    desfazer_amizade(usuarios, indice_usuario, indice_amigo)
                    print("Amizade removida com sucesso! Voce e seu amigo perderam 150 de aura.", '\nEstes sao seus amigos agora:', usuarios[indice_usuario].amigos, '\n')
                else:
                    print('\nEste amigo nao existe na sua lista de amigos. Tente mandar para outra pessoa.\n')
            else:
                print('\nUsuario inexistente ou amigo nao exitente na plataforma. Tente novamente\n')

        elif modo == 5:
            if usuarios != []:
                print('\nEstes sao os usuarios ja existentes na plataforma: ', agrupa_pessoas(usuarios, len(usuarios)))
                usuario = input("Digite o nome de usuario que quer ver os detalhes: ")
                usuario_formatado = remove_espacos(usuario)
                indice_usuario = procura_usuario(usuarios, usuario_formatado)

                if indice_usuario != -1:
                    print('\nApelido:', usuarios[indice_usuario].apelido)
                    print('Amigos', usuarios[indice_usuario].amigos)
                    print('Aura', usuarios[indice_usuario].aura)
                    print('Depoimentos', usuarios[indice_usuario].depoimentos, '\n')
                else:
                    print('\nUsuario inexistente ou amigo nao exitente na plataforma. Tente novamente\n')
            else:
                print("\nNao existem usuarios na plataforma ainda. Tente criar um usuario para ver os detalhes")
        elif modo == 6:
            # depoimentos para amigos:
            if usuarios != []:
                usuario = input('\nDigite seu nome de usuario: ')
                amigo = input('\nDigite o nome do amigo que deseja mandar o depoimento: ')
                depoimento_texto = input('\nDigite o seu depoimento : ')
                  
                depoimento_formatado = remove_espacos(depoimento_texto)
                usuario_formatado = remove_espacos(usuario)
                amigo_formatado = remove_espacos(amigo)

                indice_usuario = procura_usuario(usuarios, usuario_formatado)
                indice_amigo = procura_usuario(usuarios, amigo_formatado)

                if indice_usuario != -1 and indice_amigo != -1:
                    indice_lista_amizade = verifica_lista(usuarios[indice_usuario].amigos, usuarios[indice_amigo].apelido, len(usuarios[indice_usuario].amigos))
                    if indice_lista_amizade != -1:
                        if depoimento_texto != '':
                            depoimento(usuarios, indice_usuario, indice_amigo, depoimento_formatado)
                            print('\nDepoimento enviado com sucesso para', usuarios[indice_amigo].apelido, '\n')
                        else:
                            print('\nDepoimento invalido. Tente novamente\n')
                    else:
                        print('\nEste amigo nao existe na sua lista de amigos.\n')
                else:
                    print('\nUsuario inexistente na plataforma. Tente novamente\n')
            else:
                print("\nNao existem usuarios na plataforma ainda. Tente criar primeiro para ver as amizades recomendadas.\n")
        elif modo == 7:
            # recomendacao de amigos:
            usuario = input('\nDigite o seu nome de usuario: ')
            usuario_novo_formatado = remove_espacos(usuario)
            
            indice_usuario = procura_usuario(usuarios, usuario_novo_formatado)

            if indice_usuario != -1:
                lista_recomendacao = recomendacao_amizade(usuarios, indice_usuario)
                if lista_recomendacao != []:
                    print('\nSuas recomencoes de amizade sao: ', lista_recomendacao, '\n')
                else:
                    print('\nVoce nao tem recomendacoes de amizade.\n')
            else:
                print('\nUsuario inexistente na plataforma. Tente novamente\n')
        elif modo == 8:
            # ranking de aura:
            if usuarios != []:
                print('\nRANKING POR AURA DOS USUARIOS - AURIUM:')
                print(ranking_aura(usuarios))
            else:
                print("\nNao existem usuarios na plataforma ainda.\n")
        elif modo == 0:
            print("\nVoce saiu do Aurium! Estaremos esperando seu acesso novamente. =) \n")
        else:
            print("\nOpção inválida! Digite um número de 0 a 8.\n")

if __name__ == '__main__':
    main()