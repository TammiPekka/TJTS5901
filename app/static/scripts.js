document.addEventListener("DOMContentLoaded", function () {
    let debounceTimer;
    let searchInput = document.getElementById("search");
    let suggestionsList = document.getElementById("suggestions");

    if (!searchInput || !suggestionsList) {
        console.error("Search input or suggestions list not found!");
        return;
    }

searchInput.addEventListener("input", function() {
    clearTimeout(debounceTimer);
    let query = this.value.trim();
    //empty the list if input is empty
    if (query.length === 0) {
        while (suggestionsList.firstChild) {
            suggestionsList.removeChild(suggestionsList.firstChild);
        }
        return;
    }

    if (query.length < 2) return;

    debounceTimer = setTimeout(() => {
        fetch(`/get_cities?q=${query}`)
        .then(response => response.json())
        .then(data => {
            //console.log("Received data:", data);
            while (suggestionsList.firstChild) {
                suggestionsList.removeChild(suggestionsList.firstChild);
            }

            if (data.length === 0) {
                let noResultItem = document.createElement("li");
                noResultItem.textContent = "No suggestions found";
                suggestionsList.appendChild(noResultItem);
            } else {
                data.slice(0, 5).forEach(city => {
                    let listItem = document.createElement("li");
                    listItem.textContent = `${city.name}, ${city.country}`;
                    listItem.setAttribute("role", "option"); // Accessibility improvement
                    listItem.addEventListener("click", function () {
                        searchInput.value = city.name + ", " + city.country;
                        while (suggestionsList.firstChild) {
                            suggestionsList.removeChild(suggestionsList.firstChild);
                        }
                        suggestionsList.classList.remove("show"); // Hide after selection
                    });
                    suggestionsList.appendChild(listItem);
                });
            }

            // Show only if there are suggestions
            if (suggestionsList.childNodes.length > 0) {
                suggestionsList.classList.add("show");
            } else {
                suggestionsList.classList.remove("show");
            }
        })
        .catch(error => console.error("Error fetching suggestions:", error));
    }, 300);
});

// Hide suggestions when clicking outside
document.addEventListener("click", function (event) {
    if (!searchInput.contains(event.target) && !suggestionsList.contains(event.target)) {
        suggestionsList.classList.remove("show");
    }
});
});