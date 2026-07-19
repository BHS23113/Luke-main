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