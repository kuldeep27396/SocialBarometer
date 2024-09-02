# SocialBarometer

SocialBarometer is a powerful social media sentiment analysis tool that collects data from various social media platforms, analyzes the sentiment of posts, and provides real-time alerts for significant sentiment shifts.

## Features

- Multi-platform data collection (Twitter, Reddit)
- Real-time sentiment analysis
- Configurable alerting system
- Scalable architecture using asyncio
- Comprehensive logging and error handling

## Requirements

- Python 3.9+
- PostgreSQL database

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/socialbarometer.git
   cd socialbarometer
   ```

2. Install Poetry (if not already installed):
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:
   ```
   poetry install
   ```

4. Set up your `.env` file with necessary credentials and configuration (see Configuration section).

## Configuration

Create a `.env` file in the root directory with the following contents:

```
DATABASE_URL=postgresql://username:password@localhost:5432/socialbarometer
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
ALERT_THRESHOLD=0.7
COLLECTION_INTERVAL=300
SEARCH_KEYWORDS=SocialBarometer,sentiment analysis
LOG_LEVEL=INFO
```

Replace the placeholder values with your actual credentials and desired configuration.

## Usage

To run SocialBarometer:

```
poetry run python -m socialbarometer.main
```

This will start the data collection and analysis process based on your configuration.

## Development

### Running Tests

To run the test suite:

```
poetry run pytest
```

### Code Formatting

We use Black and isort for code formatting. To format your code:

```
poetry run black .
poetry run isort .
```

### Linting

To run linters:

```
poetry run flake8 .
poetry run mypy .
```

## Project Structure

```
socialbarometer/
├── socialbarometer/
│   ├── __init__.py
│   ├── main.py
│   ├── collectors/
│   ├── analyzers/
│   ├── alerts/
│   ├── database/
│   └── utils/
├── tests/
├── pyproject.toml
├── README.md
└── .env
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Kuldeep Pal - kuldeep27396@gmail.com

