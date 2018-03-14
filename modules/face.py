import numpy as np
def face_distance(face_data, face_to_compare):
    """
    Given a list of face encodings, compare them to a known face encoding and get a euclidean distance
    for each comparison face. The distance tells you how similar the faces are.
    :param faces: List of face encodings to compare
    :param face_to_compare: A face encoding to compare against
    :return: A numpy ndarray with the distance for each face in the same order as the 'faces' array
    """
    if len(face_data) == 0:
        return np.empty((0))

    subs = []

    for i in range(len(face_data)):
        subs.append(face_data[i] - face_to_compare[i])
    return np.linalg.norm(subs)
