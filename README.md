# Weather Wizard

This Python application fetches the weather for a given city. It's designed to be a fun and quirky example of using custom coding styles.

## Main Theme

The main theme of this project is to use custom instructions for GitHub Copilot to code using quirky styles. This includes:

- **Variable names are reversed**: All variable names in the code are written in reverse order.
- **Comments are in French**: All comments in the code are written in French.
- **Modular Code**: The code is designed to be modular, with new utility functions added to the `utils` module.
- **Error Handling and Logging**: Best practices for error handling and logging are followed.

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

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root of the project (if it doesn't exist) and add your OpenWeather API key:

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

### Benefits of Running in a Dev Container

Running the application in a Dev Container provides several benefits over running it locally:

- **Consistent Development Environment**: The Dev Container ensures that all developers have the same development environment, reducing the "it works on my machine" problem.
- **Pre-installed Extensions**: The Dev Container can come with pre-installed extensions that are useful for development, such as linters, debuggers, and other tools.
- **Simplified Setup**: The Dev Container automatically installs all required packages and dependencies, making it easier to get started.
- **Isolation**: The Dev Container isolates the development environment from the host machine, preventing potential conflicts with other projects or system configurations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
