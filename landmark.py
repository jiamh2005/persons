#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import dlib
import glob
import numpy as np
from skimage import io

def landmark(filepath):

    predictor_path = "samples/models/shape_predictor_5_face_landmarks.dat"
    face_rec_model_path = "samples/models/dlib_face_recognition_resnet_model_v1.dat"

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

    faces = dlib.full_object_detections()

    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        # Get the landmarks/parts for the face in box d.
        shape = predictor(img, d)
        print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))
        faces.append(shape)
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        print(face_descriptor)

    dlib.save_face_chips(img, faces, filepath, 150, 0.25)

def face_distance(face_encodings, face_to_compare):
    """
    Given a list of face encodings, compare them to a known face encoding and get a euclidean distance
    for each comparison face. The distance tells you how similar the faces are.
    :param faces: List of face encodings to compare
    :param face_to_compare: A face encoding to compare against
    :return: A numpy ndarray with the distance for each face in the same order as the 'faces' array
    """
    if len(face_encodings) == 0:
        return np.empty((0))

    return np.linalg.norm(face_encodings - face_to_compare, axis=1)
