# TSP- Problém obchodného cestujúceho
Obchodný cestujúci má navštíviť viacero miest. V jeho záujme je minimalizovať cestovné náklady a 
cena prepravy je úmerná dĺžke cesty, snaží sa nájsť najkratšiu možnú cestu tak, aby každé mesto 
navštívil práve raz. Keďže sa nakoniec musí vrátiť do mesta z ktorého vychádza, jeho cesta je uzavretá 
krivka.

# Zadanie
Je daných aspoň 20 miest (20 – 40) a každé má určené súradnice ako celé čísla X a Y. Tieto súradnice 
sú náhodne vygenerované. (Rozmer mapy môže byť napríklad 200 * 200 km.) Cena cesty medzi 
dvoma mestami zodpovedá Euklidovej vzdialenosti –vypočíta sa pomocou Pytagorovej vety. Celková 
dĺžka trasy je daná nejakou permutáciou (poradím) miest. Cieľom je nájsť takú permutáciu (poradie), 
ktorá bude mať celkovú vzdialenosť čo najmenšiu.
Výstupom je poradie miest a dĺžka zodpovedajúcej cesty

# Tabu Search
Algoritmus, ktorý nájde relatívne najlepšiu (nemusí byť najlepšia) cestu prejdenia všetkých miest.
Algoritmus si vyberie horšieho nasledovníka a zároveň si uloží aktuálny stav do tzv. zoznamu 
zakázaných stavov (tabu list). Je to nevyhnutné, aby sme sa z toho horšieho nasledovníka znovu 
nedostali do tohto lokálne extrému a nevytvorili tak nekonečný cyklus.

# Simulované žíhanie
Obdobne ako pri tabu vyhľadávaní, nájdená cesta predstavuje iba relatívne najlepšiu nájdenú cestu.
Algoritmus si vezme nasledovníka, vypočíta jeho hodnotu cesty. Ak je táto hodnota menšia ako 
doposiaľ najlepšia nájdená presunie sa do nej. Ak je horšia rozhodne sa na základe 
pravdepodobnosti.
