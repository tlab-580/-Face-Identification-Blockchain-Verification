from web_search import search_with_google_lens
from web_search import save_results


IMAGE_PATH = "input/face.jpg"


def main():

    print("=" * 60)
    print("          GOOGLE LENS SEARCH TEST")
    print("=" * 60)

    try:

        results = search_with_google_lens(
            IMAGE_PATH
        )

        save_results(results)

        print("\nSearch completed successfully.")

        print("\nTop-level result sections:")

        for key in results.keys():
            print(" -", key)

    except Exception as error:

        print("\n❌ ERROR:")
        print(error)


if __name__ == "__main__":
    main()