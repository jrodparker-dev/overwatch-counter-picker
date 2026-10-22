import os
from counter_engine import *
from hero_data import *
from matchup_data import MATCHUPS

ROLE_NAMES = {
    "tank": "Tank",
    "tanks": "Tank",
    "dps": "DPS",
    "damage": "DPS",
    "support": "Support",
    "supports": "Support"
}


def main():
    print("Welcome to Overwatch Counter Picker!")

    # Get and validate role
    role_input = input("Enter your role: ").strip().casefold()
    role = ROLE_NAMES.get(role_input)

    if role is None:
        print("Invalid role!")
        return

    # Create case-insensitive hero lookup
    hero_names = {
        name.casefold(): name
        for name in MATCHUPS[role]
    }

    # Get and validate enemy hero
    enemy_input = input("Enter the enemy hero: ").strip().casefold()
    enemy_hero = hero_names.get(enemy_input)

    if enemy_hero is None:
        print("Invalid hero for the selected role!")
        return

    # Find counters
    counters = find_single_counter(role, enemy_hero)

    if not counters:
        print("No counters found.")
    else:
        print(f"\nBest counters against {enemy_hero}:")
        for i, hero in enumerate(counters, start=1):
            print(f"{i}. {hero}")


if __name__ == "__main__":
    main()
