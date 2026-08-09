function addItem() {
  let input = document.getElementById("itemInput");
  let item = input.value.trim();
  if(item !== "") {
    // Save to localStorage
    let groceries = JSON.parse(localStorage.getItem("groceries")) || [];
    groceries.push(item);
    localStorage.setItem("groceries", JSON.stringify(groceries));
    
    // Add to UI
    let li = document.createElement("li");
    li.textContent = item;
    document.getElementById("groceryList").appendChild(li);
    input.value = "";
  }
}

// Load previous groceries
window.onload = function() {
  let groceries = JSON.parse(localStorage.getItem("groceries")) || [];
  let list = document.getElementById("groceryList");
  groceries.forEach(item => {
    let li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });
}
