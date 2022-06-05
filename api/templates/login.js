let video = document.querySelector('#video');
let submitButton = document.querySelector("#login-submit-button");
let username = document.querySelector("#username");
let password = document.querySelector("#password");


function prepareVideoInMarkup() {
    // TODO
}

submitButton.addEventListener('onclick', (ev) => {
    // prepare data
    const usernameValue = username.value;
    const passwordValue = password.value;
    const data = {
        'username': usernameValue,
        'password': passwordValue
    };

    // send request
    fetch("/login", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(res => console.log(res));
});