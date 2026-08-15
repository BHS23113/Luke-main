// GOOGLE LOGIN 

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

        } else {

            if (data.redirect) {

                window.location.href = data.redirect;

            } else {

                alert("Login failed");

            }

        }

    });

}


// DELETE USER 

function openDeleteModal(id, name) {

    document.getElementById("deleteModal").style.display = "flex";

    document.getElementById("deleteName").textContent = name;

    document.getElementById("deleteForm").action = "/delete-user/" + id;

}


function closeDeleteModal() {

    document.getElementById("deleteModal").style.display = "none";

}


// ADD USER 

function openAddUserModal() {

    document.getElementById("addUserModal").style.display = "flex";

}


function closeAddUserModal() {

    document.getElementById("addUserModal").style.display = "none";

}


// EDIT ROLE

function openRoleModal(id, name, role) {

    document.getElementById("roleModal").style.display = "flex";

    document.getElementById("roleName").textContent = name;

    document.getElementById("roleSelect").value = role;

    document.getElementById("roleForm").action = "/edit-role/" + id;

}


function closeRoleModal() {

    document.getElementById("roleModal").style.display = "none";

}


// CLOSE MODALS  

window.addEventListener("click", function(event) {

    const deleteModal = document.getElementById("deleteModal");

    const addUserModal = document.getElementById("addUserModal");

    const roleModal = document.getElementById("roleModal");


    if (deleteModal && event.target === deleteModal) {

        closeDeleteModal();

    }


    if (addUserModal && event.target === addUserModal) {

        closeAddUserModal();

    }


    if (roleModal && event.target === roleModal) {

        closeRoleModal();

    }

});

// ADD NOTICE

function openAddNoticeModal() {

    document.getElementById("addNoticeModal").style.display = "flex";

}

function closeAddNoticeModal() {

    document.getElementById("addNoticeModal").style.display = "none";

}