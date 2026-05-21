import logging
import os
from datetime import datetime

# ==========================================================
# CONFIGURAÇÃO DO LOGGING
# ==========================================================
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    handlers=[
        logging.FileHandler(f'{LOG_DIR}/gestor.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('gestor')

# ==========================================================
# CONTADORES DE IDs
# ==========================================================
contador_bancarios = 1
contador_clientes = 1
contador_bancos = 1
contador_contas = 1


def gerar_id_bancario():
    global contador_bancarios
    novo_id = f"B{contador_bancarios:03d}"
    contador_bancarios += 1
    return novo_id


def gerar_id_cliente():
    global contador_clientes
    novo_id = f"C{contador_clientes:03d}"
    contador_clientes += 1
    return novo_id


def gerar_id_banco():
    global contador_bancos
    novo_id = f"BN{contador_bancos:03d}"
    contador_bancos += 1
    return novo_id


def gerar_id_conta():
    global contador_contas
    novo_id = f"CT{contador_contas:03d}"
    contador_contas += 1
    return novo_id


# ==========================================================
# VALIDAÇÕES
# ==========================================================
def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validar_nif(nif):
    return isinstance(nif, str) and nif.isdigit() and len(nif) == 9


def validar_nib(nib):
    return isinstance(nib, str) and nib.isdigit() and len(nib) == 21


def validar_tipo_conta(tipo):
    return tipo in ("corrente", "poupança")


def validar_email(email):
    partes = email.split("@")
    return len(partes) == 2 and "." in partes[1] and len(partes[1]) > 2
