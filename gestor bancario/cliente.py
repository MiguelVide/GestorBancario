# ==============================
# CRUD puro para Clientes
# ==============================

clientes = {}

def criar_cliente(nome, idade, nif, email, morada, trabalho, data_nascimento, id_bancario):
    id_cliente = len(clientes) + 1
    clientes[id_cliente] = {
        "nome": nome,
        "idade": idade,
        "nif": nif,
        "email": email,
        "morada": morada,
        "trabalho": trabalho,
        "data_nascimento": data_nascimento,
        "bancario_id": id_bancario
    }
    return id_cliente

def listar_clientes():
    if not clientes:
        print("⚠️ Sem clientes cadastrados")
        return
    print("📋 LISTA DE CLIENTES (Nome, Idade, Data Nascimento)")
    for i, c in clientes.items():
        print(f"ID: {i} | Nome: {c['nome']} | Idade: {c['idade']} | Nascimento: {c['data_nascimento']}")

def atualizar_cliente(id_cliente, nome=None, idade=None, nif=None, email=None, morada=None, trabalho=None, data_nascimento=None, id_bancario=None):
    if id_cliente not in clientes:
        print("❌ Cliente não encontrado")
        return
    c = clientes[id_cliente]
    if nome: c["nome"] = nome
    if idade: c["idade"] = idade
    if nif: c["nif"] = nif
    if email: c["email"] = email
    if morada: c["morada"] = morada
    if trabalho: c["trabalho"] = trabalho
    if data_nascimento: c["data_nascimento"] = data_nascimento
    if id_bancario: c["bancario_id"] = id_bancario
    print("✅ Cliente atualizado")

def remover_cliente(id_cliente):
    if id_cliente not in clientes:
        print("❌ Cliente não encontrado")
        return
    del clientes[id_cliente]
    print("✅ Cliente removido")