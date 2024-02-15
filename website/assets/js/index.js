// Added Lambda function and HTML for views
const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://2y6bsxtyoxgxcqz6bhhfeteghu0bfcdv.lambda-url.us-east-1.on.aws/ ");
    let data = await response.json();
    counter.innerHTML = `Views: ${data}`;
}
updateCounter();