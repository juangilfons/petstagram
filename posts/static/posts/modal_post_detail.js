// JavaScript for modal functionality
var modal = document.getElementById("postModal");
var span = document.getElementsByClassName("close")[0];

function openModal(imageSrc, caption) {
    var modal = document.getElementById("postModal"); // Ensure this ID matches your modal's ID
    var modalImage = document.getElementById("modalImage");
    var modalCaption = document.getElementById("modalCaption");

    if (modal && modalImage && modalCaption) {
        modal.style.display = "block"; // Show the modal
        modalImage.src = imageSrc; // Set the image source
        modalCaption.innerText = caption; // Set the caption
    } else {
        console.error("Modal or elements not found");
    }
}

// Close the modal when clicking the close button
span.onclick = function() {
    modal.style.display = "none";
}

// Close the modal when clicking outside of it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}