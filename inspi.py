#!/usr/bin/env python3
import time
import yaml
import pickle
import os
import random

hero_races = ("Human", "Elf", "Orc")
hero_choices = ("Warrior", "Mage", "Priest")
dungeon_maps = ("Training Room", "Slime Room", "Chimera Room", "Demonic Room")
save_file = "hero_information.txt"
game_details_path = "TextGameDetails.yml"

if os.path.exists(game_details_path):
    with open(game_details_path) as story_file:
        story_info = yaml.load(story_file, Loader=yaml.FullLoader)
        dungeon_description = story_info["dungeon_description"]
        map_level_complete = story_info["map_level_complete"]
else:
    print("Game files are missing!\nCannot run game")
    exit()

class Monster:
    def __init__(self, map_level):
        self.health = 100 * map_level
        self.attack = 20 * map_level


    def battle_action(self, hero):
        damage = random.randrange(self.attack / 2, self.attack)
        hero.attacked_by(self, damage)


    def attacked_by(self, attacker, damage):
        print("Player attacks monster for {} damage".format(damage))
        self.health -= damage


class Hero:
    def __init__(self, hero_name, hero_health, hero_attack, race_choice,
            hero_choice):
        self.health = hero_health
        self.hero_attack = hero_attack
        self.block_stance = False
        self.name = hero_name
        self.race = race_choice
        self.hero_choice = hero_choice


    def attacked_by(self, attacker, damage):
        """Apply damage taken from attacker."""

        if self.block_stance:
            damage //= 2 #// is "floor" or "integer" division

        print("Monster attacks you for {} damage.".format(damage))
        self.health -= damage

    def block(self):
        print("You switch to a defensive stance reducing damage by half!")
        self.block_stance = True
    
    def battle_action(self, monster):
        damage = random.randrange(self.hero_attack / 2, self.hero_attack)
        self.block_stance = False
        print("1. Attack\t2. Defend")
        action = input("Action: ")
        if action == '1':
            monster.attacked_by(self, damage)
        elif action == '2':
            self.block()
    
    def display_status(self):
        print("Welcome back {} the {}".format(self.name, self.race))
        print("{}, you have {} health.".format(self.hero_choice, self.health))

def create_hero():
    print("What is your name?")
    hero_name = input("My name is: ")

    print("Choose a race")
    print("1. Human\t2. Elf\t3.Orc")

    while True:
        print("Choose a class.")
        print("1.Warrior\t2. Mage\t3. Healer")
        hero_choice = input("My class is: ")
        if hero_choice == '1':
            hero = Warrior(hero_name, 200, 100, race_choice, hero_choice)
            break
        elif hero_choice == '2':
            hero = Mage(hero_name, 100, 50, race_choice, hero_choice)
            break
        elif hero_chocie == '3':
            hero = Healer(hero_name, 200, 25, race_choice, hero_choice)
            break
    return hero


