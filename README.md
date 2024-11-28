# Danelfin technical test API

This project contains a small api with one endpoint serving fixed data for testing purposes 


## Launch the API

### With Docker
```shell
  docker compose up
```

### Python
```shell
  pip3 install -r requirements.txt
  python3 -m flask run --host=0.0.0.0
```

## Usage
once the server is up and ready, you can connect to the only endpoint exposed
```shell
  curl http://localhost:5000/stocks
```

### Query Parameters
#### Filtering

You can filter the results by any property in the dataset. For example, filtering by isETF or country:

    Syntax: ?key=value
    Example: ?isETF=true&country=US

#### Pagination

Control the number of results and the starting point:

    limit: Maximum number of results to return.
        Default: 10
        Example: ?limit=5
    offset: Number of results to skip before starting to return data.
        Default: 0
        Example: ?offset=10

#### Sorting

Order the results by a specific field in ascending or descending order:

    order_by: The field to sort by.
        Default: None (no sorting applied)
        Example: ?order_by=id
    order_dir: The sorting direction (asc for ascending, desc for descending).
        Default: asc
        Example: ?order_dir=desc

#### Combining Filters, Sorting, and Pagination

You can combine multiple query parameters for more complex queries:

    Example: ?isETF=false&country=US&limit=5&offset=10&order_by=name&order_dir=asc

### Successful Response

* Status Code: 200 OK
* Body: JSON object with the following keys:
  * data: The list of filtered, sorted, and paginated results.
  * total: Total number of records after filtering.
  * limit: Limit applied to the query.
  * offset: Offset applied to the query.
  * order_by: The field used for sorting (if any).
  * order_dir: The sorting direction (asc or desc).

Example

```json lines
{
  "data": [
    {
      "id": 1,
      "name": "AAPL",
      "company": "Apple Inc",
      "shortName": "Apple",
      "country": "US",
      "isIn": "US0378331005",
      "isETF": false
    },
    {
      "id": 2,
      "name": "MSFT",
      "company": "Microsoft Corp",
      "shortName": "Microsoft",
      "country": "US",
      "isIn": "US5949181045",
      "isETF": false
    }
  ],
  "total": 2,
  "limit": 10,
  "offset": 0,
  "order_by": null,
  "order_dir": "asc"
}
```

### Error Response

* Status Code: 500 Internal Server Error
* Body: JSON object describing the error.

Example:
```json lines
{
  "error": "Invalid filter parameter provided"
}
```

