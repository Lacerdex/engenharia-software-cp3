# ============================================================
# STREAMING ENGINE - IMPLEMENTAÇÃO DE RELACIONAMENTOS UML
# Arquitetura: Composição, Agregação e Associação
# ============================================================

class Movie:
    """Entidade independente (Agregada ao catálogo)."""
    
    def __init__(self, name: str, runtime: int, category: str):
        self.name = name
        self.runtime = runtime  # em minutos
        self.category = category

    def __repr__(self):
        return f"<Movie: {self.name} | {self.category}>"


class Review:
    """Parte integrante do perfil do usuário (Composição)."""
    
    def __init__(self, score: float, text: str):
        if score < 0 or score > 10:
            raise ValueError("A pontuação deve ser entre 0 e 10.")
        
        self.score = score
        self.text = text
        self.target_movie: Movie | None = None  # Associação direcionada

    def __repr__(self):
        ref = self.target_movie.name if self.target_movie else "N/A"
        return f"[Review: {ref} - Nota: {self.score}]"


class Inventory:
    """Gerenciador de títulos (Composto pela plataforma)."""
    
    def __init__(self, label: str):
        self.label = label
        self._items: list[Movie] = []

    @property
    def total_count(self) -> int:
        return len(self._items)

    def push_movie(self, item: Movie) -> None:
        """Adiciona um objeto Movie ao inventário (Agregação)."""
        self._items.append(item)
        print(f" -> Recurso '{item.name}' vinculado ao inventário '{self.label}'.")

    def show_content(self) -> None:
        print(f"\n--- EXPLORAR: {self.label.upper()} ({self.total_count} itens) ---")
        for m in self._items:
            print(f" > {m.name:25} | {m.runtime} min | Gênero: {m.category}")


class Customer:
    """Usuário final. Gerencia o ciclo de vida de suas Review (Composição)."""
    
    def __init__(self, username: str, contact: str, tier: str):
        self.username = username
        self.contact = contact
        self.tier = tier
        self._history: list[Review] = []

    def post_review(self, movie: Movie, review: Review) -> None:
        """Cria o elo entre a avaliação e o filme."""
        review.target_movie = movie
        self._history.append(review)
        print(f" [LOG] Usuário '{self.username}' postou uma nota {review.score} para '{movie.name}'.")

    def display_activity(self) -> None:
        print(f"\n--- PERFIL: {self.username} [{self.tier}] ---")
        for r in self._history:
            movie_title = r.target_movie.name if r.target_movie else "Desconhecido"
            print(f" * {movie_title:25} | Avaliação: {r.score}/10")
            print(f"   Comentário: \"{r.text}\"")


class ServiceProvider:
    """Root do sistema. Controla a existência dos Inventories (Composição)."""
    
    def __init__(self, brand: str, region: str):
        self.brand = brand
        self.region = region
        self._collections: list[Inventory] = []

    def link_inventory(self, inv: Inventory) -> None:
        self._collections.append(inv)

    def __repr__(self):
        return f"Provider(Brand={self.brand}, Region={self.region})"


# ------------------------------------------------------------
# AMBIENTE DE EXECUÇÃO (DEMO)
# ------------------------------------------------------------
if __name__ == "__main__":
    print("::: INICIANDO MIDDLEWARE DE STREAMING :::\n")

    # Instanciando o provedor principal
    service = ServiceProvider("Netflix", "Global")

    # Gerando inventário via composição lógica
    main_inventory = Inventory("Top 10 Brasil")
    service.link_inventory(main_inventory)

    # Definindo objetos independentes
    m1 = Movie("Oppenheimer", 180, "Biography/Drama")
    m2 = Movie("Barbie", 114, "Adventure/Comedy")

    print("[ Gerenciamento de Assets ]")
    main_inventory.push_movie(m1)
    main_inventory.push_movie(m2)

    # Configuração de usuário e interação
    user = Customer("Ana", "ana@provider.com", "Gold Tier")
    
    # Criando avaliação
    feedback = Review(9.5, "Obra prima técnica.")
    
    print("\n[ Processamento de Feedback ]")
    user.post_review(m1, feedback)

    # Saída de dados estruturada
    main_inventory.show_content()
    user.display_activity()

    print("\n" + ":" * 40)
    print("::: TESTE DE PERSISTÊNCIA DE MEMÓRIA :::")
    
    # Simulação: O inventário é destruído
    del main_inventory
    
    # O objeto m1 deve persistir por ser uma agregação
    try:
        print(f" Objeto '{m1.name}' recuperado da memória: {m1}")
        print(" STATUS: Agregação validada (O dado sobrevive à coleção).")
    except NameError:
        print(" ERRO: O dado foi perdido.")
    
    print(":" * 40)