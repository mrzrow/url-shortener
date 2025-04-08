# URL SHORTENER

A microservice that allows users to create a short, unique URL alias. This alias can then be used in the browser's address bar to redirect to the original website.

---

## Run

Create a `docker-compse.yml` file using the following template. Specify the values:

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

Run `docker-compose up --build` in command line.
The service will be available at: `127.0.0.1:8888`.

---

## Endpoints

#### POST `/v1/url/`

Creates short URL

Request Body Example:

```json
{
    "url": "https://example.com/"    
}
```

Response Example:

```json
{
    "short_url": "https://example.com/"
}
```

#### GET `/v1/url/{short_url}`

Performs redirection.

Request Parameters:

- **short_url** `[string]` - short alias of the URL

#### GET `/v1/url/id/{url_id}`

Gets URL object from database.

Request Parameters:

- **url_id** `[int]` - ID of the URL in database.
  
Response Example:

```json
{
  "id": 0,
  "url": "string",
  "short_url": "string"
}
```
