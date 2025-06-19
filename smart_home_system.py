from abc import ABC, abstractmethod


class SmartDevice(ABC):
    """
    Abstract base class representing a generic smart device.

    Attributes:
        _device_id (str): Unique ID of the device.
        _name (str): Name of the device.
        _is_on (bool): Status of the device (True if on, False if off).
    """

    def __init__(self, device_id, name):
        """
        Initializes the smart device with ID and name.

        Args:
            device_id (str): Unique device identifier.
            name (str): Name of the device.
        """
        self._device_id = device_id
        self._name = name
        self._is_on = False

    @property
    def name(self):
        """
        Returns the name of the device.

        Returns:
            str: Device name.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Sets a new name for the device.

        Args:
            new_name (str): New name for the device.
        """
        self._name = new_name
        print(f"Device name updated to: {self._name}")

    @abstractmethod
    def turn_on(self):
        """Turns the device on. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def turn_off(self):
        """Turns the device off. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def get_status(self):
        """Returns the current status of the device. Must be implemented by subclasses."""
        pass

    def is_device_on(self):
        """
        Checks if the device is on.

        Returns:
            bool: True if on, False otherwise.
        """
        return self._is_on

    def __str__(self):
        """
        Returns a human-readable string of device info.

        Returns:
            str: Formatted device status.
        """
        return f"{self.name} (ID: {self._device_id}) - {self.get_status()}"


class SmartLight(SmartDevice):
    """
    Represents a smart light with adjustable brightness.

    Attributes:
        _brightness (int): Brightness level from 0 to 100.
    """

    def __init__(self, device_id, name, brightness=50):
        super().__init__(device_id, name)
        self._brightness = brightness

    def turn_on(self):
        self._is_on = True
        print(f"[ON] Smart light '{self._name}' is now ON.")

    def turn_off(self):
        self._is_on = False
        print(f"[OFF] Smart light '{self._name}' is now OFF.")

    def get_status(self):
        return f"On, Brightness: {self._brightness}%" if self._is_on else "Off"

    def set_brightness(self, level):
        """
        Sets brightness level if device is on.

        Args:
            level (int): Brightness between 0 and 100.
        """
        if 0 <= level <= 100:
            if self._is_on:
                self._brightness = level
                print(f"[Brightness Set] Brightness of '{self._name}' set to {level}%.")
            else:
                print(f"[Action Blocked] Cannot set brightness. '{self._name}' is OFF.")
        else:
            print("[Invalid Input] Brightness must be between 0 and 100.")

    def __str__(self):
        return (
            f"Smart Light '{self.name}' (ID: {self._device_id}) - {self.get_status()}"
        )


class SmartThermostat(SmartDevice):
    """
    Represents a smart thermostat with adjustable target temperature.

    Attributes:
        _target_temp (float): Target temperature in Celsius.
    """

    def __init__(self, device_id, name, target_temp):
        super().__init__(device_id, name)
        self._target_temp = target_temp

    def turn_on(self):
        self._is_on = True
        print(f"[ON] Smart light '{self._name}' is now ON.")

    def turn_off(self):
        self._is_on = False
        print(f"[OFF] Smart light '{self._name}' is now OFF.")

    def get_status(self):
        return f"On, Target Temp: {self._target_temp}°C" if self._is_on else "Off"

    def set_temperature(self, temp):
        """
        Sets the target temperature.

        Args:
            temp (float): Desired temperature in Celsius.
        """
        if not self._is_on:
            print(f"[Action Blocked] Cannot set temperature. '{self._name}' is OFF.")
        self._target_temp = temp
        print(
            f"[Temperature Set] Target temperature of '{self._name}' set to {self._target_temp}°C."
        )

    def __str__(self):
        return f"Smart Thermostat '{self.name}' (ID: {self._device_id}) - {self.get_status()}"


