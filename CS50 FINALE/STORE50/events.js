//layout events
let navBtn = document.querySelector("#select-display");
let navOptions = document.querySelector(".display-option");

navBtn.addEventListener("click", () => {
    navOptions.classList.toggle("hidden");
});
