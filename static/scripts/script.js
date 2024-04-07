document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file-input');
    const uploadProgress = document.getElementById('upload-progress');
    const progressBar = uploadProgress.querySelector('.progress-bar');

    fileInput.addEventListener('change', function() {
        const file = this.files[0];
        uploadFile(file);
    });

    function uploadFile(file) {
        const formData = new FormData();
        formData.append('file', file);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/upload', true);

        let uploadedBytes = 0;

        xhr.upload.onprogress = function(event) {
            if (event.lengthComputable) {
                uploadedBytes = event.loaded;
                const totalBytes = event.total;
                const progress = (uploadedBytes / totalBytes) * 100;
                progressBar.style.width = progress + '%';
                progressBar.setAttribute('aria-valuenow', progress);
                progressBar.textContent = Math.round(progress) + '%';
                uploadProgress.style.display = 'block';
            }
        };

        xhr.onload = function() {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                console.log('File uploaded successfully:', response.filename);
                uploadProgress.style.display = 'none';
            } else {
                console.error('Error uploading file:', xhr.statusText);
            }
        };

        xhr.onerror = function() {
            console.error('Error uploading file:', xhr.statusText);
        };

        xhr.send(formData);
    }
});