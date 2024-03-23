
const urlWishes = '/api/wishes/member/';
const wishesContainer = document.getElementById('wishesContainer');

const arr = location.href.split('/');
const memberId = arr[arr.length - 2];

const endPoint = urlWishes + memberId;
async function fetchAboutMember(memberId) {
    let response = await fetch(endPoint);
    let wishes = response.json();
    return wishes;
}


const wishCardTemplate = `<div class="card shadow p-3 mb-5 bg-body-tertiary rounded" style="width: 90%;" wishId="PlaceholderWishId">
    <div class="card-body">
        <div class="card-subtitle">PlaceholderWishDescription</div>
        <div>Status: PlaceholderWishStatus</div>
        <div>Utworzone: PlaceholderWishDate</div>
        <br>

        <div class="d-flex">
            <div class="p-2 flex-grow-1">
            <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bag-check-fill" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M10.5 3.5a2.5 2.5 0 0 0-5 0V4h5zm1 0V4H15v10a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V4h3.5v-.5a3.5 3.5 0 1 1 7 0m-.646 5.354a.5.5 0 0 0-.708-.708L7.5 10.793 6.354 9.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0z"/>
                </svg>
            </button>
            </div>
        <div class="p-2">
            <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
                </svg>
            </button>        
            </div>
        </div>

    </div>
        <br><br>
</div><br>`




fetchAboutMember(memberId).then(
    wishes => {
        const header = document.getElementById('header');


        if (wishes[0].owner_member) {
            header.innerText = `Życzenia: ${wishes[0].owner_member.name}`;
        }

        else if (wishes[0].owner_user.username) {
            header.innerText = `Życzenia: ${wishes[0].owner_user.username}`;
        }

        else {
            header.innerText = '';
            wishesContainer.appendChild(
                document.createTextNode(
                    'Ten użytkownik nie ma jeszcze zadnych życzeń'
                )
            );
        };


        wishes.forEach(wish => {
            console.log(wish);
            let newNode = document.createElement('div');
            let newNodeHTML = wishCardTemplate.replaceAll('PlaceholderWishId', wish.id);
            newNodeHTML = newNodeHTML.replaceAll('PlaceholderWishDescription', wish.descriprion);
            newNodeHTML = newNodeHTML.replaceAll('PlaceholderWishStatus', wish.status_value.toLowerCase());
            newNodeHTML = newNodeHTML.replaceAll(
                'PlaceholderWishDate',
                `${wish.created_on.substring(0, 11).replace('T', ' ')}`
            )
            newNode.innerHTML = newNodeHTML;
            wishesContainer.appendChild(newNode);
        });
    }
);