class Room:
    """
    Represents a room in the smart home with a collection of smart devices.

    Attributes:
        room_name (str): Name of the room.
        devices (list): List of SmartDevice instances.
    """

    def __init__(self, room_name):
        self.room_name = room_name
        self.devices = []

    def add_device(self, device: SmartDevice):
        if device not in self.devices:
            self.devices.append(device)
            print(f"[Device Added] '{device.name}' added to room '{self.room_name}'.")
        else:
            print(f"Device {device} is already present")

    def remove_device(self, device_id):
        for device in self.devices:
            if device._device_id == device_id:
                self.devices.remove(device)
                print(
                    f"[Device Removed] Device '{device_id}' removed from '{self.room_name}'."
                )
                return
        print(f"[Remove Failed] Device '{device_id}' not found in '{self.room_name}'.")

    def get_device(self, device_id):
        for device in self.devices:
            if device._device_id == device_id:
                return device
        return None

    def list_devices(self):
        print(f"\n--- Devices in Room: {self.room_name} ---")
        if not self.devices:
            print("No devices in this room.")
        else:
            for device in self.devices:
                print(device)

    def __len__(self):
        return len(self.devices)

    def __str__(self):
        return f"Room: {self.room_name} ({len(self)} devices)"


class SmartHome:
    """
    Represents a smart home containing multiple rooms.

    Attributes:
        home_name (str): Name of the smart home.
        rooms (dict): Dictionary mapping room names to Room objects.
    """

    def __init__(self, home_name):
        self.home_name = home_name
        self.rooms = {}

    def add_room(self, room: Room):
        if room.room_name in self.rooms:
            print("Room is already present")
            return
        self.rooms[room.room_name] = room
        print("Room added successfully")

    def get_room(self, room_name):
        return self.rooms.get(room_name, None)

    def list_all_rooms(self):
        print(f"\n=== Rooms in Smart Home: {self.home_name} ===")
        if not self.rooms:
            print("No rooms in the smart home.")
        else:
            for room in self.rooms.values():
                print(room)

    def control_device(self, room_name, device_id, action, value=None):
        room = self.get_room(room_name)
        if not room:
            print(f"[Error] Room '{room_name}' not found.")
            return
        device = room.get_device(device_id)
        if not device:
            print(f"[Error] Device '{device_id}' not found in room '{room_name}'.")
            return

        if action == "turn_on":
            device.turn_on()
        elif action == "turn_off":
            device.turn_off()
        elif action == "set_brightness" and hasattr(device, "set_brightness"):
            device.set_brightness(value)
        elif action == "set_temperature" and hasattr(device, "set_temperature"):
            device.set_temperature(value)
        else:
            print(
                f"[Unsupported Action] '{action}' not valid for device '{device.name}'."
            )

    def __len__(self):
        return len(self.rooms)

    def __str__(self):
        return f"Smart Home: {self.home_name} ({len(self)} rooms)"


home = SmartHome("Ninawe Villa")

living_room = Room("Living Room")
bedroom = Room("Bedroom")
kitchen = Room("Kitchen")

home.add_room(living_room)
home.add_room(bedroom)
home.add_room(kitchen)

light1 = SmartLight("L001", "Living Room Light", brightness=70)
light2 = SmartLight("L002", "Bedroom Lamp", brightness=40)
thermo1 = SmartThermostat("T001", "Living Room Thermostat", target_temp=22)
thermo2 = SmartThermostat("T002", "Bedroom Thermostat", target_temp=20)

living_room.add_device(light1)
living_room.add_device(thermo1)
bedroom.add_device(light2)
bedroom.add_device(thermo2)

home.control_device("Living Room", "L001", "turn_on")
home.control_device("Living Room", "T001", "turn_off")
home.control_device("Bedroom", "L002", "turn_on")
home.control_device("Bedroom", "T002", "turn_on")

home.control_device("Living Room", "L001", "set_brightness", 90)
home.control_device("Living Room", "T001", "set_temperature", 24)
home.control_device("Bedroom", "T002", "set_temperature", 21)

home.control_device("Bedroom", "L002", "turn_off")
home.control_device("Bedroom", "L002", "set_brightness", 25)

living_room.list_devices()
bedroom.list_devices()
kitchen.list_devices()

home.list_all_rooms()

home.control_device("Garage", "L001", "turn_on")
home.control_device("Living Room", "X999", "turn_on")

print(f"\nTotal devices in Living Room: {len(living_room)}")
print(f"Total rooms in Smart Home: {len(home)}")

print(str(living_room))
print(str(home))
