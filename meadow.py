## 2.1.1 TAD posicao: Representam posicoes do tipo (x, y), em que x e y sao valores positivos que podem ser arbitrariamente grandes

#Construtor
def cria_posicao(x, y):
    '''
    int, int --> posicao
    Recebe dois numeros inteiros maiores ou iguais a 0 e converte-os numa posicao (x, y)
    '''
    if type(x) != int or type(y) !=int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return((x, y))

def cria_copia_posicao(p):
    '''
    posicao --> posicao
    Recebe uma posicao e retorna uma copia dessa posicao
    '''
    return cria_posicao(obter_pos_x(p), obter_pos_y(p))

#Seletores
def obter_pos_x(p):
    '''
    posicao --> int
    Recebe uma posicao e retorna a sua componente x
    '''
    return(p[0])

def obter_pos_y(p):
    '''
    posicao --> int
    Recebe uma posicao e retorna a sua componente y
    '''
    return(p[1])

#Reconhecedor
def eh_posicao(arg):
    '''
    universal --> boolean
    Recebe um argumento e retorna True se e so se o argumento corresponder a um TAD posicao,
    caso contrario retorna False
    '''
    return (type(arg) == tuple and len(arg) == 2 and obter_pos_x(arg) >= 0 and obter_pos_y(arg) >= 0)
    
#Teste
def posicoes_iguais(p1, p2):
    '''
    posicao, posicao --> booleano
    Recebe duas posicoes e retorna True caso elas sejam ambas posicoes e iguais, caso
    contrario retorna False
    '''
    return (eh_posicao(p1) and eh_posicao(p2) and obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2))
    
#Transformador
def posicao_para_str(p):
    '''
    posicao --> string
    Recebe uma posicao e retorna a sua string correspondente na forma '(x, y)', em que
    x e y sao as coordenadas da posicao
    '''
    return('(' + str(obter_pos_x(p)) + ', ' + str(obter_pos_y(p)) + ')')
    
    
#Funcoes de alto nivel
def obter_posicoes_adjacentes(p):
    '''
    posicao --> tuplo
    Recebe uma posicao e retorna um tuplo contendo todas as posicoes adjacentes a essa
    posicao
    '''
    posicoes_adjacentes = ()
    if obter_pos_y(p) > 0:
        posicoes_adjacentes += (cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1),)
    posicoes_adjacentes += (cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p)),)
    posicoes_adjacentes += (cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1),)
    if obter_pos_x(p) > 0:
        posicoes_adjacentes += (cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p)),)
    return posicoes_adjacentes


def ordenar_posicoes(t):
    '''
    tuplo --> tuplo
    Recebe um tuplo contendo diversas posicoes e retorna um tuplo com as mesmas posicoes
    de entrada ordendas segundo as ordens de leitura do prado
    '''
    j = 1
    l = list(t)
    while j < len(l):
        if obter_pos_y(l[j - 1]) > obter_pos_y(l[j]):
            l[j - 1], l[j] = l[j], l[j - 1]
            j = 1
        elif obter_pos_y(l[j - 1]) == obter_pos_y(l[j]):
            if obter_pos_x(l[j - 1]) > obter_pos_x(l[j]):
                l[j - 1], l[j] = l[j], l[j - 1]
                j = 1
            else:
                j += 1
        else:
            j += 1
    return(tuple(l))



##2.1.2: TAD Animal: Representam os animais do prado, que podem ser presas ou predadores. Todos os animais sao caracterizados pelos atributos especie, idade e frequencia de reproducao, sendo que os predadores sao tambem caracterizados pela sua fome e frequencia de alimentacao.

#Construtores
def cria_animal(s, r, a):
    '''
    string, int, int --> animal
    Recebe uma string correspondente a especie e dois inteiros positivos ou nulos correspondentes
    a frequencia de reproducao e a frequencia de alimentacao e retorna o animal
    '''
    if type(s) != str or type(r) != int or type(a) != int or len(s) < 1 or r <= 0 or a < 0:
        raise ValueError('cria_animal: argumentos invalidos')
    return({'s': s, 'r': r, 'a': a, 'i': 0, 'f': 0})
    
