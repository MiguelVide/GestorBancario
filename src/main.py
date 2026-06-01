import tkinter as tk
from tkinter import ttk, messagebox

from bancario import criar_bancario, listar_bancarios, consultar_bancario, atualizar_bancario, remover_bancario
from cliente import criar_cliente, listar_clientes, consultar_cliente, atualizar_cliente, remover_cliente
from banco import criar_banco, listar_bancos, consultar_banco, atualizar_banco, remover_banco
from conta_bancaria import criar_conta, listar_contas, consultar_conta, atualizar_conta, remover_conta

# ──────────────────────────────────────────────
# Paleta
# ──────────────────────────────────────────────
BG        = "#0f1117"
PANEL     = "#1a1d27"
CARD      = "#22263a"
ACCENT    = "#4f8ef7"
ACCENT2   = "#34d399"
DANGER    = "#f87171"
TXT       = "#e8eaf0"
TXT_DIM   = "#6b7280"
BORDER    = "#2e3250"
FONT_TITLE = ("Consolas", 22, "bold")
FONT_SUB   = ("Consolas", 11, "bold")
FONT_BODY  = ("Consolas", 10)
FONT_BTN   = ("Consolas", 10, "bold")

# ──────────────────────────────────────────────
# Helpers visuais
# ──────────────────────────────────────────────
def styled_btn(parent, text, cmd, color=ACCENT, fg=BG, **kw):
    b = tk.Button(parent, text=text, command=cmd,
                  bg=color, fg=fg, font=FONT_BTN,
                  relief="flat", cursor="hand2", padx=10, pady=4, **kw)
    b.bind("<Enter>", lambda e: b.config(bg=_lighten(color)))
    b.bind("<Leave>", lambda e: b.config(bg=color))
    return b

def _lighten(hex_color):
    r, g, b = int(hex_color[1:3],16), int(hex_color[3:5],16), int(hex_color[5:7],16)
    return f"#{min(255,r+30):02x}{min(255,g+30):02x}{min(255,b+30):02x}"

def make_tree(parent, columns, col_names, heights=12):
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Custom.Treeview",
        background=PANEL, foreground=TXT, fieldbackground=PANEL,
        rowheight=24, font=FONT_BODY, borderwidth=0)
    style.configure("Custom.Treeview.Heading",
        background=CARD, foreground=ACCENT, font=FONT_SUB, relief="flat")
    style.map("Custom.Treeview", background=[("selected", ACCENT)])
    style.configure("Custom.TCombobox", fieldbackground=PANEL, background=PANEL,
                    foreground=TXT, selectbackground=ACCENT)

    frame = tk.Frame(parent, bg=BG)
    tree = ttk.Treeview(frame, columns=columns, show="headings",
                        height=heights, style="Custom.Treeview")
    for c, n in zip(columns, col_names):
        tree.heading(c, text=n)
        tree.column(c, width=130, anchor="w")
    sb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=sb.set)
    tree.pack(side="left", fill="both", expand=True)
    sb.pack(side="right", fill="y")
    return frame, tree

# ──────────────────────────────────────────────
# Helpers para carregar opções de dropdowns
# ──────────────────────────────────────────────
def _opcoes_bancarios():
    code, data = listar_bancarios()
    if code != 200:
        return []
    return [f"{id_} — {d['nome']}" for id_, d in data.items()]

def _opcoes_clientes():
    code, data = listar_clientes()
    if code != 200:
        return []
    return [f"{id_} — {d['nome']}" for id_, d in data.items()]

def _opcoes_bancos():
    code, data = listar_bancos()
    if code != 200:
        return []
    return [f"{id_} — {d['nome']}" for id_, d in data.items()]

def _id_de_opcao(opcao):
    """Extrai o ID da string 'B001 — Nome'"""
    return opcao.split(" — ")[0].strip() if opcao else ""

