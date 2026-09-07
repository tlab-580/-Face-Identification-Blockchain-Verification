from face_detector import load_and_encode


IMAGE_PATH = "input/face.jpg"


def main():

    print("=" * 50)
    print("       FACECHAIN VERIFY")
    print("       FACE DETECTION TEST")
    print("=" * 50)

    try:

        encoding, location = load_and_encode(
            IMAGE_PATH
        )

        print("\n" + "=" * 50)
        print("RESULT")
        print("=" * 50)

        print("✓ Face detected")
        print("✓ Face encoded")

        print("\nFace location:")
        print(location)

        print("\nEncoding length:")
        print(len(encoding))

        print("\nFirst 5 encoding values:")
        print(encoding[:5])

        print("\n✓ FACE DETECTION MODULE WORKING")

    except Exception as error:

        print("\n❌ ERROR:")
        print(error)


if __name__ == "__main__":
    main()