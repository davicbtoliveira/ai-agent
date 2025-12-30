# AI Agent

This project uses modern Python tooling for dependency management and configuration.

## Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Installation

### Install uv

If you don't have `uv` installed, you can install it using:

```bash
pip install uv
```

Or follow the [official installation guide](https://github.com/astral-sh/uv#installation).

### Install Dependencies

Use `uv` to install project dependencies:

```bash
uv pip install -r requirements.txt
```

Or, if you have a `pyproject.toml` configuration:

```bash
uv sync
```

## Environment Setup

### Configure GEMINI_API_KEY

This project requires a Google Gemini API key. Follow these steps to set it up:

1. **Create a `.env` file** in the project root directory:

```bash
cp .env.example .env
```

2. **Add your Gemini API key** to the `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

3. **Load environment variables** in your application:

Using Python's `python-dotenv` package:

```python
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
```

### Obtaining Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

## .env File Structure

```
GEMINI_API_KEY=your_gemini_api_key_here
```

⚠️ **Important**: Never commit the `.env` file to version control. Add it to `.gitignore`:

```
# .gitignore
.env
.env.local
```

## Running the Project

Once dependencies are installed and environment variables are configured, you can run the project:

```bash
python main.py
```

## Development

### Adding New Dependencies

Use `uv` to add new packages:

```bash
uv pip install package_name
```

Then update your `requirements.txt` or `pyproject.toml` file accordingly.

## Troubleshooting

- **`uv` command not found**: Make sure `uv` is installed and added to your PATH
- **API Key errors**: Verify your `GEMINI_API_KEY` is correctly set in the `.env` file
- **Missing dependencies**: Run `uv sync` or `uv pip install -r requirements.txt` again

## License

This project is licensed under the MIT License.
