
export async function postData(url = '', data = {}, method = "POST") {
    const csrf_token = getCookie('csrftoken')
    const response = await fetch(url, {
        method: method,
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


export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}