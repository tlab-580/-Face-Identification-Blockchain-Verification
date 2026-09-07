const { ethers } = require("ethers");

const CONTRACT_ADDRESS =
    "0x7ced9bac2f4286f00c25b2ad84596b29036f4e34";

async function main() {

    const provider = new ethers.JsonRpcProvider(
        "http://127.0.0.1:8545"
    );

    const code = await provider.getCode(CONTRACT_ADDRESS);

    console.log("======================================");
    console.log(" FACECHAINVERIFY CONTRACT TEST");
    console.log("======================================");

    console.log("Contract Address:");
    console.log(CONTRACT_ADDRESS);

    if (code === "0x") {

        console.log("❌ Contract NOT found");

    } else {

        console.log("✅ Contract found on blockchain");
        console.log("Bytecode length:", code.length);

    }

    console.log("======================================");
}

main().catch((error) => {

    console.error("❌ Error:");
    console.error(error);

});