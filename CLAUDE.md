# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Meishiki is a Python library for calculating Four Pillars of Destiny (四柱推命). It takes a person's birth date, time, and sex to generate fortune-telling predictions and charts in various output formats (HTML, Markdown, CLI).

## Development Commands

### Installation & Setup
```bash
pip install -e .                    # Install in development mode
pip install -r requirements-dev.txt # Install development dependencies
```

### Testing
```bash
pytest --cov=meishiki ./tests       # Run all tests with coverage
pytest -s tests/output/test_html.py::test_output_html_basic  # Run specific test
```

### Code Quality
```bash
mypy meishiki                       # Type checking
black .                             # Code formatting
```

### Running the Application
```bash
python3 ./generate_html.py YYYY-MM-DD HH:MM SEX  # Generate HTML output (SEX: 0=male, 1=female)
python3 ./mcp_server.py             # Run MCP server for Claude Desktop integration
```

## Architecture

### Core Components

- **meishiki/meishiki.py**: Core `Meishiki` dataclass and `build_meishiki()` function for fortune calculation
- **meishiki/unsei.py**: `Unsei` class and `build_unsei()` for fortune progression calculations  
- **meishiki/output.py**: Output formatting functions (`output_html()`, `output_markdown()`, `output_stdio()`)
- **meishiki/consts.py**: Configuration constants loaded from `consts.yaml`, includes `Sex` and `TemplateType` enums

### Data Flow

1. Input: Birth datetime + Sex enum → `build_meishiki()` 
2. Core calculation: Creates `Meishiki` object with fortune elements (tenkan, chishi, zokan, etc.)
3. Fortune analysis: `build_unsei(meishiki)` → `Unsei` object with timeline predictions
4. Output: Various formatters render results using Jinja2 templates

### Key Files

- **generate_html.py**: CLI entry point for HTML generation
- **mcp_server.py**: MCP server using FastMCP for Claude Desktop integration  
- **template/**: Jinja2 HTML templates for output formatting
- **consts.yaml**: Configuration data for fortune-telling constants
- **tests/**: Comprehensive test suite including output format tests

### Testing Structure

- Core logic tests in `test_meishiki.py`, `test_unsei.py`
- Output format tests in `tests/output/` directory
- Structure validation in `test_meishiki_structure.py`
- Uses pytest with coverage reporting

## MCP Integration

This project includes MCP (Model Context Protocol) server support for Claude Desktop integration. The `calculate_meishiki()` tool accepts ISO8601 datetime strings and Sex enums, returning Markdown-formatted fortune readings.