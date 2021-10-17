def toutes_phrases(phrase, length, nb_mots):
    mots = ["Bu ", "Ga ", "Meu ", "Zo "]
    if length <= nb_mots:
        for mot in mots:
            nv_phrase = phrase + mot
            if len(nv_phrase.split()) == nb_mots:
                print(phrase + mot.rstrip())
            toutes_phrases(phrase + mot, length + 1, nb_mots)     

nombre_de_mot_dans_phrase = int(input())
toutes_phrases('',1, nombre_de_mot_dans_phrase)
