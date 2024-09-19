
print("Welcome to wavelength to colour converter")


wavelength = int(input(" enter an integer wavelength between 380 and 750: "))

if 380 <= wavelength < 450:
    color = "Violet"
elif 450 <= wavelength < 495:
    color = "Blue"
elif 495 <= wavelength < 570:
    color = "Green"
elif 570 <= wavelength < 590:
    color = "Yellow"
elif 590 <= wavelength < 620:
    color = "Orange"
elif 620 <= wavelength <= 750:
    color = "Red"
else:
    color = None


if color:
    print(f"\nThank you, the wavelength that you entered in nanometres is {wavelength}")
    print(f"The colour for this wavelength is...{color}")
else:
    print("\nError: The wavelength you entered is outside the visible spectrum.")
