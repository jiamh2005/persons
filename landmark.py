#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import dlib
import glob
from skimage import io

def landmark(filepath):

    predictor_path = "samples/models/shape_predictor_5_face_landmarks.dat"

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    print("Processing file: {}".format(filepath))
    img = io.imread(filepath)

    # Ask the detector to find the bounding boxes of each face. The 1 in the
    # second argument indicates that we should upsample the image 1 time. This
    # will make everything bigger and allow us to detect more faces.
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))

    faces = dlib.full_object_detections()

    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        # Get the landmarks/parts for the face in box d.
        shape = predictor(img, d)
        print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))
        faces.append(shape)

    dlib.save_face_chips(img, faces, filepath, 150, 0.25)
