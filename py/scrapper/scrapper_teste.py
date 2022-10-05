import requests
from bs4 import BeautifulSoup
import time
import random

file = open('D:\\testep\[novo]\scrap_teste2.csv','w', encoding='utf-8')

#lista = ['XXX',
#         'https://pt.wikipedia.org/wiki/Antologia',
#         'https://uol.com.br',
#         'https://en.wikipedia.org/wiki/Andro_Dunos',
#         'https://en.wikipedia.org/wiki/NBA_Jam_(1993_video_game)',
#         'https://en.wikipedia.org/wiki/NBA_Hangtime',
#         'https://en.wikipedia.org/wiki/NBA_Showtime:_NBA_on_NBC',
#         'https://en.wikipedia.org/wiki/NBA_Hoopz']

lista = [
'https://en.wikipedia.org/wiki/Aero_Fighters_2',
'https://en.wikipedia.org/wiki/Aero_Fighters#Developer',
'https://en.wikipedia.org/wiki/Aero_Fighters_3',
'https://en.wikipedia.org/wiki/Aggressors_of_Dark_Kombat',
'https://en.wikipedia.org/wiki/Alpha_Mission_II',
'https://en.wikipedia.org/wiki/Andro_Dunos',
'https://en.wikipedia.org/wiki/Visco_Corporation',
'https://en.wikipedia.org/wiki/Art_of_Fighting#Art_of_Fighting_(1992)',
'https://en.wikipedia.org/wiki/Art_of_Fighting#Art_of_Fighting_2_(1994)',
'https://en.wikipedia.org/wiki/Art_of_Fighting#Art_of_Fighting_3:_The_Path_of_the_Warrior_(1996)',
'https://en.wikipedia.org/wiki/Ken_Shimura',
'https://en.wikipedia.org/wiki/Bang_Bang_Busters',
'https://en.wikipedia.org/wiki/Bang_Bead',
'https://en.wikipedia.org/wiki/Baseball_Stars_2',
'https://en.wikipedia.org/wiki/Baseball_Stars_Professional',
'https://en.wikipedia.org/wiki/Battle_Flip_Shot',
'https://en.wikipedia.org/wiki/Blazing_Star',
'https://en.wikipedia.org/wiki/Aicom',
'https://en.wikipedia.org/wiki/Blue%27s_Journey',
'https://en.wikipedia.org/wiki/Alpha_Denshi',
'https://en.wikipedia.org/wiki/Bomberman:_Panic_Bomber',
'https://en.wikipedia.org/wiki/Hudson_Soft',
'https://en.wikipedia.org/wiki/Eighting',
'https://en.wikipedia.org/wiki/Breakers_(1996_video_game)',
'https://en.wikipedia.org/wiki/Breakers_(1996_video_game)#Breakers_Revenge',
'https://en.wikipedia.org/wiki/Burning_Fight',
'https://en.wikipedia.org/wiki/Chibi_Maruko-chan#Video_games',
'https://en.wikipedia.org/wiki/Takara',
'https://en.wikipedia.org/wiki/Crossed_Swords_(video_game)',
'https://en.wikipedia.org/wiki/Crossed_Swords_II',
'https://en.wikipedia.org/wiki/Cyber-Lip',
'https://en.wikipedia.org/wiki/Double_Dragon_(Neo-Geo)',
'https://en.wikipedia.org/wiki/Techn%C5%8Ds_Japan',
'https://en.wikipedia.org/wiki/Eight_Man_(video_game)',
'https://en.wikipedia.org/wiki/Far_East_of_Eden:_Kabuki_Klash',
'https://en.wikipedia.org/wiki/Racjin',
'https://en.wikipedia.org/wiki/Red_Entertainment',
'https://en.wikipedia.org/wiki/Fatal_Fury:_King_of_Fighters',
'https://en.wikipedia.org/wiki/Fatal_Fury_2',
'https://en.wikipedia.org/wiki/Fatal_Fury_3:_Road_to_the_Final_Victory',
'https://en.wikipedia.org/wiki/Fatal_Fury_Special',
'https://en.wikipedia.org/wiki/Fight_Fever',
'https://en.wikipedia.org/wiki/Football_Frenzy',
'https://en.wikipedia.org/wiki/Galaxy_Fight:_Universal_Warriors',
'https://en.wikipedia.org/wiki/Sunsoft',
'https://en.wikipedia.org/wiki/Ganryu_(video_game)',
'https://en.wikipedia.org/wiki/Garou:_Mark_of_the_Wolves',
'https://en.wikipedia.org/wiki/Ghost_Pilots',
'https://en.wikipedia.org/wiki/Goal!_Goal!_Goal!',
'https://en.wikipedia.org/wiki/Gururin',
'https://en.wikipedia.org/wiki/Ironclad_(video_game)',
'https://en.wikipedia.org/wiki/Aicom',
'https://en.wikipedia.org/wiki/Karnov%27s_Revenge',
'https://en.wikipedia.org/wiki/Data_East',
'https://en.wikipedia.org/wiki/King_of_the_Monsters_(video_game)',
'https://en.wikipedia.org/wiki/King_of_the_Monsters_2',
'https://en.wikipedia.org/wiki/Kizuna_Encounter',
'https://en.wikipedia.org/wiki/Last_Resort_(video_game)',
'https://en.wikipedia.org/wiki/League_Bowling',
'https://en.wikipedia.org/wiki/Legend_of_Success_Joe',
'https://en.wikipedia.org/wiki/Magical_Drop#Magical_Drop_II_(マジカルドロップ2)',
'https://en.wikipedia.org/wiki/Magical_Drop#Magical_Drop_III_(マジカルドロップ3)',
'https://en.wikipedia.org/wiki/Magician_Lord',
'https://en.wikipedia.org/wiki/Matrimelee',
'https://en.wikipedia.org/wiki/Atlus',
'https://en.wikipedia.org/wiki/Noise_Factory',
'https://en.wikipedia.org/wiki/Metal_Slug_(1996_video_game)',
'https://en.wikipedia.org/wiki/Nazca_Corporation',
'https://en.wikipedia.org/wiki/Metal_Slug_2',
'https://en.wikipedia.org/wiki/Metal_Slug_3',
'https://en.wikipedia.org/wiki/Metal_Slug_4',
'https://en.wikipedia.org/wiki/Mega_Enterprise',
'https://en.wikipedia.org/wiki/Metal_Slug_5',
'https://en.wikipedia.org/wiki/Metal_Slug_2#Metal_Slug_X',
'https://en.wikipedia.org/wiki/Money_Puzzle_Exchanger',
'https://en.wikipedia.org/wiki/Mutation_Nation',
'https://en.wikipedia.org/wiki/NAM-1975',
'https://en.wikipedia.org/wiki/Neo_Bomberman',
'https://en.wikipedia.org/wiki/Neo_Drift_Out:_New_Technology',
'https://en.wikipedia.org/wiki/Neo_Geo_Cup_%2798:_The_Road_to_the_Victory',
'https://en.wikipedia.org/wiki/Mr._Do!#Ports_and_sequels',
'https://en.wikipedia.org/wiki/Neo_Turf_Masters',
'https://en.wikipedia.org/wiki/Nightmare_in_the_Dark',
'https://en.wikipedia.org/wiki/Ninja_Combat',
'https://en.wikipedia.org/wiki/Ninja_Commando',
'https://en.wikipedia.org/wiki/Ninja_Master%27s:_Ha%C5%8D_Ninp%C5%8D_Ch%C5%8D',
'https://en.wikipedia.org/wiki/Over_Top',
'https://en.wikipedia.org/wiki/Pleasure_Goal:_5_on_5_Mini_Soccer',
'https://en.wikipedia.org/wiki/Pochi_and_Nyaa',
'https://en.wikipedia.org/wiki/Compile_(company)',
'https://en.wikipedia.org/wiki/Taito',
'https://en.wikipedia.org/wiki/Power_Spikes_II',
'https://en.wikipedia.org/wiki/Prehistoric_Isle_2',
'https://en.wikipedia.org/wiki/Pulstar_(video_game)',
'https://en.wikipedia.org/wiki/Puzzle_Bobble',
'https://en.wikipedia.org/wiki/Puzzle_Bobble_2',
'https://en.wikipedia.org/wiki/Puzzle_de_Pon!',
'https://en.wikipedia.org/wiki/Puzzle_de_Pon!',
'https://en.wikipedia.org/wiki/Puzzled_(video_game)',
'https://en.wikipedia.org/wiki/Rage_of_the_Dragons',
'https://en.wikipedia.org/wiki/Evoga',
'https://en.wikipedia.org/wiki/Ragnagard',
'https://en.wikipedia.org/wiki/Real_Bout_Fatal_Fury',
'https://en.wikipedia.org/wiki/Real_Bout_Fatal_Fury_2:_The_Newcomers',
'https://en.wikipedia.org/wiki/Real_Bout_Fatal_Fury_Special',
'https://en.wikipedia.org/wiki/Riding_Hero',
'https://en.wikipedia.org/wiki/Robo_Army',
'https://en.wikipedia.org/wiki/Samurai_Shodown_(1993_video_game)',
'https://en.wikipedia.org/wiki/Samurai_Shodown_II',
'https://en.wikipedia.org/wiki/Samurai_Shodown_III',
'https://en.wikipedia.org/wiki/Samurai_Shodown_IV',
'https://en.wikipedia.org/wiki/Samurai_Shodown_V',
'https://en.wikipedia.org/wiki/Samurai_Shodown_V_Special',
'https://en.wikipedia.org/wiki/Savage_Reign',
'https://en.wikipedia.org/wiki/Sengoku_(1991_video_game)',
'https://en.wikipedia.org/wiki/Sengoku_2',
'https://en.wikipedia.org/wiki/Sengoku_3',
'https://en.wikipedia.org/wiki/Shinsetsu_Samurai_Spirits_Bushid%C5%8D_Retsuden',
'https://en.wikipedia.org/wiki/Asatsu-DK',
'https://en.wikipedia.org/wiki/Fuji_TV',
'https://en.wikipedia.org/wiki/Shock_Troopers',
'https://en.wikipedia.org/wiki/Shock_Troopers:_2nd_Squad',
'https://en.wikipedia.org/wiki/Sh%C5%8Dgi_no_Tatsujin:_Master_of_Syougi',
'https://en.wikipedia.org/wiki/SNK_vs._Capcom:_SVC_Chaos',
'https://en.wikipedia.org/wiki/Capcom',
'https://en.wikipedia.org/wiki/Soccer_Brawl',
'https://en.wikipedia.org/wiki/Spinmaster',
'https://en.wikipedia.org/wiki/Stakes_Winner',
'https://en.wikipedia.org/wiki/Stakes_Winner_2',
'https://en.wikipedia.org/wiki/Street_Slam',
'https://en.wikipedia.org/wiki/Strikers_1945_Plus',
'https://en.wikipedia.org/wiki/Psikyo',
'https://en.wikipedia.org/wiki/Super_Baseball_2020',
'https://en.wikipedia.org/wiki/Super_Dodge_Ball_(Neo_Geo)',
'https://en.wikipedia.org/wiki/Super_Sidekicks',
'https://en.wikipedia.org/wiki/Super_Sidekicks#Super_Sidekicks_2:_The_World_Championship',
'https://en.wikipedia.org/wiki/Super_Sidekicks#Super_Sidekicks_3:_The_Next_Glory',
'https://en.wikipedia.org/wiki/Tecmo_World_Soccer_%2796',
'https://en.wikipedia.org/wiki/Tecmo',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_%2794',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_%2795',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_%2796',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_%2796#Release',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_%2797',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_%2798',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_%2799',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_2000',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_2001',
'https://en.wikipedia.org/wiki/Eolith_(company)',
'https://en.wikipedia.org/wiki/SNK#2003–2016:_SNK_Playmore',
'https://en.wikipedia.org/wiki/SNK#2001–2003:_Bankruptcy_and_Playmore_Corporation',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_2002',
'https://en.wikipedia.org/wiki/Playmore',
'https://en.wikipedia.org/wiki/The_King_of_Fighters_2003',
'https://en.wikipedia.org/wiki/SNK#2001–2003:_Bankruptcy_and_Playmore_Corporation',
'https://en.wikipedia.org/wiki/The_Last_Blade',
'https://en.wikipedia.org/wiki/The_Last_Blade_2',
'https://en.wikipedia.org/wiki/The_Super_Spy',
'https://en.wikipedia.org/wiki/Super_Sidekicks#The_Ultimate_11:_SNK_Football_Championship',
'https://en.wikipedia.org/wiki/Thrash_Rally',
'https://en.wikipedia.org/wiki/Top_Hunter:_Roddy_%26_Cathy',
'https://en.wikipedia.org/wiki/Top_Player%27s_Golf',
'https://en.wikipedia.org/wiki/Twinkle_Star_Sprites',
'https://en.wikipedia.org/wiki/Viewpoint_(video_game)',
'https://en.wikipedia.org/wiki/Sammy_Corporation',
'https://en.wikipedia.org/wiki/Voltage_Fighter_Gowcaizer',
'https://en.wikipedia.org/wiki/Waku_Waku_7',
'https://en.wikipedia.org/wiki/Windjammers_(video_game)',
'https://en.wikipedia.org/wiki/World_Heroes_(video_game)',
'https://en.wikipedia.org/wiki/World_Heroes_2',
'https://en.wikipedia.org/wiki/World_Heroes_2_Jet',
'https://en.wikipedia.org/wiki/World_Heroes_Perfect',
'https://en.wikipedia.org/wiki/Zed_Blade',
'https://en.wikipedia.org/wiki/NMK_(company)',
'https://en.wikipedia.org/wiki/ZuPaPa!',
]

