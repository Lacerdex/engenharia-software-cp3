# ============================================================
# DIAGRAMA DE SEQUÊNCIA — SISTEMA DE TRANSFERÊNCIA (NUBANK)
# Desenvolvimento de Sistemas - Arquitetura de Software
# ============================================================


class BancoDados:
    """Simulação da camada de persistência e dados das contas."""

    def __init__(self) -> None:
        self.accounts = {"user_123": 500.0}

    def checar_saldo(self, account_id: str) -> float:
        return self.accounts.get(account_id, 0.0)

    def realizar_debito(self, account_id: str, amount: float) -> bool:
        current_balance = self.checar_saldo(account_id)
        if current_balance >= amount:
            self.accounts[account_id] = current_balance - amount
            return True
        return False


class API_Nubank:
    """Camada de backend que processa as regras de negócio."""

    def __init__(self) -> None:
        self.db = BancoDados()

    def efetuar_pagamento(self, customer_id: str, value: float) -> dict:
        balance = self.db.checar_saldo(customer_id)

        if balance < value:
            return {"success": False, "reason": "saldo insuficiente"}

        # Executa o débito se houver saldo
        self.db.realizar_debito(customer_id, value)
        new_balance = self.db.checar_saldo(customer_id)

        return {"success": True, "remaining_balance": new_balance}


class AplicativoMovel:
    """Interface do usuário que dispara as ações no fluxo do diagrama."""

    def __init__(self) -> None:
        self.backend = API_Nubank()

    def enviar_pix(self, conta_id: str, valor_transferencia: float) -> None:
        print(f"[Mobile] Solicitando envio de R$ {valor_transferencia:,.2f}...")

        response = self.backend.efetuar_pagamento(conta_id, valor_transferencia)

        if response["success"]:
            saldo_atual = response["remaining_balance"]
            print(
                f"[Mobile] ✅ Sucesso! Novo saldo disponível: R$ {saldo_atual:,.2f}"
            )
        else:
            motivo_falha = response["reason"]
            print(f"[Mobile] ❌ Falha na operação: {motivo_falha}")


# ============================================================
# EXECUÇÃO DOS CENÁRIOS DE TESTE
# ============================================================
if __name__ == "__main__":
    client_app = AplicativoMovel()

    print("--- Cenário 1: Margem de saldo positiva ---")
    client_app.enviar_pix("user_123", 200.0)

    print("\n--- Cenário 2: Tentativa sem saldo suficiente ---")
    client_app.enviar_pix("user_123", 500.0)

    print("\n--- Cenário 3: Débitos consecutivos ---")
    client_app.enviar_pix("user_123", 100.0)
    client_app.enviar_pix("user_123", 250.0)