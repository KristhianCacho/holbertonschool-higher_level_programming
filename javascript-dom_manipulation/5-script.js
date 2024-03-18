document.getElementById("update_header").addEventListener("click", updateHeader);

function updateHeader()
{
    const header = document.querySelector("header");
    header.textContent = "New Header!!!";
}
