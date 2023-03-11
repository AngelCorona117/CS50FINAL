//layout events (nav Bar)
let navBtn = document.querySelector("#select-display");
let navOptions = document.querySelector(".display-option");

navBtn.addEventListener("click", () => {
    navOptions.classList.toggle("hidden");
});

//dev mode events
//select every input
let inputs = document.querySelectorAll(".dev-input");
//select form
let form = document.querySelector("#form");
form.addEventListener("submit", (event) => {
    event.preventDefault();
    //for every input create a new item and display them
    for (let input of inputs) {
        console.log(input.value);
    }
})

