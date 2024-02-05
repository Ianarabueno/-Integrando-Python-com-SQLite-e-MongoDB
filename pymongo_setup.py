from pymongo import MongoClient

# Conectar ao MongoDB Atlas (substitua 'sua_string_de_conexao' e 'seu_nome_de_banco' pelos valores reais)
client = MongoClient('https://diosql-9361f-default-rtdb.firebaseio.com/')
db = client['seu_nome_de_banco']

# Criar a coleção 'bank' se ainda não existir
if 'bank' not in db.list_collection_names():
    db.create_collection('bank')

# Obter a coleção 'bank'
bank_collection = db['bank']

# Inserir documentos com a estrutura mencionada
document1 = {
    'cliente_id': 1,
    'nome': 'Cliente A',
    'contas': [
        {'numero': '123456', 'saldo': 1000},
        # Adicione mais contas se necessário
    ]
}

document2 = {
    'cliente_id': 2,
    'nome': 'Cliente B',
    'contas': [
        {'numero': '654321', 'saldo': 500},
        # Adicione mais contas se necessário
    ]
}

bank_collection.insert_many([document1, document2])

# Recuperação de informações com base nos pares de chave e valor
# Exemplo de recuperação de contas de um cliente específico
cliente_id = 1
cliente_document = bank_collection.find_one({'cliente_id': cliente_id})

if cliente_document:
    print(f"Cliente: {cliente_document['nome']}")
    for conta in cliente_document['contas']:
        print(f"Conta: {conta['numero']}, Saldo: {conta['saldo']}")
else:
    print(f"Cliente com ID {cliente_id} não encontrado.")
