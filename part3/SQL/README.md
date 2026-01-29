# HBnB SQL Scripts

This project contains SQL scripts used to create the database schema
and insert initial data for the HBnB application.

The purpose of this task is to design the database structure using
raw SQL without relying on any ORM.

---

## Files

### create_tables.sql
Defines the database schema and creates all required tables:
- users
- places
- reviews
- amenities
- place_amenity

This script also defines:
- Primary keys
- Foreign key relationships
- Unique constraints
- Many-to-many relationship between places and amenities

---

### insert_initial_data.sql
Inserts initial data into the database, including:
- An administrator user with a fixed UUID and hashed password
- Initial amenities:
  - WiFi
  - Swimming Pool
  - Air Conditioning

---

### test_crud.sql
Contains sample SQL statements to test CRUD operations
(Create, Read, Update, Delete) on the database tables.

---

## Notes
- UUIDs are used as primary keys for all tables.
- Passwords are stored in hashed format.
- These scripts are written using standard SQL.