# ══════════════════════════════════════════════
# FormDialog — suporta Entry e Combobox
#
# fields = lista de dicts:
#   {"key": str, "label": str, "type": "entry"|"combo", "options_fn": callable}
# ══════════════════════════════════════════════
class FormDialog(tk.Toplevel):
    def __init__(self, parent, title, fields, on_submit, defaults=None):
        super().__init__(parent)
        self.title(title)
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()

        tk.Label(self, text=title, bg=BG, fg=ACCENT, font=FONT_SUB).pack(pady=(14,6))

        card = tk.Frame(self, bg=CARD, padx=16, pady=12)
        card.pack(padx=20, pady=(0,12), fill="x")
        card.columnconfigure(1, weight=1)

        self.vars = {}      # key -> StringVar
        self._combos = {}   # key -> Combobox (para atualizar opções)

        for i, f in enumerate(fields):
            key    = f["key"]
            label  = f["label"]
            ftype  = f.get("type", "entry")
            default = (defaults or {}).get(key, "")

            tk.Label(card, text=label, bg=CARD, fg=TXT_DIM,
                     font=FONT_BODY).grid(row=i, column=0, sticky="w",
                                          padx=(10,6), pady=3)

            var = tk.StringVar(value=default)
            self.vars[key] = var

            if ftype == "combo":
                options_fn = f.get("options_fn", lambda: [])
                opts = options_fn()
                cb = ttk.Combobox(card, textvariable=var, values=opts,
                                  state="readonly", font=FONT_BODY, width=26)
                # Se default é um ID simples, tenta mostrar a opção correspondente
                if default and not " — " in default:
                    match = next((o for o in opts if o.startswith(default)), "")
                    var.set(match)
                cb.grid(row=i, column=1, padx=(0,10), pady=3, sticky="ew")
                self._combos[key] = cb
            else:
                e = tk.Entry(card, textvariable=var, bg=PANEL, fg=TXT,
                             insertbackground=TXT, relief="flat",
                             font=FONT_BODY, width=28)
                e.grid(row=i, column=1, padx=(0,10), pady=3, sticky="ew")

        btns = tk.Frame(self, bg=BG)
        btns.pack(pady=(0,14))
        styled_btn(btns, "💾  Guardar", lambda: self._submit(on_submit),
                   color=ACCENT2, fg=BG).pack(side="left", padx=6)
        styled_btn(btns, "Cancelar", self.destroy,
                   color=PANEL, fg=TXT).pack(side="left", padx=6)

        self.center()

    def center(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth()  - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"+{x}+{y}")

    def _submit(self, on_submit):
        # Para campos combo, extrai só o ID
        data = {}
        for k, var in self.vars.items():
            val = var.get().strip()
            if k in self._combos:
                val = _id_de_opcao(val)
            data[k] = val

        ok, msg = on_submit(data)
        if ok:
            messagebox.showinfo("Sucesso", msg)
            self.destroy()
        else:
            messagebox.showerror("Erro", str(msg))

# ══════════════════════════════════════════════
# BaseTab
# ══════════════════════════════════════════════
class BaseTab(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, bg=BG)
        tk.Label(self, text=title, bg=BG, fg=ACCENT,
                 font=FONT_TITLE).pack(pady=(18,8), padx=20, anchor="w")
        tk.Frame(self, bg=BORDER, height=1).pack(fill="x", padx=20, pady=(0,12))

        main = tk.Frame(self, bg=BG)
        main.pack(fill="both", expand=True, padx=20)
        main.columnconfigure(0, weight=3)
        main.columnconfigure(1, weight=1)

        self.tree_frame, self.tree = self._make_tree(main)
        self.tree_frame.grid(row=0, column=0, sticky="nsew", padx=(0,12))
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        btn_panel = tk.Frame(main, bg=PANEL, padx=12, pady=12)
        btn_panel.grid(row=0, column=1, sticky="nsew")
        for text, cmd, color in [
            ("➕  Criar",   self.open_create, ACCENT2),
            ("✏️  Editar",  self.open_edit,   ACCENT),
            ("🗑  Remover", self.do_remove,   DANGER),
            ("🔄  Refresh", self.refresh,     TXT_DIM),
        ]:
            styled_btn(btn_panel, text, cmd, color=color,
                       fg=BG if color != TXT_DIM else TXT,
                       width=16).pack(fill="x", pady=4)

        self.selected_id = None
        self.refresh()

    def _make_tree(self, parent): raise NotImplementedError
    def refresh(self):            raise NotImplementedError
    def open_create(self):        raise NotImplementedError
    def _open_edit_dialog(self, rid): raise NotImplementedError
    def _remove(self, rid):       raise NotImplementedError

    def _on_select(self, _=None):
        sel = self.tree.selection()
        self.selected_id = self.tree.item(sel[0])["values"][0] if sel else None

    def open_edit(self):
        if not self.selected_id:
            messagebox.showwarning("Aviso", "Seleciona um registo primeiro.")
            return
        self._open_edit_dialog(self.selected_id)

    def do_remove(self):
        if not self.selected_id:
            messagebox.showwarning("Aviso", "Seleciona um registo primeiro.")
            return
        if messagebox.askyesno("Confirmar", f"Remover '{self.selected_id}'?"):
            self._remove(self.selected_id)
            self.refresh()

    def _clear_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

