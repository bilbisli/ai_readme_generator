# auto-readme-with-gemini
Automated README generation powered by Google Gemini, designed to intelligently document your projects.

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Powered by Gemini](https://img.shields.io/badge/Powered%20by-Gemini-brightgreen)](https://ai.google.dev/gemini)
<!-- TODO: Add more relevant badges like workflow status, license, etc. -->

## Table of Contents
*   [Overview](#overview)
*   [Project Structure](#project-structure)
    *   [Directory Tree](#directory-tree)
    *   [Key Directories and Core Project Files](#key-directories-and-core-project-files)
*   [Quick Start](#quick-start)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
    *   [Minimal Usage Example](#minimal-usage-example)
*   [Configuration / Advanced Usage](#configuration--advanced-usage)
*   [Troubleshooting / Common Errors](#troubleshooting--common-errors)
    *   [Generic Issues](#generic-issues)
    *   [Project-Specific Logic Errors](#project-specific-logic-errors)
*   [Roadmap](#roadmap)
*   [Contributing](#contributing)
*   [License](#license)
*   [Support & Contact](#support--contact)
*   [Acknowledgments](#acknowledgments)

## Overview
`auto-readme-with-gemini` is a command-line tool that automates the creation of comprehensive `README.md` files for software projects. It achieves this by first scanning the project's directory structure and contents to gather context, and then leveraging the power of Google's Gemini large language model to intelligently generate a well-structured and informative README. The goal is to significantly reduce the manual effort involved in documentation, ensuring consistency and accuracy.

**Key Features:**
*   **Automated Project Analysis:** Scans your project files and directories to understand its layout and contents.
*   **AI-Powered Content Generation:** Utilizes Google Gemini to draft intelligent and contextually relevant README sections.
*   **Customizable Output:** (Inferred, future feature) Potentially configurable to tailor the README structure or content based on user preferences.
*   **Python-based:** Built entirely in Python, making it accessible and extensible for Python developers.

## Project Structure

### Directory Tree
```text
auto-readme-with-gemini/
│   ├─ .env                # Environment variables (e.g., API keys)
│   ├─ .env.example        # Example file for .env configuration
│   ├─ .idea/              # IDE-specific configuration files (e.g., PyCharm)
│   ├─ main.py             # Main entry point for the application
│   ├─ requirements.txt    # Python dependency list
│   ├─ src/                # Core source code
│   │   ├─ generate_readme.py  # Logic for generating README content using Gemini
│   │   ├─ project_scanner.py  # Module to scan and analyze project structure
```

### Key Directories and Core Project Files

*   `.env` and `.env.example`: These files are crucial for configuring the application, especially for sensitive information like API keys. `.env.example` provides a template of required environment variables, which must be copied to `.env` and populated with actual values (e.g., `GEMINI_API_KEY`).
*   `main.py`: This is the primary executable script. When you run the project, execution begins here. It acts as the orchestrator, coordinating calls to `project_scanner.py` and `generate_readme.py` to achieve the README generation process.
*   `requirements.txt`: This file lists all the Python packages required for the project to run. It's essential for setting up the development or execution environment correctly using `pip`.
*   `src/`: This directory encapsulates the main business logic and helper modules of the application.
    *   `src/generate_readme.py`: This is a core component responsible for interacting with the Google Gemini API. It takes the project context (likely gathered by `project_scanner.py`) and uses it as input for the Gemini model to produce the actual README content in Markdown format. This module handles the prompts and parsing of the AI's response.
    *   `src/project_scanner.py`: Another core component, this module is responsible for analyzing the target software project. It likely traverses directories, identifies file types, reads file contents (selectively, to gather context without passing entire source code), and builds a structured representation of the project that `generate_readme.py` can then use.

## Quick Start

### Prerequisites
*   **Python:** Version 3.8 or higher.
*   **pip:** Python package installer (usually comes with Python).
*   **Google Gemini API Key:** You will need an API key from Google AI Studio to interact with the Gemini model.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/bilbisli/ai_readme_generator.git
    cd auto-readme-with-gemini
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Linux/macOS
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your Gemini API Key:**
    Copy the example environment file and populate it with your actual API key:
    ```bash
    cp .env.example .env
    ```
    Then, open `.env` in a text editor and add your Gemini API key:
    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    ```

### Minimal Usage Example

To generate a `README.md` for the current project:

```bash
python main.py <target_project_directory>

# TODO: Add specific CLI arguments if any are inferred or expected,
# e.g., for specifying target directory, output file, or template.
# Example: python main.py --target-dir ../my_project --output-file ../my_project/README.md
```
Upon successful execution, a `README.md` file should be generated in the specified output location (likely the current directory or the target project's root).

## Configuration / Advanced Usage

The primary configuration is done via environment variables loaded from the `.env` file.

*   `GEMINI_API_KEY`: (Required) Your personal API key for accessing the Google Gemini API. Without this, the application cannot generate content.

```.env
# .env example
GEMINI_API_KEY="your-secret-gemini-api-key"
# TODO: Add other potential environment variables for configuration,
# e.g., MODEL_NAME, TEMPERATURE, TOP_P, MAX_OUTPUT_TOKENS, EXCLUDE_DIRS, etc.
```

**Advanced Usage:**
(No specific flags or API examples can be inferred from the directory structure, so this section serves as a placeholder for future additions.)
*   **Customizing Target Project:** The tool likely needs a way to specify which project directory to scan if it's not the current working directory.
*   **Output Path:** Options to define where the generated `README.md` should be saved.
*   **Template Customization:** (Potential future feature) Allowing users to provide custom Markdown templates for the generated README.

## Troubleshooting / Common Errors

### Generic Issues
*   **Missing Dependencies:**
    *   **Error:** `ModuleNotFoundError: No module named 'some_package'`
    *   **Solution:** Ensure all required packages are installed. Run `pip install -r requirements.txt` within your activated virtual environment.
*   **Incorrect Python Version:**
    *   **Error:** Syntax errors or unexpected behavior specific to Python versions.
    *   **Solution:** Verify you are using Python 3.8 or newer. Check with `python --version`.
*   **Permissions Issues:**
    *   **Error:** `Permission denied` when trying to read or write files.
    *   **Solution:** Ensure the user running the script has read permissions for the project directory and write permissions for the output location of the `README.md`.
*   **Network Connectivity:**
    *   **Error:** Issues connecting to the Gemini API (e.g., `ConnectionError`, `Timeout`).
    *   **Solution:** Check your internet connection and ensure no firewalls or proxies are blocking access to Google's API endpoints.

### Project-Specific Logic Errors
*   **Invalid or Missing `GEMINI_API_KEY`:**
    *   **Error:** Authentication failures or `401 Unauthorized` errors from the Gemini API.
    *   **Cause:** The `GEMINI_API_KEY` in your `.env` file is missing, empty, or incorrect.
    *   **Solution:** Double-check your `.env` file and ensure `GEMINI_API_KEY` is set to a valid key obtained from Google AI Studio. Restart the script after making changes.
*   **Gemini API Rate Limits / Quota Exceeded:**
    *   **Error:** Errors indicating too many requests or exceeding usage limits.
    *   **Cause:** You've hit the API's rate limit or your quota for Gemini API usage.
    *   **Solution:** Wait for a short period before retrying, or review your Google Cloud project's quota limits for the Gemini API.
*   **Project Scanning Failures (`src/project_scanner.py`):**
    *   **Error:** The script crashes or produces an unhelpful README for very large, deeply nested, or unusually structured projects.
    *   **Cause:** `project_scanner.py` might encounter file types it doesn't know how to process, or the project's size/complexity might exceed its internal limits or lead to memory issues.
    *   **Solution:** For large projects, consider running the tool on a smaller, representative subset of the project first. If the issue persists, manually inspect the target project's structure for unusual patterns that might confuse the scanner. (Future: `project_scanner.py` might need exclusion patterns.)
*   **Unsatisfactory README Content (`src/generate_readme.py`):**
    *   **Error:** The generated README is too short, inaccurate, hallucinates information, or is not in the desired Markdown format.
    *   **Cause:** The input provided by `project_scanner.py` might lack sufficient context for Gemini, the prompt used might be too generic, or Gemini itself might generate less-than-ideal output.
    *   **Solution:** Experiment with regenerating the README. Ensure your project has meaningful file names and some initial code comments that `project_scanner.py` can pick up. (Future: Allow users to refine prompts or provide additional context.)

## Roadmap
This section typically lists future features. As no `TODO`/`FIXME` comments were provided in the analyzed project, this serves as a general placeholder.
*   **Configuration Enhancements:** Allow more granular control over `README` sections, depth of scanning, and exclusion patterns.
*   **Command-Line Arguments:** Implement robust CLI arguments for target directory, output file, and other options.
*   **Template Support:** Enable users to provide custom Markdown templates for README generation.
*   **Improved Project Context:** Enhance `project_scanner.py` to intelligently identify key files (e.g., `package.json`, `setup.py`, `Dockerfile`) and extract more relevant context.
*   **Framework Detection:** (Advanced) Automatically detect common frameworks (e.g., Flask, Django, React) and tailor README content accordingly.
*   **Testing:** Implement a comprehensive test suite.

## Contributing
We welcome contributions to `auto-readme-with-gemini`! If you're interested in improving this tool, please consider:
1.  **Reporting Bugs:** If you find any issues, please open an issue on the project's GitHub repository.
2.  **Suggesting Features:** Have an idea for a new feature? Open an issue to discuss it.
3.  **Submitting Pull Requests:** Feel free to fork the repository, make your changes, and submit a pull request. Please ensure your code adheres to standard Python style guidelines and includes relevant tests if applicable.

(There is no `CONTRIBUTING.md` file in the provided structure, so this is a generic summary.)

## License
This project is currently unlicensed. Please check for a `LICENSE` file in the repository or contact the project maintainers for licensing information.

## Support & Contact
If you encounter any issues or have questions, please use the GitHub Issues page for this project.

*   **GitHub Issues:** [https://github.com/bilbisli/ai_readme_generator/issues](https://github.com/bilbisli/ai_readme_generator/issues)
*   **Email:** [bilbisli@gmail.com](bilbisli@gmail.com)

## Acknowledgments
*   Powered by [Google Gemini API](https://ai.google.dev/gemini)
*   Developed with [Python](https://www.python.org/)
*   Special thanks to the open-source community for countless valuable libraries and tools.