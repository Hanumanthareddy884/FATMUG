BEGINING SETUP

create new env file:
python -m venv env

Clone the repository:
git clone https://github.com/Hanumanthareddy884/FATMUG.git

setup the folder: cd vendor

Activate env:
.\env\scripts\activate

Install dependencies:
pip install -r requirements.txt

Setup postgres connection:
Create new vendor database and password:admin@123

Apply database migrations:
python manage.py migrate

Create Super user account:
python manage.py createsuperuser
set user name and password

Run the development server using following command:
python manage.py runserver

----------------------------------------------
API instruction Details

API Endpoint Details:

i am used modelviewset
All APIs Authentication required

VENDORS:

* List/Create Vendors:

URL: api/vendors/
Method: GET (List Vendors), POST (Create Vendor)

* Retrieve/Update Vendor:

URL: api/vendors/<int:pk>/
Method: GET (Retrieve Vendor), PUT (Update Vendor)

* Delete Vendor:
URL: api/vendors/delete/<int:pk>/
Method: DELETE


PURCHASE ORDERS:

* List/Create Purchase Orders:

URL: api/purchase-orders/
Method: GET and POST Purchase Order

* Retrieve/Update Purchase Order:

URL: api/purchase-orders/<int:pk>/
Method: GET,PUT,Delete

--------------------------------------------

Acknowledge Purchase Order:

URL: api/purchase-orders/<int:pk>/acknowledge/
Method: PUT Ack purchader order

Retrieve Vendor Performance:
URL: /vendors/<int:pk>/performance/
Method: GET performance based on vendor

If anything fell free to contact me: reddyreddy884@gmail.com
