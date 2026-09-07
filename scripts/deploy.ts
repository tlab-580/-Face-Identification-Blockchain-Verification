import { network } from "hardhat";

async function main() {
  const { viem } = await network.connect();

  const faceChainVerify = await viem.deployContract("FaceChainVerify");

  console.log("======================================");
  console.log(" FaceChainVerify Deployment");
  console.log("======================================");
  console.log("Contract Address:", faceChainVerify.address);
  console.log("======================================");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});