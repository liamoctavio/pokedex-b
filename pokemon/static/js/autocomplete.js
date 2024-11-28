document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-input");
  const autocompleteList = document.getElementById("autocomplete-list");

  searchInput.addEventListener("input", function () {
    const query = this.value;
    if (query.length > 0) {
      fetch(`/autocomplete/?query=${query}`)
        .then((response) => response.json())
        .then((data) => {
          autocompleteList.innerHTML = "";
          if (data.length > 0) {
            autocompleteList.style.display = "block"; // Mostrar sugerencias
            data.forEach((item) => {
              const suggestionItem = document.createElement("div");
              suggestionItem.classList.add("autocomplete-suggestion");
              suggestionItem.textContent = item;
              suggestionItem.addEventListener("click", function () {
                searchInput.value = item;
                autocompleteList.innerHTML = "";
                autocompleteList.style.display = "none"; // Ocultar sugerencias
              });
              autocompleteList.appendChild(suggestionItem);
            });
          } else {
            autocompleteList.style.display = "none"; // Ocultar sugerencias si no hay resultados
          }
        });
    } else {
      autocompleteList.innerHTML = "";
      autocompleteList.style.display = "none"; // Ocultar sugerencias si el campo está vacío
    }
  });

  document.addEventListener("click", function (e) {
    if (e.target !== searchInput) {
      autocompleteList.innerHTML = "";
      autocompleteList.style.display = "none"; // Ocultar sugerencias al hacer clic fuera del campo de búsqueda
    }
  });
});
