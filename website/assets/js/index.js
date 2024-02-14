// Added Lambda function and HTML for views
const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://i5apjkjlhcq2v4cbtkeijtsrre0ahxps.lambda-url.us-east-1.on.aws/ ");
    let data = await response.json();
    counter.innerHTML = `Views: ${data}`;
}
updateCounter();