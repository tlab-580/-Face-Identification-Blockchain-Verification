from face_detector import load_and_encode
from matcher import compare_faces


IMAGE_PATH = "input/face.jpg"


def main():

    print("=" * 50)
    print("       FACECHAIN VERIFY")
    print("       FACE MATCHING TEST")
    print("=" * 50)

    try:

        reference_encoding, location = load_and_encode(
            IMAGE_PATH
        )

        print("\n✓ Reference face encoded")

        result = compare_faces(
            reference_encoding,
            IMAGE_PATH
        )

        print("\nCandidate comparison:")
        print("--------------------------------")

        print(
            f"Face distance: {result['distance']}"
        )

        print(
            f"Match: {result['match']}"
        )

        if result["match"]:
            print("\n✓ FACE MATCH CONFIRMED")
        else:
            print("\n✗ FACE DOES NOT MATCH")

    except Exception as error:

        print("\n❌ ERROR:")
        print(error)


if __name__ == "__main__":
    main()