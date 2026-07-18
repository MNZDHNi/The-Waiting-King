from dataclasses import dataclass


@dataclass
class InitConfig:
    # screen size
    width: int = 100
    height: int = 30
