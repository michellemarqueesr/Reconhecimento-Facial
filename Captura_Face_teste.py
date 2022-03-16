#Importando as bibliotecas
import cv2
import numpy as np


classificador = cv2.CascadeClassifier(r'C:\Users\miche\PycharmProjects\pythonProject1\cascades\haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0) #Camera padrão == 0

amostra = 1 #numero da amostra atual
numeroMaxAmostras = 25
nome = input("Digite o seu nome: ") #nome que aparecerá na face reconhecida
altura, largura = 220, 220 #tamanho padrão da imagem para treinamento

while True:
    status, imagem = camera.read() #Le o estado da cãmera e a imagem capturada
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza,scaleFactor=1.5,minSize=(150,150))
    for (x,y,altura,largura) in facesDetectadas:
        cv2.rectangle(imagem, (x,y) , (x+largura,y+altura), (0,0,255), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Média: ", np.average(imagemCinza))
            if np.average(imagemCinza) > 110:
                #Redimensiona a imagem para 220x220 pixels
                imagemFace = cv2.resize(imagemCinza[y: y+altura, x: x+largura], (largura,altura))

                #Local que ficará cada foto tirada
                localFoto = r'C:\Users\miche\PycharmProjects\pythonProject1\imagens' + str(nome)+" "+ str(amostra)+ ".jpg"

                #Grava a foto na pasta
                cv2.imwrite(localFoto, imagemFace)
                amostra +=1 #Adiciona uma unidade no contador de amostras
    cv2.imshow("Face detectada", imagem) #Exibe a foto na tela
    if amostra > numeroMaxAmostras: #Se capturou as 25 anostras
        break

print("Fotos Capturadas com Sucesso!!")
camera.release() #Libera a Câmera
cv2.destroyAllWindows() #Finaliza a janela
