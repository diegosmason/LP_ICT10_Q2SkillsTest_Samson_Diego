from pyscript import display, document


nonmetals = {
    "Hydrogen": {"symbol": "H", "atomic_number": 1, "atomic_mass": 1.008},
    "Helium": {"symbol": "He", "atomic_number": 2, "atomic_mass": 4.0026},
    "Carbon": {"symbol": "C", "atomic_number": 6, "atomic_mass": 12.011},
    "Nitrogen": {"symbol": "N", "atomic_number": 7, "atomic_mass": 14.007},
    "Oxygen": {"symbol": "O", "atomic_number": 8, "atomic_mass": 15.999},
    "Fluorine": {"symbol": "F", "atomic_number": 9, "atomic_mass": 18.998},
    "Neon": {"symbol": "Ne", "atomic_number": 10, "atomic_mass": 20.180},
    "Phosphorus": {"symbol": "P", "atomic_number": 15, "atomic_mass": 30.974},
    "Sulfur": {"symbol": "S", "atomic_number": 16, "atomic_mass": 32.06},
    "Chlorine": {"symbol": "Cl", "atomic_number": 17, "atomic_mass": 35.45},
    "Argon": {"symbol": "Ar", "atomic_number": 18, "atomic_mass": 39.948},
    "Selenium": {"symbol": "Se", "atomic_number": 34, "atomic_mass": 78.971},
    "Bromine": {"symbol": "Br", "atomic_number": 35, "atomic_mass": 79.904},
    "Krypton": {"symbol": "Kr", "atomic_number": 36, "atomic_mass": 83.798},
    "Iodine": {"symbol": "I", "atomic_number": 53, "atomic_mass": 126.90},
    "Xenon": {"symbol": "Xe", "atomic_number": 54, "atomic_mass": 131.29},
    "Radon": {"symbol": "Rn", "atomic_number": 86, "atomic_mass": 222.0},
}

def element_checker(e):
    document.getElementById('result').innerHTML = " " 
    element1 = document.getElementById('first_name').value.strip().title()


    info = nonmetals.get(
    element1, {
        "symbol" : "Element not found", 
        "atomic_number" : "-", 
        "atomic_mass" : "-"
    }


    )

    # <b>Element:</b> {info['name']} <br>

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {info['symbol']}  <br>

    <b> Atomic Number:</b> {info['atomic_number']} <br>
    <b> Atomic Mass:</b> {info['atomic_mass']}
    """