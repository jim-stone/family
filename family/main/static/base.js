import { postData } from "/static/common.js";

const urlLogin = '/login/'
const urlRegister = '/api/users/'
const loginButton = document.getElementById('loginButton');
const registerButton = document.getElementById('registerButton');

// async function postData(url = '', data = {}) {
//     const csrf_token = document.cookie.split('csrftoken=')[1]
//     const response = await fetch(url, {
//         method: "POST",
//         headers: {
//             'Accept': 'application/json',
//             'Content-Type': 'application/json',
//             "X-CSRFToken": csrf_token
//         },
//         body: JSON.stringify(data),
//         redirect: "follow"
//     })
//     return response.json();
// };



registerButton.addEventListener('click', e => {
    let f = document.getElementById('first_name').value;
    let l = document.getElementById('last_name').value;
    let email = document.getElementById('email').value;
    let u = document.getElementById('new-username').value;
    let p = document.getElementById('new-password').value;
    let pr = document.getElementById('new-password-repeat').value;
    let data = {
        "first_name": f,
        "last_name": l,
        "email": email,
        "username": u,
        "password": p
    };
    console.log(data);
    if (p != pr) {
        console.log(p, pr);
        window.alert("Wprowadzone hasła muszą być takie same.")
    }
    else {
        postData(urlRegister, data)
            .then(response => {
                console.log(response)
                window.alert("Użytkownik zarejestrowany. Możesz się zalogować.");
                location.reload(true);
            });
    }
});


loginButton.addEventListener('click', e => {
    let u = document.getElementById('username').value;
    let p = document.getElementById('password').value;
    console.log(u, p);
    console.log(document.cookie);
    let data = {
        "username": u,
        "password": p
    };
    console.log(data);
    postData(urlLogin, data)
        .then(() => {
            location.reload(true);
        });
});



