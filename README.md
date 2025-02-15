# Weather Wizard

This Python application fetches the weather for a given city. It's designed to be a fun and quirky example of using custom coding styles.

## Getting Started

### Prerequisites

- An OpenWeather API key (You can get one [here](https://openweathermap.org/appid))
- Python 3.9 or higher (only if running locally)

### Installation

#### Running in a Dev Container

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/weather-wizard.git
    cd weather-wizard
    ```

2. Open the project in Visual Studio Code. When prompted, reopen the project in the Dev Container.

3. The required packages will be installed automatically.

4. Create a `.env` file in the root of the project (if it doesn't exist) and add your OpenWeather API key:

    ```plaintext
    API_KEY=your_actual_api_key_here
    ```

#### Running Locally

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/weather-wizard.git
    cd weather-wizard
    ```

2. Create a virtual environment and activate it:

    ```bash
    # Bash
    python -m venv venv
    source venv/bin/activate
    ```
    ```powershell
    # PowerShell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of the project (if it doesn't exist) and add your OpenWeather API key:

    ```plaintext
    API_KEY=your_actual_api_key_here
    ```

### How to Use

1. Run the application:

    ```bash
    python -m weather_wizard.main
    ```

2. Enter the name of the city when prompted.

### Custom Coding Rules

Just for fun, this project uses some unconventional coding styles:

- Variable names are reversed.
- Comments are in French.

### Challenge Accepted?

Feel free to modify the code, add new features, or come up with even wilder coding rules! Have fun!

### Configuration

Update the `.env` file with your OpenWeather API key.

```plaintext
API_KEY=your_actual_api_key_here
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
