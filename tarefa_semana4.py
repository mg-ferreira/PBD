from collections import Counter, defaultdict
from matplotlib import pyplot as plt
import math, random

users = [
    {"id": 0, "name": "Hero"}, 
    {"id": 1, "name": "Dunn"}, 
    {"id": 2, "name": "Sue"}, 
    {"id": 3, "name": "Chi"}, 
    {"id": 4, "name": "Thor"}, 
    {"id": 5, "name": "Clive"}, 
    {"id": 6, "name": "Hicks"}, 
    {"id": 7, "name": "Devin"}, 
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
    user["friends"] = []

for i, j in friendships:
   users[i]["friends"].append(users[j])
   users[j]["friends"].append(users[i])

#   print(users)

def number_of_friends (user):
    return len(user['friends'])
# print(number_of_friends(users[0]))

total_connections = sum([number_of_friends(u) for u in users])
# print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users
# print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# print(num_friends_by_id)

lista_ordenada = sorted(num_friends_by_id, key = lambda num_friends: num_friends[1], reverse = True)
# print(lista_ordenada)

def friends_of_friends_ids_bad (user):
    return [
        foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]
    ]

def not_the_same (user, other_user):
    return user["id"] != other_user["id"]

def not_friends (user, other_user):
    return all (not_the_same(friend, other_user) for friend in user["friends"])

# print(not_friends(users[0], users[9]))

def friends_of_friends (user):
    return set([
        foaf["id"]
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same (user, foaf)
        and not_friends(user, foaf)
    ])

# print (friends_of_friends(users[0]))

def friends_of_friends_ids_frequency (user):
    return Counter([
        foaf["id"]
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf)
        and not_friends(user, foaf)
    ])

# print (friends_of_friends_ids_frequency(users[4]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"), (0, "GraphQL")
]

def data_scientists_who_like (target_interest):
    return [
        user_id for user_id, interest in interests if interest == target_interest
    ]

# print (data_scientists_who_like("Big Data"))

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

user_id_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_id_by_interest[interest].append(user_id)

# print ('Interesses por usuário')
# print (interests_by_user_id)
# print ('Usuários por interesse')
# print (user_id_by_interest)

def user_with_common_interest_with (user):
    return set([
        interested_user_id
        for interest in interests_by_user_id[user['id']]
        for interested_user_id in user_id_by_interest[interest]
        if interested_user_id != user["id"]
    ])

# print ('Usuários com interesses em comum')
# for user in users:
#     print (user_with_common_interest_with (user))

def most_common_interests_with (user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user['id']]
        for interested_user_id in user_id_by_interest[interest]
        if interested_user_id != user['id']
    )

# print (most_common_interests_with(users[0]))

salario_e_experiencia = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2),
]

salario_por_experiencia = defaultdict(list)
for salario, experiencia in salario_e_experiencia:
    salario_por_experiencia[experiencia].append(salario)

salario_medio_por_experiencia = {
    experiencia: sum (salarios) / len (salarios)
    for experiencia, salarios in salario_por_experiencia.items()
}

# print (salario_medio_por_experiencia)

def rotulo_por_experiencia (experiencia):
    if experiencia < 2 :
        return '(0,2)'
    elif experiencia < 5:
        return '[2,5)'
    else:
        return '[5, ...)'

salario_por_rotulo = defaultdict(list)
for salario, experiencia in salario_e_experiencia:
    salario_por_rotulo[rotulo_por_experiencia(experiencia)].append(salario)

# print (salario_por_rotulo)

salario_medio_por_rotulo = {
    rotulo: sum(salarios) / len(salarios)
    for rotulo, salarios in salario_por_rotulo.items()
}

# print (salario_medio_por_rotulo)

experiencia_e_tipo_de_conta = [
    (0.7, 'paga'),
    (1.9, 'gratuita'),
    (2.5, 'paga'),
    (4.2, 'gratuita'),
    (6, 'gratuita'),
    (6.5, 'gratuita'),
    (7.5, 'gratuita'),
    (8.1, 'gratuita'),
    (8.7, 'paga'),
    (10, 'paga')
]

def classificar_como_paga_ou_gratuita (experiencia):
    if experiencia < 3:
        return 'paga'
    elif experiencia < 8.5:
        'gratuita'
    else:
        return 'paga'

