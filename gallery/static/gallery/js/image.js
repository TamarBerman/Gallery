// JavaScript function to handle the download action
function downloadAllImages() {
  alert("Downloading all images");
  // You may need to adjust the URLs based on your actual URLs
  const tallImageUrl = "{{ imageDetails.tallImage.url }}";
  const landImageUrl = "{{ imageDetails.landImage.url }}";
  const squareImageUrl = "{{ imageDetails.squareImage.url }}";

  // Create a zip file
  const zip = new JSZip();

  // Fetch images and add them to the zip file
  Promise.all([
    fetch(tallImageUrl)
      .then((response) => response.blob())
      .then((blob) => zip.file("tall_image.jpg", blob)),
    fetch(landImageUrl)
      .then((response) => response.blob())
      .then((blob) => zip.file("landscape_image.jpg", blob)),
    fetch(squareImageUrl)
      .then((response) => response.blob())
      .then((blob) => zip.file("square_image.jpg", blob)),
  ]).then(() => {
    // Generate and initiate the download of the zip file
    zip.generateAsync({ type: "blob" }).then(function (content) {
      saveAs(content, "images.zip");
    });
  });
}

// Attach the download function to the button click event
document
  .getElementById("downloadAllButton")
  .addEventListener("click", downloadAllImages);


  const submitReviewForm=()=> {
    // Trigger the form submission
    document.getElementById('reviewForm').submit();
  }



  ////////////////////////////////

  function openUserModal(user) {
    // alert("in FUNC");
    // Use JavaScript to get the current review.user details
    var userDetails = getUserDetails(user.username);

    const displayModalDiv = document.getElementById('openModal');
    const displayButton = document.getElementById('displayButton');

    let element = document.createElement('div');
    element.innerHTML = `
      <div class="modal fade" tabindex="-1" role="dialog" id="firstModal">
        <div class="modal-dialog modal-dialog-centered modal-sm" role="document">
          <div class="modal-content">
            <div class="modal-body p-0 text-center">
              <div class="bg-info p-3 rounded">
                <div id="trophy" class="text-center d-inline-block fs-1 lh-1 p-4 rounded-circle bg-white">
                  <div class="trophy-content">
                    <h1 class="text-center">{{ user.username|first|upper }}</h1>
                  </div>
                </div>
              </div>
              <div class="mt-5 px-5">
                <h3>${user.username}</h3>
                <p class="my-2 pb-3">email: <strong>${user.email}</strong></p>
              </div>
            </div>
            <div class="text-center pb-2">
              <a href="{% if user.is_authenticated %}{% url 'chat_view' user.username%} {% else %}{% url 'login'%} {% endif %}" type="button" class="btn btn-primary px-4 rounded-pill">Go to Chat</a><br />
              <a class="btn btn-sm text-secondary" data-bs-dismiss="modal" aria-label="Close"><small>Skip</small></a>
            </div>
          </div>
        </div>
      </div>
    `;
    displayModalDiv.innerHTML = ''; // Clear previous content
    displayModalDiv.appendChild(element);
    displayButton.click();
  }

  // Function to fetch user details (you can replace this with your actual implementation)
  function getUserDetails(username) {
    // Implement logic to fetch user details based on the username
    // This is just a placeholder, replace it with your actual implementation
    return {
      username: username,
      email: 'user@example.com' // Replace with actual email
    };
  }



  $(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
  });