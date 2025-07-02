# MCP Server - Context Enhancement Tool

A FastAPI-based Model Context Protocol (MCP) server that enhances simple text contexts into elaborate, detailed prompts with caching functionality. 
**Developed for Google Colab with GPU support.**

## Features

- **Context Elaboration Tool**: Transform simple text contexts into detailed, elaborate prompts
- **Cached Prompts**: Access pre-generated elaborate prompts by concept ID
- **Prompt Cache Management**: List all cached elaborate prompts
- **CSV Data Loading**: Load pre-trained elaborate prompts from CSV files

## Project Structure

```
mcp_server/
├── main.py                      # FastAPI application with MCP endpoints
├── models.py                    # Pydantic models for request/response schemas
├── cache.py                     # Caching functionality and prompt elaboration
├── requirements.txt             # Python dependencies
├── similarity_results_train.csv # Training data for cached elaborate prompts
├── MCPServer.ipynb              # Google Colab notebook implementation
└── README.md                    # This file
```

## API Endpoints

### Tools
- `POST /tool/get_elaborate_description_prompt` - Transform simple context into elaborate prompts

### Resources
- `GET /resource/cached_description/{concept_id}` - Get cached elaborate prompt by ID
- `GET /resource/cached_description_list` - List all cached elaborate prompts

## Quick Start

### For Google Colab (Recommended)
1. Open the `MCPServer.ipynb` notebook in Google Colab
2. Run all cells to install dependencies and start the server
3. The server will create a public ngrok tunnel - access the API at: `{ngrok_url}/docs`

### For Local Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API documentation at: `http://localhost:8000/docs`

## Usage Examples

### Generate Elaborate Prompt
```bash
curl -X POST "http://localhost:8000/tool/get_elaborate_description_prompt" \
     -H "Content-Type: application/json" \
     -d '{"context": "a sunset over mountains"}'
```

### Get Cached Elaborate Prompt
```bash
curl "http://localhost:8000/resource/cached_description/concept123"
```

### List All Cached Elaborate Prompts
```bash
curl "http://localhost:8000/resource/cached_description_list"
```

## Data Format

The server loads cached elaborate prompts from `similarity_results_train.csv` with the following format:
- `input`: The simple concept/context identifier
- `finetuned_model_answer`: The elaborate, enhanced prompt

## Development

This server is designed to work with Phi-4 or similar language models for transforming simple text contexts into elaborate, detailed prompts. **The project is optimized for Google Colab** with GPU support for running the fine-tuned model efficiently.

### Key Features for Colab:
- **ngrok integration**: Creates public tunnels for accessing the server externally
- **GPU support**: Leverages Colab's free GPU for model inference
- **Pre-configured setup**: All dependencies and model loading handled in the notebook
- **Easy access**: Server documentation available at `{ngrok_url}/docs` after running

### Local Development Notes:
The current implementation includes placeholder logic in `cache.py` that can be replaced with actual model calls for context enhancement and prompt elaboration when running locally without GPU access.
