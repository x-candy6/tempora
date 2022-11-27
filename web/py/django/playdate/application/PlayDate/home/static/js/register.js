/* register.js - Requires DEFER
*   Contains the javascript necessary for the registration
*   page. All that is required is validation.
*
*   We validate the following fields:
*   - Username:
*       Required, 150 characters or less. Letters, digits, @, ., +, -, _ allowed
*   - Email:
*       Required, must be of format []#[].[]
*   - Password: 
*       Required, 8 characters at least, not all numeric   
*   - PW Confirmation:
*       Must match the previous password.
*/

// username
// Required
// <= 150 characters
// Letters, Digits, and + - . @ _
username = document.getElementById("id_username");
username.pattern = "[0-9a-zA-Z@.+_-]*";
username.addEventListener("input", (event) => {
    if (username.validity.valueMissing) {
        username.setCustomValidity("A username is required.");
        username.reportValidity();
    } else if(username.validity.tooLong) {
        password.setCustomValidity("Your username must be 150 characters or less.");
        username.reportValidity();
    } else if (username.validity.patternMismatch) {
        username.setCustomValidity("The username must consist of letters, digits, +, -, ., @, and _.");
        username.reportValidity();
    } else {
        username.setCustomValidity("");
    }
});

// Email
// Required
// Format: []@[].[]
email = document.getElementById("id_email");
email.required = true;
email.pattern = ".*[@].*[.].*";
email.addEventListener("input", (event) => {
    if (email.validity.typeMismatch || email.validity.patternMismatch) {
        email.setCustomValidity("Please enter a valid e-mail address.");
        email.reportValidity();
    } else {
        email.setCustomValidity("");
    }
});

// Password
// Required
// At least 8 characters
// Not just numbers
password = document.getElementById("id_password1");
password.minLength = 8;
password.pattern = ".*[^0-9].*";
password.addEventListener("input", (event) => {
    password.setCustomValidity("");
    if (password.validity.valueMissing) {
        password.setCustomValidity("A password is required.");
        password.reportValidity();
    } else if (password.validity.patternMismatch) {
        password.setCustomValidity("The password must not consist only of digits.");
        password.reportValidity();
    } else if(password.validity.tooShort) {
        password.setCustomValidity("Your password must be 8 characters or more.");
        password.reportValidity();
    } else {
        password.setCustomValidity("");
    }
});

// Confirmation
// Must match password
confirmPW = document.getElementById("id_password2");
confirmPW.addEventListener("input", (event) => {
    if (password.value !== confirmPW.value) {
        confirmPW.setCustomValidity("Please repeat the password you created above.");
        confirmPW.reportValidity();
    } else {
        confirmPW.setCustomValidity("");
    }
});
confirmPW.previousElementSibling.textContent = "Re-enter password: ";