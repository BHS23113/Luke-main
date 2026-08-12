// ================= GOOGLE LOGIN =================

function handleCredentialResponse(response) {

    console.log("TOKEN:", response.credential);

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            credential: response.credential
        })
    })

    .then(res => res.json())

    .then(data => {

        console.log("SERVER RESPONSE:", data);

        if (data.status === "success") {

            window.location.href = data.redirect;

        }

        else {

            if (data.redirect) {

                window.location.href = data.redirect;

            }

            else {

                alert("Login failed");

            }

        }

    });

}


// ================= USERS PAGE =================

function openDeleteModal(id, name) {

    document.getElementById("deleteModal").style.display = "flex";

    document.getElementById("deleteName").textContent = name;

    document.getElementById("deleteForm").action = "/delete-user/" + id;

}


function closeDeleteModal() {

    document.getElementById("deleteModal").style.display = "none";

}


function openAddUserModal() {

    document.getElementById("addUserModal").style.display = "flex";

}


function closeAddUserModal() {

    document.getElementById("addUserModal").style.display = "none";

}


window.addEventListener("click", function(event) {

    const deleteModal = document.getElementById("deleteModal");
    const addUserModal = document.getElementById("addUserModal");

    if (deleteModal && event.target === deleteModal) {
        closeDeleteModal();
    }

    if (addUserModal && event.target === addUserModal) {
        closeAddUserModal();
    }

});