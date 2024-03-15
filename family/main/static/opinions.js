
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
        console.log(opinions);
    }
)

console.log('???????????????')