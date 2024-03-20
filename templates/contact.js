function handleFormSubmit(event) {
    event.preventDefault();
    
    var name = document.getElementById("name").value.trim();
    var email = document.getElementById("email").value.trim();
    
    if (name === "" || email === "") {
        alert("Please fill in all required fields");
    } else {
        alert("Form submitted successfully!");
        document.getElementById("submitForm").reset();
    }
}

document.getElementById("submitForm").addEventListener("submit", handleFormSubmit);


