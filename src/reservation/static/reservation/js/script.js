montant = document.querySelector("#id_montant");
partiel = document.querySelector("#id_participation_partielle")
partiel.checked
    ? (montant.type="number")
    : (montant.type="hidden");

function toggleMontant(event) {
  montant = document.querySelector("#id_montant");
  console.log(event)
  event.target.checked
    ? (montant.type="number")
    : (montant.type="hidden");
}

