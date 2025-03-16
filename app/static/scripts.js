document.addEventListener("DOMContentLoaded", function () {
    let debounceTimer;
    let searchInput = document.getElementById("search");
    let suggestionsList = document.getElementById("suggestions");
    let previousSearches = document.getElementById("previous-searches");

    if (!searchInput || !suggestionsList) {
        console.error("Search input or suggestions list not found!");
        return;
    }

    // Handle Search Input and Suggestions
    searchInput.addEventListener("input", function () {
        clearTimeout(debounceTimer);
        let query = this.value.trim();

        if (query.length === 0) {
            suggestionsList.innerHTML = ""; // Clear the list
            return;
        }

        if (query.length < 2) return;

        debounceTimer = setTimeout(() => {
            fetch(`/get_cities?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsList.innerHTML = ""; // Clear previous suggestions

                    if (data.length === 0) {
                        let noResultItem = document.createElement("li");
                        noResultItem.textContent = "No suggestions found";
                        suggestionsList.appendChild(noResultItem);
                    } else {
                        data.slice(0, 5).forEach(city => {
                            let listItem = document.createElement("li");
                            listItem.textContent = `${city.name}, ${city.country}`;
                            listItem.setAttribute("role", "option");
                            listItem.classList.add("suggestion-item");

                            listItem.addEventListener("click", function () {
                                searchInput.value = city.name + ", " + city.country;
                                suggestionsList.innerHTML = ""; // Clear suggestions
                                suggestionsList.classList.remove("show");
                            });

                            suggestionsList.appendChild(listItem);
                        });
                    }

                    suggestionsList.classList.toggle("show", suggestionsList.childNodes.length > 0);
                })
                .catch(error => console.error("Error fetching suggestions:", error));
        }, 300);
    });

    // **Handle Clicking Outside to Hide Suggestions**
    document.addEventListener("click", function (event) {
        if (!searchInput.contains(event.target) && !suggestionsList.contains(event.target)) {
            suggestionsList.classList.remove("show");
        }
    });

    // Handle Clicking on Previous Searches
    if (previousSearches) {
        previousSearches.addEventListener("click", function (event) {
            let clickedElement = event.target;

            if (clickedElement.classList.contains("search-item")) {
                let cityName = clickedElement.getAttribute("data-city");
                let tempWeather = clickedElement.getAttribute("data-temp-weather");
                let tempOpen = clickedElement.getAttribute("data-temp-open");
                let avg = clickedElement.getAttribute("data-avg");
                let dif = clickedElement.getAttribute("data-dif");
                let lat = clickedElement.getAttribute("data-lat"); 
                let lon = clickedElement.getAttribute("data-lon");
                updateWeatherDisplay(cityName, tempWeather, tempOpen, avg, dif, lat, lon);

                
            }
        });
    }

    // Function to Update Weather Display without Reloading
    function updateWeatherDisplay(city, tempWeather, tempOpen, avg, dif, lat, lon) {
        document.getElementById("city-name").textContent = city;
        document.getElementById("temp1").textContent = tempWeather;
        document.getElementById("temp2").textContent = tempOpen;
        document.getElementById("avg1").textContent = avg;
        document.getElementById("dif1").textContent = dif;
        updateMap(lat, lon);
    }

    function updateMap(lat, lon) {

        const mapImage = document.getElementById("map-image"); 
        if (mapImage) {
            mapImage.src = `https://static-maps.yandex.ru/1.x/?ll=${lon},${lat}&z=10&size=600,400&l=map&lang=en_US`;
        }
    }
    
});

// Handle removing previous searches
document.addEventListener("DOMContentLoaded", function () {
    let clearHistoryButton = document.getElementById("clear-history");
    let previousSearchesList = document.getElementById("previous-searches");

    if (clearHistoryButton) {
        clearHistoryButton.addEventListener("click", function () {
            fetch("/clear_history", { method: "POST" }) // Call Flask route
                .then(response => {
                    if (response.ok) {
                        // Remove each child (list item) one by one
                        while (previousSearchesList.firstChild) {
                            previousSearchesList.removeChild(previousSearchesList.firstChild);
                        }
                    }
                })
                .catch(error => console.error("Error clearing history:", error));
        });
    }
    //refresh data that is shown on the page
    const refreshButton = document.getElementById("refresh-btn");

    if (refreshButton) {
        refreshButton.addEventListener("click", function () {
            const city = document.getElementById("city-name").textContent.trim();
            if (!city || city === "Enter city" || city === "City not found") {
                alert("No city selected for refresh.");
                return;
            }

            // Reload the page and append the city to the URL
            window.location.href = `/?city=${encodeURIComponent(city)}`;
        });
    }
});
