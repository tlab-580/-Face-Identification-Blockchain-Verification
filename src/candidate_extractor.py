import json


RESULTS_PATH = "output/lens_results.json"


def load_results():

    with open(
        RESULTS_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def extract_candidates(results):

    candidates = []

    visual_matches = results.get(
        "visual_matches",
        []
    )

    for item in visual_matches:

        candidate = {
            "title": item.get("title"),
            "link": item.get("link"),
            "source": item.get("source"),
            "thumbnail": item.get("thumbnail")
        }

        candidates.append(candidate)

    return candidates


def display_candidates(candidates):

    print("\n" + "=" * 70)
    print("              CANDIDATE SEARCH RESULTS")
    print("=" * 70)

    if not candidates:

        print("\nNo visual matches were found.")

        return

    print(
        f"\nTotal candidates found: {len(candidates)}"
    )

    for index, candidate in enumerate(
        candidates,
        start=1
    ):

        print("\n" + "-" * 70)

        print(f"Candidate #{index}")

        print(
            f"Title     : {candidate['title']}"
        )

        print(
            f"Source    : {candidate['source']}"
        )

        print(
            f"Page URL  : {candidate['link']}"
        )

        print(
            f"Image URL : {candidate['thumbnail']}"
        )


def main():

    try:

        results = load_results()

        candidates = extract_candidates(
            results
        )

        display_candidates(
            candidates
        )

    except FileNotFoundError:

        print(
            "\n❌ lens_results.json was not found."
        )

        print(
            "Run test_search.py first."
        )

    except Exception as error:

        print("\n❌ ERROR:")
        print(error)


if __name__ == "__main__":
    main()