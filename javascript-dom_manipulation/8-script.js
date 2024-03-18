document.addEventListener("DOMContentLoaded", function () {
  // Get a reference to the hello div element
  const helloDiv = document.getElementById("hello");

  // Fetch data from the URL using the Fetch API
  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => {
      // Check if the response status is OK (200)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      // Parse the response text as JSON
      return response.json();
    })
    .then((data) => {
      // Extract the translation of "hello" from the data
      const helloTranslation = data.hello;
      // Display the translation in the hello div
      helloDiv.textContent = helloTranslation;
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
});
