# main.py
import api_handler
import database_handler

class Report:
    """A class to represent a combined weather and news report."""
    def __init__(self, city, temperature, weather_description, headlines):
        self.city = city
        self.temperature = temperature
        self.weather_description = weather_description
        self.headlines = headlines

    def display(self):
        """Prints the formatted report to the console."""
        print("\n" + "="*40)
        print(f"REPORT FOR: {self.city.upper()}")
        print("="*40)
        print("\n--- WEATHER ---")
        print(f"Temperature: {self.temperature}°C")
        print(f"Conditions: {self.weather_description.capitalize()}")
        print("\n--- TOP NEWS HEADLINES ---")
        for i, headline in enumerate(self.headlines, 1):
            print(f"{i}. {headline}")
        print("\n" + "="*40)

def main():
    """Main function to run the application."""
    # Initialize the database
    database_handler.init_db()

    city = input("Enter a city name to get a report: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    print(f"\nFetching data for {city}...")
    
    # Fetch weather data
    weather_data, weather_error = api_handler.get_weather(city)
    if weather_error:
        print(f"Error fetching weather: {weather_error}")
        return

    # Fetch news data (assuming UK for simplicity, you could extend this)
    news_data, news_error = api_handler.get_news('gb')
    if news_error:
        print(f"Error fetching news: {news_error}")
        return

    # Create a report object using the fetched data
    current_report = Report(
        city=weather_data['city'],
        temperature=weather_data['temperature'],
        weather_description=weather_data['description'],
        headlines=news_data
    )

    # Display the report and save it to the database
    current_report.display()
    database_handler.save_report(current_report)

if __name__ == "__main__":
    main()
