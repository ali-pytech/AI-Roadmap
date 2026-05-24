# Day 27 — Multi-Format Persistence with OOP

Today I built a system that combines **Object-Oriented Programming pillars** with **multi-format file handling (JSON + CSV)**.  
This project shows how services can be stored in both hierarchical (JSON) and tabular (CSV) formats, making data flexible and reusable.



## Project: Multi-Format Service Manager

### Features
- **Encapsulation** → secure attributes (`__fee`, `__monthly_rent`).  
- **Inheritance** → child classes (`Iqama`, `Invoice`, `Housing`) reuse parent `Service`.  
- **Polymorphism** → each class implements `process()` differently.  
- **Abstraction** → abstract base class `Service` enforces structure.  
- **JSON Handling** → hierarchical records saved and loaded.  
- **CSV Handling** → tabular records saved and loaded.  

## Reflections
- I can now design systems that **store data in multiple formats simultaneously**.   
- This project is a **Saudi-context showcase**: storing Iqama, VAT, and Housing records in both JSON and CSV for government + business use.  

