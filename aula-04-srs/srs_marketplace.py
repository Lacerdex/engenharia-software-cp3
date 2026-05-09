# ============================================================
# 🚀 SRS em Python — Rode no Google Colab!
# Aula 04 — Engenharia de Software · FIAP
# ============================================================
from dataclasses import dataclass, field
from typing import List
from enum import Enum

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"

@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str

@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str  # Desempenho, Segurança, Usabilidade...
    descricao: str
    criterio_aceitacao: str
@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)
        print(f"✅ RF '{req.id}' adicionado!")

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)
        print(f"✅ RNF '{req.id}' adicionado!")

    def validar_requisito(self, rf: RequisitoFuncional):
            resultados = {}

            if len(rf.descricao) < 20:
                resultados["descricao"] = "Descrição muito curta"

            if rf.pre_condicao == "":
                resultados["pre_condicao"] = "Pre-condição não preenchida"

            if any(char.isdigit() for char in rf.descricao):
                resultados["descricao_num"] = "Descrição contém números (evite em requisitos)"

            return resultados


    def relatorio(self):
        print(f"\n{'='*50}")
        print(f"📋 SRS — {self.projeto} v{self.versao}")
        print(f"{'='*50}")
        print(f"📝 {self.descricao}\n")

        print(f"🔧 REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"  [{rf.id}] {rf.nome} — Prioridade: {rf.prioridade.value}")
            print(f"       Ator: {rf.ator}")
            print(f"       📌 {rf.descricao}\n")

        print(f"⚡ REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"  [{rnf.id}] {rnf.categoria}")
            print(f"       📌 {rnf.descricao}")
            print(f"       ✔️  Critério: {rnf.criterio_aceitacao}\n")

# ---- Criando o SRS do App de Delivery ----
srs = SRS(
    projeto="App de Delivery — Módulo Rastreamento",
    versao="1.0",
    descricao="Sistema de rastreamento em tempo real de entregadores."
)

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

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-001",
    categoria="Desempenho",
    descricao="O sistema deve suportar 50.000 usuários simultâneos.",
    criterio_aceitacao="Teste de carga com JMeter: 50k req/s com latência < 500ms"
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-002",
    categoria="Segurança",
    descricao="Dados de localização devem ser criptografados em trânsito.",
    criterio_aceitacao="Uso de TLS 1.3 validado por ferramenta de auditoria"
))

erros = srs.validar_requisito(srs.requisitos_funcionais[0])
print(f"\n\nErros encontrados: {erros}\n\n")
srs.relatorio()