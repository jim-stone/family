
const urlOpinions = '/api/opinions/about_member/'
const urlMembers = '/api/members/';
const opinionsContainer = document.getElementById('opinionsContainer');

const arr = location.href.split('/');
const memberId = arr[arr.length - 2];

const endPoint = urlOpinions + memberId;
const memberEndPoint = urlMembers + memberId
const header = document.getElementById('header')
let PlusCounter = header.getElementsByClassName("badge")[0]
let MinusCounter = header.getElementsByClassName("badge")[1]


async function fetchAboutMember(memberId) {
    let response = await fetch(endPoint);
    let opinions = response.json();
    return opinions;
}

async function fetchMember() {
    let response = await fetch(memberEndPoint);
    let member = response.json();
    return member;
}



fetchAboutMember(memberId).then(
    opinions => {

        fetchMember().then(
            member => {
                header.innerText = `Opinie o ${member.name}   `;
                if (opinions) {
                    PlusCounter.classList.remove('hidden')
                    MinusCounter.classList.remove('hidden')
                    PlusCounter.innerHTML = opinions[0].plus_count
                    MinusCounter.innerHTML = opinions[0].minus_count
                    header.appendChild(PlusCounter)
                    header.appendChild(MinusCounter)
                }
            }
        );


        opinions.forEach(opinion => {


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


