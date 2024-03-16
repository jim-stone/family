
export async function postData(url = '', data = {}) {
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