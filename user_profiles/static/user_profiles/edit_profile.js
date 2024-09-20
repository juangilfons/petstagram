    document.getElementById('id_profile_picture').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
    document.getElementById('profile-pic-display').src = e.target.result;
};

    if (file) {
    reader.readAsDataURL(file);
}
});