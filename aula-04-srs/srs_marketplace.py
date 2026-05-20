# ============================================================
# 🚀 Sistema SRS — Engenharia de Software
# 📚 Aula 04 · FIAP
# ============================================================

from dataclasses import dataclass, field
from typing import List
from enum import Enum


# ============================================================
# 🎯 ENUM DE PRIORIDADE
# ============================================================

class Prioridade(Enum):
    ALTA = "🔴 Alta"
    MEDIA = "🟡 Média"
    BAIXA = "🟢 Baixa"


# ============================================================
# 📌 REQUISITOS FUNCIONAIS
# ============================================================

@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str


# ============================================================
# ⚡ REQUISITOS NÃO FUNCIONAIS
# ============================================================

@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str
    descricao: str
    criterio_aceitacao: str


# ============================================================
# 🧠 CLASSE PRINCIPAL SRS
# ============================================================

@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str

    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    # --------------------------------------------------------
    # ➕ Adicionar RF
    # --------------------------------------------------------
    def adicionar_rf(self, req: RequisitoFuncional):

        self.requisitos_funcionais.append(req)

        print("\n" + "─" * 55)
        print(f"✅ REQUISITO FUNCIONAL ADICIONADO")
        print("─" * 55)
        print(f"📌 ID: {req.id}")
        print(f"📝 Nome: {req.nome}")
        print(f"🎯 Prioridade: {req.prioridade.value}")
        print("─" * 55 + "\n")

    # --------------------------------------------------------
    # ➕ Adicionar RNF
    # --------------------------------------------------------
    def adicionar_rnf(self, req: RequisitoNaoFuncional):

        self.requisitos_nao_funcionais.append(req)

        print("\n" + "─" * 55)
        print(f"⚡ REQUISITO NÃO FUNCIONAL ADICIONADO")
        print("─" * 55)
        print(f"📌 ID: {req.id}")
        print(f"🛡️ Categoria: {req.categoria}")
        print("─" * 55 + "\n")

    # --------------------------------------------------------
    # 🔍 Validação de Requisitos
    # --------------------------------------------------------
    def validar_requisito(self, rf: RequisitoFuncional):

        resultados = {}

        if len(rf.descricao) < 20:
            resultados["descricao"] = "Descrição muito curta"

        if rf.pre_condicao == "":
            resultados["pre_condicao"] = "Pre-condição não preenchida"

        if any(char.isdigit() for char in rf.descricao):
            resultados["descricao_num"] = (
                "Descrição contém números "
                "(evite números em requisitos)"
            )

        return resultados

    # --------------------------------------------------------
    # 📋 Relatório Geral
    # --------------------------------------------------------
    def relatorio(self):

        print("\n")
        print("═" * 70)
        print(f"📋 DOCUMENTO SRS — {self.projeto}")
        print(f"📦 Versão: {self.versao}")
        print("═" * 70)

        print(f"\n📝 DESCRIÇÃO DO SISTEMA")
        print("─" * 70)
        print(f"{self.descricao}")

        # ====================================================
        # 🔧 RFs
        # ====================================================

        print("\n")
        print("🔧 REQUISITOS FUNCIONAIS")
        print("═" * 70)

        for rf in self.requisitos_funcionais:

            print(f"""
┌─────────────────────────────────────────────────────────────
│ 📌 {rf.id} — {rf.nome}
├─────────────────────────────────────────────────────────────
│ 🎯 Prioridade : {rf.prioridade.value}                     
│ 👤 Ator        : {rf.ator}
│ ⚙️ Pré-condição: {rf.pre_condicao}
│ ✅ Pós-condição: {rf.pos_condicao}
├─────────────────────────────────────────────────────────────
│ 📝 Descrição:
│ {rf.descricao}
└─────────────────────────────────────────────────────────────
""")

        # ====================================================
        # ⚡ RNFs
        # ====================================================

        print("\n")
        print("⚡ REQUISITOS NÃO FUNCIONAIS")
        print("═" * 70)

        for rnf in self.requisitos_nao_funcionais:

            print(f"""
┌─────────────────────────────────────────────────────────────
│ 📌 {rnf.id} — {rnf.categoria}
├─────────────────────────────────────────────────────────────
│ 📝 Descrição:
│ {rnf.descricao}
├─────────────────────────────────────────────────────────────
│ ✔️ Critério de Aceitação:
│ {rnf.criterio_aceitacao}
└─────────────────────────────────────────────────────────────
""")


# ============================================================
# 🚀 CRIAÇÃO DO SRS
# ============================================================

srs = SRS(
    projeto="App de Delivery — Módulo Rastreamento",
    versao="1.0",
    descricao="Sistema de rastreamento em tempo real de entregadores."
)

# ============================================================
# 🔧 REQUISITOS FUNCIONAIS
# ============================================================

srs.adicionar_rf(RequisitoFuncional(
    id="RF-001",
    nome="Rastreamento em Tempo Real",
    descricao="Exibir posição do entregador no mapa atualizada a cada 3 segundos.",
    prioridade=Prioridade.ALTA,
    ator="Cliente",
    pre_condicao="Pedido com status 'Em rota'",
    pos_condicao="Cliente visualiza localização atual do entregador"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-002",
    nome="Notificação de Status",
    descricao="Enviar push notification ao cliente quando status do pedido mudar.",
    prioridade=Prioridade.ALTA,
    ator="Sistema",
    pre_condicao="Cliente com notificações habilitadas",
    pos_condicao="Cliente notificado sobre mudança de status"
))

# ============================================================
# ⚡ REQUISITOS NÃO FUNCIONAIS
# ============================================================

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-001",
    categoria="Desempenho",
    descricao="O sistema deve suportar 50.000 usuários simultâneos.",
    criterio_aceitacao=(
        "Teste de carga com JMeter: "
        "50k req/s com latência menor que 500ms"
    )
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-002",
    categoria="Segurança",
    descricao="Dados de localização devem ser criptografados em trânsito.",
    criterio_aceitacao=(
        "Uso de TLS 1.3 validado por ferramenta de auditoria"
    )
))

# ============================================================
# 🔍 VALIDAÇÃO
# ============================================================

print("\n")
print("🔎 VALIDANDO REQUISITOS...")
print("═" * 70)

erros = srs.validar_requisito(srs.requisitos_funcionais[0])

if erros:

    print("\n⚠️ Problemas encontrados:\n")

    for campo, erro in erros.items():
        print(f"• {campo}: {erro}")

else:

    print("\n✅ Nenhum erro encontrado!")

# ============================================================
# 📋 RELATÓRIO FINAL
# ============================================================

srs.relatorio()