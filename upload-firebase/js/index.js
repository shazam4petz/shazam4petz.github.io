// save file to firebase storage
function previewFile() {
  var storage = firebase.storage();

  var file = document.getElementById("files").files[0];
  console.log(file);

  var storageRef = firebase.storage().ref();

  // dynamically set reference to the file name
  var thisRef = storageRef.child(file.name);

  // put request upload file to firebase storage
  thisRef.put(file).then(function(snapshot) {
    console.log('Uploaded a blob or file!');
  });

  // get request to get URL for uploaded file
  thisRef.getDownloadURL().then(function(url) {
    console.log(url);
  })

  // GET
  const Http = new XMLHttpRequest();
  Http.open("GET", url);
  Http.send();
  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
  }

  // POST
  var xhr = new XMLHttpRequest();
  xhr.open("POST", 'https://us-central1-hackher413-petid.cloudfunctions.net/function-1', true);
  xhr.send(JSON.stringify({
    url: url
  }), xhr.onreadystatechange = (e) => {
    console.log(xhr.responseText)
  });

}