#url = 'https://www.mobygames.com/game/final-fight'

for i in lista:

    try:
        titulo = 0
        titulo_jogo = 0
        
        contador = random.randint(3, 10)
        time.sleep(contador)
        
        #url = lista[i]
        #print(i)
        page = requests.get(i)

        #print(page.status_code)

        #status = page.status_code

        soup = BeautifulSoup(page.text, 'html.parser')

        conteudo = soup.prettify()

        titulo = soup.title.string
        titulo_jogo = soup.find_all('th')[0].get_text()

        #print(titulo)


        lista_esq = soup.find_all('th')
        cont_tag = 0
        texto_esq = 'VAZIO'
        ntag_th = 'VAZIO'
        for i2 in lista_esq:
            #print(i.get_text())
            texto = i2.get_text()
            if texto == 'Platform(s)':
                texto_esq = texto
                ntag_th = cont_tag
            else:
                cont_tag += 1
        #print('ntag:' + str(ntag))

        #lista_dir = soup.find_all('td')[ntag].get_text()
        #print(texto_esq + ': ' + lista_dir)

        lista_dir = soup.find_all('td')
        cont_tag = 0
        texto_dir = 'VAZIO'
        ntag_td = 'VAZIO'

        for i3 in lista_dir:
            #print(i.get_text())
            texto = i3.get_text()
            #print(texto)
            if texto[0:7] == 'Arcade,':
                #print(type(texto))
                #print(texto)
                texto_dir = texto
                ntag_td = cont_tag
                controle = 'OK'
                break
           # if texto[0:6] == 'Arcade':
           #     #print(type(texto))
           #     #print(texto)
           #     texto_dir = texto
           #     ntag_td = cont_tag
           #     controle = 'OK'
           #     break
            elif texto == 'Arcade':
                #print(type(texto))
                #print(texto)
                texto_dir = texto
                ntag_td = cont_tag
                controle = 'OK'
                break
            elif texto[0:8] == '\nArcade\n':
                #print(texto)
                texto_dir = texto
                ntag_td = cont_tag
                controle = 'OK'
                break
            else:
                #print(type(texto))
                #print('----------')
                #print(texto[0:7])
                controle = 'FALHOU'
                cont_tag += 1
                

