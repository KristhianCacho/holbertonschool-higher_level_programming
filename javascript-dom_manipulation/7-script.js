document.addEventListener("DOMContentLoaded", function () {
  // Get a reference to the list_movies ul element
  const listMoviesUl = document.getElementById("list_movies");

  // Fetch data from the URL using the Fetch API
  fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then((response) => {
      // Check if the response status is OK (200)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      // Parse the JSON response
      return response.json();
    })
    .then((data) => {
      // Iterate over the movie objects and extract their titles
      data.results.forEach((movie) => {
        const movieTitle = movie.title;
        // Create a list item for each movie title and append it to the ul
        const listItem = document.createElement("li");
        listItem.textContent = movieTitle;
        listMoviesUl.appendChild(listItem);
      });
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
});
