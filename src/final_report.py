import json


LENS_RESULTS = "output/lens_results.json"
VERIFICATION_RESULTS = "output/verification_results.json"
FINAL_REPORT = "output/final_report.json"


def load_json(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def create_report():

    lens_data = load_json(
        LENS_RESULTS
    )

    verification_data = load_json(
        VERIFICATION_RESULTS
    )

    visual_matches = lens_data.get(
        "visual_matches",
        []
    )

    # Create a lookup table for verification results
    verification_lookup = {}

    for result in verification_data:

        verification_lookup[
            result["filename"]
        ] = result

    final_results = []

    for index, verification in enumerate(
        verification_data
    ):

        filename = verification["filename"]

        # Google Lens results are normally
        # in the same order as downloaded candidates.
        lens_item = (
            visual_matches[index]
            if index < len(visual_matches)
            else {}
        )

        final_result = {

            "candidate_image":
                filename,

            "title":
                lens_item.get("title"),

            "source":
                lens_item.get("source"),

            "page_url":
                lens_item.get("link"),

            "image_url":
                lens_item.get("thumbnail"),

            "face_distance":
                verification.get(
                    "face_distance"
                ),

            "face_match":
                verification.get(
                    "match",
                    False
                )
        }

        final_results.append(
            final_result
        )

    # Sort matching candidates first
    final_results.sort(
        key=lambda item: (
            not item["face_match"],
            item["face_distance"]
            if item["face_distance"] is not None
            else 999
        )
    )

    with open(
        FINAL_REPORT,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            final_results,
            file,
            indent=2,
            ensure_ascii=False
        )

    return final_results


def display_report(results):

    print("\n" + "=" * 80)
    print("                 FINAL VERIFICATION REPORT")
    print("=" * 80)

    print(
        f"\nTotal candidates: {len(results)}"
    )

    matches = [
        item
        for item in results
        if item["face_match"]
    ]

    print(
        f"Face matches: {len(matches)}"
    )

    print("\n" + "-" * 80)

    for index, item in enumerate(
        results,
        start=1
    ):

        print(
            f"\nCandidate #{index}"
        )

        print(
            f"Image       : {item['candidate_image']}"
        )

        print(
            f"Title       : {item['title']}"
        )

        print(
            f"Source      : {item['source']}"
        )

        print(
            f"Face Match  : {item['face_match']}"
        )

        print(
            f"Face Distance: {item['face_distance']}"
        )

        print(
            f"Page URL    : {item['page_url']}"
        )

    print("\n" + "=" * 80)

    print(
        f"✓ Final report saved to {FINAL_REPORT}"
    )


def main():

    try:

        results = create_report()

        display_report(
            results
        )

    except FileNotFoundError as error:

        print("\n❌ Required file not found:")
        print(error)

        print(
            "\nMake sure you have already run:"
        )

        print(
            "python src\\test_search.py"
        )

        print(
            "python src\\download_candidates.py"
        )

        print(
            "python src\\verify_candidates.py"
        )

    except Exception as error:

        print("\n❌ ERROR:")
        print(error)


if __name__ == "__main__":
    main()