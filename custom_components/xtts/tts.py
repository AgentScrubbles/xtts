"""
Setting up TTS entity.
"""
import logging
from homeassistant.components.tts import TextToSpeechEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import generate_entity_id
from .const import CONF_URL, CONF_VOICE, DOMAIN
from .xtts_engine import XTTSEngine
from homeassistant.exceptions import MaxLengthExceeded

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up X Text-to-speech platform via config entry."""
    engine = XTTSEngine(
        config_entry.data[CONF_VOICE],
        config_entry.data[CONF_URL]
    )
    async_add_entities([XTTSEntity(hass, config_entry, engine)])


class XTTSEntity(TextToSpeechEntity):
    """The XTTS entity."""
    _attr_has_entity_name = True
    _attr_should_poll = False

    def __init__(self, hass, config, engine):
        """Initialize TTS entity."""
        self.hass = hass
        self._engine = engine
        self._config = config
        self._attr_unique_id = f"{config.data[CONF_VOICE]}"
        self.entity_id = generate_entity_id("tts.xtts_{}", config.data[CONF_VOICE], hass=hass)

    @property
    def default_language(self):
        """Return the default language."""
        return "en"

    @property
    def supported_languages(self):
        """Return the list of supported languages."""
        return self._engine.get_supported_langs()

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._attr_unique_id)},
            "model": f"{self._config.data[CONF_VOICE]}",
            "manufacturer": "xtts"
        }

    @property
    def name(self):
        """Return name of entity"""
        return f"{self._config.data[CONF_VOICE]}"

    def get_tts_audio(self, message, language, options=None):
        """Convert a given text to speech and return it as bytes."""
        try:
            speech = self._engine.get_tts(message)

            # The response should contain the audio file content
            return "wav", speech.content
        except MaxLengthExceeded:
            _LOGGER.error("Maximum length of the message exceeded")
        except Exception as e:
            _LOGGER.error("Unknown Error: %s", e)

        return None, None
