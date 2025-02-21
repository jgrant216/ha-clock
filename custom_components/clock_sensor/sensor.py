from datetime import timedelta
import logging

import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME, STATE_UNKNOWN
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

# Set a throttle to ensure updates every minute
MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=1)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the time sensor."""
    async_add_entities([TimeSensor()])


class TimeSensor(Entity):
    """Representation of a Time Sensor."""

    def __init__(self):
        """Initialize the time sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Current Time"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch the current time."""
        from datetime import datetime
        self._state = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return "mdi:clock"

