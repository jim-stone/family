
const urlWishes = '/api/wishes/'
const wishesContainer = document.getElementById('wishesContainer');


const memberId = location.href.split('/')[4]
// const endPoint = urlWishes + memberId;




async function fetchAboutMember(memberId) {
    let response = await fetch(urlWishes);
    let wishes = response.json();
    return wishes;
}




fetchAboutMember(memberId).then(
    wishes => {
        const header = document.getElementById('header');
        header.innerText = `Życzenia familymembera nr ${memberId}`;
        wishes.forEach(wish => {
            console.log(wish);
            wishesContainer.appendChild(
                document.createTextNode(
                    `${wish.descriprion} *** `
                )
            );
        });
    }
);

