Weather Widget
A simple weather and time widget built with Python and PyQt5.

This widget displays the current weather for a specified city, along with the current time and date. It uses the WeatherStack API to fetch weather data.

Features:
Real-time updates: Time, date, and weather are updated automatically at regular intervals.
Customizable: Easily change the city and other settings via the .env file.
User-friendly: A clean and intuitive graphical interface.
Getting Started:
Prerequisites:
Python 3.x: Ensure you have Python installed.
Required libraries:
Bash

pip install requests PyQt5 python-dotenv
WeatherStack API key: Sign up for a free API key at https://www.weatherstack.com/
Setup:
Clone the repository:
<!-- end list -->

Bash

git clone https://your-repository-url.git
Create a .env file: Create a file named .env at the root of your project. Add the following lines, replacing the placeholders with your actual values:
<!-- end list -->

API_KEY=your_weatherstack_api_key
CITY=your_desired_city
Run the application:
<!-- end list -->

Bash

python main.py
Customization:
Change city: Modify the CITY variable in your .env file.
Adjust update intervals: Modify the timer intervals in main.py to change how frequently the data is updated.
Customize appearance: Modify the stylesheets in main.py to change the look and feel of the widget.
Add more features: Explore the WeatherStack API documentation to add features like humidity, wind speed, etc.
Structure:
weather.py: Handles fetching weather data from the API and parsing the response.
main.py: Creates the graphical user interface using PyQt5 and displays the weather information.
.env: Stores your API key and city for security and convenience.
Additional Notes:
Error handling: Implement error handling to gracefully handle situations like network errors or invalid API keys.
Localization: Consider adding support for multiple languages.
Testing: Write unit tests to ensure the code works as expected.
Deployment: Explore options for deploying the widget as a desktop application or a web application.
Example Output:

Time: 14:30
Date: 10-01-2025
Weather: Sunny, 10°C
