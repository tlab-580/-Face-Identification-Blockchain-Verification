# 🔐 FaceChainVerify

### Blockchain-Based Face Verification System

FaceChainVerify is a **face verification and blockchain-based record integrity system** that combines Artificial Intelligence, Computer Vision, and Blockchain technology.

The system accepts a face image from the user, compares it against a collection of candidate images using facial recognition, generates a **SHA-256 hash** of the uploaded image, and permanently records the verification result on a blockchain network.

---

## 🚀 Features

* 🧑‍💻 **Face Detection** using `face_recognition`
* 🔍 **Face Matching** against multiple candidate images
* 📊 **Verification Analysis** with face-distance scores
* 🔐 **SHA-256 Image Hashing**
* ⛓️ **Blockchain Verification Storage**
* 🌐 **Flask Web Interface**
* ⚡ **Ganache Local Blockchain**
* 🦊 **Hardhat Smart Contract Development**
* 📋 Displays blockchain transaction details
* 🆔 Generates a unique blockchain verification ID

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    │   Uploads Image     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Flask Web App    │
                    │      app.py         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Face Detection   │
                    │  face_recognition   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Face Matching    │
                    │  Compare with       │
                    │  Candidate Images   │
                    └──────────┬──────────┘
                               │
                     ┌─────────┴─────────┐
                     │                   │
                     ▼                   ▼
             ┌──────────────┐    ┌──────────────┐
             │  VERIFIED /  │    │   SHA-256    │
             │ NOT VERIFIED │    │    Hashing   │
             └──────────────┘    └──────┬───────┘
                                        │
                                        ▼
                              ┌──────────────────┐
                              │ Smart Contract   │
                              │   Blockchain     │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ Verification ID  │
                              │ Transaction Hash │
                              │ Timestamp        │
                              │ Verifier Address │
                              └──────────────────┘
```

---

## 🔄 How It Works

### 1. Upload Image

The user uploads a face image through the Flask web interface.

### 2. Face Detection

The system detects the face using the `face_recognition` Python library and generates a numerical **face encoding**.

### 3. Candidate Comparison

The uploaded face encoding is compared with the candidate images stored in:

```text
output/candidates/
```

The system calculates the face distance for every candidate.

The current matching threshold is:

```text
Face Distance < 0.50
```

If at least one candidate satisfies the threshold, the verification result becomes:

```text
VERIFIED
```

Otherwise:

```text
NOT_VERIFIED
```

### 4. SHA-256 Hash Generation

The uploaded image is hashed using the SHA-256 cryptographic hashing algorithm.

Example:

```text
dbe640dbad75fe650785b564125e23864b35948d0a88c19f4b17b1f9cbd6648c
```

The hash provides a unique digital representation of the uploaded file.

### 5. Blockchain Storage

The verification result and image hash are submitted to the `FaceChainVerify` smart contract.

The blockchain record contains:

* Verification ID
* Image Hash
* Verification Result
* Timestamp
* Verifier Wallet Address
* Transaction Hash

### 6. Result Display

The final result is displayed in the browser:

```text
Verification Result

Status: VERIFIED
Candidates Checked: 59
Face Match: YES
SHA-256: ...
Blockchain ID: ...
Transaction: ...
```

---

## 🛠️ Technologies Used

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| Python           | Backend and AI processing       |
| Flask            | Web application backend         |
| HTML             | Web interface                   |
| CSS              | User interface styling          |
| JavaScript       | Frontend interaction            |
| face_recognition | Face detection and matching     |
| OpenCV / dlib    | Computer vision dependencies    |
| SHA-256          | Image integrity hashing         |
| Solidity         | Smart contract development      |
| Hardhat          | Smart contract development      |
| Ganache          | Local blockchain network        |
| Web3.py          | Python-blockchain communication |
| Ethers.js        | Blockchain testing/interactions |
| Node.js          | Hardhat and JavaScript tooling  |

---

## 📁 Project Structure

```text
FaceChainVerify/
│
├── app.py
├── blockchain.py
├── requirements.txt
├── package.json
├── package-lock.json
├── hardhat.config.ts
├── tsconfig.json
├── README.md
├── .gitignore
│
├── contracts/
│   └── FaceChainVerify.sol
│
├── scripts/
│   ├── deploy.ts
│   └── send-op-tx.ts
│
├── blockchain/
│   ├── check_contract.cjs
│   ├── contract-address.txt
│   ├── test_connection.js
│   └── test_transaction.cjs
│
├── src/
│   ├── candidate_extractor.py
│   ├── download_candidates.py
│   ├── face_detector.py
│   ├── final_report.py
│   ├── hashing.py
│   ├── matcher.py
│   ├── run_facechainverify.py
│   ├── test_face.py
│   ├── test_match.py
│   ├── test_search.py
│   ├── verify_candidates.py
│   └── web_search.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

