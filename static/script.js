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

    const addDutyModal = document.getElementById("addDutyModal");
    const deleteDutyModal = document.getElementById("deleteDutyModal");


    if (deleteModal && event.target === deleteModal) {
        closeDeleteModal();
    }


    if (addUserModal && event.target === addUserModal) {
        closeAddUserModal();
    }


    if (roleModal && event.target === roleModal) {
        closeRoleModal();
    }


    if (addDutyModal && event.target === addDutyModal) {
        closeAddDutyModal();
    }


    if (deleteDutyModal && event.target === deleteDutyModal) {
        closeDeleteDutyModal();
    }

});

// ADD NOTICE

function openAddNoticeModal() {

    document.getElementById("addNoticeModal").style.display = "flex";

}

function closeAddNoticeModal() {

    document.getElementById("addNoticeModal").style.display = "none";

}

// DELETE NOTICE

function openDeleteNoticeModal(id, title) {

    document.getElementById("deleteNoticeModal").style.display = "flex";

    document.getElementById("deleteNoticeTitle").textContent = title;

    document.getElementById("deleteNoticeForm").action =
        "/delete-notice/" + id;

}


function closeDeleteNoticeModal() {

    document.getElementById("deleteNoticeModal").style.display = "none";

}

//  NOTICE LINE LIMIT 

const noticeTextarea = document.querySelector(
    '#addNoticeModal textarea[name="content"]'
);

if (noticeTextarea) {

    noticeTextarea.addEventListener("input", function () {

        const maxLines = 8;

        const lines = this.value.split("\n");

        if (lines.length > maxLines) {

            this.value = lines.slice(0, maxLines).join("\n");

        }

    });

}


// ADD LOCKER DUTY MODAL

function openAddDutyModal() {
    document.getElementById("addDutyModal").style.display = "flex";
}

function closeAddDutyModal() {
    document.getElementById("addDutyModal").style.display = "none";
}

// DELETE LOCKER DUTY MODAL

function openDeleteDutyModal(dutyId, name) {

    document.getElementById("deleteDutyName").textContent = name;

    document.getElementById("deleteDutyForm").action =
        "/delete-locker-duty/" + dutyId;

    document.getElementById("deleteDutyModal").style.display = "flex";
}


function closeDeleteDutyModal() {

    document.getElementById("deleteDutyModal").style.display = "none";
}

console.log("LOCKER DUTY DELETE JS LOADED");

function openDeleteDutyModal(dutyId, name) {

    console.log("DELETE BUTTON CLICKED");
    console.log("Duty ID:", dutyId);
    console.log("Name:", name);

    document.getElementById("deleteDutyName").textContent = name;

    document.getElementById("deleteDutyForm").action =
        "/delete-locker-duty/" + dutyId;

    document.getElementById("deleteDutyModal").style.display = "flex";
}

function closeDeleteDutyModal() {

    document.getElementById("deleteDutyModal").style.display = "none";
}