document.addEventListener("DOMContentLoaded", function () {
  // Get a reference to the character div element
  const characterDiv = document.getElementById("character");

  // Fetch data from the URL using the Fetch API
  fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then((response) => {
      // Check if the response status is OK (200)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      // Parse the JSON response
      return response.json();
    })
    .then((data) => {
      // Extract the character name from the data
      const characterName = data.name;
      // Display the character name in the character div
      characterDiv.textContent = `Character Name: ${characterName}`;
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
});
