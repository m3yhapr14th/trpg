from module.Unit import *

# 히드라
hydra_level = randint(1, 6)
hydra_hp = randint(50, 70)
hydra_mp = 0
hydra_power = randint(10, 15)
hydra_defense = randint(5, 8)
hydra_job = "괴무르족"

Hydra = Unit("히드라", hydra_level, hydra_hp, hydra_mp, hydra_power, hydra_defense, hydra_job, 100)
