import tkinter as tk
from tkinter import ttk, messagebox


class Montadora:
    def __init__(self, codigoMontadora, estado, razaoSocial):
        self.codigoMontadora = codigoMontadora
        self.estado = estado
        self.razaoSocial = razaoSocial
    def setCodigoMontadora(self, codigoMontadora):
        self.codigoMontadora = codigoMontadora
    def setEstado(self, estado):
        self.estado = estado
    def setRazaoSocial(self, razaoSocial):
        self.razaoSocial = razaoSocial
    def getCodigoMontadora(self): return self.codigoMontadora
    def getEstado(self): return self.estado
    def getRazaoSocial(self): return self.razaoSocial


class Modelo:
    def __init__(self, codigoModelo, nomeModelo, montadora):
        self.codigoModelo = codigoModelo
        self.nomeModelo = nomeModelo
        self.montadora = montadora

    def setCodigoModelo(self, codigoModelo):
        self.codigoModelo = codigoModelo
    def setNomeModelo(self, nomeModelo):
        self.nomeModelo = nomeModelo
    def setMontadora(self, montadora):
        self.montadora = montadora
    def getCodigoModelo(self): return self.codigoModelo
    def getNomeModelo(self): return self.nomeModelo
    def getMontadora(self): return self.montadora


class Carro:
    def __init__(self, placa, modelo, anoFabricacao):
        self.placa = placa
        self.modelo = modelo
        self.anoFabricacao = anoFabricacao

    def setPlaca(self, placa):
        self.placa = placa
    def setModelo(self, modelo):
        self.modelo = modelo
    def setAnoFabricacao(self, anoFabricacao):
        self.anoFabricacao = anoFabricacao
    def getPlaca(self): return self.placa
    def getModelo(self): return self.modelo
    def getAnoFabricacao(self): return self.anoFabricacao


montadoras = []
modelos = []
carros = []


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Carros")
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_montadora = MontadoraTab(notebook)
        self.tab_modelo = ModeloTab(notebook, self.tab_montadora)
        self.tab_carro = CarroTab(notebook, self.tab_modelo)

        notebook.add(self.tab_montadora, text="Montadoras")
        notebook.add(self.tab_modelo, text="Modelos")
        notebook.add(self.tab_carro, text="Carros")


class MontadoraTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self._build_form()
        self._build_list()

    def _build_form(self):
        form = tk.LabelFrame(self, text="Cadastrar Montadora", padx=8, pady=8)
        form.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        tk.Label(form, text="Código:").grid(row=0, column=0, sticky="w")
        self.entry_codigo = tk.Entry(form, width=20)
        self.entry_codigo.grid(row=0, column=1, pady=3)

        tk.Label(form, text="Estado (UF):").grid(row=1, column=0, sticky="w")
        self.entry_estado = tk.Entry(form, width=20)
        self.entry_estado.grid(row=1, column=1, pady=3)

        tk.Label(form, text="Razão Social:").grid(row=2, column=0, sticky="w")
        self.entry_razao = tk.Entry(form, width=20)
        self.entry_razao.grid(row=2, column=1, pady=3)

        tk.Button(form, text="Cadastrar", command=self._cadastrar).grid(
            row=3, column=0, columnspan=2, pady=6
        )

    def _build_list(self):
        list_frame = tk.LabelFrame(self, text="Montadoras Cadastradas", padx=8, pady=8)
        list_frame.grid(row=0, column=1, padx=10, pady=10)

        cols = ("Código", "Razão Social", "Estado")
        self.tree = ttk.Treeview(list_frame, columns=cols, show="headings", height=10)
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack()

    def _cadastrar(self):
        codigo_str = self.entry_codigo.get().strip()
        estado = self.entry_estado.get().strip()
        razao = self.entry_razao.get().strip()

        if not codigo_str or not estado or not razao:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return
        if not codigo_str.isdigit():
            messagebox.showwarning("Aviso", "Código deve ser numérico.")
            return

        montadora = Montadora(int(codigo_str), estado, razao)
        montadoras.append(montadora)
        self.tree.insert("", "end", values=(montadora.getCodigoMontadora(),
                                            montadora.getRazaoSocial(),
                                            montadora.getEstado()))
        self.entry_codigo.delete(0, "end")
        self.entry_estado.delete(0, "end")
        self.entry_razao.delete(0, "end")

    def get_montadoras_display(self):
        return [f"{m.getCodigoMontadora()} - {m.getRazaoSocial()}" for m in montadoras]


