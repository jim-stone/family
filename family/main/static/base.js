// import { postData } from "/static/common.js";

const urlLogin = '/login/'
const loginButton = document.getElementById('loginButton');

async function postData(url = '', data = {}) {
    const csrf_token = document.cookie.split('csrftoken=')[1]
    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "X-CSRFToken": csrf_token
        },
        body: JSON.stringify(data),
        redirect: "follow"
    })
    return response.json();
};



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
        .then(response => {
            console.log(response)
        });
});






