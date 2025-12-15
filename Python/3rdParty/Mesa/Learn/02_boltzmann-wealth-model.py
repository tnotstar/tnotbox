import mesa
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Función para calcular Gini (Igual que antes)
def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.agents]
    x = sorted(agent_wealths)
    N = len(agent_wealths)
    if N == 0: return 0
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B

# 2. El Agente (Actualizado para Mesa 3.0)
class MoneyAgent(mesa.Agent):
    def __init__(self, model):
        # NOTA: En Mesa 3.0 ya no pasamos unique_id, solo el modelo
        super().__init__(model)
        self.wealth = 1

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other_agent = self.random.choice(cellmates)
            if self.wealth > 0 and other_agent != self:
                self.wealth -= 1
                other_agent.wealth += 1

    def step(self):
        self.move()
        self.give_money()

# 3. El Modelo (Actualizado: sin Scheduler explícito)
class MoneyModel(mesa.Model):
    def __init__(self, N, width, height):
        super().__init__()
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        
        # NOTA: No necesitamos self.schedule = RandomActivation...
        
        # Crear agentes
        for _ in range(self.num_agents):
            # Al instanciar el agente con (self), se añade solo a self.agents
            a = MoneyAgent(self) 
            
            # Posicionar
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": "wealth"}
        )

    def step(self):
        self.datacollector.collect(self)
        # NOTA: Nueva forma de activar agentes aleatoriamente en Mesa 3.0
        self.agents.shuffle().do("step")

# --- EJECUCIÓN Y GRÁFICOS ---

model = MoneyModel(100, 10, 10)

print("Ejecutando simulación con Mesa 3.0...")
for i in range(100):
    model.step()

# Obtener datos
gini = model.datacollector.get_model_vars_dataframe()
agent_wealth = model.datacollector.get_agent_vars_dataframe()
end_wealth = agent_wealth.xs(99, level="Step")["Wealth"]

# Graficar
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(gini)
axs[0].set_title("Evolución de la Desigualdad (Gini)")
axs[0].set_ylabel("Coeficiente Gini")
axs[0].set_xlabel("Pasos")

axs[1].hist(end_wealth, bins=range(int(end_wealth.max())+1), edgecolor='black')
axs[1].set_title("Distribución de Riqueza Final")
axs[1].set_xlabel("Riqueza")
axs[1].set_ylabel("Agentes")

plt.tight_layout()
plt.show()