from math import trunc
import sys
import random
import pygame
from pygame import time
from pygame import surface
#from V1 import Calculador




#corredor=Calculador({1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}, 0,[],[],[],[],[],[],[],[],[],[])

pygame.init()


class Juego():

    def __init__(self,amarillo_patito, lista_colores, tareas_por_defecto, lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8, lista9, lista10, tiempo, window):
        self.amarillo_patito=(255,255,197)          
        self.lista_colores=[(242,140,116), (188,33,28), (238,136,175), (129,193,203), (80,99,13), (11,69,10),(64,82,117), (33,143,254), (115,89,186), (185,180,138), (182,140,82), (158,106,168)]
        #Diccionario vacío por defecto de las tareas y sus tiempos
        self.tareas_por_defecto={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
        self.lista1=[]
        self.lista2=[]
        self.lista3=[]
        self.lista4=[]
        self.lista5=[]
        self.lista6=[]
        self.lista7=[]
        self.lista8=[]
        self.lista9=[]
        self.lista10=[]                  
        self.tiempo=1
        self.window=1355
      

    def tareas(self):
        num_tareas=int(input("¿Cúantas tareas se van a ejecutar?: "))
        tareas={}

        for i in range(1,num_tareas):

            tareas["Tarea "+str(i)]=int(random.randrange(1, 51))

        print(tareas)
        return tareas

    def random_tareas(self):
        for clave in self.tareas_por_defecto:        
            self.tareas_por_defecto[clave]=random.randrange(1,40)
        print(self.tareas_por_defecto)


    def main(self):
        estado=True
        clock=pygame.time.Clock()    
        ancho, alto= self.window, 335
        
        pygame.display.set_caption("Multiprogramación")
        
        #Defino los valores de la ventana
        ventana= pygame.display.set_mode((ancho, alto), pygame.RESIZABLE) #Tamaño de ventana


        def graficacion(self, vetana):    
            #Defino los valores de un cuadrado x,y,ancho,alto
            x,y=50,50
                    
            num_tiempos=random.randrange(1,10)
            #tamaño de cuadrado=20x20
            indice=random.randrange(len(self.lista_colores))
            color_random=self.lista_colores[indice]
            
            for i in range(num_tiempos):
                cuadrado=pygame.Rect(x,y,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                x+=20

        
            
       
        
        #Imprime texto y rayas
        def imprime_texto():
            #Declaro los textos que ocupare
            fuente=pygame.font.Font(None, 17)
            texto1=fuente.render("Tarea 1", True, (0,0,0))
            texto2=fuente.render("Tarea 2", True, (0,0,0))
            texto3=fuente.render("Tarea 3", True, (0,0,0))
            texto4=fuente.render("Tarea 4", True, (0,0,0))
            texto5=fuente.render("Tarea 5", True, (0,0,0))
            texto6=fuente.render("Tarea 6", True, (0,0,0))
            texto7=fuente.render("Tarea 7", True, (0,0,0))
            texto8=fuente.render("Tarea 8", True, (0,0,0))
            texto9=fuente.render("Tarea 9", True, (0,0,0))
            texto10=fuente.render("Tarea 10", True, (0,0,0))
            
            ventana.blit(texto1,(8,53))
            ventana.blit(texto2,(8,75))
            ventana.blit(texto3,(8,96))
            ventana.blit(texto4,(8,116))
            ventana.blit(texto5,(8,135))
            ventana.blit(texto6,(8,155))
            ventana.blit(texto7,(8,175))
            ventana.blit(texto8,(8,196))
            ventana.blit(texto9,(8,215))
            ventana.blit(texto10,(3,235))

            x2, y2= 50,50 #x, y de las rayas  
            #Imprime las rayas
            for j in range(11):
                pygame.draw.line(ventana, (0,0,0),(x2, y2),(self.window, y2),1) #(x,y) de inicio, (x,y) de fin, ancho
                y2+=20
        
        veces=0
        while estado:
            clock.tick(60)

            #Con esto creo el evento exit, para salir de la ventana
            for event in pygame.event.get():            
                if event.type==pygame.QUIT:
                    estado=False
                    
            #Asigno los valores de mi ventana
            ventana.fill(self.amarillo_patito)#Color de mi ventana
            #pygame.draw.rect(ventana,verde_hanzo,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)        
            
            

            def graficoT():
                estado3=True
                indice=random.randrange(len(self.lista_colores))
                color_random=self.lista_colores[indice]                

                ubicacion=50
                state=True              
                clave=1
                
                def un_metodo(clave, ubicacion, color_random):
                    yt1=50
                    yt2=70
                    yt3=90
                    yt4=110
                    yt5=130
                    yt6=150
                    yt7=170
                    yt8=190
                    yt9=210
                    yt10=230
                    if clave==1:
                        cuadrado=pygame.Rect(ubicacion,yt1,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                                      
                    elif clave==2:
                        cuadrado=pygame.Rect(ubicacion,yt2,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    elif clave==3:
                        cuadrado=pygame.Rect(ubicacion,yt3,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    elif clave==4:
                        cuadrado=pygame.Rect(ubicacion,yt4,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    elif clave==5:
                        cuadrado=pygame.Rect(ubicacion,yt5,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    elif clave==6:
                        cuadrado=pygame.Rect(ubicacion,yt6,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    elif clave==7:
                        cuadrado=pygame.Rect(ubicacion,yt7,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    elif clave==8:
                        cuadrado=pygame.Rect(ubicacion,yt8,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    elif clave==9:
                        cuadrado=pygame.Rect(ubicacion,yt9,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    elif clave==10:
                        cuadrado=pygame.Rect(ubicacion,yt10,5,20) #Creo el cuadrado (X,Y, largo, ancho)            
                        pygame.draw.rect(ventana,color_random,cuadrado,border_radius =0) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)                                                           
                        
                    else:
                        pass     
                    
                def met_tiempo(clave, tiempo):
                    if clave==1:
                        self.lista1.append(tiempo)
                    elif clave==2:
                        self.lista2.append(tiempo)
                    elif clave==3:
                        self.lista3.append(tiempo)
                    elif clave==4:
                        self.lista4.append(tiempo)
                    elif clave==5:
                        self.lista5.append(tiempo)
                    elif clave==6:
                        self.lista6.append(tiempo)
                    elif clave==7:
                        self.lista7.append(tiempo)
                    elif clave==8:
                        self.lista8.append(tiempo)
                    elif clave==9:
                        self.lista9.append(tiempo)
                    elif clave==10:
                        self.lista10.append(tiempo)
                    else:
                        pass

                #tiempo=self.tiempo
                while state:
                    try:
                        if clave in self.tareas_por_defecto:
                            pass
                        else:
                            clave+=1

                        if 0 in self.tareas_por_defecto:
                            del self.tareas_por_defecto[0]

                        if self.tareas_por_defecto[clave]>0:

                            if self.tareas_por_defecto[clave]>3:
                                met_tiempo(clave, self.tiempo)                                                                                                       
                                for j in range(3):      
                                    print("*****Procesando*****")              
                                    self.tareas_por_defecto[clave]-=1                        
                                    print("A la tarea",clave ,"le restan",self.tareas_por_defecto[clave], "tiempo(s)")   
                                    un_metodo(clave, ubicacion, color_random)   
                                    ubicacion+=5
                                    self.tiempo+=1                                                                       
                                
                                met_tiempo(clave, self.tiempo)
                                self.tiempo+=1
                                print(self.tareas_por_defecto)

                            elif self.tareas_por_defecto[clave]==3:
                                met_tiempo(clave, self.tiempo)
                                for r in range(3):
                                    print("*****Procesando*****")                                                                               
                                    un_metodo(clave, ubicacion, color_random)  
                                    ubicacion+=5
                                    self.tiempo+=1
                                    self.tareas_por_defecto[clave]-=1                        
                                    print("A la tarea",clave ,"le restan",self.tareas_por_defecto[clave], "tiempo(s)")   
                                met_tiempo(clave, self.tiempo)
                                self.tiempo+=1                                                  
                                print("La tarea {} ha terminado".format(clave))
                                del self.tareas_por_defecto[clave]
                                print(self.tareas_por_defecto)

                            elif self.tareas_por_defecto[clave]==2:
                                met_tiempo(clave, self.tiempo)
                                for h in range(2):
                                    print("*****Procesando*****")
                                    un_metodo(clave, ubicacion, color_random)
                                    ubicacion+=5
                                    self.tiempo+=1
                                    self.tareas_por_defecto[clave]-=1                        
                                    print("A la tarea",clave ,"le restan",self.tareas_por_defecto[clave], "tiempo(s)")
                                met_tiempo(clave, self.tiempo)
                                self.tiempo+=1                                
                                print("La última tarea que ha entradon en reposo es: Tarea {}".format(clave))                        
                                print("Reutilizaremos un valor")
                                
                                try:
                                        if self.tareas_por_defecto[clave+1]==1:   
                                            print("*****Procesando*****")                                         
                                            met_tiempo(clave+1, self.tiempo)
                                            un_metodo(clave+1, ubicacion, color_random)
                                            ubicacion+=5
                                            self.tiempo+=1
                                            self.tareas_por_defecto[clave+1]-=1                        
                                            print("A la tarea",clave+1 ,"le restan",self.tareas_por_defecto[clave+1], "tiempo(s)")
                                            print("La tarea {} ha terminado".format(clave+1))
                                            met_tiempo(clave+1, self.tiempo)
                                            self.tiempo+=1
                                            del self.tareas_por_defecto[clave+1]
                                            
                                        
                                        elif self.tareas_por_defecto[clave+1]>1:
                                            met_tiempo(clave+1, self.tiempo)
                                            print("*****Procesando*****")
                                            un_metodo(clave+1, ubicacion, color_random)
                                            ubicacion+=5
                                            self.tiempo+=1
                                            self.tareas_por_defecto[clave+1]-=1                        
                                            print("A la tarea",clave+1 ,"le restan",self.tareas_por_defecto[clave+1], "tiempo(s)")
                                            met_tiempo(clave+1, self.tiempo)
                                            self.tiempo+=1
                                            
                                            
                                except:
                                        #print("Entro al exept Las tareas debierom de haber terminado")                                        
                                        pass              
                                self.tiempo+=1          
                                del self.tareas_por_defecto[clave]
                                print(self.tareas_por_defecto)


                            elif self.tareas_por_defecto[clave]==1:    
                                met_tiempo(clave, self.tiempo) 
                                print("*****Procesando*****")   
                                un_metodo(clave, ubicacion, color_random)
                                ubicacion+=5
                                self.tiempo+=1
                                met_tiempo(clave, self.tiempo) 
                                self.tiempo+=1               
                                self.tareas_por_defecto[clave]-=1
                                #print("A la tarea",clave ,"le restan",self.tareas_por_defecto[clave+1], "tiempo(s)")                        
                                print("La tarea",clave, "ha terminado")
                                print("La última tarea que ha entradon en reposo es: Tarea {}".format(clave))
                                print("Reutilizaremos dos valores")                                                  
                                try:
                                    if self.tareas_por_defecto[clave+1]>2:
                                        met_tiempo(clave+1, self.tiempo)
                                        for z in range(2):
                                            print("*****Procesando*****")
                                            un_metodo(clave+1, ubicacion, color_random)
                                            ubicacion+=5
                                            self.tiempo+=1
                                            self.tareas_por_defecto[clave+1]-=1                        
                                            print("A la tarea",clave+1 ,"le restan",self.tareas_por_defecto[clave+1], "tiempo(s)")
                                        met_tiempo(clave+1, self.tiempo)
                                        self.tiempo+=1
                                    elif self.tareas_por_defecto[clave+1]==2:
                                        met_tiempo(clave+1, self.tiempo)
                                        for q in range(2):
                                            print("*****Procesando*****")
                                            un_metodo(clave+1, ubicacion, color_random)
                                            ubicacion+=5
                                            self.tiempo+=1
                                            self.tareas_por_defecto[clave+1]-=1                        
                                            print("A la tarea",clave+1 ,"le restan",self.tareas_por_defecto[clave+1], "tiempo(s)")
                                            del self.tareas_por_defecto[clave+1]
                                        met_tiempo(clave+1, self.tiempo)
                                        self.tiempo+=1
                                    elif self.tareas_por_defecto[clave+1]==1:
                                            met_tiempo(clave+1, self.tiempo)  
                                            print("*****Procesando*****")                                      
                                            un_metodo(clave+1, ubicacion, color_random)
                                            ubicacion+=5
                                            self.tiempo+=1
                                            self.tareas_por_defecto[clave+1]-=1
                                            met_tiempo(clave+1, self.tiempo) 
                                            self.tiempo+=1           
                                            print("A la tarea",clave+1 ,"le restan",self.tareas_por_defecto[clave+1], "tiempo(s)")
                                            try:
                                                met_tiempo(clave+2, self.tiempo)
                                                print("*****Procesando*****")
                                                un_metodo(clave+2, ubicacion, color_random)
                                                ubicacion+=5
                                                self.tiempo+=2
                                                met_tiempo(clave+2, self.tiempo)
                                                self.tiempo+=2
                                                self.tareas_por_defecto[clave+2]-=2
                                                print("A la tarea",clave+2 ,"le restan",self.tareas_por_defecto[clave+1], "tiempo(s)")
                                                if self.tareas_por_defecto[clave+2]<=0:
                                                    del self.tareas_por_defecto[clave+2]
                                            except:
                                                pass
                                        
                                except:                                                                           
                                    pass
                                del self.tareas_por_defecto[clave]     
                                print(self.tareas_por_defecto)
                                  
                           
                        elif self.tareas_por_defecto[clave]==0:
                            print("La tarea {} ha terminado".format(clave))
                            del self.tareas_por_defecto[clave]
                        
                        
                        
                            
                    except:                        
                        if len(self.tareas_por_defecto)<=0:
                            print("Tareas terminadas")
                            state=False                  
                    
                    clave+=1     
                    #self.tiempo+=1
                    if clave>=11:
                        clave=1
                    
                    esta="vacio"            
                    j=0
                    r=0
                    h=0     
                    z=0
                
                '''while estado3:
                    for clave in self.tareas_por_defecto:
                        print("clave:",clave, "valor:", self.tareas_por_defecto[clave])
                        
                        #print(tareas_por_defecto[clave])
                        #if tareas_por_defecto[clave]>0:
                        if clave==1:
                            
                            for j in range(3):
                                cuadrado=pygame.Rect(ubicacion,yt1,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                                           
                                ubicacion+=20
                            #ubicacion+=60
                            
                        elif clave==2:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt2,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20

                        elif clave==3:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt5,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20
                                
                        elif clave==4:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt4,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20          

                        elif clave==5:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt5,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20

                        elif clave==6:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt6,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20

                        elif clave==7:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt7,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20

                        elif clave==8:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt8,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20

                        elif clave==9:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt9,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20

                        elif clave==10:
                                for j in range(3):
                                    cuadrado=pygame.Rect(ubicacion,yt10,20,20) #Creo el cuadrado (X,Y, largo, ancho)            
                                    pygame.draw.rect(ventana,color_random,cuadrado,border_radius =3) #Aquí estoy dibujando un cuadrado (ventana, color, figura, borde)
                                    
                                    ubicacion+=20
                            
                        if self.tareas_por_defecto[clave]<=0:
                                estado3=False   '''
                            
                #print(self.tareas_por_defecto)                     
            
            if veces<1:
                veces+=1
                #graficacion(ventana) #Cuadros de prueba            
                imprime_texto()#Texto y rayas  
                self.random_tareas()#Random     
                graficoT()
                print("El procesador utuliza 3 tiempos de ejecución por tarea")
                print("\nLa tarea 1 tuvo las siguiente(s) E/S y bloqueo:", multi.lista1)
                print("La tarea 2 tuvo las siguiente(s) E/S y bloqueo:", multi.lista2)
                print("La tarea 3 tuvo las siguiente(s) E/S y bloqueo:", multi.lista3)
                print("La tarea 4 tuvo las siguiente(s) E/S y bloqueo:", multi.lista4)
                print("La tarea 5 tuvo las siguiente(s) E/S y bloqueo:", multi.lista5)
                print("La tarea 6 tuvo las siguiente(s) E/S y bloqueo:", multi.lista6)
                print("La tarea 7 tuvo las siguiente(s) E/S y bloqueo:", multi.lista7)
                print("La tarea 8 tuvo las siguiente(s) E/S y bloqueo:", multi.lista8)
                print("La tarea 9 tuvo las siguiente(s) E/S y bloqueo:", multi.lista9)
                print("La tarea 10 tuvo las siguiente(s) E/S y bloqueo:", multi.lista10)
                pygame.display.update() #Aquí actualizo mi ventana
            

multi= Juego((),[],{}, [],[],[],[],[],[],[],[],[],[], 0, 0)

multi.main()