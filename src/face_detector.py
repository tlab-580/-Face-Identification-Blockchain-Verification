import face_recognition


def load_and_encode(image_path):
    print(f"\nLoading image: {image_path}")

    image = face_recognition.load_image_file(image_path)

    print("Detecting face...")

    locations = face_recognition.face_locations(image)

    if len(locations) == 0:
        raise ValueError("No face detected in the image.")

    print(f"Faces detected: {len(locations)}")

    if len(locations) > 1:
        print("Warning: More than one face detected.")
        print("Using the first face.")

    print("Generating face encoding...")

    encodings = face_recognition.face_encodings(
        image,
        known_face_locations=locations
    )

    if not encodings:
        raise ValueError("Could not generate face encoding.")

    print("Face encoding generated successfully.")

    return encodings[0], locations[0]