class ModeloTab(tk.Frame):
    def __init__(self, parent, montadora_tab):
        super().__init__(parent)
        self.montadora_tab = montadora_tab
        self._build_form()
        self._build_list()

    def _build_form(self):
        form = tk.LabelFrame(self, text="Cadastrar Modelo", padx=8, pady=8)
        form.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        tk.Label(form, text="Código:").grid(row=0, column=0, sticky="w")
        self.entry_codigo = tk.Entry(form, width=20)
        self.entry_codigo.grid(row=0, column=1, pady=3)

        tk.Label(form, text="Nome:").grid(row=1, column=0, sticky="w")
        self.entry_nome = tk.Entry(form, width=20)
        self.entry_nome.grid(row=1, column=1, pady=3)

        tk.Label(form, text="Montadora:").grid(row=2, column=0, sticky="w")
        self.combo_montadora = ttk.Combobox(form, width=18, state="readonly")
        self.combo_montadora.grid(row=2, column=1, pady=3)

        tk.Button(form, text="Atualizar Lista", command=self._refresh_combo).grid(
            row=3, column=0, columnspan=2, pady=2
        )
        tk.Button(form, text="Cadastrar", command=self._cadastrar).grid(
            row=4, column=0, columnspan=2, pady=4
        )

    def _build_list(self):
        list_frame = tk.LabelFrame(self, text="Modelos Cadastrados", padx=8, pady=8)
        list_frame.grid(row=0, column=1, padx=10, pady=10)

        cols = ("Código", "Nome", "Montadora")
        self.tree = ttk.Treeview(list_frame, columns=cols, show="headings", height=10)
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        self.tree.pack()

    def _refresh_combo(self):
        self.combo_montadora["values"] = self.montadora_tab.get_montadoras_display()

    def _cadastrar(self):
        codigo_str = self.entry_codigo.get().strip()
        nome = self.entry_nome.get().strip()
        selected = self.combo_montadora.get()

        if not codigo_str or not nome or not selected:
            messagebox.showwarning("Aviso", "Preencha todos os campos e selecione uma montadora.")
            return
        if not codigo_str.isdigit():
            messagebox.showwarning("Aviso", "Código deve ser numérico.")
            return

        codigo_montadora = int(selected.split(" - ")[0])
        montadora = next((m for m in montadoras if m.getCodigoMontadora() == codigo_montadora), None)
        if montadora is None:
            messagebox.showerror("Erro", "Montadora não encontrada.")
            return

        modelo = Modelo(int(codigo_str), nome, montadora)
        modelos.append(modelo)
        self.tree.insert("", "end", values=(modelo.getCodigoModelo(),
                                            modelo.getNomeModelo(),
                                            montadora.getRazaoSocial()))
        self.entry_codigo.delete(0, "end")
        self.entry_nome.delete(0, "end")
        self.combo_montadora.set("")

    def get_modelos_display(self):
        return [f"{m.getCodigoModelo()} - {m.getNomeModelo()}" for m in modelos]


class CarroTab(tk.Frame):
    def __init__(self, parent, modelo_tab):
        super().__init__(parent)
        self.modelo_tab = modelo_tab
        self._build_form()
        self._build_list()

    def _build_form(self):
        form = tk.LabelFrame(self, text="Cadastrar Carro", padx=8, pady=8)
        form.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        tk.Label(form, text="Placa:").grid(row=0, column=0, sticky="w")
        self.entry_placa = tk.Entry(form, width=20)
        self.entry_placa.grid(row=0, column=1, pady=3)

        tk.Label(form, text="Ano Fabricação:").grid(row=1, column=0, sticky="w")
        self.entry_ano = tk.Entry(form, width=20)
        self.entry_ano.grid(row=1, column=1, pady=3)

        tk.Label(form, text="Modelo:").grid(row=2, column=0, sticky="w")
        self.combo_modelo = ttk.Combobox(form, width=18, state="readonly")
        self.combo_modelo.grid(row=2, column=1, pady=3)

        tk.Button(form, text="Atualizar Lista", command=self._refresh_combo).grid(
            row=3, column=0, columnspan=2, pady=2
        )
        tk.Button(form, text="Cadastrar", command=self._cadastrar).grid(
            row=4, column=0, columnspan=2, pady=4
        )

    def _build_list(self):
        list_frame = tk.LabelFrame(self, text="Carros Cadastrados", padx=8, pady=8)
        list_frame.grid(row=0, column=1, padx=10, pady=10)

        cols = ("Placa", "Modelo", "Montadora", "Ano")
        self.tree = ttk.Treeview(list_frame, columns=cols, show="headings", height=10)
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110)
        self.tree.pack()

    def _refresh_combo(self):
        self.combo_modelo["values"] = self.modelo_tab.get_modelos_display()

    def _cadastrar(self):
        placa = self.entry_placa.get().strip()
        ano_str = self.entry_ano.get().strip()
        selected = self.combo_modelo.get()

        if not placa or not ano_str or not selected:
            messagebox.showwarning("Aviso", "Preencha todos os campos e selecione um modelo.")
            return
        if not ano_str.isdigit():
            messagebox.showwarning("Aviso", "Ano deve ser numérico.")
            return

        codigo_modelo = int(selected.split(" - ")[0])
        modelo = next((m for m in modelos if m.getCodigoModelo() == codigo_modelo), None)
        if modelo is None:
            messagebox.showerror("Erro", "Modelo não encontrado.")
            return

        carro = Carro(placa, modelo, int(ano_str))
        carros.append(carro)
        self.tree.insert("", "end", values=(carro.getPlaca(),
                                            modelo.getNomeModelo(),
                                            modelo.getMontadora().getRazaoSocial(),
                                            carro.getAnoFabricacao()))
        self.entry_placa.delete(0, "end")
        self.entry_ano.delete(0, "end")
        self.combo_modelo.set("")


if __name__ == "__main__":
    app = App()
    app.mainloop()
