# Little Lemon API Project

A fully functioning API project for a hypothetical restaurant called Little Lemon. Client application developers can use the APIs to develop web and mobile applications. People with different roles are able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders.

## Functionality

The following actions can be performed while using this API:

-   The admin can assign users to the manager group
-   You can access the manager group with an admin token
-   The admin can add menu items
-   The admin can add categories
-   Managers can log in
-   Managers can update the item of the day
-   Managers can assign users to the delivery crew
-   Managers can assign orders to the delivery crew
-   The delivery crew can access orders assigned to them
-   The delivery crew can update an order as delivered
-   Customers can register
-   Customers can log in using their username and password and get access tokens
-   Customers can browse all categories
-   Customers can browse all the menu items at once
-   Customers can browse menu items by category
-   Customers can paginate menu items
-   Customers can sort menu items by price
-   Customers can add menu items to the cart
-   Customers can access previously added items in the cart
-   Customers can place orders
-   Customers can browse their own orders

## Implemented Endpoints

This section outlines the accessible API endpoints:

### User Endpoints:

Permissions: [No Role Required]

-   `/api/create-user` (POST) - Creates a new user with name, email, and password

Permissions: [Valid Users]

-   `/auth/users/me` (GET) - Displays only current user details
-   `/auth/token/login` (POST) - Generates access tokens that can be used in other API calls (only for valid users)

### Menu Item Endpoints:

Permissions: [Customers, Delivery Crew]

-   `/api/menu-items` (GET) - List all menu items, returns 200 OK
-   `/api/menu-items` (POST, PUT, PATCH, DELETE) - Returns 403 UNAUTHORIZED
-   `/api/menu-items/{menuItem}` (GET) - Lists a single menu item
-   `/api/menu-items/{menuItem}` (POST, PUT, PATCH, DELETE) - Return 403 UNAUTHORIZED

Permissions: [Managers]

-   `/api/menu-items` (GET) - List all menu items, returns 200 OK
-   `/api/menu-items` (POST) - Creates a new menu item, returns 201 - Created
-   `/api/menu-items/{menuItem}` (GET) - Lists a single menu item
-   `/api/menu-items/{menuItem}` (PUT, PATCH) - Updates a single menu item
-   `/api/menu-items/{menuItem}` (DELETE) - Deletes menu item

### User Group Management Endpoints:

Permissions: [Managers]

-   `api/groups/manager/users` (GET) - Returns all managers
-   `api/groups/manager/users` (POST) - Assign the user in the payload to the manager group (201 CREATED)
-   `api/groups/manager/users/{userId}` (DELETE) - 200 OK if everything is ok. If user not found, return 404
-   `api/groups/delivery-crew/users` (GET) - Assign user in payload to the delivery crew group (201 CREATED)
-   `api/groups/delivery-crew/users/{userID}` (DELETE) - 200 OK if deleted. If not found, returns 404

### Cart Endpoints:

Permissions: [Customer]

-   `/api/cart/menu-items` (GET) - Returns current items in cart for the current user token
-   `/api/cart/menu-items` (POST) - Adds the menu item to the cart. Set authenticated user as the user ID for
    these items
-   `/api/cart/menu-items` (DELETE) - Deletes all menu items added by the current user token

### Order Management Endpoints:

Permissions: [Customer]

-   `/api/orders` (GET): Returns all orders with order items created by the user
-   `/api/orders` (POST): Creates a new order item for the current user
-   `/api/orders/{orderId}` (GET): Returns all items for this order ID. Returns 404 if ID is invalid
-   `/api/orders/{orderId}` (PUT, PATCH): Updates an order

Permissions: [Manager]

-   `/api/orders` (GET): Returns all orders from all users
-   `/api/orders/{orderId}` (DELETE): Deletes a specific order

Permissions: [Delivery Crew]

-   `/api/orders` (GET): Returns all orders with items assigned to the delivery crew
-   `/api/orders/{orderId}` (PATCH): Update delivery status (0 undelivered, 1 delivered)

## Note

Use Insomnia to test is much more effective than using the browsable API view. Just open the database to view item/user IDs, for use as keys when making requests as they are the primary keys of their respective models.
