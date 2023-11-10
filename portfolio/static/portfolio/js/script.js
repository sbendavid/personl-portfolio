// Get references to the overlay and buttons
document.addEventListener("DOMContentLoaded", function() {
    const contactOverlay = document.getElementById("contactOverlay");
    const openContactButton = document.getElementById("openContactButton");
    const closeContactButton = document.getElementById("closeContactButton");

    // Function to open the Contact Us form
    function openContactForm() {
        contactOverlay.style.display = "block";
    }

    // Function to close the Contact Us form
    function closeContactForm() {
        contactOverlay.style.display = "none";
    }

    // Event listeners for opening and closing the Contact Us form
    openContactButton.addEventListener("click", openContactForm);
    closeContactButton.addEventListener("click", closeContactForm);
});

const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})