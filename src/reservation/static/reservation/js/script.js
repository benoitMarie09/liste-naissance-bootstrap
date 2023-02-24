partial = document.querySelector('#id_participation_partielle')
partial.addEventListener('change', toggleMontant)

function toggleMontant(event){
    montant = document.querySelector('#id_montant')
    montantContainer = document.querySelector('#montant__container')
    montant.disabled = !event.target.checked  
    event.target.checked ? montantContainer.style.display = "block" : montantContainer.style.display = "none"
}