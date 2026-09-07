import sys
import os
import json
import uuid

# Add src folder to Python path
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        "src"
    )
)

from flask import Flask, render_template, request, jsonify

from face_detector import load_and_encode
from matcher import compare_faces
from hashing import calculate_sha256
from blockchain import store_verification

# ==========================================
# FLASK CONFIGURATION
# ==========================================

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
CANDIDATE_FOLDER = "output/candidates"
RESULTS_FILE = "output/verification_results.json"

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("output", exist_ok=True)


# ==========================================
# FILE VALIDATION
# ==========================================

def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


# ==========================================
# VERIFY CANDIDATES
# ==========================================

def verify_candidates(reference_image):

    print("\n======================================")
    print(" FACE VERIFICATION")
    print("======================================")

    print(
        "Reference image:",
        reference_image
    )

    # Generate reference face encoding
    reference_encoding, _ = load_and_encode(
        reference_image
    )

    print(
        "\nScanning candidate folder..."
    )

    verification_results = []

    if not os.path.exists(CANDIDATE_FOLDER):

        raise FileNotFoundError(
            "Candidate folder not found: "
            + CANDIDATE_FOLDER
        )

    candidate_files = [
        filename
        for filename in os.listdir(
            CANDIDATE_FOLDER
        )
        if filename.lower().endswith(
            (
                ".jpg",
                ".jpeg",
                ".png",
                ".webp"
            )
        )
    ]

    candidate_files.sort()

    print(
        "Candidates found:",
        len(candidate_files)
    )

    for filename in candidate_files:

        candidate_path = os.path.join(
            CANDIDATE_FOLDER,
            filename
        )

        try:

            result = compare_faces(
                reference_encoding,
                candidate_path
            )

            distance = result["distance"]
            match = result["match"]

            verification_results.append(
                {
                    "filename": filename,
                    "face_distance": distance,
                    "match": match
                }
            )

            print(
                f"{filename} → "
                f"distance={distance}, "
                f"match={match}"
            )

        except Exception as error:

            print(
                f"Error processing {filename}:",
                error
            )

            verification_results.append(
                {
                    "filename": filename,
                    "face_distance": None,
                    "match": False,
                    "error": str(error)
                }
            )

    # Save results
    with open(
        RESULTS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            verification_results,
            file,
            indent=4
        )

    matches = [
        item
        for item in verification_results
        if item.get("match") is True
    ]

    match_found = len(matches) > 0

    result = (
        "VERIFIED"
        if match_found
        else "NOT_VERIFIED"
    )

    print(
        "\nCandidates checked:",
        len(verification_results)
    )

    print(
        "Matching candidates:",
        len(matches)
    )

    print(
        "Final result:",
        result
    )

    return {
        "candidates_checked": len(
            verification_results
        ),
        "matching_candidates": len(matches),
        "match_found": match_found,
        "result": result,
        "verification_results":
            verification_results
    }


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# ==========================================
# STATUS
# ==========================================

@app.route("/status")
def status():

    return jsonify(
        {
            "status": "FaceChainVerify backend running"
        }
    )


# ==========================================
# VERIFY IMAGE
# ==========================================

@app.route(
    "/verify",
    methods=["POST"]
)
def verify():

    try:

        # ----------------------------------
        # Check uploaded file
        # ----------------------------------

        if "image" not in request.files:

            return jsonify(
                {
                    "error":
                        "No image uploaded."
                }
            ), 400

        file = request.files["image"]

        if file.filename == "":

            return jsonify(
                {
                    "error":
                        "No image selected."
                }
            ), 400

        if not allowed_file(
            file.filename
        ):

            return jsonify(
                {
                    "error":
                        "Unsupported image format."
                }
            ), 400

        # ----------------------------------
        # Save uploaded image
        # ----------------------------------

        extension = file.filename.rsplit(
            ".",
            1
        )[1].lower()

        unique_filename = (
            str(uuid.uuid4())
            + "."
            + extension
        )

        uploaded_path = os.path.join(
            UPLOAD_FOLDER,
            unique_filename
        )

        file.save(
            uploaded_path
        )

        print("\n======================================")
        print(" NEW VERIFICATION REQUEST")
        print("======================================")

        print(
            "Uploaded image:",
            uploaded_path
        )

        # ----------------------------------
        # FACE VERIFICATION
        # ----------------------------------

        verification = verify_candidates(
            uploaded_path
        )

        # ----------------------------------
        # SHA-256 HASH
        # ----------------------------------

        print(
            "\nGenerating SHA-256..."
        )

        image_hash = calculate_sha256(
            uploaded_path
        )

        print(
            "SHA-256:",
            image_hash
        )

        # ----------------------------------
        # BLOCKCHAIN
        # ----------------------------------

        print(
            "\nStoring verification on blockchain..."
        )

        blockchain_result = store_verification(
            image_hash,
            verification["result"]
        )

        # ----------------------------------
        # FINAL RESPONSE
        # ----------------------------------

        response = {

            "status":
                verification["result"],

            "candidates_checked":
                verification[
                    "candidates_checked"
                ],

            "matching_candidates":
                verification[
                    "matching_candidates"
                ],

            "face_match":
                "YES"
                if verification["match_found"]
                else "NO",

            "image_hash":
                image_hash,

            "blockchain_id":
                blockchain_result[
                    "blockchain_id"
                ],

            "transaction":
                blockchain_result[
                    "transaction"
                ],

            "timestamp":
                blockchain_result[
                    "timestamp"
                ],

            "verifier":
                blockchain_result[
                    "verifier"
                ],

            "block_number":
                blockchain_result[
                    "block_number"
                ]
        }

        print(
            "\n======================================"
        )

        print(
            " VERIFICATION COMPLETE"
        )

        print(
            "======================================"
        )

        print(
            json.dumps(
                response,
                indent=4
            )
        )

        return jsonify(response)

    except Exception as error:

        print(
            "\n❌ Verification error:"
        )

        print(error)

        return jsonify(
            {
                "error": str(error)
            }
        ), 500


# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":

    print(
        "======================================"
    )

    print(
        " FACECHAINVERIFY FLASK SERVER"
    )

    print(
        "======================================"
    )

    print(
        "Server: http://127.0.0.1:5000"
    )

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )