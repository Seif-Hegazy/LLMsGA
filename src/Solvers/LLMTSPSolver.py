from abc import abstractmethod

import tsplib95.models

from src.PopulationInitializers.PopulationInitializer import PopulationInitializer
from src.Models.Model import Model


class LLMTSPSolver:
    """
    Abstract base class for LLM TSP Solvers
    Different solvers can use different LLMs or different
    ways to solve the TSP problem

    This class is used to facilitate easy swapping of solvers
    """

    def __init__(self, model: Model, population_initializer: PopulationInitializer):
        self.model = model
        self.population_initializer = population_initializer

    @abstractmethod
    def solve(self, problem: tsplib95.models.StandardProblem, problem_optimal_distance: float) -> str:
        pass
