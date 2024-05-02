const CLOCK_CONTAINER = document.querySelector(".clock-container");

function createStripe(numberOfItems) {
  const stripe = document.createElement("ul");
  stripe.classList.add("stripe");
  for (let i = 0; i < numberOfItems; i++) {
    const item = document.createElement("li");
    item.innerHTML = `<span>${i}</span>`;
    stripe.appendChild(item);
  }

  CLOCK_CONTAINER.appendChild(stripe);
}

function moveStripe(selectedItem, stripe) {
  const items = [...stripe.querySelectorAll("li")];
  const [item] = items.filter((elem) => elem.textContent === selectedItem);
  if (!item) return;

  const stripeRect = stripe.getBoundingClientRect();
  const itemRect = item.getBoundingClientRect();

  const offset = itemRect.top - stripeRect.top;
  stripe.style.transform = `translateY(-${offset}px)`;

  items.forEach((elem) => elem.classList.remove("selected"));
  item.classList.add("selected");
}

function updateClock() {
  const date = new Date();
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const seconds = String(date.getSeconds()).padStart(2, "0");

  const currentTime = [...hours, ...minutes, ...seconds];

  const stripes = [...CLOCK_CONTAINER.querySelectorAll(".stripe")];
  stripes.forEach((stripe, index) => moveStripe(currentTime[index], stripe));
}

// generate stripes
[3, 10, 6, 10, 6, 10].forEach(createStripe);

updateClock();
setInterval(updateClock, 1000);