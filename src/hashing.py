import hashlib


def calculate_sha256(file_path):

    sha256 = hashlib.sha256()

    with open(
        file_path,
        "rb"
    ) as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def main():

    file_path = "output/final_report.json"

    print("=" * 60)
    print("              SHA-256 HASH TEST")
    print("=" * 60)

    try:

        file_hash = calculate_sha256(
            file_path
        )

        print("\nFile:")
        print(file_path)

        print("\nSHA-256 Hash:")
        print(file_hash)

        with open(
            "output/final_report_hash.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(file_hash)

        print(
            "\n✓ Hash saved to output/final_report_hash.txt"
        )

        print(
            "\n✓ SHA-256 HASH GENERATED SUCCESSFULLY"
        )

    except FileNotFoundError:

        print(
            "\n❌ final_report.json not found."
        )

        print(
            "Run final_report.py first."
        )


if __name__ == "__main__":
    main()