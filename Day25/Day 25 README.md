# Day 25 — File Handling + OOP Integration

Today I combined **File Handling (JSON)** with **Object-Oriented Programming pillars** to build a **Service Data Manager**.  
This system saves and retrieves records for Iqama, VAT, and Housing services, showing how OOP can work with persistent storage.



## Project: Service Data Manager

### Features
- **Encapsulation** → secure attributes (`__fee`, `__monthly_rent`) with getters/setters.  
- **Inheritance** → child classes (`Iqama`, `Invoice`, `Housing`) reuse parent `Service`.  
- **Polymorphism** → each class implements `process()` differently.  
- **Abstraction** → abstract base class `Service` enforces structure.  
- **File Handling** → records saved to `services.json` and read back.

### Example Output

Loaded Data from File:
{'type': 'Iqama', 'holder': 'Ali', 'year': 2026, 'fee': 800}
{'type': 'Invoice', 'item': 'Laptop', 'total': 6900.0}
{'type': 'Housing', 'apartment': 'Apartment A', 'annual_rent': 30000}


## Reflections
- I can now design **persistent systems** that store data beyond runtime.  
- Recruiters will see I can combine **OOP design with file handling** for real-world applications.  
- This project is a **Saudi-context showcase**: storing Iqama, VAT, and Housing records in files for practical use.  


