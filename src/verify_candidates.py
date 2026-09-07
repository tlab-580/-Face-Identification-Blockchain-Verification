import os
import json

from face_detector import load_and_encode
from matcher import compare_faces


REFERENCE_IMAGE = "input/face.jpg"
CANDIDATE_FOLDER = "output/candidates"
RESULTS_FILE = "output/verification_results.json"


def main():

    print("=" * 70)
    print("             FACECHAIN VERIFY")
    print("             CANDIDATE VERIFICATION")
    print("=" * 70)

    # --------------------------------------------------
    # Step 1: Encode reference face
    # --------------------------------------------------

    print("\n[1] Loading reference image...")

    try:

        reference_encoding, location = load_and_encode(
            REFERENCE_IMAGE
        )

        print("✓ Reference face encoded")

    except Exception as error:

        print("\n❌ Could not process reference image.")
        print(error)
        return

    # --------------------------------------------------
    # Step 2: Find candidate images
    # --------------------------------------------------

    print("\n[2] Searching candidate folder...")

    if not os.path.exists(CANDIDATE_FOLDER):

        print(
            f"❌ Folder not found: {CANDIDATE_FOLDER}"
        )

        return

    candidate_files = []

    for filename in os.listdir(CANDIDATE_FOLDER):

        if filename.lower().endswith(
            (".jpg", ".jpeg", ".png", ".webp")
        ):

            candidate_files.append(filename)

    if not candidate_files:

        print("❌ No candidate images found.")

        return

    print(
        f"✓ Found {len(candidate_files)} candidate image(s)"
    )

    # --------------------------------------------------
    # Step 3: Compare faces
    # --------------------------------------------------

    print("\n[3] Comparing candidate faces...")
    print("-" * 70)

    verification_results = []

    for index, filename in enumerate(
        candidate_files,
        start=1
    ):

        candidate_path = os.path.join(
            CANDIDATE_FOLDER,
            filename
        )

        print(f"\nCandidate #{index}: {filename}")

        try:

            result = compare_faces(
                reference_encoding,
                candidate_path
            )

            distance = result["distance"]
            match = result["match"]

            if distance is None:

                print("Face detected: NO")
                print("Match: NO")

            else:

                print("Face detected: YES")
                print(
                    f"Face distance: {distance:.4f}"
                )

                if match:

                    print("Match: YES ✓")

                else:

                    print("Match: NO ✗")

            verification_results.append(
                {
                    "filename": filename,
                    "face_distance": distance,
                    "match": match
                }
            )

        except Exception as error:

            print(
                f"❌ Error processing {filename}: {error}"
            )

            verification_results.append(
                {
                    "filename": filename,
                    "face_distance": None,
                    "match": False,
                    "error": str(error)
                }
            )

    # --------------------------------------------------
    # Step 4: Save verification results
    # --------------------------------------------------

    with open(
        RESULTS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            verification_results,
            file,
            indent=2
        )

    # --------------------------------------------------
    # Step 5: Summary
    # --------------------------------------------------

    matches = [
        result
        for result in verification_results
        if result["match"]
    ]

    print("\n" + "=" * 70)
    print("                    VERIFICATION SUMMARY")
    print("=" * 70)

    print(
        f"Candidates checked : {len(verification_results)}"
    )

    print(
        f"Face matches        : {len(matches)}"
    )

    print(
        f"Results saved       : {RESULTS_FILE}"
    )

    if matches:

        print("\n✓ MATCHING CANDIDATE(S):")

        for result in matches:

            print(
                f"  • {result['filename']} "
                f"(distance: {result['face_distance']:.4f})"
            )

    else:

        print("\n✗ No matching candidates found.")

    print("\n✓ Candidate verification completed.")


if __name__ == "__main__":
    main()