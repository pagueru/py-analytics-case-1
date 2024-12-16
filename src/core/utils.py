"""
Módulo de utilitários para o projeto.

Este módulo contém funções auxiliares que facilitam o desenvolvimento e manutenção do projeto. 
Inclui operações como limpeza do terminal e inicialização de configurações, além de qualquer 
outra funcionalidade de suporte que possa ser adicionada futuramente.

Funções:
- start_config(): Limpa o terminal e registra o início do script.
"""

import os

from .logger import logger


def start_config() -> None:
    """
    Limpa o terminal e registra o início do script.

    Raises:
        RuntimeError: Se houver erro ao limpar a tela do terminal.
    """
    # Executa o comando e verifica o resultado
    resultado: int = os.system("cls" if os.name == "nt" else "clear")

    if resultado != 0:
        logger.error("Falha ao limpar a tela do terminal.")
        raise RuntimeError("Erro ao tentar limpar a tela do terminal.")

    # Registra o início do script no log
    logger.info("Iniciando o script.")
