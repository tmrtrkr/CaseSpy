chrome.commands.onCommand.addListener((command) => {
  if (command === "triggerSendToApi") {
    fetch("http://localhost:5000/trigger-sendToApi")
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error("Error:", error));
  } else if (command === "takeShot1") {
    fetch("http://localhost:5000/take-shot1")
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error("Error:", error));
  } else if (command === "takeShot2") {
    fetch("http://localhost:5000/take-shot2")
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error("Error:", error));
  }
});
