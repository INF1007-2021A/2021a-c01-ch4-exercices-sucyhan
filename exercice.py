#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    longueur= len(string)
    return longueur

def remove_third_char(string: str) -> str:
   supprime=list(string)
   for x in supprime:
       if x=='w':
           x=='z'
           return supprime


def replace_char(string: str, old_char: str, new_char: str) -> str:
    string=list(string)
    string[6]="z"
    string="".join(string)
    return string


def get_number_of_char(string: str, char: str) -> int:
    compte=0
    for x in range(len(string)):
        if string[x]==char:
            compte+=1
    return compte


def get_number_of_words(sentence: str, word: str) -> int:
    compter=0
    split=sentence.split()
    for i in range(len(split)):
        if split[i]==word:
            compter+=1
    return compter



def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
