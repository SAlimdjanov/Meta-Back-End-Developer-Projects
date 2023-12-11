# Little Lemon API Project

A fully functioning API project for a hypothetical restaurant called Little Lemon. Client application developers can use the APIs to develop web and mobile applications. People with different roles are able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders. (Work in Progress)

## Implemented Endpoints

**User Endpoints:**

Permissions: [No Role Required]

-   `users` (POST) - Creates a new user with name, email, and password

Permissions: [Valid Users]

-   `users/users/me` (GET) - Displays only current user details
-   `token/login` (POST) - Generates access tokens that can be used in other API calls (only for valid
    users)

**Menu Item Endpoints:**

Permissions: [Customers, Delivery Crew]

-   `menu-items` (GET) - List all menu items, returns 200 OK
-   `menu-items` (POST, PUT, PATCH, DELETE) - Returns 403 UNAUTHORIZED
-   `menu-items/{menuItem}` (GET) - Lists a single menu item
-   `menu-items/{menuItem}` (POST, PUT, PATCH, DELETE) - Return 403 UNAUTHORIZED

Permissions: [Managers]

-   `menu-items` (GET) - List all menu items, returns 200 OK
-   `menu-items` (POST) - Creates a new menu item, returns 201 - Created
-   `menu-items/{menuItem}` (GET) - Lists a single menu item
-   `menu-items/{menuItem}` (PUT, PATCH) - Updates a single menu item
-   `menu-items/{menuItem}` (DELETE) - Deletes menu item

**User Group Management Endpoints:**

Permissions: [Managers]

-   `groups/manager/users` (GET) - Returns all managers
-   `groups/manager/users` (POST) - Assign the user in the payload to the manager group (201 CREATED)
-   `groups/manager/users/{userId}` (DELETE) - 200 OK if everything is ok. If user not found, return 404
-   `groups/delivery-crew/users` (GET) - Assign user in payload to the delivery crew group (201 CREATED)
-   `groups/delivery-crew/users/{userID}` (DELETE) - 200 OK if deleted. If not found, returns 404

**Cart Endpoints:**

Permissions: [Customer]

-   `cart/menu-items` (GET) - Returns current items in cart for the current user token
-   `cart/menu-items` (POST) - Adds the menu item to the cart. Set authenticated user as the user ID for
    these items
-   `cart/menu-items` (DELETE) - Deletes all menu items added by the current user token

**Order Management Endpoints:**

Permissions: [Customer]

-   `orders` (GET): Returns all orders with order items created by the user
-   `orders` (POST): Creates a new order item for the current user
-   `orders/{orderId}` (GET): Returns all items for this order ID. Returns 404 if ID is invalid
-   `orders/{orderId}` (PUT, PATCH): Updates an order

Permissions: [Manager]

-   `orders` (GET): Returns all orders from all users
    `orders/{orderId}` (DELETE): Deletes a specific order

Permissions: [Delivery Crew]

-   `orders` (GET): Returns all orders with items assigned to the delivery crew
-   `orders/{orderId}` (PATCH): Update delivery status (0 undelivered, 1 delivered)
