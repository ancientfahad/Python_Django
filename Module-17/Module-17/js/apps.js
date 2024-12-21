const buttons = document.getElementsByTagName("button");

function updateTotal() {
  const basePrice = 1299;
  const memoryCost = parseInt(
    document.getElementById("memory-cost").textContent
  );
  const storageCost = parseInt(
    document.getElementById("storage-cost").textContent
  );
  const deliveryCost = parseInt(
    document.getElementById("delivery-cost").textContent
  );
  return basePrice + memoryCost + storageCost + deliveryCost;
}

for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", function () {
    if (buttons[i].id === "8gb-memory") {
      highlightSelection("memory", "8gb-memory");
      customizationPrice("memory-cost", 0);
    } else if (buttons[i].id === "16gb-memory") {
      highlightSelection("memory", "16gb-memory");
      customizationPrice("memory-cost", 150);
    } else if (buttons[i].id === "256gb-storage") {
      highlightSelection("storage", "256gb-storage");
      customizationPrice("storage-cost", 0);
    } else if (buttons[i].id === "512gb-storage") {
      highlightSelection("storage", "512gb-storage");
      customizationPrice("storage-cost", 100);
    } else if (buttons[i].id === "1tb-storage") {
      highlightSelection("storage", "1tb-storage");
      customizationPrice("storage-cost", 200);
    } else if (buttons[i].id === "late-delivery") {
      highlightSelection("delivery", "late-delivery");
      customizationPrice("delivery-cost", 0);
    } else if (buttons[i].id === "early-delivery") {
      highlightSelection("delivery", "early-delivery");
      customizationPrice("delivery-cost", 20);
    }
    else{
      promoCode();
    }
  });
}

function customizationPrice(id, cost) {
  const now = document.getElementById(id);
  now.textContent = cost;
  const totalCost = updateTotal();
  const totalPrice = document.getElementById("total-price");
  totalPrice.textContent = totalCost;
}

function highlightSelection(id, selectedId) {
  const buttons = document.querySelectorAll(`button[id*='${id}']`);
  buttons.forEach((button) => {
    if (button.id === selectedId) {
      button.classList.add("selected");
    } else {
      button.classList.remove("selected");
    }
  });
}

// function promoCode()
function promoCode() {
  const inputField = document.getElementById("input-field");
  const promoCode = inputField.value.trim();
  const totalPriceElement = document.getElementById("total-price");
  const userPaymentElement = document.getElementById("user-payment");

  // Parse current total price
  let totalPrice = parseInt(totalPriceElement.textContent);

  if (promoCode.toUpperCase() === "OSTAD") {
    const discountedPrice = totalPrice * 0.9; // Apply 10% discount
    totalPriceElement.textContent = discountedPrice.toFixed(2); // Update Total Price
    userPaymentElement.textContent = discountedPrice.toFixed(2); // Update User Payment
    alert("Promo code applied successfully!");

    /*inputField.disabled = true; // Disable the input field
    document.getElementById("apply-btn").disabled = true; // Disable the apply button*/
    
  } else {
    alert("Invalid promo code. Please try again.");
  }
}