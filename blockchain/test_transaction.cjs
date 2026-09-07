const { ethers } = require("ethers");
const fs = require("fs");


const RPC_URL = "http://127.0.0.1:8545";

const CONTRACT_ADDRESS =
    "0x7ced9bac2f4286f00c25b2ad84596b29036f4e34";


const ABI = [
    "function storeVerification(string _imageHash, string _result) public returns (uint256)",
    "function getVerification(uint256 _id) public view returns (string imageHash, string result, uint256 timestamp, address verifier)",
    "function getVerificationCount() public view returns (uint256)"
];


async function main() {

    console.log("======================================");
    console.log(" FACECHAINVERIFY BLOCKCHAIN");
    console.log("======================================");


    // Connect to local blockchain
    const provider = new ethers.JsonRpcProvider(
        RPC_URL
    );


    // Get private key from environment variable
    const privateKey = process.env.PRIVATE_KEY;

    if (!privateKey) {

        console.log(
            "❌ PRIVATE_KEY environment variable not found"
        );

        console.log(
            "Please set your local blockchain private key first."
        );

        return;
    }


    // Create wallet
    const wallet = new ethers.Wallet(
        privateKey,
        provider
    );


    console.log(
        "Wallet:",
        wallet.address
    );


    // Connect to smart contract
    const contract = new ethers.Contract(
        CONTRACT_ADDRESS,
        ABI,
        wallet
    );


    // ======================================
    // READ SHA-256 HASH
    // ======================================

    const hashFile =
        "output/final_report_hash.txt";


    if (!fs.existsSync(hashFile)) {

        console.log(
            "❌ Hash file not found:"
        );

        console.log(hashFile);

        console.log(
            "Run hashing.py first."
        );

        return;
    }


    const imageHash =
        fs.readFileSync(
            hashFile,
            "utf8"
        ).trim();


    // ======================================
    // READ ACTUAL VERIFICATION RESULTS
    // ======================================

    const verificationFile =
        "output/verification_results.json";


    if (!fs.existsSync(verificationFile)) {

        console.log(
            "❌ Verification results file not found:"
        );

        console.log(verificationFile);

        console.log(
            "Run verify_candidates.py first."
        );

        return;
    }


    const verificationResults =
        JSON.parse(
            fs.readFileSync(
                verificationFile,
                "utf8"
            )
        );


    // Check whether at least one candidate matched
    const matchFound =
        verificationResults.some(
            (item) => item.match === true
        );


    const result =
        matchFound
            ? "VERIFIED"
            : "NOT_VERIFIED";


    console.log(
        "\nVerification analysis:"
    );

    console.log(
        "Candidates checked:",
        verificationResults.length
    );

    console.log(
        "Matching candidate found:",
        matchFound
    );

    console.log(
        "Final result:",
        result
    );


    // ======================================
    // STORE ON BLOCKCHAIN
    // ======================================

    console.log(
        "\nStoring verification..."
    );

    console.log(
        "Image Hash:",
        imageHash
    );

    console.log(
        "Result:",
        result
    );


    const tx =
        await contract.storeVerification(
            imageHash,
            result
        );


    console.log(
        "\nTransaction sent:"
    );

    console.log(tx.hash);


    console.log(
        "\nWaiting for confirmation..."
    );


    await tx.wait();


    console.log(
        "✅ Transaction confirmed"
    );


    // ======================================
    // READ STORED DATA
    // ======================================

    const count =
        await contract.getVerificationCount();


    console.log(
        "\nTotal verifications:",
        count.toString()
    );


    const id =
        Number(count) - 1;


    const verification =
        await contract.getVerification(id);


    console.log(
        "\n======================================"
    );

    console.log(
        " STORED VERIFICATION"
    );

    console.log(
        "======================================"
    );


    console.log(
        "ID:",
        id
    );

    console.log(
        "Image Hash:",
        verification[0]
    );

    console.log(
        "Result:",
        verification[1]
    );

    console.log(
        "Timestamp:",
        verification[2].toString()
    );

    console.log(
        "Verifier:",
        verification[3]
    );

    console.log(
        "Transaction Hash:",
        tx.hash
    );


    console.log(
        "======================================"
    );

    console.log(
        "✅ BLOCKCHAIN VERIFICATION SUCCESSFUL"
    );

    console.log(
        "======================================"
    );
}


main().catch(
    (error) => {

        console.error(
            "\n❌ Error:"
        );

        console.error(error);

    }
);