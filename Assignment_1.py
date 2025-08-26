# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand        # Public attribute
        self.model = model        # Public attribute
        self._is_on = False       # Protected attribute (encapsulation)

    def power_on(self):
        self._is_on = True
        print(f"{self.brand} {self.model} is now ON")

    def power_off(self):
        self._is_on = False
        print(f"{self.brand} {self.model} is now OFF")

    def status(self):
        return "ON" if self._is_on else "OFF"


# Child class: Smartphone inherits from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_mp):
        super().__init__(brand, model)   # Call parent constructor
        self.storage = storage           # Unique to Smartphone
        self.camera_mp = camera_mp       # Unique to Smartphone
        self.apps = []                   # Store installed apps

    # Method specific to Smartphone
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"Installed {app_name} on {self.brand} {self.model}")

    # Polymorphism: redefine power_on()
    def power_on(self):
        self._is_on = True
        print(f"{self.brand} {self.model} (Smartphone) is booting up...")

    # Encapsulation example: get apps safely
    def get_installed_apps(self):
        return self.apps


# Another Child class: Tablet inherits from Device
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    # Polymorphism: redefine power_on()
    def power_on(self):
        self._is_on = True
        print(f"{self.brand} {self.model} (Tablet) with {self.screen_size}-inch screen is now ON")


# Test the classes
if __name__ == "__main__":
    # Create unique objects
    phone1 = Smartphone("Apple", "iPhone 15", "256GB", 48)
    phone2 = Smartphone("Samsung", "Galaxy S24", "512GB", 64)
    tablet1 = Tablet("Microsoft", "Surface Pro 9", 13)

    # Test Smartphone methods
    phone1.power_on()
    phone1.install_app("WhatsApp")
    phone1.install_app("Instagram")
    print("Installed apps:", phone1.get_installed_apps())
    phone1.power_off()

    print("------")

    # Test second phone
    phone2.power_on()
    phone2.install_app("Telegram")
    print("Installed apps:", phone2.get_installed_apps())

    print("------")

    # Test Tablet
    tablet1.power_on()
    tablet1.power_off()