def cria_copia_animal(a):
    '''
    animal --> animal
    Recebe um animal e retorna uma copia desse animal
    '''
    return cria_animal(obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a))

#Seletores
def obter_especie(a):
    '''
    animal --> string
    Recebe um animal e retorna a string correspondente a sua especie
    '''
    return a['s']

def obter_freq_reproducao(a):
    '''
    animal --> int
    Recebe um animal e retorna a sua frequencia de reproducao
    '''
    return a['r']

def obter_freq_alimentacao(a):
    '''
    animal --> int
    Recebe um animal e retorna a sua frequencia de alimentacao
    '''
    return a['a']

def obter_idade(a):
    '''
    animal --> int
    Recebe um animal e retorna a sua idade
    '''
    return a['i']

def obter_fome(a):
    '''
    animal --> int
    Recebe um animal e retorna a sua fome
    '''
    return a['f']

#Modificadores
def aumenta_idade(a):
    '''
    animal --> animal
    Recebe um animal e retorna-o com a sua idade incrementada em uma unidade
    '''
    a['i'] = obter_idade(a) + 1
    return a

def reset_idade(a):
    '''
    animal --> animal
    Recebe um animal e retorna-o com a sua idade igual a 0
    '''
    a['i'] = 0
    return a

def aumenta_fome(a):
    '''
    animal --> animal
    Recebe um animal e retorna-o com a sua fome incrementada em uma unidade
    '''    
    if obter_freq_alimentacao(a) > 0:
        a['f'] = obter_fome(a) + 1
    return a

def reset_fome(a):
    '''
    animal --> animal
    Recebe um animal e retorna-o com a sua fome igual a 0
    '''    
    if obter_freq_alimentacao(a) > 0:
        a['f'] = 0
    return a

#Reconhecedores
def eh_animal(arg):
    '''
    universal --> boolean
    Recebe um argumento e retorna True se e so se o argumento corresponder a um TAD
    animal, se não retorna False
    '''
    if type(arg) == dict and sorted(arg.keys()) == sorted(['s', 'r', 'a', 'i', 'f']):
        if type(obter_especie(arg)) == str and type(obter_freq_reproducao(arg)) == type(obter_freq_alimentacao(arg)) == type(obter_idade(arg)) == type(obter_fome(arg)) == int:
            return True
    else: 
        return False
    
def eh_predador(arg):
    '''
    universal --> boolean
    Recebe um atgumento e retorna True caso seja um animal predador (ou seja, se a
    sua frequencia de alimentacao for maior do que 0), se nao retorna False
    '''
    return (eh_animal(arg) and obter_freq_alimentacao(arg) > 0)
    
def eh_presa(arg):
    '''
    universal --> boolean
    Recebe um atgumento e retorna True caso seja um animal presa (ou seja, se a
    sua frequencia de alimentacao for igual a 0), se nao retorna False
    '''    
    return (eh_animal(arg) and obter_freq_alimentacao(arg) == 0)

#Testes
def animais_iguais(a1, a2):
    '''
    animal, animal --> boolean
    Recebe dois animais e retorna True se os dois animais forem iguais e False caso
    nao sejam
    '''
    match = 0
    if eh_animal(a1) == eh_animal(a2) == True:
        for i in a1.keys():
            if a1[i] == a2[i]:
                match += 1
    return match == 5


#Transformadores
def animal_para_char(a):
    '''
    animal --> string
    Recebe um animal e retorna uma string correspondente ao carater que o representa
    (a primeira letra do nome da sua especie, maiuscula se for predador, minuscula se
    for presa)
    '''
    char = obter_especie(a)[0]
    if eh_predador(a):
        if 64 < ord(char) < 91:
            return char
        if 96 < ord(char) < 123:
            return chr(ord(char) - 32)
    else:
        if 64 < ord(char) < 91:
            return chr(ord(char) + 32)
        if 96 < ord(char) < 123:
            return char

