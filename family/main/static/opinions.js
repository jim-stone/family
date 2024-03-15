
const urlOpinions = '/api/opinions/about_member/'
const opinionsContainer = document.getElementById('opinionsContainer');
const memberId = location.href.split('/')[4]

const endPoint = urlOpinions + memberId;

async function fetchAboutMember(memberId) {
    let response = await fetch(endPoint);
    let opinions = response.json();
    return opinions;
}

fetchAboutMember(memberId).then(
    opinions => {
        opinions.forEach(opinion => {
            console.log(opinion);
            let newElement = document.createElement('div');
            let sign = opinion.value + 1 ? 'Plus' : 'Minus';
            let repr = `${sign} od ${opinion.member_source.name} za: ${opinion.comment}`;
            newElement.innerText = repr;
            opinionsContainer.appendChild(newElement);

        });
    }
)

console.log('???????????????')