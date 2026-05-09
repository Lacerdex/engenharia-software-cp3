import time

print("=" * 40)
print("🏋️ GymTrack — Validador de Treino")
print("=" * 40)

# --- DADOS DO TREINO (mude os valores para testar!) ---
exercicio = "Supino Reto"
peso_kg   = 80
repeticoes = 10

# -------------------------------------------------------
# RF01 — O sistema deve validar o nome do exercício
# (não pode ser vazio)
# -------------------------------------------------------

if exercicio == "":
  print("❌ [RF01] O nome do exercício não pode ser vazio!")
else:
  print(f"✅ [RF01] Nome do exercício válido!")

# -------------------------------------------------------
# RF02 — O peso deve estar entre 1 e 300 kg
# -------------------------------------------------------

if 1 <= peso_kg <= 300:
  print(f"✅ [RF02] Peso válido!")
else:
  print("❌ [RF02] Peso inválido!")

# -------------------------------------------------------
# RF03 — As repetições devem estar entre 1 e 50
# -------------------------------------------------------

if repeticoes >= 1 and repeticoes <= 50:
  print("✅ [RF03] Repetições válidas!")
else:
  print("❌ [RF03] Repetições inválidas!")
print("="*40)

# -------------------------------------------------------
# RNF01 — O registro deve ocorrer em menos de 200ms
# -------------------------------------------------------
inicio = time.time()

# Simula o registro no banco de dados
time.sleep(0.05)
print(f"✅ Série registrada: {exercicio} | {peso_kg}kg x {repeticoes} reps")
print("=" * 40)
fim = time.time()
tempo_ms = (fim - inicio) * 1000
if tempo_ms < 200:
    print(f"✅ [RNF01] Tempo de registro: {tempo_ms:.2f}ms ← dentro do limite!")
else:
    print(f"❌ [RNF01] Lento demais: {tempo_ms:.2f}ms ← limite é 200ms")
print("=" * 40)