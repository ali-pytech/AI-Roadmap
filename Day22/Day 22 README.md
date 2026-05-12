# Day 22 — Inheritance & Polymorphism in Python OOP

Today I advanced into **Inheritance and Polymorphism** — two pillars of Object-Oriented Programming.  
- **Inheritance** allows child classes to reuse and extend parent functionality.  
- **Polymorphism** lets methods behave differently depending on the object type.  

---

## Projects I Built

###Iqama Inheritance
- Parent class: `Document` (holder, year).  
- Child class: `Iqama` adds `fee` and overrides `info()`.  
- Shows how child classes extend parent functionality.

###VAT Invoice Inheritance
- Parent class: `Transaction` (item, price).  
- Child class: `Invoice` adds quantity and VAT, overrides `summary()`.  
- Demonstrates reuse + extension.

###Housing Inheritance
- Parent class: `Property` (name, monthly rent).  
- Child class: `Housing` adds `annual_rent()`.  
- Shows extension of functionality.

###Student Polymorphism
- Parent class: `Person`.  
- Child classes: `Student` and `Teacher`.  
- Both override `role()` differently → polymorphism in action.

###Shopping Cart Polymorphism
- Parent class: `Item`.  
- Child class: `CartItem` overrides `description()` to show subtotal.  
- Same method name, different behavior.



##  Reflections
- **Inheritance** saves time by reusing parent code.  
- **Polymorphism** makes systems flexible and adaptable.  
- Together, they make applications **scalable, professional, and realistic**.  
- My repo now shows **advanced OOP design** — a big leap forward.


