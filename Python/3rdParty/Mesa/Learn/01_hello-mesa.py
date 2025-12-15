#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mesa

# 1. Definición del Agente
class AgenteRegalo(mesa.Agent):
    """Un agente que regala dinero si tiene."""
    def __init__(self, model):
        super().__init__(model)
        self.dinero = 1  # Dotación inicial

    def step(self):
        # Lógica: Si tengo dinero, elijo a otro agente y se lo doy
        if self.dinero > 0:
            # Seleccionar un agente al azar de la lista total de agentes del modelo
            otros_agentes = self.model.agents
            beneficiario = self.random.choice(otros_agentes)
            
            # Transferencia (evitando dárselo a uno mismo si se desea, opcional)
            if beneficiario != self:
                self.dinero -= 1
                beneficiario.dinero += 1

# 2. Definición del Modelo
class ModeloEconomiaSimple(mesa.Model):
    """Modelo donde los agentes intercambian dinero aleatoriamente."""
    def __init__(self, N):
        super().__init__()
        self.num_agentes = N
        
        # Crear N agentes
        for _ in range(self.num_agentes):
            AgenteRegalo(self)  # Se añade automáticamente a self.agents

    def step(self):
        # Activar a todos los agentes en orden aleatorio
        self.agents.shuffle().do("step")

# --- EJECUCIÓN (Script) ---

if __name__ == "__main__":
    # Configuración
    NUM_AGENTES = 10
    PASOS = 5

    print(f"--- Iniciando Simulación con {NUM_AGENTES} agentes ---")
    model = ModeloEconomiaSimple(NUM_AGENTES)

    # Estado inicial
    print("\nEstado Inicial (Dinero por agente):")
    print([a.dinero for a in model.agents])

    # Correr simulación
    for i in range(PASOS):
        model.step()
        print(f"\n--- Paso {i+1} ---")
        riqueza_actual = [a.dinero for a in model.agents]
        print(f"Distribución: {riqueza_actual}")

    print("\n--- Simulación Finalizada ---")
    # Verificamos que el dinero total se conserve (Economía cerrada)
    total_dinero = sum([a.dinero for a in model.agents])
    print(f"Dinero total en el sistema: {total_dinero} (Debe ser {NUM_AGENTES})")
