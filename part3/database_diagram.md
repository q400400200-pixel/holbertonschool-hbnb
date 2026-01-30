# HBnB Database ER Diagram

```mermaid
erDiagram

    USER {
        CHAR(36) id
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR email
        VARCHAR password
        BOOLEAN is_admin
    }

    PLACE {
        CHAR(36) id
        VARCHAR title
        TEXT description
        DECIMAL price
        FLOAT latitude
        FLOAT longitude
        CHAR(36) owner_id
    }

    REVIEW {
        CHAR(36) id
        TEXT text
        INT rating
        CHAR(36) user_id
        CHAR(36) place_id
    }

    AMENITY {
        CHAR(36) id
        VARCHAR name
    }

    PLACE_AMENITY {
        CHAR(36) place_id
        CHAR(36) amenity_id
    }

    USER ||--o{ PLACE : owns
    USER ||--o{ REVIEW : writes
    PLACE ||--o{ REVIEW : receives
    PLACE ||--o{ PLACE_AMENITY : has
    AMENITY ||--o{ PLACE_AMENITY : includes
