# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:19:04 2016

@author: Philippe

Affichage des valeurs intermédiaires pour debug
"""

from constante import ACTIVATION_ANA, ACTIVATION_PARAM, ACTIVATION_REF,\
    AFFICHE_HORIZON, ANA_ECART_MC, ANA_FILTRAGE, ANA_FILTRAGE_BIBLIO, \
    ANA_HEURE, ANA_PROFONDEUR, ANA_SCENARIO, ANNEE_POINT, C_MEM_ANA, \
    C_MEM_PARAM, DATE_INIT, DEBUG_ANALOGIE, DEBUG_BUFFER, DEBUG_DONNEES, \
    DEBUG_PARAMETRE, DEBUG_PREDICTION, DEBUG_PREDICTION1, DEBUG_PREDICTION2, \
    DEBUG_PREDICTION3, DEBUG_PREDICTION4, DEBUG_PREDICTION5, DEB_MATIN, \
    DEB_MIDI, DEB_NUIT, DEB_SOIR, FILE_BIBLIO, FILTRE, HEURE_POINT, HORIZON, \
    INTER_POINT, JOUR_POINT, MATIN, MAXI, MAX_POINT, MAX_SEQ, \
    MIDI, MIN_POINT, MIN_SEQ, MOIS_POINT, N2AIXA, N2AIXC, N2CINQ, N2PLOM, \
    N2RABA, N2STLO, NB_PREDICTEURS, NB_SEQ, NON_FILTRE, NUIT, N_ATTRIBUT,\
    N_DEPART, N_LIGNE, N_RESULT, O3AIXA, O3AIXP, O3CINQ, PARA_ECART_MC, \
    PARA_HEURE, PARA_HORIZON_POINT, PARA_PROFONDEUR, PARA_SENS, PCAIXA, \
    PCAIXC, PCCINQ, PCRABA, PCSTLO, PRED_RESULTAT, SEQUENCE, \
    SOIR, TAILLE_BUFFER, TIME_HEURE, TYPE_POINT, VAL_ANNEE, VAL_HEURE, \
    VAL_JOUR, VAL_MOIS, VAL_VALEUR, V_MOYENNE, V_PREDIC, V_PREDIC2, V_PREDIC3,\
    REF_SCENARIO, I_ANA, I_PARAM, I_MEILLEUR, I_REF, I_VENT, I_ALGO


def Affiche_Donnees_Traitees(donnees):

    print("heure", "non-filtre", "sequence", "type_point", "filtre")
    # for i in range(1, 10):
    for i in range(6184, 6204):
        print(donnees[HEURE_POINT, i],
              donnees[NON_FILTRE, i],
              donnees[SEQUENCE, i],
              donnees[TYPE_POINT, i],
              donnees[FILTRE, i])
    print(donnees[HEURE_POINT, N_LIGNE - 1],
          donnees[NON_FILTRE, N_LIGNE - 1],
          donnees[SEQUENCE, N_LIGNE - 1],
          donnees[TYPE_POINT, N_LIGNE - 1],
          donnees[FILTRE, N_LIGNE - 1])


def Affiche_Buffer(buffer):

    print("non filtre", "filtre", "sequence", "type_point", "heure", "jour",
          "mois", "annee")
    print(buffer)


def Affiche_Analogie(buffer, b_pred_analogie, ecart_predicteur):

    i = 6
    k = 0
    print("b_pred-ana0600", "b_pred_ana0640",
          b_pred_analogie[k, i, 0, k], b_pred_analogie[k, i, 1, k],
          b_pred_analogie[k, i, 2, k], b_pred_analogie[k, i, 3, k],
          b_pred_analogie[k, i, 4, k])
    print("ecart_pred-ana60", ecart_predicteur[i+I_ANA, k])


def Affiche_Reference(buffer, b_pred_reference, ecart_predicteur):

    k = 0
    print("pred-ref0...pred_ref3", b_pred_reference[0, 0, k],
          b_pred_reference[0, 1, k], b_pred_reference[0, 2, k],
          b_pred_reference[0, 3, k])
    print("ecart_pred-ref0", "ecart_pred_ref3", ecart_predicteur[0+I_REF, k],
          ecart_predicteur[3+I_REF, k])


def Affiche_Parametre(buffer, b_pred_parametre, ecart_predicteur):

    k = 0
    print("pred-para0", "pred_para1", b_pred_parametre[0, 0, k],
          b_pred_parametre[0, 1, k])
    print("ecart_pred-para0", "ecart_pred_para1",
          ecart_predicteur[0+I_PARAM, k], ecart_predicteur[1+I_PARAM, k])


def Affiche_Vent(buffer, b_pred_vent, ecart_predicteur):

    k = 0
    print("pred-vent0", "pred_vent1",
          b_pred_vent[0, 0, k], b_pred_vent[0, 1, k])
    print("ecart_pred-vent0", "ecart_pred_vent1",
          ecart_predicteur[0+I_VENT, k], ecart_predicteur[1+I_VENT, k])


def Affiche_Algo(buffer, b_pred_algo, coef_algo, ecart_predicteur):

    k = 0
    print("pred-algo0", "pred_algo4",
          b_pred_algo[0, 0, k], b_pred_algo[0, 1, k], b_pred_algo[0, 2, k],
          b_pred_algo[0, 3, k], b_pred_algo[0, 4, k])
    print("coef_algo0", "coef_algo3",
          coef_algo[k, 0], coef_algo[k, 1], coef_algo[k, 2], coef_algo[k, 3])
    print("ecart_pred-algo0", "ecart_pred_algo3",
          ecart_predicteur[0+I_ALGO, k], ecart_predicteur[1+I_ALGO, k],
          ecart_predicteur[2+I_ALGO, k], ecart_predicteur[3+I_ALGO, k])


def Affiche_Prediction(b_pred_vent, b_pred_reference,
                       coef_predicteur, memoire_moyenne_ana, b_pred_analogie,
                       b_pred_parametre, b_pred_filtre, b_pred_meilleur,
                       buffer, b_pred_tableau, ecart_predicteur, b_pred_algo,
                       coef_algo):

    if DEBUG_PREDICTION1:
        k = 0
        print("non filtre", "filtre", "b_pred_meil", "ecart_pred_meil**2")
        print(buffer[NON_FILTRE, TAILLE_BUFFER], buffer[FILTRE, TAILLE_BUFFER],
              b_pred_meilleur[0, k], ecart_predicteur[I_MEILLEUR, k]**2)
        print("mem_ana(0) ... mem_ana(7)")
        print(memoire_moyenne_ana[0], memoire_moyenne_ana[1],
              memoire_moyenne_ana[2], memoire_moyenne_ana[3],
              memoire_moyenne_ana[4], memoire_moyenne_ana[5],
              memoire_moyenne_ana[6], memoire_moyenne_ana[7])
        print("pred-ref0", "pred_ref1", "pred_ref2")
        print(b_pred_reference[0, 0, k], b_pred_reference[0, 1, k],
              b_pred_reference[0, 2, k])
        print("coef_pred-ref0, coef_pred_ref1, coef_pred_ref2")
        print(coef_predicteur[k, 0+I_REF, 1], coef_predicteur[k, 1+I_REF, 1],
              coef_predicteur[k, 2+I_REF, 1])
        j0 = round(memoire_moyenne_ana[0], 0)
        j1 = round(memoire_moyenne_ana[1], 0)
        j2 = round(memoire_moyenne_ana[2], 0)
        j3 = round(memoire_moyenne_ana[3], 0)
        j4 = round(memoire_moyenne_ana[4], 0)
        j5 = round(memoire_moyenne_ana[5], 0)
        j6 = round(memoire_moyenne_ana[6], 0)
        j7 = round(memoire_moyenne_ana[7], 0)
        print("pred-ana0, pred_ana1, pred_ana2, ....  pred_ana7")
        print(b_pred_analogie[0, 0, j0, k],
              b_pred_analogie[0, 1, j1, k],
              b_pred_analogie[0, 2, j2, k],
              b_pred_analogie[0, 3, j3, k],
              b_pred_analogie[0, 4, j4, k],
              b_pred_analogie[0, 5, j5, k],
              b_pred_analogie[0, 6, j6, k],
              b_pred_analogie[0, 7, j7, k])
        print("coef_pred-ana0, ana1, ana2, ... , ana7")
        print(coef_predicteur[k, 0 + I_ANA, 1],
              coef_predicteur[k, 1 + I_ANA, 1],
              coef_predicteur[k, 2 + I_ANA, 1],
              coef_predicteur[k, 3 + I_ANA, 1],
              coef_predicteur[k, 4 + I_ANA, 1],
              coef_predicteur[k, 5 + I_ANA, 1],
              coef_predicteur[k, 6 + I_ANA, 1],
              coef_predicteur[k, 7 + I_ANA, 1])
        print("pred-para0, pred_para1, pred_para2, pred_para3, pred_para4")
        print(b_pred_parametre[0, 0, k],
              b_pred_parametre[0, 1, k],
              b_pred_parametre[0, 2, k],
              b_pred_parametre[0, 3, k],
              b_pred_parametre[0, 4, k])
        print("coef_pred-para0, para1, para2, para3, para4")
        print(coef_predicteur[k, 0 + I_PARAM, 1],
              coef_predicteur[k, 1 + I_PARAM, 1],
              coef_predicteur[k, 2 + I_PARAM, 1],
              coef_predicteur[k, 3 + I_PARAM, 1],
              coef_predicteur[k, 4 + I_PARAM, 1])
        print("pred-vent0, pred_vent1, pred_vent2, pred_vent3, pred_vent4")
        print(b_pred_vent[0, 0, k],
              b_pred_vent[0, 1, k],
              b_pred_vent[0, 2, k],
              b_pred_vent[0, 3, k],
              b_pred_vent[0, 4, k])
        print("coef_pred-vent0, vent1, vent2, vent3, vent4")
        print(coef_predicteur[k, 0 + I_VENT, 1],
              coef_predicteur[k, 1 + I_VENT, 1],
              coef_predicteur[k, 2 + I_VENT, 1],
              coef_predicteur[k, 3 + I_VENT, 1],
              coef_predicteur[k, 4 + I_VENT, 1])
        print("pred-algo0, pred_algo1, pred_algo2, pred_algo3, pred_algo4")
        print(b_pred_algo[0, 0, k],
              b_pred_algo[0, 1, k],
              b_pred_algo[0, 2, k],
              b_pred_algo[0, 3, k],
              b_pred_algo[0, 4, k])
        print("coef_pred-algo0, algo1, algo2, algo3, algo4")
        print(coef_algo[k, 0],
              coef_algo[k, 1],
              coef_algo[k, 2],
              coef_algo[k, 3],
              coef_algo[k, 4])