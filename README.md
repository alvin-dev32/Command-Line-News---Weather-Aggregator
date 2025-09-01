Command-Line News & Weather Aggregator

A Python-based command-line tool that fetches and displays the current weather and top news headlines for a user-specified city. The generated report is then saved to a local SQLite database for historical record-keeping.

This project demonstrates proficiency in intermediate Python concepts including API integration, JSON data processing, object-oriented programming (OOP), and database management.

(Replace the placeholder above with a screenshot of your application running)
Features

    Real-Time Data: Fetches up-to-the-minute weather from OpenWeatherMap and top news headlines from NewsAPI.

    Object-Oriented Design: Uses a Report class to cleanly structure and manage the aggregated data.

    Database Storage: Saves each generated report with a timestamp to an SQLite database (reports.db).

    Modular Codebase: Logic is separated into distinct modules for API handling, database operations, and the main application flow.

    Error Handling: Includes checks for API request failures and invalid user input.

Technologies Used

    Python 3

    Libraries:

        requests: For making HTTP requests to external APIs.

        sqlite3: For database interaction.

Setup & Installation

    Clone the Repository:

    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name

    Install Dependencies:

    pip install requests

    Get API Keys:

        Sign up for a free API key at OpenWeatherMap.

        Sign up for a free developer API key at NewsAPI.org.

    Configure API Keys:

        Open the config.py file.

        Paste your API keys into the respective WEATHER_API_KEY and NEWS_API_KEY variables.

How to Run

Execute the main script from your terminal:

python main.py

You will be prompted to enter a city name. The script will then fetch the data, display the report on the console, and confirm that the report has been saved to the database.
