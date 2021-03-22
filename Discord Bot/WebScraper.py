import requests
from bs4 import BeautifulSoup
import bs4

# left to right: Nor, Fir, Wat, Ele, Gra, Ice, Fig, Poi, Gro, Fly, Psy, Bug, Roc, Gho, Dra, Dar, Ste, Fai

# the first axis of the matrix is the type of attack, and the second axis is the type of the defending pokemon. This
# does not take into account dual types
# TODO implement type advantage

type_matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 0, 1, 1, .5, 1],       # Normal
               [1, .5, .5, 1, 2, 2, 1, 1, 1, 1, 1, 2, .5, 1, .5, 1, 2, 1],     # Fire
               [1, 2, .5, 1, .5, 1, 1, 1, 2, 1, 1, 1, 2, 1, .5, 1, 1, 1],      # Water
               [1, 1, 2, .5, .5, 1, 1, 1, 0, 2, 1, 1, 1, 1, .5, 1, 1, 1],      # Electric
               [1, .5, 2, 1, .5, 1, 1, .5, 2, .5, 1, .5, 2, 1, .5, 1, .5, 1],  # Grass
               [1, .5, .5, 1, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, .5, 1],     # Ice
               [2, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, .5],    # Fighting
               [1, 1, 1, 1, 2, 1, 1, .5, .5, 1, 1, 1, .5, .5, 1, 1, 0, 2],     # Poison
               [1, 2, 1, 2, .5, 1, 1, 2, 1, 0, 1, .5, 2, 1, 1, 1, 2, 1],       # Ground
               [1, 1, 1, .5, 2, 1, 2, 1, 1, 1, 1, 2, .5, 1, 1, 1, .5, 1],      # Flying
               [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, .5, 1, 1, 1, 1, 0, .5, 1],       # Psychic
               [1, .5, 1, 1, 2, 1, .5, .5, 1, .5, 2, 1, 1, .5, 1, 2, .5, .5],  # Bug
               [1, 2, 1, 1, 1, 2, .5, 1, .5, 2, 1, 2, 1, 1, 1, 1, .5, 1],      # Rock
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 1],        # Ghost
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, .5, 0],        # Dragon
               [1, 1, 1, 1, 1, 1, .5, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, .5],      # Dark
               [1, .5, .5, .5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, .5, 2],     # Steel
               [1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, 2, 2, .5, 1]]      # Fairy


def grab_poke(poke):

    url = "https://pokemondb.net/pokedex/" + poke
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("a", class_="type-icon")

    temp = []
    tracker = 0

    for result in results:
        if result.has_attr("title"):
            continue
        elif result.parent.has_attr("class"):
            continue
        else:
            if result.text in temp:
                continue
            elif tracker >= 2:
                break
            else:
                temp.append(result.text)
                tracker += 1

    return temp


def turn_to_string(lis):

    temp = ""

    for item in lis:
        temp += item + " "

    return temp


def get_poke_image(poke):
    url = "https://pokemondb.net/pokedex/" + poke
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("img")

    return results["src"]


def get_poke_dex_entry(poke):
    url = "https://pokemondb.net/pokedex/" + poke
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    pokedex_entry = soup.find("td", class_="cell-med-text")

    return pokedex_entry.next_element


def get_type(_type):
    switcher = {
        "normal": 0,
        "fire": 1,
        "water": 2,
        "electric": 3,
        "grass": 4,
        "ice": 5,
        "fighting": 6,
        "poison": 7,
        "ground": 8,
        "flying": 9,
        "psychic": 10,
        "bug": 11,
        "rock": 12,
        "ghost": 13,
        "dragon": 14,
        "dark": 15,
        "steel": 16,
        "fairy": 17
    }

    return switcher.get(_type.lower())


def get_gen(gen):
    switcher = {
        "1": "Generation I",
        "I": "Generation I",
        "2": "Generation II",
        "II": "Generation II",
        "3": "Generation III",
        "III": "Generation III",
        "4": "Generation IV",
        "IV": "Generation IV",
        "5": "Generation V",
        "V": "Generation V",
        "6": "Generation VI",
        "VI": "Generation VI",
        "7": "Generation VII",
        "VII": "Generation VII",
        "8": "Generation VIII",
        "VIII": "Generation VIII"
    }

    return switcher.get(gen.upper())


def get_color(_type):
    switcher = {
        "Normal": 0xE1C699,
        "Fire": 0xFF6347,
        "Water": 0x008080,
        "Electric": 0xFFFF33,
        "Grass": 0x7EC850,
        "Ice": 0xA5F2F3,
        "Fighting": 0x800000,
        "Poison": 0x301934,
        "Ground": 0xC2B280,
        "Flying": 0x87CEEB,
        "Psychic": 0xFF69B4,
        "Bug": 0x9ACD32,
        "Rock": 0xD3D3D3,
        "Ghost": 0x30106B,
        "Dragon": 0xB19CD9,
        "Dark": 0x5C4033,
        "Steel": 0xEBECF0,
        "Fairy": 0xFFB6C1
    }

    return switcher.get(_type)

