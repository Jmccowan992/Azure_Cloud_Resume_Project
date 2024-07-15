const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://jrmcccloudapi.azurewebsites.net/api/http_trigger?");
    let data = await response.json();
    counter.innerHTML = ` Views: ${data}`;
}

updateCounter();