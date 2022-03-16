#Instalação de Biblioteca
import cv2 #Comando: pip install opencv-contrib-python

classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
#Arquivo treinado
reconhecedor.read('classificadorLBPH_V1.yml')

#Caminho da Câmera
camera = cv2.VideoCapture(0)

while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faceDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5)

    for (x, y, l, a) in faceDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (100, 100))
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        id, confianca = reconhecedor.predict(imagemFace)
        #Atribuindo o ID para o nome de cada pessoa
        if id == 1:
            nome = "Michelle Marques"
        if id == 2:
            nome = "Igor Carli"
        elif id ==3:
            nome = "Investidor Secreto"
        #Configuração do texto que aparece no retangulo
        cv2.putText(imagem, nome, (x,y + (a + 30)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))

    #Finalizar o programa pressione Q do seu teclado
    cv2.imshow("Face", imagem)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()