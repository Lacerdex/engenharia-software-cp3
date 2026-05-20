# ============================================================
# 🚀 Sistema de Cadastro de Usuário
# ============================================================

import re


def exibir_status(titulo: str, mensagem: str, icone: str = "•"):
    """Exibe mensagens formatadas no terminal."""
    print(f"{icone} {titulo}")
    print(f"   {mensagem}\n")


def cadastro_usuario(email: str, senha: str, email_ja_existe: bool, confirmou_email: bool, indice: int) -> str:
    """
    Fluxo de cadastro de usuário inspirado em apps modernos.
    """

    print("\n" + "═" * 55)
    print(f"        📋 INICIANDO TESTE {indice}")
    print("═" * 55 + "\n")

    # ========================================================
    # 1️⃣ Validar e-mail
    # ========================================================
    exibir_status("Validando e-mail...", f"Verificando formato de: {email}", "🔎")

    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"

    if not re.match(padrao_email, email):
        return (
            "❌ ERRO NO CADASTRO\n"
            "──────────────────────────────\n"
            "O e-mail informado é inválido.\n"
            "Exemplo válido: joao@email.com"
        )

    # ========================================================
    # 2️⃣ Verificar duplicidade
    # ========================================================
    exibir_status("Consultando banco de dados...", "Verificando se o e-mail já existe", "🗂️")

    if email_ja_existe:
        return (
            "⚠️ E-MAIL JÁ CADASTRADO\n"
            "──────────────────────────────\n"
            "Este e-mail já possui uma conta.\n"
            "Faça login ou recupere sua senha."
        )

    # ========================================================
    # 3️⃣ Criar conta
    # ========================================================
    exibir_status("Criando conta...", f"Usuário: {email}", "👤")

    # ========================================================
    # 4️⃣ Enviar confirmação
    # ========================================================
    exibir_status(
        "Enviando confirmação...",
        f"Um link foi enviado para {email}",
        "📨"
    )

    # ========================================================
    # 5️⃣ Validar confirmação
    # ========================================================
    if not confirmou_email:
        return (
            "⌛ CADASTRO EXPIRADO\n"
            "──────────────────────────────\n"
            "O link de confirmação não foi utilizado.\n"
            "Solicite um novo e-mail de ativação."
        )

    # ========================================================
    # 6️⃣ Sucesso
    # ========================================================
    return (
        "✅ CADASTRO CONCLUÍDO\n"
        "──────────────────────────────\n"
        f"Bem-vindo(a), {email}!\n"
        "Sua conta foi ativada com sucesso."
    )


# ============================================================
# 🧪 TESTES
# ============================================================

print(cadastro_usuario("joao@email.com", "senha123", False, True, 1))

print(cadastro_usuario("email-invalido", "senha123", False, True, 2))

print(cadastro_usuario("joao@email.com", "senha123", True, True, 3))