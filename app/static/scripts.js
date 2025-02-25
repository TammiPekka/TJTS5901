let debounceTimer;
document.getElementById("search").addEventListener("input", function() {
    clearTimeout(debounceTimer);
    let query = this.value;
    if (query.length < 2) return;

    debounceTimer = setTimeout(() => {
        fetch(`/get_cities?q=${query}`)
        .then(response => response.json())
        .then(data => {
            let suggestionsList = document.getElementById("suggestions");
            suggestionsList.innerHTML = "";

            data.forEach(city => {
                let listItem = document.createElement("li");
                listItem.textContent = `${city.name}, ${city.country}`;
                listItem.addEventListener("click", function() {
                    document.getElementById("search").value = city.name;
                    suggestionsList.innerHTML = "";
                });
                suggestionsList.appendChild(listItem);
            });
        })
        .catch(error => console.error("Error fetching suggestions:", error));
    }, 300); // 300ms debounce delay
});