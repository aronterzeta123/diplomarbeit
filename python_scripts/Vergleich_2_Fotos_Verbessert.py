#!/usr/bin/python3

import face_recognition as fr
c=""
konstant_image=fr.load_image_file("./richtige.jpg")
ipanjoftun_image=fr.load_image_file("%s.jpg"%(image2))
biden_encoding=fr.face_encodings(konstant_image)[0]
unknown_encoding=fr.face_encodings(ipanjoftun_image)[0]
try:
    results=fr.compare_faces([biden_encodings],unknown_encoding)
    c="matched"
    print ("Kot")
except:
    c="not matched"
