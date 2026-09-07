import json
import os
import requests


RESULTS_PATH = "output/lens_results.json"
OUTPUT_FOLDER = "output/candidates"


def load_results():

    with open(
        RESULTS_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def get_candidates(results):

    return results.get(
        "visual_matches",
        []
    )


def download_image(url, output_path):

    try:

        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        content_type = response.headers.get(
            "Content-Type",
            ""
        )

        if not content_type.startswith("image/"):

            print(
                "  ✗ URL did not return an image"
            )

            return False

        with open(
            output_path,
            "wb"
        ) as file:

            file.write(
                response.content
            )

        return True

    except Exception as error:

        print(
            f"  ✗ Download failed: {error}"
        )

        return False


def main():

    print("=" * 70)
    print("             CANDIDATE IMAGE DOWNLOADER")
    print("=" * 70)

    try:

        results = load_results()

        candidates = get_candidates(
            results
        )

        if not candidates:

            print(
                "\n❌ No visual matches found."
            )

            return

        os.makedirs(
            OUTPUT_FOLDER,
            exist_ok=True
        )

        downloaded = 0

        for index, candidate in enumerate(
            candidates,
            start=1
        ):

            image_url = candidate.get(
                "thumbnail"
            )

            title = candidate.get(
                "title",
                "Unknown"
            )

            print(
                f"\nCandidate #{index}"
            )

            print(
                f"Title: {title}"
            )

            if not image_url:

                print(
                    "  ✗ No image URL available"
                )

                continue

            filename = (
                f"candidate_{index}.jpg"
            )

            output_path = os.path.join(
                OUTPUT_FOLDER,
                filename
            )

            print(
                "  Downloading image..."
            )

            success = download_image(
                image_url,
                output_path
            )

            if success:

                print(
                    f"  ✓ Saved: {filename}"
                )

                downloaded += 1

        print("\n" + "=" * 70)

        print(
            f"Downloaded images: {downloaded}"
        )

        print(
            f"Location: {OUTPUT_FOLDER}"
        )

        print("=" * 70)

    except FileNotFoundError:

        print(
            "\n❌ lens_results.json not found."
        )

        print(
            "Run test_search.py first."
        )

    except Exception as error:

        print("\n❌ ERROR:")
        print(error)


if __name__ == "__main__":
    main()