def animal_para_str(a):
    '''
    animal --> string
    Recebe um animal e retorna a string que o representa, formada da seguinte maneira:
    <nome da especie> [<idade>/<freq reproducao>;<fome>/<freq alimentacao>] (predador)
    <nome da especie> [<idade>/<freq reproducao>] (presa
    '''
    if eh_predador(a):
        return obter_especie(a) + ' [' + str(obter_idade(a)) + '/' + str(obter_freq_reproducao(a)) + ';' + str(obter_fome(a)) + '/' + str(obter_freq_alimentacao(a)) + ']' 
    else:
        return obter_especie(a) + ' [' + str(obter_idade(a)) + '/' + str(obter_freq_reproducao(a)) + ']' 
    return None


#Funcoes de alto nivel
def eh_animal_fertil(a):
    '''
    animal --> boolean
    Recebe um animal e indica se o animal esta fertil, ou seja, se a sua idade atingiu
    a sua frequencia de reproducao e se vai multiplicar
    '''
    return obter_idade(a) >= obter_freq_reproducao(a)

def eh_animal_faminto(a):
    '''
    animal --> boolean
    Recebe um animal e indica se o predador esta faminto, ou seja, se a sua fome atingiu
    a sua frequencia de alimentacao e se vai morrer de fome
    '''
    if eh_predador(a):
        return obter_fome(a) == obter_freq_alimentacao(a)
    else:
        return False
    
def reproduz_animal(a):
    '''
    animal --> animal
    Recebe um animal e devolve um novo animal igual ao de entrada com idade e fome (se for
    predador) iguais a 0, alterando a idade do animal de entrada para 0
    '''
    reset_idade(a) 
    novo_animal = cria_copia_animal(a)
    if eh_predador(novo_animal):
        reset_fome(novo_animal)
    return novo_animal




## 2.1.3 TAD Prado: Representam o proprio prado, o mapa do ecossistema onde se deslocam e interagem os animais

#Construtores
def cria_prado(d, r, a, p):
    '''
    posicao, tuplo, tuplo, tuplo --> prado
    Recebe um tuplo contendo a posicao da montanha do canto inferior direito do prado, um
    tuplo com 0 ou mais posicoes correspondentes aos rochedos que nao sao as montanhas delimitantes
    do prado, um tuplo com 1 ou mais animais e um tuplo com as mesmas dimensoes com as posicoes
    ocupadas pelos animais, retornando o prado
    '''
    rochas, animais = 0, 0
    if eh_posicao(d) and type(r) == type(a) == type(p) == tuple:
        for pos in r:
            if eh_posicao(pos) and 0 < obter_pos_x(pos) < obter_pos_x(d) and 0 < obter_pos_y(pos) < obter_pos_y(d):
                rochas += 1
        if len(a) == len(p):
            for q in range(0, len(a)):
                if eh_animal(a[q]) and eh_posicao(p[q]) and 0 < obter_pos_x(p[q]) < obter_pos_x(d) and 0 < obter_pos_y(p[q]) < obter_pos_y(d):
                    animais += 1
        if rochas == len(r) and animais == len(a) == len(p):
            return {'dim': d, 'rochas': r, 'animais': a, 'pos_animais': p}
    raise ValueError('cria_prado: argumentos invalidos')


def cria_copia_prado(m):
    '''
    prado --> prado
    Recebe um prado e retorna uma copia do prado
    '''
    return m.copy()


#Seletores:
def obter_tamanho_x(m):
    '''
    prado --> int
    Recebe um prado e devolve o numero de colunas do prado
    '''
    return obter_pos_x(m['dim']) + 1

