from web3 import Web3
import os


# ==========================================
# FACECHAINVERIFY BLOCKCHAIN CONFIGURATION
# ==========================================

RPC_URL = "http://127.0.0.1:8545"

CONTRACT_ADDRESS = Web3.to_checksum_address(
    "0x7ced9bac2f4286f00c25b2ad84596b29036f4e34"
)


ABI = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_imageHash",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_result",
                "type": "string"
            }
        ],
        "name": "storeVerification",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_id",
                "type": "uint256"
            }
        ],
        "name": "getVerification",
        "outputs": [
            {
                "internalType": "string",
                "name": "imageHash",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "result",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "timestamp",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "verifier",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getVerificationCount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]


# ==========================================
# CONNECT TO GANACHE
# ==========================================

w3 = Web3(
    Web3.HTTPProvider(RPC_URL)
)


def check_connection():

    if not w3.is_connected():
        raise ConnectionError(
            "Could not connect to Ganache at "
            + RPC_URL
        )

    return True


# ==========================================
# GET WALLET
# ==========================================

def get_wallet():

    private_key = os.environ.get("PRIVATE_KEY")

    if not private_key:
        raise ValueError(
            "PRIVATE_KEY environment variable not found."
        )

    account = w3.eth.account.from_key(
        private_key
    )

    return account


# ==========================================
# CONNECT TO CONTRACT
# ==========================================

def get_contract():

    return w3.eth.contract(
        address=CONTRACT_ADDRESS,
        abi=ABI
    )


# ==========================================
# STORE VERIFICATION
# ==========================================

def store_verification(
    image_hash,
    result
):

    check_connection()

    account = get_wallet()

    contract = get_contract()

    print("\n======================================")
    print(" FACECHAINVERIFY BLOCKCHAIN")
    print("======================================")

    print(
        "Wallet:",
        account.address
    )

    print(
        "\nImage Hash:",
        image_hash
    )

    print(
        "Result:",
        result
    )

    # Get current nonce
    nonce = w3.eth.get_transaction_count(
        account.address
    )

    # Build transaction
    transaction = contract.functions.storeVerification(
        image_hash,
        result
    ).build_transaction(
        {
            "from": account.address,
            "nonce": nonce,
            "chainId": 1337,
            "gas": 300000,
            "gasPrice": w3.eth.gas_price
        }
    )

    # Sign transaction
    signed_transaction = account.sign_transaction(
        transaction
    )

    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(
        signed_transaction.raw_transaction
    )

    tx_hash_hex = tx_hash.hex()

    print(
        "\nTransaction sent:"
    )

    print(
        tx_hash_hex
    )

    print(
        "\nWaiting for confirmation..."
    )

    receipt = w3.eth.wait_for_transaction_receipt(
        tx_hash
    )

    print(
        "Transaction confirmed"
    )

    # Read total count
    count = contract.functions.getVerificationCount().call()

    # Latest verification ID
    verification_id = count - 1

    # Read stored verification
    verification = contract.functions.getVerification(
        verification_id
    ).call()

    print(
        "\nTotal verifications:",
        count
    )

    print(
        "\n======================================"
    )

    print(
        " STORED VERIFICATION"
    )

    print(
        "======================================"
    )

    print(
        "ID:",
        verification_id
    )

    print(
        "Image Hash:",
        verification[0]
    )

    print(
        "Result:",
        verification[1]
    )

    print(
        "Timestamp:",
        verification[2]
    )

    print(
        "Verifier:",
        verification[3]
    )

    print(
        "Transaction Hash:",
        tx_hash_hex
    )

    print(
        "======================================"
    )

    return {
        "blockchain_id": verification_id,
        "image_hash": verification[0],
        "result": verification[1],
        "timestamp": verification[2],
        "verifier": verification[3],
        "transaction": tx_hash_hex,
        "block_number": receipt.blockNumber
    }


# ==========================================
# TEST BLOCKCHAIN CONNECTION
# ==========================================

if __name__ == "__main__":

    try:

        check_connection()

        print(
            "✅ Connected to Ganache"
        )

        print(
            "Chain ID:",
            w3.eth.chain_id
        )

        account = get_wallet()

        print(
            "Wallet:",
            account.address
        )

        contract = get_contract()

        count = contract.functions.getVerificationCount().call()

        print(
            "Total verifications:",
            count
        )

        print(
            "\n✅ BLOCKCHAIN CONNECTION SUCCESSFUL"
        )

    except Exception as error:

        print(
            "\n❌ Blockchain Error:"
        )

        print(error)