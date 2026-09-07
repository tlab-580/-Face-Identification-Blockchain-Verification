const imageInput = document.getElementById("imageInput");

const fileName = document.getElementById("fileName");

const verifyForm = document.getElementById("verifyForm");

const verifyButton = document.getElementById("verifyButton");

const resultCard = document.getElementById("resultCard");


imageInput.addEventListener("change", function () {

    if (imageInput.files.length > 0) {

        fileName.textContent =
            imageInput.files[0].name;

    } else {

        fileName.textContent =
            "No image selected";

    }

});


verifyForm.addEventListener("submit", async function (event) {

    event.preventDefault();


    if (imageInput.files.length === 0) {

        alert("Please select an image.");

        return;

    }


    const formData = new FormData();

    formData.append(
        "image",
        imageInput.files[0]
    );


    verifyButton.disabled = true;

    verifyButton.textContent =
        "VERIFYING...";


    try {

        const response = await fetch(
            "/verify",
            {
                method: "POST",
                body: formData
            }
        );


        const data = await response.json();


        document.getElementById("status").textContent =
            data.status || "-";


        document.getElementById("candidates").textContent =
            data.candidates_checked || "-";


        document.getElementById("faceMatch").textContent =
            data.face_match || "-";


        document.getElementById("imageHash").textContent =
            data.image_hash || "-";


        document.getElementById("blockchainId").textContent =
            data.blockchain_id || "-";


        document.getElementById("transaction").textContent =
            data.transaction || "-";


        resultCard.style.display = "block";


    } catch (error) {

        console.error(error);

        alert(
            "Verification failed. Please check the Flask server."
        );

    }


    verifyButton.disabled = false;

    verifyButton.textContent =
        "VERIFY IMAGE";

});