def obter_tamanho_y(m):
    '''
    prado --> int
    Recebe um prado e devolve o numero de linhas do prado
    '''    
    return obter_pos_y(m['dim']) + 1

def obter_numero_predadores(m):
    '''
    prado --> int
    Recebe um prado e devolve o numero de animais predadores presentes nesse prado
    '''
    return len([x for x in m['animais'] if eh_predador(x)])


def obter_numero_presas(m):
    '''
    prado --> int
    Recebe um prado e devolve o numero de animais presas presentes nesse prado
    '''    
    return len([y for y in m['animais'] if eh_presa(y)])


def obter_posicao_animais(m):
    '''
    prado --> tuplo
    Recebe um prado e devolve um tuplo correspondente as posicoes dos animais ordenadas
    segundo a ordem de leitura do prado
    '''
    return ordenar_posicoes(m['pos_animais'])


def obter_animal(m, p):
    '''
    prado, posicao --> animal
    Recebe um prado e uma posicao desse prado e retorna o animal que se encontra nessa posicao
    '''
    i = 0
    while i < len(m['pos_animais']):
        if posicoes_iguais(m['pos_animais'][i], p):
            return m['animais'][i]
        else:
            i += 1
    return None


# Modificadores
def eliminar_animal(m, p):
    '''
    prado, posicao --> prado
    Recebe um prado e uma posicao desse prado e, caso essa posicao contenha um animal,
    o animal e eliminado, retornando o prado alterado
    '''
    i = 0
    if eh_animal(obter_animal(m, p)):
        while i < len(m['pos_animais']):           
            if posicoes_iguais(m['pos_animais'][i], p):
                m['pos_animais'] = m['pos_animais'][:i] + m['pos_animais'][i+1:]
                m['animais'] = m['animais'][:i] + m['animais'][i+1:]
            else:
                i += 1
    return m

def mover_animal(m, p1, p2):
    '''
    prado, posicao, posicao --> prado
    Recebe um prado e duas posicoes do prado, em que a primeira posicao tem um animal
    e a segunda esta livre, movendo o animal da primeira posicao para a segunda, retornando
    o prado alterado
    '''
    for i in range(0, len(m['pos_animais'])):
        if posicoes_iguais(m['pos_animais'][i], p1):
            m['pos_animais'] = m['pos_animais'][:i] + (p2,) + m['pos_animais'][i+1:]
    return m


def inserir_animal(m, a, p):
    '''
    prado, animal, posicao --> prado
    Recebe um prado, um animal e uma posicao, adiciona o animal e a sua posicao correspondente
    ao prado, sendo retornado o prado alterado
    '''
    m['animais'] += (a,)
    m['pos_animais'] += (p,)
    return m

#Reconhecedores
def eh_prado(arg):
    '''
    universal --> boolean
    Recebe um argumento e retora True se e so se o argumento corresponder a um TAD prado, senao
    retorna False
    '''
    def nao_eh_muro(pos):
        '''
        posicao --> boolean
        Funcao auxiliar que recebe uma funcao e retorna True apenas se essa posicao nao corresponder
        a um limite do prado, se corresponder retorna False)
        '''
        return (eh_posicao(pos)) and (0 < obter_pos_x(pos) < dim_x) and (0 < obter_pos_y(pos) < dim_y)
    if type(arg) == dict and sorted(arg.keys()) == sorted(['animais', 'dim', 'rochas', 'pos_animais']) and eh_posicao(arg['dim']) and type(arg['rochas']) == type(arg['animais']) == type(arg['pos_animais']) == tuple:
        dim_x, dim_y = obter_pos_x(arg['dim']), obter_pos_y(arg['dim'])
        rochas_corretas = [r for r in arg['rochas'] if nao_eh_muro(r)]
        animais_corretos = [a for a in arg['animais'] if eh_animal(a)]
        pos_corretas = [p for p in arg['pos_animais'] if nao_eh_muro(p)]
        if len(rochas_corretas) == len(arg['rochas']) and len(animais_corretos) == len(arg['animais']) and len(pos_corretas) == len(arg['pos_animais']):
            return True
    return False


