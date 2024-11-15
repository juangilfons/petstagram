// JavaScript for modal functionality
var modal = document.getElementById("postModal");
var span = document.getElementsByClassName("close")[0];

function openModal(postId ,imageSrc, caption, username, profilePicUrl, postTime, currentUser) {
    var modal = document.getElementById("postModal"); // Ensure this ID matches your modal's ID
    var modalImage = document.getElementById("modalImage");
    var modalCaption = document.getElementById("modalCaption");
    var modalUsername = document.getElementById("modalUsername");
    var modalProfilePic = document.getElementById("modalProfilePic");
    var modalPostTime = document.getElementById("modalPostTime");
    var modalDeleteBtn = document.getElementById("deleteForm");

    if (modal && modalImage && modalCaption) {
        modal.style.display = "block"; // Show the modal
        modalImage.src = imageSrc; // Set the image source
        modalCaption.innerHTML = '<b>' + username + ':</b> ' + caption;
        modalUsername.innerText = username;
        modalProfilePic.src = profilePicUrl;
        modalPostTime.innerText = postTime;

        if (currentUser === username) {
            modalDeleteBtn.style.display = "block";
            modalDeleteBtn.action = `/delete/${postId}/`
        }

        document.body.style.overflow = 'hidden';  // Disable scrolling
        document.body.style.backgroundColor = 'lightgray'
        document.getElementById('navbar').style.backgroundColor = 'lightgray';
    } else {
        console.error("Modal or elements not found");
    }
}

// Close the modal when clicking the close button
span.onclick = function() {
    modal.style.display = "none";
    document.body.style.overflow = 'auto';
    document.body.style.backgroundColor = 'white'
    document.getElementById('navbar').style.backgroundColor = 'rgba(255, 255, 255, 0.6)';
    document.getElementById("deleteForm").style.display = 'none';
}

// Close the modal when clicking outside of it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
        document.body.style.overflow = 'auto';
        document.body.style.backgroundColor = 'white'
        document.getElementById('navbar').style.backgroundColor = 'rgba(255, 255, 255, 0.6)';
        document.getElementById("deleteForm").style.display = 'none';
    }
}

function confirmDelete(event) {
    event.preventDefault();
    if (confirm("Are you sure you want to delete this post?")) {
        const form = document.getElementById("deleteForm");
        form.submit();
    }
}