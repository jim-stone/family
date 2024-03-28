
const urlOpinions = '/api/opinions/about_member/'
const opinionsContainer = document.getElementById('opinionsContainer');

const arr = location.href.split('/');
const memberId = arr[arr.length - 2];

const endPoint = urlOpinions + memberId;
const header = document.getElementById('header')

async function fetchAboutMember(memberId) {
    let response = await fetch(endPoint);
    let opinions = response.json();
    return opinions;
}


fetchAboutMember(memberId).then(
    opinions => {
        console.log('ssss: ', sessionStorage);
        opinions.forEach(opinion => {
            header.innerText = `Opinie o ${opinion.member_target.name}`;
            let newElement = document.createElement('tr');
            let sign = opinion.value + 1 ? 'Plus' : 'Minus';
            let repr = `${sign} od ${opinion.member_source.name} 
            za: ${opinion.comment} 
            ${opinion.created_on.substring(0, 16).replace('T', ' ')}`;
            newElement.innerHTML = `<div class="${sign}">${repr}</div><br>`
            opinionsContainer.appendChild(newElement);
        });
    }
);


