import math
from random import randint
import time
import random
import matplotlib.pyplot as plt
import numpy

def generate_coordinates(nr_of_cities):                 #vygeneruje nahodne súradnice x,y pre daný počet miest
    cities = []
    for i in range(nr_of_cities):
        city = []
        x = randint(0,200)
        y = randint(0,200)
        city.append(x)
        city.append(y)
        cities.append(city)
    return cities                                       #vráti list miest, ktoré obsahujú vygenerované súradnice

def euclidean_distance(city1, city2):                   #vzorec na výpočet vzdialenosti dvoch bodov/miest na 2D mape
    return math.sqrt(abs(city1[0] - city2[0])**2 + (abs(city1[1] - city2[1])**2))

def fitness(path, cities):                              #vypočíta hodnotu cesty v danom poradí- path
    path_cost = 0
    for i in range(len(path)):
        if (i+1!=len(path)):
            path_cost = path_cost + euclidean_distance(cities[path[i]], cities[path[i+1]])
        else:
            path_cost = path_cost + euclidean_distance(cities[path[i]], cities[path[0]])
    return path_cost                                    #vráti hodnotu cesty

def permutate(path):                                    #možné permutácie poradí miest
    perm_count = 300
    path_list = []
   
    while(perm_count):
        tmp1 = 0
        tmp2 = 0

        while(tmp1==tmp2):
            tmp1 = randint(1, len(path)-1)
            tmp2 = randint(1, len(path)-1)

        if (tmp1>tmp2):
            tmp = tmp1
            tmp1 = tmp2
            tmp2 = tmp       

        range = path[tmp1:tmp2]
        new_path = path[:tmp1] + range[::-1] + path[tmp2:]
        path_list.append(new_path)
        perm_count = perm_count - 1

    return path_list                                            #vráti list obsahujúci perm_count (300) nových potomkov- vygenerovaných permutácii poradí miest

def tabu_search(nr_of_cities, cities):
    path = []
    for i in range(nr_of_cities):
        path.append(i)

    min_dist = fitness(path, cities)                    #počiatočná/zatiaľ najlepšia nájdená dĺžka cesty
    min_path = path
    pos_best = path
    tabulist = []
    tabulist.append(min_path)
    turn_count = 0                                      #počet prejdených cyklov, v ktorých sa "udržala" doposiaľ najlepšie nájdená cesta
    stop = False

    while (not stop):
        path_comb = swap_two(pos_best)
        pos_best = path_comb[0]
        for candidate in path_comb:
            if ((candidate not in tabulist) and (fitness(candidate,cities) < fitness(pos_best, cities))):       #nájde lokálne minimum
                pos_best = candidate
                print(fitness(candidate,cities))
        
        if (fitness(min_path, cities) > fitness(pos_best, cities)):                                             #porovná lokálne minimum s globálnym minimum
            min_path = pos_best
            tabulist.append(min_path)
            turn_count = 0          
        
        tabulist.append(pos_best)

        if (len(tabulist)>20):
            tabulist.pop(0)
        
        turn_count = turn_count + 1
 
        if (turn_count == 80):
            stop = True

    min_dist = fitness(min_path, cities)
    return min_dist, min_path

def swap_two(path):                                         #funkcia vymiena hodnotu na dvoch náhodných indexoch v path
    path_opt = []
    init_path = path.copy()
    for i in range(100):
        path = init_path.copy()
        r1 = randint(1, len(path)-1)
        r2 = randint(1, len(path)-1)
        while(r1==r2):
            r1 = randint(1, len(path)-1)
            r2 = randint(1, len(path)-1)

        path[r1], path[r2] = path[r2], path[r1]             #vymení hodnoty na daných indexoch
        path_opt.append(path)
    return path_opt                                             

def simulated_annealing(nr_of_cities, cities):
    path = []
    for i in range(nr_of_cities):
        path.append(i)

    min_path = path.copy()
    turn_count = 0
    T = 50                          #počiatočná teplota
    factor = 0.99                   #faktor zmenšenia teploty
    path_opt = []

    while(turn_count < 500):
        T = T*factor
        path_opt = swap_two(min_path)

        for option in path_opt:
            path_cost = fitness(option, cities)
            min_cost = fitness(min_path,cities)
            if (path_cost < min_cost):
                min_path = option.copy()
                min_cost = path_cost
                turn_count = 0
            else:
                x = numpy.random.uniform()                                     #vygeneruje číslo od (0,1)
                if x < numpy.exp((min_cost-path_cost)/T):
                    min_cost = path_cost
                    min_path = option.copy()
                    turn_count = 0
                else:                                                           #change it back
                    turn_count = turn_count + 1
            print(min_cost)

    return min_cost, min_path

def graph(path, init_path, cities, search_type):                                #funkcia na vykreslenie grafu
    x = []
    y = []
    x_init = []
    y_init = []
    for i in range(len(path)+1):       
        if (i!=len(path)):
            x.append(cities[path[i]][0])
            y.append(cities[path[i]][1])
            x_init.append(cities[init_path[i]][0])
            y_init.append(cities[init_path[i]][1])
        else:
            x.append(cities[0][0])
            y.append(cities[0][1])
            x_init.append(cities[init_path[0]][1])
            y_init.append(cities[init_path[0]][1])

    fig, axs = plt.subplots(2)
    axs[0].plot(x_init, y_init, marker = 'o', color='blue')
    axs[1].plot(x,y, marker = 'o', color='red')
    if (search_type == 1):
        fig.suptitle('Tabu search')
    elif (search_type == 2):
        fig.suptitle('Simulated annealing')
    plt.show()

def main():
    nr_of_cities = randint(20,40)
    cities = generate_coordinates(nr_of_cities)
    while(1):
        print("Tabu_search (1), Simulated annealing (2), Koniec (0)")
        user_input = input("Enter value: ")

        if (user_input=='1'):
            init_path = []
            for i in range(nr_of_cities):
                init_path.append(i)

            print("Povodna cesta: ", init_path)
            print("Povodna vzdialenost:", fitness(init_path, cities))
            
            start_time = time.time()
            distance, path = tabu_search(nr_of_cities, cities)
            print("Finalna cesta: ", path)
            print("Finalna vzdialenost: ", distance)
            print("--- %s seconds ---" % (time.time() - start_time))
                       
            graph(path, init_path , cities, 1)

        elif (user_input=='2'):
            init_path = []
            for i in range(nr_of_cities):
                init_path.append(i)

            print("Povodna cesta: ", init_path)
            print("Povodna vzdialenost:", fitness(init_path, cities))

            start_time = time.time()
            distance, path = simulated_annealing(nr_of_cities, cities)
            print("Finalna cesta: ", path)
            print("Finalna vzdialenost: ", distance)  
            print("--- %s seconds ---" % (time.time() - start_time))

            graph(path, init_path, cities, 2)
        else: 
            break

if __name__ == "__main__":
    main()