> **Note:** Face images, uploaded files, generated verification reports, virtual environments, and blockchain cache files are excluded from the Git repository for privacy and repository size considerations.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/FaceChainVerify.git
cd FaceChainVerify
```

---

## 2. Create a Python Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```cmd
venv\Scripts\activate
```

---

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

If Web3.py is not included in your requirements file:

```bash
pip install web3
```

---

## 4. Install Node.js Dependencies

```bash
npm install
```

---

# ⛓️ Blockchain Setup

FaceChainVerify currently uses a **local Ganache blockchain** for development and demonstration.

Start Ganache and make sure the RPC endpoint is:

```text
http://127.0.0.1:8545
```

The project uses:

```text
Chain ID: 1337
```

The deployed smart contract address used during development is:

```text
0x7ced9bac2f4286f00c25b2ad84596b29036f4e34
```

> For a new deployment, deploy the smart contract again and update the contract address in the relevant configuration files.

---

# 🔑 Environment Configuration

The blockchain integration requires a wallet private key.

Create a `.env` file:

```text
PRIVATE_KEY=YOUR_GANACHE_PRIVATE_KEY
```

**Never upload your private key to GitHub.**

The `.env` file should remain ignored by `.gitignore`.

---

# ▶️ Running the Application

### Step 1 — Start Ganache

Make sure Ganache is running.

### Step 2 — Start Flask

From the project directory:

```cmd
python app.py
```

You should see:

```text
FACECHAINVERIFY FLASK SERVER

Server: http://127.0.0.1:5000
```

### Step 3 — Open the Web Application

Open:

```text
http://127.0.0.1:5000
```

### Step 4 — Upload an Image

Choose a face image and click:

```text
VERIFY IMAGE
```

The system will:

```text
Upload Image
      ↓
Detect Face
      ↓
Generate Face Encoding
      ↓
Compare Candidates
      ↓
Generate SHA-256
      ↓
Store Result on Blockchain
      ↓
Display Verification Result
```

---

# 📊 Example Result

A successful verification can produce:

```text
Status: VERIFIED

Candidates Checked: 59

Face Match: YES

SHA-256:
dbe640dbad75fe650785b564125e23864b35948d0a88c19f4b17b1f9cbd6648c

Blockchain ID:
3

Transaction:
99d5341f8778b4bd351ab67669d71b628506e37f47d713ad83515c2fbe017c67
```

The same verification is also visible in the Flask terminal and recorded on the local blockchain.

---

# 🔐 Smart Contract

The `FaceChainVerify.sol` smart contract provides functions for storing and retrieving verification records.

### Store Verification

```solidity
storeVerification(
    string _imageHash,
    string _result
)
```

### Retrieve Verification

```solidity
getVerification(
    uint256 _id
)
```

### Get Verification Count

```solidity
getVerificationCount()
```

Each blockchain record contains:

```text
Verification ID
       │
       ├── Image Hash
       ├── Result
       ├── Timestamp
       └── Verifier Address
```

---

# 🎯 Project Objectives

The main objectives of FaceChainVerify are:

1. Automate face verification using AI.
2. Compare an uploaded face against multiple candidates.
3. Generate a cryptographic hash for the uploaded image.
4. Store verification records on a blockchain.
5. Provide tamper-resistant verification records.
6. Create a simple web interface for users.
7. Demonstrate the integration of AI and Blockchain technologies.

---

# 🌟 Advantages

### Artificial Intelligence

Automates face detection and matching instead of relying completely on manual verification.

### Cryptographic Hashing

SHA-256 creates a unique fingerprint of the uploaded image.

### Blockchain

Verification records are stored in a tamper-resistant distributed ledger.

### Transparency

The transaction hash and blockchain verification ID can be used to trace a verification record.

### Automation

The complete process can be performed through a web interface.

---

# 🔮 Future Enhancements

Future versions of FaceChainVerify can include:

* ☁️ Deployment on a public blockchain or testnet
* 📱 Mobile application
* 🔐 Stronger identity verification
* 🧠 Improved face recognition models
* 👥 Role-based access for administrators and verifiers
* 📊 Verification history dashboard
* 🔎 Blockchain verification explorer
* 🗄️ Secure cloud-based candidate database
* 🛡️ Encryption and privacy-preserving storage
* 📈 Analytics dashboard
* 🚀 Production deployment using Docker and cloud infrastructure

---

# ⚠️ Privacy & Security

Face recognition involves sensitive biometric information.

This prototype is intended for **educational, research, and demonstration purposes**.

For real-world deployment:

* Obtain appropriate user consent.
* Follow applicable privacy and data-protection laws.
* Avoid storing unnecessary biometric data.
* Encrypt sensitive information.
* Secure wallet credentials.
* Never expose private keys.
* Implement appropriate access controls.
* Use secure production infrastructure.

---

# 👩‍💻 Project

**FaceChainVerify**

### Domain

```text
Artificial Intelligence
Computer Vision
Blockchain
Web Development
Cybersecurity
```

### Project Type

```text
AI + Blockchain Integration
```

---

# 📜 License

This project is intended for educational and research purposes.

You may add an appropriate open-source license such as MIT License if you decide to make the project fully open source.

---

## ⭐ Acknowledgement

This project demonstrates how **Artificial Intelligence, Computer Vision, Cryptographic Hashing, and Blockchain** can be combined to create a verifiable digital identity/face verification workflow.

If you find this project useful, consider giving the repository a ⭐.

