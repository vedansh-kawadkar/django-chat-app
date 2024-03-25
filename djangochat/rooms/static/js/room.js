/////////////////----Room desc modal ----/////////////////// 

var modal = document.getElementById("about-room-modal");
var groupinfo = document.getElementById("icon1");
var plist = document.getElementById("icon2");
var span = document.getElementsByClassName("close")[0];
var modal2 = document.getElementById("participants-modal");

groupinfo.onclick = function() {
    modal.style.display = "block";
}

plist.onclick = function() {
    modal2.style.display = "block";
}


span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(e) {
    if(e.target==modal) {
        modal.style.display = "none";
        }
    
    if(e.target==modal2){
        modal2.style.display = 'none';
    }
}

/////////////////----Chat Web Socket----/////////////////// 

const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);
const expiry = JSON.parse(document.getElementById('json-expiry').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + roomName
    + '/'
);


chatSocket.onmessage = function(e) {
    console.log('onmessage')
    console.log(expiry)
    const data = JSON.parse(e.data);
    if(data.message){

        let hm = '<div class="chat-message-box"><div class="chat-user-icon"><i class="fa fa-user-circle" aria-hidden="true" id="user-icon"></i></div><div class="chat-msg"><p class="font-semibold">'+data.username+'</p><p id="chat-message">'+data.message+'</p></div></div>';


        console.log(hm)
        document.querySelector("#chat-messages").innerHTML+=hm;

        scrollToBottom()

    }
    else{
        alert("Please type something!")
    }

};

chatSocket.onclose = function(e) {
    console.log('onclosed')
};

document.querySelector('#chat-msg-send').onclick = function(e){
        e.preventDefault();

        const messageInputDom = document.querySelector("#chat-msg-input");
        const message = messageInputDom.value;

        chatSocket.send(JSON.stringify({
            "message":message,
            "username":userName,
            "room":roomName
        }));

        messageInputDom.value = "";

        return false;
    };

function scrollToBottom(){
    const objDiv = document.querySelector("#chat-messages");
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom()

///////////-----Add participant to list-----///////////////////////

document.addEventListener('DOMContentLoaded', function() {
    const addParticipantBtn = document.getElementById('add-participant-btn');
    const participantsList = document.getElementById('participants-list');

    addParticipantBtn.addEventListener('click', function() {
        // Simulate adding a participant (you can replace this with your actual API call)
        // This is a sample API call using Fetch API
        fetch('room/'+''+'/add_participant/', {
            method: 'POST',
            // Add any required headers and body data
        })
        .then(response => {
            if (response.ok) {
                // If the API call was successful, add the participant to the list
                return response.json(); // assuming API returns participant data
            } else {
                throw new Error('Failed to add participant');
            }
        })
        .then(data => {
            // Create a new list item element for the participant
            const participantItem = document.createElement('li');
            participantItem.textContent = data.name; // Assuming 'name' is the property returned by your API
            participantsList.appendChild(participantItem);
        })
        .catch(error => {
            console.error('Error adding participant:', error);
            // Handle error
        });
    });
});
