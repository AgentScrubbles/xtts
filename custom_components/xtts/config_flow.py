"""Config flow for XTTS text-to-speech custom component."""
from __future__ import annotations
from typing import Any
import voluptuous as vol
import logging

from homeassistant import data_entry_flow
from homeassistant.config_entries import ConfigFlow
from homeassistant.helpers.selector import selector
from homeassistant.exceptions import HomeAssistantError

from .const import URL, CONF_MODEL, CONF_VOICE, DOMAIN, MODELS, VOICES

_LOGGER = logging.getLogger(__name__)


async def validate_user_input(user_input: dict):
    """Validate user input fields."""
    if user_input.get(URL) is None:
        raise ValueError("URL is required")
    if user_input.get(CONF_VOICE) is None:
        raise ValueError("Voice is required")

class XTTSConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for XTTS."""
    VERSION = 1
    data_schema = vol.Schema({
        vol.Required(URL, default=""): str,
        vol.Required(CONF_VOICE, default=""): str
    })

    async def async_step_user(self, user_input: dict[str, Any] | None = None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            try:
                await validate_user_input(user_input)
                await self.async_set_unique_id(f"{user_input[CONF_VOICE]}")
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title="XTTS", data=user_input)
            except data_entry_flow.AbortFlow:
                return self.async_abort(reason="already_configured")
            except ValueError as e:
                _LOGGER.exception(str(e))
                errors["base"] = str(e)
            except Exception as e:  # pylint: disable=broad-except
                _LOGGER.exception(str(e))
                errors["base"] = "unknown_error"
        return self.async_show_form(step_id="user", data_schema=self.data_schema, errors=errors, description_placeholders=user_input)
