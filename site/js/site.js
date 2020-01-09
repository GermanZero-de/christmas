var url = window.location.origin;
var plzInputId = "#Postleitzahl";
var displayResultsContainerId = "#data-container";
var formErrorClass = ".form-fail";

function clearDataContainer() {
  var container = document.querySelector(displayResultsContainerId);
  if (!container) {
    return;
  }
  container.innerHTML = '';
}

function clearError() {
  var errorMsg = document.querySelector(formErrorClass);
  if (errorMsg) {
    errorMsg.style.display = 'none';
  }
}

function onSuccess(data) {
  console.log(data);
  /** {
  "first_name": "Stefan",
  "last_name": "Liebich",
  "degree": null,
  "picture_url": "https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/users/stefanliebichwebseite_1.jpg",
  "party": "DIE LINKE"
  } */
  var container = document.querySelector(displayResultsContainerId);
  console.log(container);
  if (!container) {
    return;
  }
  var firstName =  data.first_name;
  var lastName = data.last_name;
  var fullName = '<div class="result-field result-field-name">'+ firstName + ' ' + lastName + '</div>';
  var degree = data.degree ? ('<div class="result-field result-field-degree">'+ data.degree+'</div>') : '';
  var party = '<div class="result-field result-field-party">'+ data.party+'</div>';
  const address = '<div class="result-field result-field-address">'+ 'Deutscher Bundestag <br> Platz der Republik 1 <br> 11011 Berlin'+'</div>';
  var picture = data.picture_url ? ('<div class="result-field result-field-picture"><img class="result-field-picture-img" src="'+data.picture_url+'"/></div>') : '';
  var content =  fullName + degree + party + address + picture;
  container.innerHTML = content;
  clearError();
}

function onError(err) {
  console.error(err);
  var errorMsg = document.querySelector(formErrorClass);
  if (errorMsg) {
    errorMsg.style.display = 'block';
    errorMsg.innerHTML = err.message;
  }
}

function getPostalCode() {
  var input = document.querySelector(plzInputId);
  if (input) {
    return input.value;
  }
}

async function onFormSubmit() {
  try {
    clearDataContainer();
    clearError();
    var postcode = getPostalCode();

    if (postcode) {
      var response = await fetch(url,
      {
        method: "post",
        headers: {
          "Content-type": "application/x-www-form-urlencoded"
        },
        body: "postcode="+postcode,
        mode: "cors",
      })

      if (response && response.ok) {
        try {
        var data = await response.json();
        onSuccess(data);
      } catch(e) {
        onError(new Error('Ungültige Postleitzahl'));
      }
      } else {
        onError(new Error('Invalid response'));
      }
    }
  } catch(e) {
    onError(e);
  }
}

