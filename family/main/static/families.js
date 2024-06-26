import { postData } from "/static/common.js";

const urlFamilies = '/api/families/'
const urlOpinions = '/api/opinions/'
const membersContainer = document.getElementById('membersContainer')

const memberCardTemplate = `<div class="card" style="width: 10rem;" id="PlaceholderMemberId">
    <div class="card-body">
        <div class="card-subtitle">PlaceholderMemberName</div>
        <br>
        <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle"
                viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16" />
                <path
                    d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4" />
            </svg>
        </button>
        <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#exampleModal">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-dash-circle"
                viewBox="0 0 16 16">
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16" />
                <path d="M4 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 4 8" />
            </svg>
        </button>
        <br><br>
        <p><a href="/opinions/PlaceholderMemberId" class="opinionsLink">Lista ocen</a></p>
        <p><a href="/wishes/PlaceholderMemberId" class="wishesLink">Lista życzeń</a></p>



<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Ocena</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
      <div class="input-group input-group-lg">
      <span class="input-group-text" id="inputGroup-sizing-lg">Za co: </span>
      <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
    </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Anuluj</button>
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Dodaj</button>
      </div>
    </div>
  </div>
</div>

    </div>
</div>`


async function fetchFamilies() {
  let response = await fetch(urlFamilies);
  let families = response.json()
  return families;
}


fetchFamilies().then(families => {

  if (families == '') {
    const msg = "Jesteś niezalogowany lub nie należysz jeszcze do żadnej rodziny.";
    let newNode = document.createElement('div');
    newNode.innerText = msg;
    membersContainer.appendChild(newNode);
  }

  else {
    let firstFamily = families[0];
    let members = firstFamily.members;
    let addAssessment = function () { }
    let cancelAssessment = function () { }

    members.forEach(element => {
      let newNode = document.createElement('div');
      let newNodeHTML = memberCardTemplate.replaceAll('PlaceholderMemberName', element.name);
      newNodeHTML = newNodeHTML.replaceAll('PlaceholderMemberId', element.id);
      newNode.innerHTML = newNodeHTML;
      let opinionsLink = newNode.getElementsByClassName("opinionsLink")
      membersContainer.appendChild(newNode)
      let plusButton = newNode.getElementsByClassName("btn")[0]
      let minusButton = newNode.getElementsByClassName("btn")[1]


      plusButton.addEventListener('click', function (e) {
        let modal = document.getElementById("exampleModal")
        modal.dataset.memberId = element.id
        modal.dataset.value = 1

        let modalTitle = modal.getElementsByClassName("modal-title")[0]
        modalTitle.innerHTML = `Plus dla ${element.name}`
        modalTitle.style.color = "green"

        let modalSaveButton = modal.getElementsByClassName("btn")[1]
        let modalCancelButton = modal.getElementsByClassName("btn")[0]

        modalSaveButton.addEventListener('click', addAssessment = function (e) {
          // cleaning before
          modalSaveButton.removeEventListener('click', addAssessment);
          modalCancelButton.removeEventListener('click', cancelAssessment);
          // proper function
          let data = {
            "member_target": modal.dataset.memberId,
            "value": modal.dataset.value,
            "comment": modal.getElementsByClassName("form-control")[0].value
          };
          let url = urlOpinions;
          postData(url = urlOpinions, data = data).then(response => {
            if (
              response.detail == "Authentication credentials were not provided."
            ) {
              window.alert("Przed tą czynnością musisz się zalogować")
            };
          });
          //cleaning after
          modal.getElementsByClassName("form-control")[0].value = null;
        });

        modalCancelButton.addEventListener('click', cancelAssessment = function (e) {
          // cleaning before
          modalSaveButton.removeEventListener('click', addAssessment);
          modalCancelButton.removeEventListener('click', cancelAssessment);
          // proper function
          console.log('Assessment cancelled');
          //cleaning after
          modal.getElementsByClassName("form-control")[0].value = null;
        });

      })

      minusButton.addEventListener('click', function (e) {
        let modal = document.getElementById("exampleModal")
        modal.dataset.memberId = element.id
        modal.dataset.value = -1

        let modalTitle = modal.getElementsByClassName("modal-title")[0]
        modalTitle.innerHTML = `Minus dla ${element.name}`
        modalTitle.style.color = "red"

        let modalSaveButton = modal.getElementsByClassName("btn")[1]
        let modalCancelButton = modal.getElementsByClassName("btn")[0]

        modalSaveButton.addEventListener('click', addAssessment = function (e) {
          // cleaning before
          modalSaveButton.removeEventListener('click', addAssessment);
          modalCancelButton.removeEventListener('click', cancelAssessment);
          // proper function
          let data = {
            "member_target": modal.dataset.memberId,
            "value": modal.dataset.value,
            "comment": modal.getElementsByClassName("form-control")[0].value
          };
          let url = urlOpinions;
          postData(url = urlOpinions, data = data).then(response => {
            if (
              response.detail == "Authentication credentials were not provided."
            ) {
              window.alert("Przed tą czynnością musisz się zalogować")
            };
          });
          //cleaning after
          modal.getElementsByClassName("form-control")[0].value = null;
        });

        modalCancelButton.addEventListener('click', cancelAssessment = function (e) {
          // cleaning before
          modalSaveButton.removeEventListener('click', addAssessment);
          modalCancelButton.removeEventListener('click', cancelAssessment);
          // proper function
          console.log('Assessment cancelled');
          //cleaning after
          modal.getElementsByClassName("form-control")[0].value = null;
        });

      })

    });
  }
})