def eh_posicao_animal(m, p):
    '''
    prado, posicao --> boolean
    Recebe um prado e uma posicao desse prado, retorna True apenas se essa posicao
    estiver ocupada com um animal.
    '''
    for pos in obter_posicao_animais(m):
        if posicoes_iguais(p, pos):
            return True
    return False

def eh_posicao_obstaculo(m, p):
    '''
    prado, posicao --> boolean
    Recebe um prado e uma posicao desse prado, retorna True apenas se essa posicao
    corresponder a uma montanha ou a um rochedo, senao retorna False
    '''
    match = 0
    for obs in m['rochas']:
        if posicoes_iguais(p, obs):
            match += 1
    return (match != 0 or obter_pos_x(p) == 0 or obter_pos_y(p) == 0 or obter_pos_x(p) == (obter_tamanho_x(m) - 1) or obter_pos_y(p) == (obter_tamanho_y(m) - 1))

def eh_posicao_livre(m, p):
    '''
    prado, posicao --> boolean
    Recebe um prado e uma posicao desse prado, retorna True apenas se essa posicao
    corresponde a um espaco livre, ou seja, se nao estiver ocupada por animais, rochedos
    ou montanhas, senao retorna False
    '''
    return (not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p))


#Teste
def prados_iguais(m1, m2):
    '''
    prado, prado --> boolean
    Recebe dois prados e retorna True apenas se eles forem iguais, senao retorna False
    '''
    match = 0
    if eh_prado(m1) and eh_prado(m2):
        for i in ['animais', 'dim', 'rochas', 'pos_animais']:
            if m1[i] == m2[i]:
                match += 1
    return match == 4


#Transformador
def prado_para_str(m):
    '''
    prado --> string
    Recebe um prado e retorna a string correpondente a esse prado: os limites do prado
    sao definidos com os carateres '+', '|' e '-', as rochas aparecem como '@' e os animais
    aparecem representados com a primeira letra do nome da sua especie, em maiuscula se for
    predador, minuscula se for presa
    '''
    def avalia_posicoes(m, p):
        if (obter_pos_x(p) == 0 or obter_pos_x(p) == obter_tamanho_x(m) - 1) and (obter_pos_y(p) == 0 or obter_pos_y(p) == obter_tamanho_y(m) - 1):
            return '+'
        elif obter_pos_x(p) == 0 or obter_pos_x(p) == obter_tamanho_x(m) - 1:
            return '|'
        elif obter_pos_y(p) == 0 or obter_pos_y(p) == obter_tamanho_y(m) - 1:
            return '-'
        else:
            if eh_posicao_obstaculo(m, p):
                return '@'
            elif eh_posicao_animal(m, p):
                return animal_para_char(obter_animal(m, p))
            else:
                return '.'
       
    prado_str = ''
    for y in range(0, obter_tamanho_y(m)):
        for x in range(0, obter_tamanho_x(m)):
            prado_str += avalia_posicoes(m, cria_posicao(x, y))
        prado_str += '\n'
    prado_str = prado_str[:len(prado_str) - 1]
    return prado_str


#Funcoes de alto nivel
def obter_valor_numerico(m, p):
    '''
    prado, posicao --> int
    Recebe um prado e uma posicao e retorna a ordem correespondente a essa posicao
    na leitura do prado
    '''
    return ((obter_tamanho_x(m)) * (obter_pos_y(p)) + obter_pos_x(p))

