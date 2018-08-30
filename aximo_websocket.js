
var wsUrl = "ws://127.0.0.1:5678/"
var ws = new WebSocket(wsUrl)

// When the connection is open, send some data to the server
ws.onopen = function() {
  ws.send("ping"); // Send the message 'Ping' to the server
};

// Log errors
ws.onerror = function (error) {
  console.log('WebSocket Error ' + error);
};

// Log messages from the server
ws.onmessage = function (e) {
  console.log('Server: ' + e.data);
};