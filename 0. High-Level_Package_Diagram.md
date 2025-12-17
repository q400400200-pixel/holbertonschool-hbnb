# **High-Level Package Diagram for HBnB Application**

## **Overview**
This document provides a high-level package diagram illustrating the three-layer architecture of the HBnB application. It demonstrates how different components are organized and interact using the **Facade Pattern**.

## **Three-Layer Architecture**
The application is structured into three primary layers:

### **1. Presentation Layer (Services, API)**
- Responsible for handling user interactions.
- Exposes API endpoints that communicate with the Business Logic Layer.
- Calls the Facade to simplify interactions with underlying components.

### **2. Business Logic Layer (Models)**
- Contains the core application logic.
- Defines models representing system entities (e.g., User, Place, Review, Amenity).
- Uses the Facade to abstract interactions with the Persistence Layer.

### **3. Persistence Layer (Database Access)**
- Manages data storage and retrieval operations.
- Provides an interface for CRUD operations on the database.
- Business Logic Layer interacts with this layer via the Facade.

## **Package Diagram (Mermaid.js Representation)**
<img width="300" height="600" alt="image" src="https://github.com/user-attachments/assets/d9ba0434-974c-467d-8e6f-748aaee24c28" />

To access the Mermaid.js link: [Mermaid Diagram Link](https://www.mermaidchart.com/d/bfbce0d1-93cf-4c7f-92a8-9b566e81df5c)

## **Explanation Layer Interactions with Facade**
The **Facade Pattern** helps manage complexity between system layers:  
- The **Presentation Layer** interacts with the **Business Logic Layer** through a **Facade**, instead of accessing databases directly.  
- The **Facade** offers a clear and simple interface to work with business models, promoting separation of concerns.  
- The **Persistence Layer** is encapsulated within the Business Logic Layer, keeping database operations hidden from the user interface.