# ══════════════════════════════════════════════
# TAB BANCÁRIOS  (sem IDs externos)
# ══════════════════════════════════════════════
class TabBancarios(BaseTab):
    FIELDS = [
        {"key": "nome",            "label": "Nome"},
        {"key": "nif",             "label": "NIF"},
        {"key": "email",           "label": "Email"},
        {"key": "morada",          "label": "Morada"},
        {"key": "data_nascimento", "label": "Data Nasc. (YYYY-MM-DD)"},
    ]

    def __init__(self, parent):
        super().__init__(parent, "👤  Bancários")

    def _make_tree(self, parent):
        return make_tree(parent,
            ("id","nome","nif","email","morada","data_nascimento"),
            ("ID","Nome","NIF","Email","Morada","Data Nasc."))

    def refresh(self):
        self._clear_tree()
        code, data = listar_bancarios()
        if code == 200:
            for d in data.values():
                self.tree.insert("", "end", values=(
                    d["id"], d["nome"], d["nif"],
                    d["email"], d["morada"], d["data_nascimento"]))

    def open_create(self):
        def submit(data):
            code, obj = criar_bancario(data["nome"], data["nif"], data["email"],
                                       data["morada"], data["data_nascimento"])
            if code == 201:
                self.refresh()
                return True, f"Bancário criado: {obj['id']}"
            return False, obj
        FormDialog(self, "Criar Bancário", self.FIELDS, submit)

    def _open_edit_dialog(self, rid):
        _, raw = consultar_bancario(rid)
        d = raw[rid]
        defaults = {f["key"]: d.get(f["key"], "") for f in self.FIELDS}
        def submit(data):
            code, obj = atualizar_bancario(rid,
                data["nome"] or None, data["nif"] or None,
                data["email"] or None, data["morada"] or None,
                data["data_nascimento"] or None)
            if code == 200:
                self.refresh()
                return True, "Bancário atualizado."
            return False, obj
        FormDialog(self, "Editar Bancário", self.FIELDS, submit, defaults)

    def _remove(self, rid):
        remover_bancario(rid)

