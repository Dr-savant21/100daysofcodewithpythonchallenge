const locationInput = document.querySelector('.searchBar');
const submitButton = document.querySelector('.icon');
const stateElement = document.querySelector('.state');
const countryElement = document.querySelector('.country');
const tempElement = document.querySelector('.temp');
const descElement = document.querySelector('.desc');
const highTempElement = document.querySelector('.high-temp');
const windElement = document.querySelector('.wind');
const sunriseElement = document.querySelector('.sunrise');
const lowTempElement = document.querySelector('.low-temp');
const rainElement = document.querySelector('.rain');
const sunsetElement = document.querySelector('.sunset');
const hourDataElement = document.querySelector('.hour-data');

submitButton.addEventListener('click', () => {
  const location = locationInput.value;

  fetch(`/weather?location=${location}`)
    .then(response => response.json())
    .then(data => {
      if (data.name && data.sys && data.sys.country && data.main && data.weather && data.weather[0]) {
        // Update the HTML elements with the weather data
        stateElement.textContent = data.name;
        countryElement.textContent = data.sys.country;
        tempElement.textContent = `${Math.round(data.main.temp)}\u00B0`;
        descElement.textContent = data.weather[0].description;
        highTempElement.textContent = `${Math.round(data.main.temp_max)}\u00B0 High`;
        windElement.textContent = `${Math.round(data.wind.speed)}mph Wind`;
        sunriseElement.textContent = formatTime(data.sys.sunrise);
        lowTempElement.textContent = `${Math.round(data.main.temp_min)}\u00B0 Low`;
        rainElement.textContent = `${data.clouds.all}% Rain`;
        sunsetElement.textContent = formatTime(data.sys.sunset);

        // Update hourly weather data
        const hourlyData = data.hourly.slice(0, 7); // Limit to 7 hours
        hourDataElement.innerHTML = '';
        hourlyData.forEach(hour => {
          const hourElement = document.createElement('div');
          hourElement.classList.add('hour');

          const timeElement = document.createElement('div');
          timeElement.classList.add('time');
          timeElement.textContent = formatTime(hour.dt);
          hourElement.appendChild(timeElement);

          const iconElement = document.createElement('div');
          iconElement.classList.add('icon');
          const iconImage = document.createElement('img');
          iconImage.src = getIconUrl(hour.weather[0].icon);
          iconImage.alt = hour.weather[0].description;
          iconElement.appendChild(iconImage);
          hourElement.appendChild(iconElement);

          const tempElement = document.createElement('div');
          tempElement.classList.add('temp');
          tempElement.textContent = `${Math.round(hour.temp)}\u00B0`;
          hourElement.appendChild(tempElement);

          hourDataElement.appendChild(hourElement);
        });
      } else {
        console.log('Invalid data received from the API.');
      }
    })
    .catch(error => {
      console.log(error);
    });
});

// Helper function to format time from UNIX timestamp
function formatTime(timestamp) {
  const date = new Date(timestamp * 1000);
  const hours = date.getHours().toString().padStart(2, '0');
  const minutes = date.getMinutes().toString().padStart(2, '0');
  return `${hours}:${minutes}`;
}

// Helper function to get the URL of weather icon
function getIconUrl(iconCode) {
  return `https://openweathermap.org/img/wn/${iconCode}.png`;
}
