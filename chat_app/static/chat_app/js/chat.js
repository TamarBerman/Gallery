document.addEventListener('DOMContentLoaded', function () {

    const chatSocket = new WebSocket(
      "ws://" + window.location.host + "/ws/chat/{{ recipient_username }}/"
    );

    chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      const message = data["message"];
      const sender = data["sender"];
      const chatBox = document.getElementById("chat-box");
      const messageElement = document.createElement("div");
      const messageContent = document.createElement("span");
      const messageSender = document.createElement("p");

      if (sender === "{{ request.user.username }}") {
        messageElement.classList.add("mb-2", "flex", "justify-end");
        messageElement.innerHTML = `
          <div>
          <div class="fw-bold mb-1" style="
          text-align: end;  "> you 😊</div>
              <div class="flex-shrink-1 bg-primary bg-gradient
              rounded py-2 px-3 ml-3">
                  ${message}
              </div>
          </div>
          `;
      } else {
        messageElement.classList.add("mb-2", "flex", "justify-start");
        messageElement.innerHTML = `
          <div>
          <div class="fw-bold mb-1">
      ${sender}

          </div>
              <div class="flex-shrink-1 bg-gray-300 rounded py-2 px-3 ml-3" style="ackground-color: lightgray">
                  ${message}
              </div>
          </div>
          `;
      }

      // Append the message element to the chat box
      chatBox.appendChild(messageElement);
      chatBox.scrollTop = chatBox.scrollHeight;
    };

    document.querySelector("#chat-input").addEventListener("keyup", function (e) {
      if (e.key === "Enter") {
        const messageInput = document.querySelector("#chat-input");
        const message = messageInput.value;
        chatSocket.send(
          JSON.stringify({
            message: message,
          })
        );
        messageInput.value = "";
      }
    });

  // ... (previous code)

  // users details
  document.addEventListener("click", function (event) {
    if (event.target.classList.contains("sender-name")) {
        event.preventDefault();
        const senderUsername = event.target.textContent.trim();
        alert("senderUsername: " + senderUsername);
        // Call the view to get user details
        fetch(`/user_detail/${senderUsername}/`)
            .then((response) => {
                if (!response.ok) {
                    if (response.status === 404) {
                        throw new Error("User not found");
                    } else {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                }
                return response.json();
            })
            .then((userDetails) => {
                console.log("Received user details:", userDetails);

                // Dynamically include the user detail template
                const userDetailContainer = document.getElementById(
                    "user-detail-container"
                );
                userDetailContainer.innerHTML = `
                        <h2>User Details</h2>
                        <p><strong>Username:</strong> ${userDetails.username}</p>
                        <p><strong>Email:</strong> ${userDetails.email}</p>
                        <!-- Add other user details as needed -->
                    `;

                // Update the content of the static modal
                const modalBody = document.getElementById("modal-body");
                modalBody.innerHTML = `
                        <div class="bg-info p-3 rounded">
                            <div id="trophy" class="text-center d-inline-block fs-1 lh-1 p-4 rounded-circle bg-white">
                                <div class="trophy-content">
                                    <h1 class="text-center">${userDetails.username
                                        .charAt(0)
                                        .toUpperCase()}</h1>
                                </div>
                            </div>
                        </div>
                        <div class="mt-5 px-5">
                            <h3>${userDetails.username}</h3>
                            <p class="my-2 pb-3">email: <strong>${
                                userDetails.email
                            }</strong></p>
                        </div>
                    `;

                // Show the Bootstrap modal
                const firstModal = new bootstrap.Modal(
                    document.getElementById("firstModal")
                );
                firstModal.show();
                // Optionally, show a modal or toggle visibility of the user details
                // based on your UI/UX requirements
            })
            .catch((error) => {
                console.error("Error fetching user details:", error);
            });
    }
  });
  });
    // ... (remaining code)