def obter_movimento(m, p):
    '''
    prado, posicao --> posicao
    Recebe um prado e uma posicao e retorna a posicao correspondente ao movimento certo
    feito por esse animal caso seja ou predador ou presa
    '''
    def movimento_standart(m, p):
        '''
        prado, posicao --> posicao
        Recebe um prado e uma posicao e retorna a posicao para onde deve avancar o animal
        dessa posicao seguindo o procedimento base de movimento no prado.
        '''
        posicoes_vizinhas = [x for x in obter_posicoes_adjacentes(p) if eh_posicao_livre(m, x)]
        if len(posicoes_vizinhas) > 0:
            return posicoes_vizinhas[(obter_valor_numerico(m,p))%(len(posicoes_vizinhas))]
        else:
            return p
    
    if eh_predador(obter_animal(m, p)):
        posicoes_presa = [x for x in obter_posicoes_adjacentes(p) if (eh_presa(obter_animal(m, x)))]
        if len(posicoes_presa) > 0:
            return posicoes_presa[obter_valor_numerico(m, p) % len(posicoes_presa)]
        else:
            return movimento_standart(m, p)
    else:
        return movimento_standart(m, p)




# 2.2. Funcoes adicionais

def geracao(m):
    '''
    prado --> prado
    O prado entregue como argumento e modificado, fazendo com que o prado evolua uma
    geracao completa. Isto e, segundo a ordem de leitura do prado, comecando do canto 
    superior esquerdo para o canto inferior direito e avancando linha a linha, cada animal
    realiza o seu respetivo turno de acao: a sua idade aumenta em 1, a sua fome aumenta 
    por 1 se for predador, reproduz-se se atingir a idade fertil, morre de fome caso seja
    predador e fique faminto. Cada animal tambem se movimenta no maximo uma vez por geracao,
    sendo que as presas vagueiam pelo prado segundo as regras definidas, enquanto que os
    predadores, se tiverem presas nas suas posicoes adjacentes, avancam e comem a presa,
    ocupando o seu lugar, se nao houver presas por ai movimenta-se tal como as presas.
    '''
    def reproducao(m, pos_atual, animal):
        '''
        prado, posicao, animal
        Verifica se o animal entegue e fertil e, se for, reproduz-se, criando uma copia
        do animal e colocando-a na posicao antiga do animal original.
        '''
        if eh_animal_fertil(animal):
            inserir_animal(m, reproduz_animal(animal), pos_atual)
            
    def mover(pos_atual, animal):
        '''
        posicao, animal
        Controla o movimento dos animais: se for predador verifica se ha posicoes com presas
        ha sua volta e alimenta-se caso haja, se for presa ou predador sem presas ha volta
        movimenta-se de acordo com as regras definidas.
        '''
        def alimentacao(pos_atual, animal):
            '''
            posicao, animal
            Controla a alimentacao dos predadores, verificando se estao famintos (caso estejam
            morrem de fome), aumentando a fome por um a cada geracao e vendo se o animal e capaz
            de se alimentar nessa geracao.
            '''
            nonlocal moveu
            aumenta_fome(animal)
            if eh_animal_faminto(animal):
                eliminar_animal(m, pos_atual)
            else:
                pos_escolhida = obter_movimento(m, pos_atual)
                if eh_posicao_animal(m, pos_escolhida):     
                    eliminar_animal(m, pos_escolhida)
                    mover_animal(m, pos_atual, pos_escolhida)
                    reset_fome(animal)
                    reproducao(m, pos_atual, animal)
                    moveu = True
                    
        moveu = False # Variavel que controla se um predador se alimentou ou nao
        if eh_predador(animal):
            alimentacao(pos_atual, animal)
        if (eh_predador(animal) and moveu == False) or eh_presa(animal):
            if not posicoes_iguais(pos_atual, obter_movimento(m, pos_atual)): # O animal so se move/reproduz caso a sua posicao inicial seja diferente da final
                mover_animal(m, pos_atual, obter_movimento(m, pos_atual)) 
                reproducao(m, pos_atual, animal)
                
    pos_fixas = tuple(obter_posicao_animais(m))
    prado_antigo = cria_copia_prado(m)
    for pos_atual in pos_fixas:
        animal = obter_animal(m, pos_atual)
        if animais_iguais(animal, obter_animal(prado_antigo, pos_atual)): # Verifica se o animal dessa posicao ainda nao se moveu
            aumenta_idade(animal)
            mover(pos_atual, animal)
    return m



