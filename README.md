# Test assignment for the company *webtronics.ru*

![FastAPI](https://img.shields.io/badge/FastAPI-FFCF40?style=for-the-badge&logo=fastapi&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-000000?style=for-the-badge&logo=python&logoColor=white) ![Pydantic](https://img.shields.io/badge/Pydantic-000000?style=for-the-badge&logo=python&logoColor=white) ![Alembic](https://img.shields.io/badge/Alembic-000000?style=for-the-badge&logo=python&logoColor=white) ![Postgres](https://img.shields.io/badge/postgresql-FFCF40?style=for-the-badge&logo=postgresql&logoColor=white)

# Tasks

- There should be some form of authentication and registration (JWT, Oauth, Oauth 2.0, etc..)
- As a user I need to be able to signup and login
- As a user I need to be able to create, edit, delete and view posts
- As a user I can like or dislike other users’ posts but not my own 
- The API needs a UI Documentation (Swagger/ReDoc)

# How to install
1. Clone a repository
```
git clone https://github.com/xodiumx/test_for_webtronics
```
2. Create a virtual environment
```
py -3.10 -m venv venv
```
3. Activate venv
```
source venv/Scripts/activate or source env/bin/activate
```
4. Download dependencies
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
5. Change directory
```
cd src
```
6. Create `.env` file
```
SECRET_KEY=KDOuifes@@ruy432iiupupifesUIPDASBDKGA3dko5OwCXyli1Il8M
USER_SECRET_KEY=KDOuifehtryuoigreuo@4327TG!!*&g8cbSAidsamopi~!^

SERVER_HOST=127.0.0.1
SERVER_PORT=8000

DB_HOST=localhost
DB_PORT=5432
DB_NAME=social
DB_USER=postgres
DB_PASS=admin
```
7. Use migrations
```
alembic upgrade head
```
8. Start app
```
uvicorn app:app --reload
```
# How it works

### Registation and authentication endpoints
```
- auth/jwt/login (POST)
- auth/jwt/logout (POST)
- auth/jwt/register (POST)
```
- The client sends a `POST` request to the endpoint `auth/jwt/register` in the form
```
{
  "email": "maks@example.com",
  "password": "maks1234",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}
```
- Fields `is_active`, `is_superuser`, `is_verified` - are changed to default during data processing
- Next, the client enters authorization data *email* and *password* by endpoint `/auth/jwt/login` and receives JWT - token which is stored in `cookie`
- on the `/post` endpoint all CRUD operations are available
- To create a like, the user sends a post request to the `/like` endpoint
- And for delete like, delete request to the `/like_remove` endpoint, same with dislikes

### Detailed documentation is available at the endpoint `/docs`
