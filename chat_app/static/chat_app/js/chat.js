document.addEventListener("DOMContentLoaded", function () {
    // creating a websocket instance for bi-direction connection communication / long-live connection as chatSocket constant
    // ws:// is a websocket protocol prefix to create a connection over an unencrypted connection.
    const chatSocket = new WebSocket(
      "ws://" + window.location.host + "/ws/chat/{{ recipient_username }}/"
    );
    //  function gets executed whenever a new message (broadcasted message) is received, and the message data becomes available to e.data property.
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

    document
      .querySelector("#chat-input")
      .addEventListener("keyup", function (e) {
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
  });