#        texto_li = soup.find_all('li')
#        for i4 in texto_li:
#            print(i4.get_text())


        conteudo = str(i) + ';' + str(titulo) + ';' + str(titulo_jogo) + ';' + 'ntag_th:' + str(ntag_th) + ';' + str(texto_esq) + ';' + 'ntag_td:' + str(ntag_td) + ';' + str(texto_dir) + ';' + 'Esperou ' + str(contador) + ' segundos.' + ';' + controle + '\n'


    #    print('')
    #    print('---------------------------')
    #    print('')
    #    for i in lista_dir:
    #        print(i.get_text())

        #print('Esperou ' + str(contador) + ' segundos.' + '\n')

        
        print(conteudo)

    except:
        conteudo = str(i) + ';' + str(titulo) + ';' + str(titulo_jogo) + ';' + '0' + ';' + '0' + ';' + '0' + ';' + '0' + ';' + 'Esperou ' + str(contador) + ' segundos.' + ';' + 'FALHOU except\n'
        print(conteudo)
        
    #print('Esperou ' + str(contador) + ' segundos.' + '\n')
        file.write(conteudo)

file.close()


'''
#wikipedia

#print('Meu 1º scraper... :)\n')

#titulo = soup.title.string
#plataformas = soup.find_all('td')[6].get_text()
#for i in soup.find_all('a'):
#    print(i.get('href'))


#print('Título do jogo:', soup.find_all('th')[0].get_text())
#'Activision Anthology'

#print(soup.find_all('th')[3].get_text())
#'Platform(s)'

#print('Plataformas:', soup.find_all('td')[3].get_text())
#'PlayStation 2, Windows, Macintosh, Game Boy Advance, digiBlast, PlayStation Portable, iOS, Android'




#moby


#print(soup.find_all('h1')[0].get_text())
#print(soup.find_all('div')[32].get_text())

titulo = soup.title.string
plataformas = soup.find_all('div')[33].get_text()


#print('Título:', titulo)
#print('Plataformas:', plataformas)


'''
