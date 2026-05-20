# ============================================================
# 🏛️ SISTEMA DE BIBLIOTECA DIGITAL — Biblioteca FIAP
# 📚 Simulação de Casos de Uso em Python
# ============================================================

# ============================================================
# 📦 BASE DE DADOS MOCKADA
# ============================================================

catalogo = [
    {"titulo": "Clean Code",               "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "The Pragmatic Programmer", "autor": "Hunt & Thomas",    "disponivel": True},
    {"titulo": "Design Patterns",          "autor": "Gang of Four",     "disponivel": True},
]

emprestimos = []


# ============================================================
# 🎨 FUNÇÃO AUXILIAR DE INTERFACE
# ============================================================

def titulo(secao):
    print("\n")
    print("═" * 70)
    print(f"{secao}")
    print("═" * 70)


# ============================================================
# 📚 UC-01 — LISTAR CATÁLOGO
# ============================================================

titulo("📚 UC-01 — CATÁLOGO DISPONÍVEL")

for livro in catalogo:

    status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"

    print(f"""
┌────────────────────────────────────────────────────────────┐
│ 📖 Livro : {livro['titulo']}
│ ✍️ Autor : {livro['autor']}
│ 📌 Status: {status}
└────────────────────────────────────────────────────────────┘
""")


# ============================================================
# 🔍 UC-02 — BUSCAR LIVRO
# ============================================================

titulo("🔍 UC-02 — BUSCA DE LIVROS")

busca = "clean"

print(f"🧠 Buscando por: '{busca}'...\n")

resultados = [
    livro for livro in catalogo
    if busca.lower() in livro["titulo"].lower()
]

if resultados:

    print("✅ RESULTADOS ENCONTRADOS:\n")

    for livro in resultados:

        status = (
            "✅ Disponível"
            if livro["disponivel"]
            else "❌ Indisponível"
        )

        print(f"""
┌────────────────────────────────────────────────────────────┐
│ 📖 {livro['titulo']}
│ ✍️ {livro['autor']}
│ 📌 Status: {status}
└────────────────────────────────────────────────────────────┘
""")

else:

    print("❌ Nenhum livro encontrado.")


# ============================================================
# 📌 UC-03 — EMPRÉSTIMO DE LIVRO
# ============================================================

titulo("📌 UC-03 — EMPRÉSTIMO")

leitor = "Ana Silva"
titulo_livro = "Clean Code"

print(f"👤 Leitor : {leitor}")
print(f"📖 Livro  : {titulo_livro}\n")

# ------------------------------------------------------------
# <<include>> Verificar disponibilidade
# ------------------------------------------------------------

livro_encontrado = None

for livro in catalogo:

    if livro["titulo"] == titulo_livro:
        livro_encontrado = livro
        break

# ------------------------------------------------------------
# Fluxos possíveis
# ------------------------------------------------------------

if livro_encontrado is None:

    print("❌ Livro não encontrado no catálogo.")

elif livro_encontrado["disponivel"] is False:

    print(f"⚠️ O livro '{titulo_livro}' já está emprestado!")

else:

    livro_encontrado["disponivel"] = False

    emprestimos.append({
        "leitor": leitor,
        "livro": titulo_livro,
        "atrasado": False
    })

    print("✅ EMPRÉSTIMO REALIZADO COM SUCESSO!")
    print(f"📖 '{titulo_livro}' foi entregue para {leitor}.")


# ============================================================
# 🔄 UC-04 — DEVOLUÇÃO DE LIVRO
# ============================================================

titulo("🔄 UC-04 — DEVOLUÇÃO")

leitor_devolvendo = "Ana Silva"
titulo_devolvendo = "Clean Code"

print(f"👤 Leitor : {leitor_devolvendo}")
print(f"📖 Livro  : {titulo_devolvendo}\n")

registro_encontrado = None

for registro in emprestimos:

    if (
        registro["leitor"] == leitor_devolvendo
        and registro["livro"] == titulo_devolvendo
    ):

        registro_encontrado = registro
        break

# ------------------------------------------------------------
# Fluxo de exceção
# ------------------------------------------------------------

if registro_encontrado is None:

    print("❌ Nenhum empréstimo ativo encontrado.")

else:

    # Atualiza disponibilidade do livro
    for livro in catalogo:

        if livro["titulo"] == titulo_devolvendo:
            livro["disponivel"] = True
            break

    # Remove empréstimo ativo
    emprestimos.remove(registro_encontrado)

    print("✅ DEVOLUÇÃO REALIZADA!")
    print(f"📚 '{titulo_devolvendo}' devolvido com sucesso.\n")

    # ========================================================
    # <<extend>> UC-05 — APLICAR MULTA
    # ========================================================

    houve_atraso = input(
        "⏰ A devolução ocorreu com atraso? (s/n): "
    ).strip().lower()

    print()

    if houve_atraso == "s":

        print("⚠️ MULTA APLICADA")
        print("📋 O leitor deverá regularizar o pagamento.")

    else:

        print("✅ DEVOLUÇÃO DENTRO DO PRAZO")
        print("👍 Nenhuma multa foi aplicada.")


# ============================================================
# 📖 ESTADO FINAL DO SISTEMA
# ============================================================

titulo("📊 ESTADO FINAL DO SISTEMA")

print("📚 CATÁLOGO ATUALIZADO:\n")

for livro in catalogo:

    status = (
        "✅ Disponível"
        if livro["disponivel"]
        else "❌ Emprestado"
    )

    print(f"• {livro['titulo']} → {status}")

print("\n📋 EMPRÉSTIMOS ATIVOS:")
print(f"{emprestimos}")