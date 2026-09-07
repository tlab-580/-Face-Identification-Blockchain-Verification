import face_recognition


def compare_faces(reference_encoding, candidate_image_path):

    image = face_recognition.load_image_file(
        candidate_image_path
    )

    locations = face_recognition.face_locations(image)

    if not locations:
        return {
            "match": False,
            "distance": None
        }

    encodings = face_recognition.face_encodings(
        image,
        known_face_locations=locations
    )

    best_distance = 1.0

    for encoding in encodings:

        distance = face_recognition.face_distance(
            [reference_encoding],
            encoding
        )[0]

        distance = float(distance)

        if distance < best_distance:
            best_distance = distance

    return {
        "match": best_distance < 0.50,
        "distance": best_distance
    }