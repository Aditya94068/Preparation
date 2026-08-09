// Load groceries from localStorage
window.onload = function() {
  let groceries = JSON.parse(localStorage.getItem("groceries")) || [];
  let list = document.getElementById("groceryList");
  if(groceries.length === 0) {
    let p = document.createElement("p");
    p.textContent = "No groceries available yet.";
    list.appendChild(p);
  } else {
    groceries.forEach(item => {
      let li = document.createElement("li");
      li.textContent = item;
      list.appendChild(li);
    });
  }
}
