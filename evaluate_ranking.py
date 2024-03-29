# -*- coding: utf-8 -*-
# Creació de la funció "evaluate_ranking.py". Feta per: Eric Díaz Cívico.
import numpy as np
import matplotlib.pyplot as plt
import os # Carreguem la llibreria corresponent a la funció de introducció de
# rutes absolutes d'un fitxer
from sklearn.metrics import average_precision_score


ruta_abs = os.path.dirname(os.path.abspath(__file__)) #Obtenim la ruta absoluta de la carpetao n es troben els fitxers
Direct_llista = open(ruta_abs+'\files\ranking_val','r') #Obrim la carpeta del directori de la llista classificada d'imatges
 
 
def Evaluate_Ranking(Direct_llista,train_or_val): #Funció declarada passant com a paràmetres 

    fitxer_anot = open(ruta_abs+"\TerrassaBuildings900\train\Annotation_"+train_or_val+".txt" , "r") #Obrim els arxius quan el valor de train_or_val sigui = a 'train'.     
    fitxer_anot2 = open(ruta_abs+"\TerrassaBuildings900\val\Annotation_"+train_or_val+".txt" , "r") #Obrim l'arxiu quan el valor de train_or_val sigui = a 'val'.
    Final_file = open(ruta_abs+"\files\Average_precision_"+train_or_val+".txt", "w") #Obrim l'arxiu on escriurem el AP per cada consulta  
    Final_file2 = open(ruta_abs+"\files\Mean_average_precision_"+train_or_val+".txt", "w") ##Obrim l'arxiu on escriurem el MAP per cada consulta  
    
    #Franc: a estas las creo para que no pete el código, luego se intentará depurar
    Final_file_train = open(ruta_abs+"/files/final_file_train.txt" ,'w')
    Final_file2_train = open(ruta_abs+"/files/final_file_train.txt" ,'w')
    Final_file_valid = open(ruta_abs+"/files/final_file_valid.txt" ,'w')
    Final_file2_valid = open(ruta_abs+"/files/final_file_valid.txt" ,'w')
    
    
    for line in Direct_llista:
        Final_file = np.random.rand(1,180) #Obrim el vector aleatori on s'inclouran el total de APs per cada consulta
        final = line.index("\n") #Indicació del final de línea de casa vector de AP's
        if train_or_val == "train":
            fitxer_anot = "Annotation_train.txt"
            APt = average_precision_score(Direct_llista,fitxer_anot)
            Final_file.append(APt)
            # A continuació escriurem en el fitxer cada línia de les APS per les imatges d'entrenamen
            Final_file_train.write(line[0:final] + "For Query "+line+":\t" + str(Final_file).replace("\n","").replace("[[","").replace("]]","") + "\n")
        else:
            fitxer_anot2 = "Annotation_valid.txt"
            APv = average_precision_score(Direct_llista,fitxer_anot2)
            Final_file.append(APv)
            # A continuació escriurem en el fitxer cada línia de les APS per les imatges de validació
            Final_file_valid.write(line[0:final] + "For Query "+line+":\t"+ str(Final_file).replace("\n","").replace("[[","").replace("]]","") + "\n") 
    Final_file_train.close() #Tanquem el fitxer corresponent a les imatges d'entrenament
    Final_file_valid.close() #Tanquem el fitxer corresponent a les imatges de validació

    for line in Final_file_train:
        for element in line:
            suma_train = (sum(line))
            sum_elems = (sum(element))
        print("Aps d'entrenament sumats!")
        Final_file2 = [] #Creem el array necessari per col·locar el valor del MAP
        MAP_train = suma_train/sum_elems #Fem la peració per obtenir aquest valor
        Final_file2.append(MAP_train) #Introduïm el valor resultant dintre del array creat
        #A Continuació esciurem el valor resultant del MAP dintre del fitxer de sortida
        Final_file2_train.write(line[0:final] + "For Query "+line+":\t" + "Mean_AVerage_Precision = "+str(Final_file2).replace("\n","").replace("[[","").replace("]]","") + "\n")
    Final_file_train.close() #Tanquem el fitxer per on hem llegit les dades dels APS de cada consulta
    Final_file2_train.close() #Tanquem el ftixer per on hem esccrit els valors del MAP resultants per cada línia
    
    
    for line in Final_file_valid:
        for element in line:
            suma_valid = (sum(line))
            sum_elems = (sum(element))
        print("Aps de validació sumats!")
        Final_file2 = [] #Creem el array necessari per col·locar el valor del MAP
        MAP_valid = suma_valid/sum_elems #Fem la peració per obtenir aquest valor
        Final_file2.append(MAP_valid) #Introduïm el valor resultant dintre del array creat
        #A Continuació esciurem el valor resultant del MAP dintre del fitxer de sortida
        Final_file2_valid.write(line[0:final] + "For Query "+line+":\t" + "Man_AVerage_Precision = "+str(Final_file2).replace("\n","").replace("[[","").replace("]]","") + "\n")
    Final_file_valid.close() #Tanquem el fitxer per on hem llegit les dades dels APS de cada consulta
    Final_file2_valid.close() #Tanquem el ftixer per on hem esccrit els valors del lMAP resultants per cada línia

Evaluate_Ranking("features_train.txt","train")
Evaluate_Ranking("features_valid.txt","valid")
