# Inventory Database Web App

A simple web application for managing inventory using Django. This app provides basic CRUD (Create, Read, Update, Delete) functionalities to help you keep track of your inventory items.

## Features

- **Create**: Add new items to the inventory.
- **Read**: View all items in the inventory.
- **Update**: Edit existing inventory items.
- **Delete**: Remove items from the inventory.

## Technologies Used

- Django
- Python
- SQLite (or your preferred database)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inventory-database.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd inventory-database
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- To add a new item, click on the "Add Item" button.
- To view items, navigate to the main inventory page.
- To edit or delete an item, select the item from the list.

## Contributing

Feel free to fork the repository and submit pull requests for improvements or features!

## License

This project is licensed under the MIT License
```
