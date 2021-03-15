string1 = input()
string2 = input()
string3 = input()

if string1 == 'vertebrado' :
    if string2 == 'ave':
        if string3 == 'carnivoro':
            print('aguia')
        if string3 == 'onivoro':
            print('pomba')
    if string2 == 'mamifero':
        if string3 == 'onivoro':
            print('homem')
        if string3 == 'herbivoro':
            print('vaca')
if string1 == 'invertebrado':
    if string2 == 'inseto':
        if string3 == 'hematofago':
            print('pulga')
        if string3 == 'herbivoro':
            print('lagarta')
    if string2 == 'anelideo':
        if string3 == 'hematofago':
            print('sanguessuga')
        if string3 == 'onivoro':
            print('minhoca')