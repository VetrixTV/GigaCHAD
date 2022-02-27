# Benötigte Bibliotheken importieren.
import cv2, sys, numpy, os, csv, time

# Dimensionen der Kamera.
(width, height) = (1920, 1080)

# Spezifiziert die Methode, mit der Gesichter erkannt werden.
face_classificator = 'haar_cascade_frontal.xml'

# Projektpfad.
project_path = os.path.curdir

# Ordername für die Daten.
datasets = 'datasets'

# Ordnername für Videobilder.
sub_data = 'videodata'

# Zusammengefügter Pfad aus Projektpfad und Daten/Videobilder.
dataset_folder_path = os.path.join(project_path, datasets, sub_data)

# Pfad der CSV-Datei, in der Koordinaten des Gesichts für die SerialAPI gespeichert werden.
csv_file_path = os.path.join(project_path, 'coordinates.csv')


# Erzeugt, wenn noch nicht existent, die Ordner, in dem die Videobilder gespeichert werden.
def create_dataset_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("Dataset directory created.")
    else:
        print("Dataset directory already exists.")

# Start des Programms ####################################################
create_dataset_directory(dataset_folder_path)

# Erstellt die CSV-Datei zunächst ohne Daten im Projektordner.
if not os.path.exists(csv_file_path):
    csv_create = open(os.path.join(project_path, 'coordinates.csv'), 'x')
    csv_create.close()

# Spezifizieren der Gesichtserkennungmethode.
face_cascade = cv2.CascadeClassifier(face_classificator)

# Die extern angeschlossene Kamera verwenden.
# 0 - Windows-Standardkamera
# 1 - 2. Kamera
webcam = cv2.VideoCapture(0)

count = 1
while count < 2147483647:
    # Bildaufnahme.
    (_, image) = webcam.read()
    # 640 x 480
    # Rechteck für die X-Achse (mit Toleranzgrenze).
    cv2.rectangle(image, (0,210), (640,270), (255,0,0), 2)
    
    # Rechteck für die Y-Achse (mit Toleranzgrenze).
    cv2.rectangle(image, (290,0), (350,480), (255, 0, 0), 2)
    
    # Bild in Graustufen konvertieren.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Gesichter im Graustufen-Bild erkennen.
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    # Für jedes Gesicht wird diese Schleife durchlaufen.
    for(xCell, yCell, faceWidth, faceHeight) in faces:
        if count % 3000:
            print('Coordinates will get saved: ', xCell, yCell)
            # Koordinaten des Gesichts in CSV-Datei speichern.
            # Try-Block ist als Sicherheitsmechanismus eingebaut, falls die CSV-Datei von der SerialAPI gelesen wird.
            try:
                with open(os.path.join(project_path, 'coordinates.csv'), 'r+') as csv:
                    csv.seek(0)
                    csv.truncate()
                    csv.write(str(xCell) + ';' + str(yCell) + '\n')
                    csv.close()
            except IOError:
                print('File is already opened')
            # Rechteck um das erkannte Gesicht zeichnen.
            cv2.rectangle(image, (xCell, yCell), (xCell + faceWidth, yCell + faceHeight), (255, 0, 0), 2)
            face = gray[yCell:yCell + faceHeight, xCell:xCell + faceWidth]
            face_resize = cv2.resize(face, (width, height))
            # Bild des Gesichts speichern.
            cv2.imwrite('% s/% s.png' % (dataset_folder_path, count), face_resize)
        else:
            cv2.rectangle(image, (xCell, yCell), (xCell + faceWidth, yCell + faceHeight), (255, 0, 0), 2)
            face = gray[yCell:yCell + faceHeight, xCell:xCell + faceWidth]
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite('% s/% s.png' % (dataset_folder_path, count), face_resize)
    count += 1
    
    cv2.imshow('OpenCV', image)
    key = cv2.waitKey(10)
    if key == 27:
        break