# ══════════════════════════════════════════════
# TAB CLIENTES  (bancario_id → Combobox)
# ══════════════════════════════════════════════
class TabClientes(BaseTab):
    FIELDS = [
        {"key": "nome",            "label": "Nome"},
        {"key": "nif",             "label": "NIF"},
        {"key": "email",           "label": "Email"},
        {"key": "morada",          "label": "Morada"},
        {"key": "trabalho",        "label": "Trabalho"},
        {"key": "data_nascimento", "label": "Data Nasc. (YYYY-MM-DD)"},
        {"key": "bancario_id",     "label": "Bancário responsável",
         "type": "combo", "options_fn": _opcoes_bancarios},
    ]

    def __init__(self, parent):
        super().__init__(parent, "🧑‍💼  Clientes")

    def _make_tree(self, parent):
        return make_tree(parent,
            ("id","nome","nif","email","trabalho","bancario_id"),
            ("ID","Nome","NIF","Email","Trabalho","Bancário"))

    def refresh(self):
        self._clear_tree()
        code, data = listar_clientes()
        if code == 200:
            for d in data.values():
                self.tree.insert("", "end", values=(
                    d["id"], d["nome"], d["nif"],
                    d["email"], d.get("trabalho",""),
                    d.get("bancario_id","")))

    def open_create(self):
        def submit(data):
            code, obj = criar_cliente(
                data["nome"], data["nif"], data["email"],
                data["morada"], data["trabalho"],
                data["data_nascimento"], data["bancario_id"])
            if code == 201:
                self.refresh()
                return True, f"Cliente criado: {obj['id']}"
            return False, obj
        FormDialog(self, "Criar Cliente", self.FIELDS, submit)

    def _open_edit_dialog(self, rid):
        _, raw = consultar_cliente(rid)
        d = raw[rid]
        defaults = {f["key"]: d.get(f["key"], "") for f in self.FIELDS}
        def submit(data):
            code, obj = atualizar_cliente(rid,
                data["nome"] or None, data["nif"] or None,
                data["email"] or None, data["morada"] or None,
                data["trabalho"] or None,
                data["data_nascimento"] or None,
                data["bancario_id"] or None)
            if code == 200:
                self.refresh()
                return True, "Cliente atualizado."
            return False, obj
        FormDialog(self, "Editar Cliente", self.FIELDS, submit, defaults)

    def _remove(self, rid):
        remover_cliente(rid)

# ══════════════════════════════════════════════
# TAB BANCOS  (sem IDs externos)
# ══════════════════════════════════════════════
class TabBancos(BaseTab):
    FIELDS = [
        {"key": "nome",     "label": "Nome"},
        {"key": "email",    "label": "Email"},
        {"key": "morada",   "label": "Morada"},
        {"key": "telefone", "label": "Telefone"},
    ]

    def __init__(self, parent):
        super().__init__(parent, "🏦  Bancos")

    def _make_tree(self, parent):
        return make_tree(parent,
            ("id","nome","email","morada","telefone"),
            ("ID","Nome","Email","Morada","Telefone"))

    def refresh(self):
        self._clear_tree()
        code, data = listar_bancos()
        if code == 200:
            for d in data.values():
                self.tree.insert("", "end", values=(
                    d["id"], d["nome"], d["email"],
                    d["morada"], d["telefone"]))

    def open_create(self):
        def submit(data):
            code, obj = criar_banco(data["nome"], data["email"],
                                    data["morada"], data["telefone"])
            if code == 201:
                self.refresh()
                return True, f"Banco criado: {obj['id']}"
            return False, obj
        FormDialog(self, "Criar Banco", self.FIELDS, submit)

    def _open_edit_dialog(self, rid):
        _, raw = consultar_banco(rid)
        d = raw[rid]
        defaults = {f["key"]: d.get(f["key"], "") for f in self.FIELDS}
        def submit(data):
            code, obj = atualizar_banco(rid,
                data["nome"] or None, data["email"] or None,
                data["morada"] or None, data["telefone"] or None)
            if code == 200:
                self.refresh()
                return True, "Banco atualizado."
            return False, obj
        FormDialog(self, "Editar Banco", self.FIELDS, submit, defaults)

    def _remove(self, rid):
        remover_banco(rid)

