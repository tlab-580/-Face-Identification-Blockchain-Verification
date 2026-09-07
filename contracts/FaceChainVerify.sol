// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FaceChainVerify {

    struct Verification {
        string imageHash;
        string result;
        uint256 timestamp;
        address verifier;
    }

    Verification[] private verifications;

    event VerificationStored(
        uint256 indexed id,
        string imageHash,
        string result,
        uint256 timestamp,
        address verifier
    );

    function storeVerification(
        string memory _imageHash,
        string memory _result
    ) public returns (uint256) {

        verifications.push(
            Verification({
                imageHash: _imageHash,
                result: _result,
                timestamp: block.timestamp,
                verifier: msg.sender
            })
        );

        uint256 id = verifications.length - 1;

        emit VerificationStored(
            id,
            _imageHash,
            _result,
            block.timestamp,
            msg.sender
        );

        return id;
    }

    function getVerification(
        uint256 _id
    )
        public
        view
        returns (
            string memory imageHash,
            string memory result,
            uint256 timestamp,
            address verifier
        )
    {
        require(_id < verifications.length, "Verification not found");

        Verification memory v = verifications[_id];

        return (
            v.imageHash,
            v.result,
            v.timestamp,
            v.verifier
        );
    }

    function getVerificationCount()
        public
        view
        returns (uint256)
    {
        return verifications.length;
    }
}