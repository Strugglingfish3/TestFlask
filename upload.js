var myFormData = new FormData();
myFormData.append('pictureFile', pictureInput.files[0]);

fetch('/upload-endpoint', {
  method: 'POST',
  body: myFormData
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error))