# print (classificar_como_paga_ou_gratuita(1.9))

users[0]["gender"] = "M"
users[0]["age"] = 28
users[1]["gender"] = "M"
users[1]["age"] = 36
users[2]["gender"] = "F"
users[2]["age"] = 25
users[3]["gender"] = "F"
users[3]["age"] = 33
users[4]["gender"] = "M"
users[4]["age"] = 26
users[5]["gender"] = "M"
users[5]["age"] = 28
users[6]["gender"] = "M"
users[6]["age"] = 32
users[7]["gender"] = "M"
users[7]["age"] = 30
users[8]["gender"] = "F"
users[8]["age"] = 25
users[9]["gender"] = "M"
users[9]["age"] = 39

def friends_per_gender_bad (user):
    Masc = 0
    Fem = 0
    for friend in user['friends']:
        if friend['gender'] == 'M':
            Masc +=1
        else:
            Fem +=1
    return (Masc, Fem)


friends_of_each_gender = defaultdict(list)
# for user in users:
#     friends_of_each_gender[user['id']] = friends_per_gender_bad(user)

# print (friends_of_each_gender)

# print ('-------------------- Exercícios Semana 2 --------------------')
# print ('1 Adicione o atributo “interessado em” aos usuários. Eles podem indicar se estão interessados em \npessoas do gendero masculino, feminino, ambos ou nenhum.\n')
for user in users:
    if user['id'] in [4, 7]:
        user['interested_in'] = 'M'
    elif user['id'] == 5:
        user['interested_in'] = 'Nenhum'
    elif user['id'] in [0, 3, 9]:
        user['interested_in'] = 'F'
    else:
        user['interested_in'] = 'Ambos'

# for user in users:
#     print ('User ID: ' + str(user['id']) + ' Interested in: ' + user['interested_in'])


# print ('\n2 Escreva uma função que faz sugestões de amizade de acordo com o atributo “interessado em”.\n')
friend_recommendation_by_gender_interest = defaultdict(list)
def users_by_gender_of_interest (user):
    return [
        friend_suggestion['id']
        for friend_suggestion in users
        if not_the_same(user, friend_suggestion)
        and not_friends(user, friend_suggestion)
        and gender_match(user, friend_suggestion)
    ]
    

def gender_match (user, other_user):
    if user['interested_in'] in ['Ambos', 'Nenhum']:
        return True
    return user['interested_in'] == other_user['gender']

# for user in users:
#     friend_recommendation_by_gender_interest[user['id']] = users_by_gender_of_interest(user)
# print (friend_recommendation_by_gender_interest)

# print ('\n3 Escreva uma função que faz sugestões de amizade de acordo com o atributo \n“interessado em” e de acordo com interesses em comum.\n')
recommended_users = defaultdict(list)

def user_by_interest_and_gender_match(user):
    lista1 = user_with_common_interest_with(user)
    lista2 = users_by_gender_of_interest(user)
    # print ('lista1: ' + str(lista1))
    # print ('lista2: ' + str(lista2))
    # print ('---- FUNÇÃO ---')
    for value in lista1:
        if value in lista2:
            recommended_users[user['id']].append(value)

for user in users:
    user_by_interest_and_gender_match(user)

# print (recommended_users)

# print ('-------------------- Exercícios Semana 3 --------------------')
# print ('1. Construa um gráfico de linha que mostra o número de amigos por usuário.\n')

def grafico_amigos():
    usuarios = [user['id'] for user in users]
    amigos = [number_of_friends(user) for user in users]
    
    
    plt.plot (usuarios, amigos, color='red', marker='o', linestyle='solid')
    plt.title ("Amigos por usuário")
    plt.ylabel ("# de amigos")
    plt.axis ([-0.5, 9.5, 0, 5])
    plt.show ()
    
# grafico_amigos()


