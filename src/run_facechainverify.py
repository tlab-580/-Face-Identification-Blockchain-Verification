import subprocess
import sys


def run_step(title, command):

    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)

    result = subprocess.run(
        command,
        check=False
    )

    if result.returncode != 0:

        print(
            f"\n❌ {title} FAILED"
        )

        sys.exit(result.returncode)

    print(
        f"\n✓ {title} COMPLETED"
    )


def main():

    print("=" * 70)
    print("              FACECHAINVERIFY")
    print("              COMPLETE PIPELINE")
    print("=" * 70)

    # Step 1: Google Lens search
    run_step(
        "STEP 1 - GOOGLE LENS SEARCH",
        [
            sys.executable,
            "src/test_search.py"
        ]
    )

    # Step 2: Extract candidates
    run_step(
        "STEP 2 - CANDIDATE EXTRACTION",
        [
            sys.executable,
            "src/candidate_extractor.py"
        ]
    )

    # Step 3: Download candidates
    run_step(
        "STEP 3 - CANDIDATE IMAGE DOWNLOAD",
        [
            sys.executable,
            "src/download_candidates.py"
        ]
    )

    # Step 4: Verify candidates
    run_step(
        "STEP 4 - FACE VERIFICATION",
        [
            sys.executable,
            "src/verify_candidates.py"
        ]
    )

    # Step 5: Generate final report
    run_step(
        "STEP 5 - FINAL REPORT",
        [
            sys.executable,
            "src/final_report.py"
        ]
    )

    # Step 6: Generate SHA-256 hash
    run_step(
        "STEP 6 - SHA-256 HASH",
        [
            sys.executable,
            "src/hashing.py"
        ]
    )

    print("\n")
    print("=" * 70)
    print("              PIPELINE COMPLETED")
    print("=" * 70)

    print("\n✓ Face search completed")
    print("✓ Candidates collected")
    print("✓ Face verification completed")
    print("✓ Final report generated")
    print("✓ SHA-256 hash generated")
    print("✓ Ready for blockchain storage")

    print("\nNext:")
    print("Run the blockchain transaction to store the hash.")


if __name__ == "__main__":
    main()