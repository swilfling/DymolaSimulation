Rem Create FMU from Energy Plus file
Rem Uses FMI standard 2.0
Rem Arguments:
Rem 1) path to Python script from EnergyPlusToFMU, for instance D:\Downloads\EnergyPlusToFMU-v3.1.0\Scripts\EnergyPlusToFMU.py
Rem Example Usage:
Rem create_fmu.bat D:\Downloads\EnergyPlusToFMU-v3.1.0\Scripts\EnergyPlusToFMU.py

python %1 -i Energy+.idd -w test.epw -a 2 _fmu-export-actuator.idf