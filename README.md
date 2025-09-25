# Claude Model Connector Protocol (MCP) Sample Server

This repository demonstrates how to create custom MCP servers that extend
Claude's capabilities through external APIs. It includes two sample
services:

Features
- Phone Lookup Service: Retrieves caller information using the Twilio
Lookup API

This was based on the tutorials and documentation found here:
- https://modelcontextprotocol.io/docs/develop/build-server#python
- https://docs.claude.com/en/docs/claude-code/mcp

## Prerequisites

- Python 3.8+

## Installation

## Clone the repository
git clone https://github.com/robinske/lookup-mcp.git
cd lookup-mcp

## Set up your environment

### macOS/Linux
```
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx
```

## Windows
```
# Install uv
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create virtual environment and activate it
uv venv
.venv\Scripts\activate

# Install dependencies
uv add mcp[cli] httpx
```

## Usage

### Add lookup service to Claude with environment variables
claude mcp add lookup --env TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token -- uv --directory /path/to/lookup-mcp run
lookup.py

## Using the Services with Claude

Ask Claude questions like:
- "Who's calling from (555) 123-4567?"

## Service APIs

Lookup Service

- get_lookup(phone_number): Gets information about phone number