# print ('2. Construa um gráfico de dispersão envolvendo salário e tempo de experiência.\n')
def grafico_salario_por_experiencia():
    salarios = [(salario//1000) for salario, _ in salario_e_experiencia]
    experiencias = [experiencia for _, experiencia in salario_e_experiencia]
    rotulos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    plt.scatter (salarios, experiencias)
    for rotulo, experiencia, salario in zip (rotulos, experiencias, salarios):
        plt.annotate (
            rotulo,
            xy = (salario, experiencia),
            xytext = (0, 10),
            textcoords = "offset points"
        )
    plt.title ("Salários vs. Experiência")
    plt.xlabel ("Salário Anual (em milhares)")
    plt.ylabel ("Experiência (em anos)")
    plt.axis ([40, 100, 0, 11])
    plt.show()
    
# grafico_salario_por_experiencia()


# print ('3. Construa um histograma envolvendo dados de pagantes e não pagantes.\n')
def grafico_histograma():
    tipos_conta = Counter( tipo for _, tipo in experiencia_e_tipo_de_conta)
    qtd_users = [valor for valor in tipos_conta.values()]
    xs = [i for i, _ in enumerate(tipos_conta)]
    plt.bar(xs, qtd_users)
    plt.xlabel ('Tipos de conta')
    plt.ylabel ('# de usuários por tipo de conta')
    plt.xticks ([i for i, _ in enumerate (tipos_conta)], tipos_conta)
    plt.title ('Usuários Pagantes vs. Não-pagantes')
    plt.show()
    
# grafico_histograma()

# print ('''4. Construa um histograma de palavras em interesses. Por exemplo, a palavra learning pode
# aparecer em machine learning e em deep learning. Quebre cada interesse em palavras para fazer
# a contagem e montar o histograma..\n''')

def obter_lista():
    palavras = []
    for item in interests:
        palavras.append(item[1])
    return palavras        
    
def split_words(lista_de_palavras):
    lista = []
    for item in lista_de_palavras:
        for palavra in item.split(' '):
            lista.append(palavra)
    return lista

def grafico_de_palavras():
    lista = obter_lista()    
    count_words = Counter (split_words(lista))
    qty_words = [v for v in count_words.values()]
    xs = [i for i, _ in enumerate(count_words)]
    plt.bar(xs, qty_words)
    plt.xlabel ('Palavras')
    plt.ylabel ('# de ocorrências em interesses')
    plt.xticks ([i for i, _ in enumerate (count_words)], count_words)
    plt.title ('Histograma de Palavras em Interesses')
    plt.show()

# grafico_de_palavras()

# ------------------------ Exercícios Semana 4 ------------------------
# 1 - Escreva uma função que constrói um histograma que mostra a quantidade de amigos que pessoas de cada sexo têm.
def group_users_by_sex_and_sum_friendships(usuarios):
    groups = []
    for user in usuarios:
        u1 = user['gender']
        u2 = len(user['friends'])
        groups.append((u1, u2))
    # print(groups)
    return groups

def histograma_amizades_por_sexo_do_usuario():
    amizades = group_users_by_sex_and_sum_friendships(users)
    xs = [i for i, _ in enumerate(amizades)]
    ys = [j for _, j in amizades]
    plt.bar(xs, ys)
    plt.axis([-0.5, 9.5, 0, 10])
    plt.title("# de amigos por gênero do usuário")
    plt.xlabel("usuarios")
    plt.ylabel('# de amigos')
    plt.xticks ([i for i, _ in enumerate(amizades)], amizades)
    plt.show()
    # print(amizades)
    # print(xs)
    # print(ys)

# histograma_amizades_por_sexo_do_usuario()


# 2 - Escreva uma função que constrói um histograma que mostra a quantidade de amigos que pessoas de cada idade têm.
def group_users_by_age(usuarios):
    amigos_por_idade = []
    for usuario in usuarios:
        age = usuario['age']
        friends = len(usuario['friends'])
        amigos_por_idade.append((age, friends))
    # print(lista_idades)
    return amigos_por_idade

# group_users_by_age(users)

def histogram_friends_qty_by_user_age(num_users):
    dados = group_users_by_age(users)
    xs = [i for i, _ in dados]
    ys = [j for _, j in dados]
    plt.bar(xs, ys)
    plt.axis([20, 40, 0, 9])
    plt.title("Amizades por idade do usuário")
    plt.xlabel('idade dos usuários')
    plt.ylabel('# de amigos')
    plt.xticks ([i for i, _ in dados])
    # print(xs)
    # print(ys)
    plt.show()

# histogram_friends_qty_by_user_age(num_users)


# 3 - Escreva uma função que calcula a variância e o desvio padrão da idade das pessoas do sexo masculino que tenham pelo menos 22 anos.
lista_idades = [user["age"] for user in users]
# print(lista_idades)

def diferencas_em_relacao_a_media(dados):
    media = sum(x for x in dados) / len(dados)
    return [x - media for x in dados]

def soma_dos_quadrados(dados):
    return sum (x**2 for x in dados)

def variancia(dados):
    return soma_dos_quadrados(diferencas_em_relacao_a_media(dados)) / (len(dados) - 1)

def desvio_padrao(dados):
    return math.sqrt(variancia(dados))

a = variancia(lista_idades)
# print(a)
b = desvio_padrao(lista_idades)
# print(b)


i = [1, 2, 2, 3, 4]
# print(set(i))


# ------------------------ Exercícios Semana 5 ------------------------
# 1 - Escreva uma função que calcula a covariância entre idade e número de amigos
def dot(x, y):
    return sum([x_i * y_i for x_i, y_i in zip(x, y)])

def sum_of_squares(v):
    return dot(v, v)

def variance(v):
    mean = sum(v) / len(v)
    return [v_i - mean for v_i in v]

def covariance(x, y):
    n = len(x)
    return dot(variance(x), variance(y)) / (n - 1)

def list_qty_of_friends(users):
    return [number_of_friends(user) for user in users]

def covariancia_idade_qtd_amigos():
    li = covariance(lista_idades, [number_of_friends(user) for user in users])
    print(f'covariance: {li}')


# 2 - Escreva uma função que calcula a correlação entre idade e número de amigos.
def correlation (x, y):
    desvio_padrao_x = math.sqrt(sum_of_squares(variance(x)) / (len(x)-1))
    desvio_padrao_y = math.sqrt(sum_of_squares(variance(y)) / (len(y)-1))
    if desvio_padrao_x > 0 and desvio_padrao_y > 0:
        return covariance(x, y) / desvio_padrao_x / desvio_padrao_y
    else:
        return 0

def correlacao_idade_qtd_amigos():
    li = [number_of_friends(user) for user in users]
    print(f'correlation: {correlation (lista_idades, li)}')


# 3 - Escreva uma função que devolve uma tupla de duas listas. A primeira lista contém quantidades
#     de amigos que cada usuário da rede tem. A segunda, quantidades de minutos passados em média
#     na rede por cada usuário. Cada lista tem tamanho n, sendo n um valor recebido como parâmetro.
#     Os dados devem ser gerados aleatoriamente. Faça três versões.
#     3.1 Gere dados aleatoriamente garantindo correlação próxima de 1.
def qtd_amigos_minutos_em_rede_1(n):
    v = [random.randint(1, 9) for n in range(n)]
    w = [v_i * 3 for v_i in v]
    return (v, w)

def correlacao_amigos_tempo_gasto_1 ():
    data = qtd_amigos_minutos_em_rede_1(10)
    # print(data)
    r = correlation(data[0], data[1])
    print(f'correlação: {r}')

#   3.2 Gere dados aleatoriamente garantindo correlação próxima de -1.
def qtd_amigos_minutos_em_rede_2(n):
    v = [random.randint(1, 9) for n in range(n)]
    w = [v_i // -4 for v_i in v]
    return (v, w)

def correlacao_amigos_tempo_gasto_2 ():
    data = qtd_amigos_minutos_em_rede_2(10)
    # print(data)
    r = correlation(data[0], data[1])
    print(f'correlação: {r}')

#   3.3 Gere dados aleatoriamente garantindo correlação próxima de 0.
def qtd_amigos_minutos_em_rede_3(n):
    v = [random.randint(1, 9) for n in range(n)]
    w = [random.randint(1, 200) for n in range(n)]
    return (v, w)

def correlacao_amigos_tempo_gasto_3 ():
    data = qtd_amigos_minutos_em_rede_3(10)
    # print(data)
    r = correlation(data[0], data[1])
    print(f'correlação: {r}')

# 4 - Escreva uma função de teste que mostra que os dados gerados no Exercício 3 estão de acordo
#     com o solicitado.
def mostra_dados():
    print('3.1 - Gere dados aleatoriamente garantindo correlação próxima de 1.')
    correlacao_amigos_tempo_gasto_1()
    print('3.2 - Gere dados aleatoriamente garantindo correlação próxima de -1.')
    correlacao_amigos_tempo_gasto_2()
    print('3.3 - Gere dados aleatoriamente garantindo correlação próxima de 0.')
    correlacao_amigos_tempo_gasto_3()


# def main():
#     covariancia_idade_qtd_amigos()
#     correlacao_idade_qtd_amigos()
#     # qtd_amigos_minutos_em_rede(10)
#     mostra_dados()

# main()

# ------------------------ Exercícios Semana 6 ------------------------
# 1 - Adicione o atributo intenção de voto à base de dados referente à rede social de cientistas de
# dados. Sorteie uma intenção de voto para cada usuário da rede. Aumente o tamanho da base de
# modo que ela tenha 100 usuários. '''
def aumenta_tamanho_base (base_existente):
    nova_base = base_existente
    for i in range (90):
        registro = {}
        registro['id'] = 10 + i
        registro['nome'] = "Novo Usuário " + str(i)
        registro['friends'] = []
        registro['gender'] = random.choice (['M', 'F'])
        registro['age'] = random.randint(18,40)
        registro['interested_in']: random.choice (['M', 'F', 'A', 'None'])
        nova_base.append(registro)
    return nova_base

base = aumenta_tamanho_base(users)

def inclui_intencao_voto_e_salario (lista):
    for usuario in lista:
        usuario['salario'] = 1200 + random.random() * 1300
        usuario['intencao_de_voto'] = random.choice (['Haddad', 'Bolsonaro'])
        # print(f"Id: {usuario['id']}, salario: {usuario['salario']}, intencao_de_voto: {usuario['intencao_de_voto']}")

inclui_intencao_voto_e_salario(base)

# 2. Há uma técnica para validação de predições realizadas por algoritmos de aprendizado de
# máquina chamada cross validation leave one out. Ela funciona da seguinte forma.
# 1. O algoritmo de predição é executado utilizando-se a base inteira exceto uma das instâncias.
# 2. O resultado obtido é comparado com o valor real.
# 3. O processo é repetido para cada uma das instâncias.
# 4. Ao final, exibe-se o percentual de acerto e erro.

# Execute o algoritmo KNN (use K=5) da forma descrita e verifique o resultado. Note que os
# dados foram gerados aleatoriamente e, portanto, usuários “próximos” não necessariamente têm
# intenção de voto igual.

def rotulo_de_maior_frequencia (pessoas):
    frequencias = Counter(pessoa['intencao_de_voto'] for pessoa in pessoas)
    mais_frequentes = frequencias.most_common(1)
    return mais_frequentes[0][0]

# rotulo_de_maior_frequencia (base)

def rotulo_de_maior_frequencia_sem_empate (pessoas):
    frequencias = Counter (pessoa['intencao_de_voto'] for pessoa in pessoas)
    rotulo, frequencia = frequencias.most_common(1)[0]
    qtde_de_mais_frequentes = len ([count for count in frequencias.values() if count == frequencia])
    if qtde_de_mais_frequentes == 1:
        return rotulo
    return rotulo_de_maior_frequencia_sem_empate (pessoas[0:len(pessoas) - 1])

# rotulo_de_maior_frequencia_sem_empate (base)

def distance (p1, p2):
    i = math.pow ((p1['age'] - p2['age']), 2)
    s = math.pow ((1 if p1['gender'] == "M" else 0) - (1 if p2['gender'] == "M" else 0), 2)
    sal = math.pow ((p1['salario'] - p2['salario']), 2)
    return math.sqrt(i + s + sal)

def knn (k, observacoes_rotuladas, nova_observacao):
    ordenados_pela_distancia = sorted (observacoes_rotuladas, key=lambda obs: distance (obs, nova_observacao))
    k_mais_proximos = ordenados_pela_distancia[:k]
    resultado = rotulo_de_maior_frequencia_sem_empate (k_mais_proximos)
    return resultado


def rotacionar (lista, pos):
    return lista[pos + 1:] + lista[:pos]


def cross_validation_leave_one_out(lista):
    precisao = 0
    for n in range(len(lista)):
        resultado = knn(5, rotacionar(lista, n), lista[n])
        if resultado == lista[n]['intencao_de_voto']:
            precisao += 1
    print (f'Taxa de Acerto: {precisao}%, Taxa de Erro: {100 - precisao}%')

def main ():
    cross_validation_leave_one_out(base)        
            

main()