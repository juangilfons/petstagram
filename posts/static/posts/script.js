const dropArea = document.getElementById('drop-area');
const inputFile = document.getElementById('id_image');

inputFile.addEventListener('change', uploadImage);

function uploadImage() {
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    dropArea.style.backgroundImage = `url(${imgLink})`;
    dropArea.textContent = ""
}

dropArea.addEventListener('dragover', function(e){
    e.preventDefault();
});

dropArea.addEventListener('drop', function(e){
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadImage();
})