# ══════════════════════════════════════════════
# TAB CONTAS  (id_cliente e id_banco → Combobox)
# ══════════════════════════════════════════════
class TabContas(BaseTab):
    FIELDS = [
        {"key": "tipo",       "label": "Tipo",
         "type": "combo", "options_fn": lambda: ["corrente", "poupança"]},
        {"key": "saldo",      "label": "Saldo Inicial"},
        {"key": "id_cliente", "label": "Cliente",
         "type": "combo", "options_fn": _opcoes_clientes},
        {"key": "id_banco",   "label": "Banco",
         "type": "combo", "options_fn": _opcoes_bancos},
    ]

    def __init__(self, parent):
        super().__init__(parent, "💳  Contas Bancárias")

    def _make_tree(self, parent):
        return make_tree(parent,
            ("id","tipo","saldo","id_cliente","id_banco"),
            ("ID","Tipo","Saldo","Cliente","Banco"))

    def refresh(self):
        self._clear_tree()
        code, data = listar_contas()
        if code == 200:
            for d in data.values():
                self.tree.insert("", "end", values=(
                    d["id"], d["tipo"], f"{d['saldo']:.2f}",
                    d["id_cliente"], d["id_banco"]))

    def open_create(self):
        def submit(data):
            try:
                saldo = float(data["saldo"])
            except ValueError:
                return False, "Saldo inválido."
            code, obj = criar_conta(data["tipo"], saldo,
                                    data["id_cliente"], data["id_banco"])
            if code == 201:
                self.refresh()
                return True, f"Conta criada: {obj['id']}"
            return False, obj
        FormDialog(self, "Criar Conta", self.FIELDS, submit)

    def _open_edit_dialog(self, rid):
        _, raw = consultar_conta(rid)
        d = raw[rid]
        defaults = {f["key"]: d.get(f["key"], "") for f in self.FIELDS}
        defaults["saldo"] = str(d.get("saldo", ""))
        def submit(data):
            saldo = None
            if data["saldo"]:
                try:
                    saldo = float(data["saldo"])
                except ValueError:
                    return False, "Saldo inválido."
            code, obj = atualizar_conta(rid,
                data["tipo"] or None, saldo,
                data["id_cliente"] or None, data["id_banco"] or None)
            if code == 200:
                self.refresh()
                return True, "Conta atualizada."
            return False, obj
        FormDialog(self, "Editar Conta", self.FIELDS, submit, defaults)

    def _remove(self, rid):
        remover_conta(rid)

# ══════════════════════════════════════════════
# APP PRINCIPAL
# ══════════════════════════════════════════════
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor Bancário")
        self.geometry("1000x580")
        self.configure(bg=BG)
        self.minsize(800, 480)

        sidebar = tk.Frame(self, bg=PANEL, width=170)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="🏛  BANCO", bg=PANEL, fg=ACCENT,
                 font=("Consolas", 14, "bold")).pack(pady=(24,4))
        tk.Label(sidebar, text="Gestor CRUD", bg=PANEL, fg=TXT_DIM,
                 font=("Consolas", 8)).pack(pady=(0,24))
        tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", padx=16, pady=(0,16))

        content = tk.Frame(self, bg=BG)
        content.pack(side="left", fill="both", expand=True)

        self.tabs = {}
        self.tab_frames = {}
        self.active_btn = None

        for label, key, TabClass in [
            ("👤  Bancários", "bancarios", TabBancarios),
            ("🧑‍💼  Clientes",  "clientes",  TabClientes),
            ("🏦  Bancos",     "bancos",     TabBancos),
            ("💳  Contas",     "contas",     TabContas),
        ]:
            frame = TabClass(content)
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.tab_frames[key] = frame

            btn = tk.Button(sidebar, text=label, bg=PANEL, fg=TXT,
                            font=FONT_BODY, relief="flat", anchor="w",
                            padx=16, pady=8, cursor="hand2",
                            command=lambda k=key: self.show_tab(k))
            btn.pack(fill="x")
            self.tabs[key] = btn

        self.show_tab("bancarios")

        tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", padx=16, pady=16)
        tk.Label(sidebar, text="v1.1", bg=PANEL, fg=TXT_DIM,
                 font=("Consolas", 8)).pack(side="bottom", pady=12)

    def show_tab(self, key):
        if self.active_btn:
            self.active_btn.config(bg=PANEL, fg=TXT)
        self.tabs[key].config(bg=ACCENT, fg=BG)
        self.active_btn = self.tabs[key]
        self.tab_frames[key].lift()


if __name__ == "__main__":
    app = App()
    app.mainloop()
