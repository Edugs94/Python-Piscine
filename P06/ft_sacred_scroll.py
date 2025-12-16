import alchemy
import alchemy.elements

print("=== Sacred Scroll Mastery ===")

# 1. Testing direct module access
# Acceso directo al archivo físico (elements.py), aquí todo es accesible.
print("Testing direct module access:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

# 2. Testing package-level access
# Acceso a través de __init__.py. Solo fire y water deberían funcionar.
print("\nTesting package-level access (controlled by __init__.py):")

# Fire y Water están expuestos en el __init__
print(f"alchemy.create_fire(): {alchemy.create_fire()}")
print(f"alchemy.create_water(): {alchemy.create_water()}")

try:
    print(f"alchemy.create_earth(): {alchemy.create_earth()}")
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")

try:
    print(f"alchemy.create_air(): {alchemy.create_air()}")
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")

# 3. Package metadata
print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")