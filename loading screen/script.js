const button = document.querySelector("#myButton");
const loadingScreen = document.querySelector("#loadingScreen");
const loadingText = document.querySelector("#loadingText");

button.addEventListener("click", function() {
  loadingScreen.style.display = "flex";
  loadingText.innerHTML = "Loading";
  let loadingDots = 0;
  let loadingInterval = setInterval(function() {
    loadingDots++;
    if (loadingDots >= 4) {
      loadingDots = 0;
    }
    loadingText.innerHTML = "Loading" + ".".repeat(loadingDots);
  }, 500);
  setTimeout(function() {
    loadingScreen.style.display = "none";
    clearInterval(loadingInterval);
  }, 5000);
});
