from hero_data import *
from matchup_data import MATCHUPS

def find_single_counter(role, enemy_hero):
    if role not in MATCHUPS or enemy_hero not in MATCHUPS[role]:
        return None

    counters = [
        hero
        for hero, matchups in MATCHUPS[role].items()
        if matchups[enemy_hero] > 0
    ]

    return sorted(
        counters,
        key=lambda hero: MATCHUPS[role][hero][enemy_hero],
        reverse=True
    )[:3]