def simula_ecossistema(n_ficheiro, n_geracoes, vb):
    '''
    string, inteiro, boolen --> tuplo
    Funcao principal, simula o ecossistema de um prado. O prado e definido de acordo com
    os conteudos do ficheiro cujo nome e referido pela string, o inteiro indica o numero
    de geracoes que vai gerar e o boolean ativa, consoante como esta definido, o modo
    verboso ou o modo quiet. No modo quiet, mostra-se pela saida standart o numero de animais,
    o numero da geracao e o prado apenas na geracao 0 e na ultima geracao. No modo verboso,
    mostra-se pela saida standart a cada geracao o prado, o numero da geracao e o numero de
    animais apenas se o numero de predadores ou presas se tiver alterado. No final retorna um
    tuplo que indica o numero de predadores vs o numero de presas no final da simulacao.
    '''
    def abrir_ficheiro(n_ficheiro):
        '''
        string --> prado
        Funcao auxiliar que recebe a string correspondente ao nome do ficheiro e retorna o prado
        por ele definido. O ficheiro de configuracao configura o prado do seguinte modo: a primeira
        linha contem uma representacao externa do canto inferior direito do prado, definindo as 
        suas dimensoes, a segunda contem a representacao externa das posicoes dos rochedos e as
        restantes linhas contem um animal diferente caracterizado pelas suas especie, frequencia
        de reproducao e frequencia de alimentacao, seguido da representacao externa da posicao que
        esse animal ocupa no prado.
        '''
        ficheiro = open(n_ficheiro, 'r')
        linhas_originais = ficheiro.readlines()
        ficheiro.close
        linhas = []
        for i in linhas_originais[:len(linhas_originais) - 1]:
            linhas += [eval(i[: len(i) -1])]
        linhas += [eval(linhas_originais[len(linhas_originais) - 1])]
        dim, obs = cria_posicao(linhas[0][0], linhas[0][1]), tuple([cria_posicao(linhas[1][x][0], linhas[1][x][1]) for x in range(len(linhas[1]))])
        linhas = linhas[2:]
        tup_ani, pos_ani = tuple(map(lambda x: x[:3], linhas)), tuple(map(lambda x: x[3], linhas))
        ani, pos = tuple(map(lambda x: cria_animal(x[0], x[1], x[2]), tup_ani)), tuple(map(lambda x: cria_posicao(x[0], x[1]), pos_ani))
        return cria_prado(dim, obs, ani, pos)
    
    prado = abrir_ficheiro(n_ficheiro)
    ger = 0
    print('Predadores: '+ str(obter_numero_predadores(prado))+ ' vs Presas: '+ str(obter_numero_presas(prado))+ ' (Gen. '+ str(ger)+')')
    print(prado_para_str(prado))
    while ger < n_geracoes:
        prado_antigo = cria_copia_prado(prado)
        geracao(prado)
        ger += 1
        if (vb) and ger <= n_geracoes and (obter_numero_presas(prado_antigo) != obter_numero_presas(prado) or obter_numero_predadores(prado_antigo) != obter_numero_predadores(prado)):
            print('Predadores: '+ str(obter_numero_predadores(prado))+ ' vs Presas: '+ str(obter_numero_presas(prado))+ ' (Gen. '+ str(ger)+')')
            print(prado_para_str(prado))
        if not(vb) and ger == n_geracoes:
            print('Predadores: '+ str(obter_numero_predadores(prado))+ ' vs Presas: '+ str(obter_numero_presas(prado))+ ' (Gen. '+ str(ger)+')')
            print(prado_para_str(prado))        
    return ((obter_numero_predadores(prado)), (obter_numero_presas(prado)))
