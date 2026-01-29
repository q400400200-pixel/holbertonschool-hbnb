-- ===============================
-- Test CRUD Operations
-- ===============================

-- ===============================
-- READ: عرض البيانات الأساسية
-- ===============================

SELECT * FROM users;
SELECT * FROM amenities;
SELECT * FROM places;
SELECT * FROM reviews;

-- ===============================
-- CREATE: إدخال بيانات تجريبية
-- ===============================

-- إدخال مستخدم عادي
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
    'Test',
    'User',
    'testuser@example.com',
    'hashed_password_example',
    FALSE
);

-- إدخال مكان يملكه المستخدم
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id)
VALUES (
    'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
    'Test Place',
    'A place for testing CRUD operations',
    100.00,
    24.7136,
    46.6753,
    'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'
);

-- إدخال تقييم للمكان
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
    'cccccccc-cccc-cccc-cccc-cccccccccccc',
    'Great place!',
    5,
    'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
    'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb'
);

-- ربط مكان بمرفق (WiFi)
INSERT INTO place_amenity (place_id, amenity_id)
VALUES (
    'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
    (SELECT id FROM amenities WHERE name = 'WiFi')
);

-- ===============================
-- UPDATE: تعديل بيانات
-- ===============================

UPDATE users
SET last_name = 'UserUpdated'
WHERE id = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa';

UPDATE places
SET price = 120.00
WHERE id = 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb';

-- ===============================
-- READ: التحقق بعد التعديل
-- ===============================

SELECT * FROM users WHERE id = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa';
SELECT * FROM places WHERE id = 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb';

-- ===============================
-- DELETE: حذف البيانات التجريبية
-- ===============================

DELETE FROM reviews WHERE id = 'cccccccc-cccc-cccc-cccc-cccccccccccc';
DELETE FROM place_amenity WHERE place_id = 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb';
DELETE FROM places WHERE id = 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb';
DELETE FROM users WHERE id = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa';

-- ===============================
-- READ: تأكيد الحذف
-- ===============================

SELECT * FROM users;
SELECT * FROM places;
SELECT * FROM reviews;
