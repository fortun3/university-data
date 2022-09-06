# university-data


http://universities.hipolabs.com/search?country=YOUR_COUNTRY
Using this API to get universities data and saving for future use.

## Methods used

### Sessions
Using session is like opening a browsing session with your script and the server. It handles multiple API calls much faster than single requests.

### Multithreading
When making multiple API calls, using multithread speeds up the program speed at least 10x times. Here none of the API calls dependent on each other. So with ThreadPoolExecutor we can have multithreading implemented easily.

### MySQL Database
Connection and using MySQL Database to save the result from API calls for future use case.
