import os
import json
import serpapi
from dotenv import load_dotenv


load_dotenv()


def search_with_google_lens(image_path):

    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise ValueError(
            "SERPAPI_KEY is missing from .env"
        )

    print("\nUploading image to Google Lens...")

    client = serpapi.Client(
        api_key=api_key
    )

    upload = client.upload_image(
        image_path
    )

    image_id = upload["image_id"]

    print("✓ Image uploaded")
    print("✓ Image ID received")

    print("\nSearching Google Lens...")

    results = client.search({
        "engine": "google_lens",
        "image_id": image_id,
        "type": "all",
        "hl": "en"
    })

    print("✓ Google Lens search completed")

    return results


def save_results(results):

    output_path = "output/lens_results.json"

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
    results.as_dict(),
    file,
    indent=2,
    ensure_ascii=False

        )

    print(
        f"\n✓ Results saved to {output_path}"
    )