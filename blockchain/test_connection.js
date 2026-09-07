const { ethers } = require("ethers");

async function main() {
    const provider = new ethers.JsonRpcProvider(
        "http://127.0.0.1:8545"
    );

    const network = await provider.getNetwork();

    console.log("=================================");
    console.log(" BLOCKCHAIN CONNECTION TEST");
    console.log("=================================");

    console.log("Chain ID:", network.chainId.toString());

    const blockNumber = await provider.getBlockNumber();

    console.log("Latest Block:", blockNumber);
    console.log("RPC:", "http://127.0.0.1:8545");

    console.log("=================================");
    console.log(" CONNECTION SUCCESSFUL");
    console.log("=================================");
}

main().catch((error) => {
    console.error("Connection failed:");
    console.error(error);
});