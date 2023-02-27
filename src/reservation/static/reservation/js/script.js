partial = document.querySelector("#id_participation_partielle");
partial.addEventListener("change", toggleMontant);

function toggleMontant(event) {
  montant = document.querySelector("#id_montant");
  montantContainer = document.querySelector("#montant__container");
  montant.disabled = !event.target.checked;
  event.target.checked
    ? (montantContainer.disabled = false)
    : (montantContainer.disabled = true);
  event.target.checked
    ? (montantContainer.style.display = "block")
    : (montantContainer.style.display = "none");
}

function isFormHtml5Valid(form) {
  for (var item of form.querySelectorAll("input,textarea,select")) {
    if (!item.checkValidity()) return false;
  }
  return true;
}
mySubmitButton = document.querySelector('button[type="submit"]');

mySubmitButton.onclick = function () {
  if (this.form && isFormHtml5Valid(this.form)) this.disabled = true;
  this.form.submit();
};
