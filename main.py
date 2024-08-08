import random

def main():
    personagem = input("Qual o nome do personagem?\n")
    print(personagem)
    
    atributos_do_personagem = {"nome": "", "level": 0, "str": 10, "dex": 10, "int": 10, "life": 200, "forca_base": 2}

    atributos_do_personagem["nome"] = personagem
    print(atributos_do_personagem)

    atributo_principal = input("Qual o seu atributo principal?\n")
    print(atributo_principal)

    atributo_do_monstro = {"nome": "", "life": 100, "forca_maxima": 10, "forca_minima": 2}

    orc = atributo_do_monstro.copy()
    orc["nome"] = "Kalgur"
    dragon = atributo_do_monstro.copy()
    dragon["nome"] = "Charizard"
    

    lista_de_monstros = [orc, dragon]

    life_do_personagem = atributos_do_personagem["life"]

    # Setup de combat
    for monstro in lista_de_monstros:
        life_do_monstro = monstro["life"]
        print(f"A luta do agora é do {atributos_do_personagem['nome']} contra {monstro['nome']}")

        # É o nosso combate
        while True:
           if life_do_personagem < 0:
              print(f"{atributos_do_personagem['nome']} morreu")
              exit(0)

           if life_do_monstro < 0:
              print(f"O {monstro['nome']} morreu")
              break

           turno = random.randint(0,1)
           if turno == 0:
               # Acessando a chave do dicionário de forma estática
               dano_base = random.randint(0,atributos_do_personagem["forca_base"])
               # Acessando a chave do dicionário de forma dinamica
               atributo = atributos_do_personagem[atributo_principal]
               dano = dano_base * atributo
               life_do_monstro -= dano 
               print(f"{atributos_do_personagem['nome']} - causou {dano}, o monstro {monstro['nome']} esta com {life_do_monstro}")
           elif turno == 1:
               dano = random.randint(monstro["forca_minima"],monstro["forca_maxima"])
               life_do_personagem -= dano
               print(f"{monstro['nome']} - causou {dano}, o personagem {atributos_do_personagem['nome']} esta com {life_do_personagem}")
                # turno do monstro
        
        
main()