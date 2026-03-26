# ==============================
# CRUD puro para Bancários
# ==============================

bancarios = {}

def criar_bancario(nome, idade, nif, email, morada, data_nascimento):
    id_bancario = len(bancarios) + 1
    bancarios[id_bancario] = {
        "nome": nome,
        "idade": idade,
        "nif": nif,
        "email": email,
        "morada": morada,
        "data_nascimento": data_nascimento
    }
    return id_bancario

def listar_bancarios():
    if not bancarios:
        print("⚠️ Sem bancários cadastrados")
        return
    print("📋 LISTA DE BANCÁRIOS (Nome, Idade, Data Nascimento)")
    for i, b in bancarios.items():
        print(f"ID: {i} | Nome: {b['nome']} | Idade: {b['idade']} | Nascimento: {b['data_nascimento']}")

def atualizar_bancario(id_bancario, nome=None, idade=None, nif=None, email=None, morada=None, data_nascimento=None):
    if id_bancario not in bancarios:
        print("❌ Bancário não encontrado")
        return
    b = bancarios[id_bancario]
    if nome: b["nome"] = nome
    if idade: b["idade"] = idade
    if nif: b["nif"] = nif
    if email: b["email"] = email
    if morada: b["morada"] = morada
    if data_nascimento: b["data_nascimento"] = data_nascimento
    print("✅ Bancário atualizado")

def remover_bancario(id_bancario):
    if id_bancario not in bancarios:
        print("❌ Bancário não encontrado")
        return
    del bancarios[id_bancario]
    print("✅ Bancário removido")

def existe_bancario(id_bancario):
    return id_bancario in bancarios