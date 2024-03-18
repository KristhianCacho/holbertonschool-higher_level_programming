document.getElementById("red_header").addEventListener("click", addClassElement);

function addClassElement()
{
    const header = document.querySelector("header");
    header.classList.add("red");
}
