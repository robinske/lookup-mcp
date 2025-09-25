from typing import Any
import httpx
import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("lookup")

TWILIO_LOOKUP_BASE = "https://lookups.twilio.com/v2/PhoneNumbers"

# Get authentication from environment variables
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# Create auth tuple
auth = (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

async def make_twilio_request(url: str, auth: tuple[str, str]) -> dict[str, Any] | None:
    """Make a request to the Twilio Lookup API with proper error handling."""
    async with httpx.AsyncClient(verify=False) as client:
        try:
            response = await client.get(url, auth=auth, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

@mcp.tool()
async def get_lookup(phone_number: str) -> str:
    """Get phone number information from Twilio Lookup API.

    Args:
        phone_number: The phone number to look up, in E.164 format (e.g. +14155552671)
    """
    url = f"{TWILIO_LOOKUP_BASE}/{phone_number}?Fields=line_type_intelligence,caller_name"
    data = await make_twilio_request(url, auth)

    if not data:
        return "Unable to fetch phone number information."

    # Process and format the lookup data
    phone_info = data.get("line_type_intelligence", {})
    caller_name_info = data.get("caller_name", {})
    carrier_name = phone_info.get("name", "Unknown")
    carrier_type = phone_info.get("type", "Unknown")
    caller_name = caller_name_info.get("caller_name", "Unknown")
    country_code = data.get("country_code", "Unknown")
    phone_number = data.get("phone_number", "Unknown")

    return f"Phone Number: {phone_number}\nCountry Code: {country_code}\nCarrier: {carrier_name}\nType: {carrier_type}\nCaller Name: {caller_name}"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')