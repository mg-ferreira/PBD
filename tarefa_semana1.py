from collections import Counter, defaultdict

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

# print (user_with_common_interest_with (users[0]))

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


print ('-------------------- Exercício Semana 1 --------------------')
print ('1 Adicione os atributos sexo e idade aos usuários da rede.\n')

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

for user in users:
    print ('User ID: ' + str(user['id']) + ' Idade: ' + str(user['age']) + ' Sexo: ' + user['gender'])


print ('''\n2 Monte um dicionário que tem como chave o id do usuário e como valor uma tupla. O primeiro
elemento da tupla deve ter a quantidade de amigos do sexo masculino e o segundo elemento da
tupla deve ter a quantidade de amigos do sexo feminino. Escreva funções conforme achar
apropriado.''')

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
for user in users:
    friends_of_each_gender[user['id']] = friends_per_gender_bad(user)

print (friends_of_each_gender)