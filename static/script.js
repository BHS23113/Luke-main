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
            } else {
                alert("Login failed");
            }
        }
    });
}


// ---------- Delete User Modal ----------

function openDeleteModal(id, name) {

    document.getElementById("deleteModal").style.display = "flex";

    document.getElementById("deleteName").textContent = name;

    document.getElementById("deleteForm").action = "/delete-user/" + id;

}

function closeDeleteModal() {

    document.getElementById("deleteModal").style.display = "none";

}

window.onclick = function(event) {

    const modal = document.getElementById("deleteModal");

    if (event.target === modal) {
        closeDeleteModal();
    }

}