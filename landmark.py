#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import dlib
import glob
import numpy as np
from skimage import io

from modules.storage.storage import *
from modules.filenamegen import nsfile, file_dir

def landmark(filepath):

    filepath = filepath.replace("\\","/")

    predictor_path = "samples/models/shape_predictor_5_face_landmarks.dat"
    face_rec_model_path = "samples/models/dlib_face_recognition_resnet_model_v1.dat"
    files_dir = file_dir(filepath)+'/'

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)
    facerec = dlib.face_recognition_model_v1(face_rec_model_path)

    print("Processing file: {}".format(filepath))
    img = io.imread(filepath)

    # Ask the detector to find the bounding boxes of each face. The 1 in the
    # second argument indicates that we should upsample the image 1 time. This
    # will make everything bigger and allow us to detect more faces.
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))

    locations = []
    for l in dets:
        locations.append([l.left(), l.right(), l.top(), l.bottom()])
    SaveImage(filepath,locations)

    ##faces = dlib.full_object_detections()

    for k, d in enumerate(dets):
        # Get the landmarks/parts for the face in box d.
        shape = predictor(img, d)
        ##faces.append(shape)
        face_descriptor = facerec.compute_face_descriptor(img, shape)

        filenames = nsfile(1)
        dlib.save_face_chip(img, shape, files_dir+filenames[0], 150, 0.25)

        fps = []
        for p in face_descriptor:
            fps.append(p)
        SaveFace(filenames[0]+'.jpg',fps, filepath)
