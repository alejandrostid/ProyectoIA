#import cv2
#import os
#import imutils
#
#mano_a= 'A'
#data_path_a='Señas/SET/A/'
#mano_b='B'
#data_path_b='Señas/SET/B/'
#
import cv2 
import numpy as np
import os
import matplotlib.pyplot as plt


ruta = ["SET/A","SET/B","SET/C","SET/D",
        "SET/E","SET/F","SET/I","SET/K",
        "SET/L","SET/M","SET/N","SET/O",
        "SET/P","SET/Q","SET/R","SET/T",
        "SET/U","SET/V","SET/W","SET/Y"]
señal_listas = []
tamaño = 420

def toma_imagen(ruta,señal_listas,tamaño):
        i=0
        for x in ruta:
            for seña in os.listdir(ruta[i]):
                seña = cv2.imread(os.path.join(ruta[i],seña),cv2.IMREAD_GRAYSCALE)
                seña_v = cv2.resize(seña,(tamaño,tamaño))
                señal_listas.append([seña_v])
                print(len(señal_listas))
                print(señal_listas)
            i +=1

toma_imagen(ruta)
