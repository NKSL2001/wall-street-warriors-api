### WIA1002 2022/2023 Semester 2
## Final Assignment Topic 5
# Wall Street Warriors API

This repository hosts the files required to run the REST API for the final assignment topic 5: Wall Street Warriors for WIA1002 2022/2023 Semester 2, Universiti Malaya.

> **Warning**
>
> DO NOT USE THIS API OUTSIDE OF YOUR FINAL PROJECT (Universiti Malaya WIA1002 2022/2023 Semester 2). WE DO NOT PROVIDE ANY GUARANTEE ON THE INFORMATION PROVIDED BY THE API, NOR WE WILL ASSUME RESPONSIBILITIES.

## API

You may access this API on the endpoint [`https://wall-street-warriors-api-um.vercel.app/`](https://wall-street-warriors-api-um.vercel.app/). API key is required for access for the API address below by appending the GET variable `apikey`. Follow the instructions provided in the project requirement PDF to get an API key for your final project.

Currently, two modules are provided:

### `price`
> **Warning**
> 
> Price might be delayed during trading time due to multiple reasons. We do not guarantee the timeliness of the API, but the functionality of this API should be enough for your project.

Allow checking of price for any particular stock symbol(s) in the last few days.

API call: `/price?apikey=APIKEY&symbol=XXXX`, multiple symbols can be requested by using comma to join them, e.g.: `symbol=AAPL,MSFT`.

Return format: JSON containing the symbol as the key, and a dictionary containing prices for multiple stages, mapping the epoch timestamp (in milliseconds) to price (in RM).

If the stock symbol is not found, the value of the symbol will be null, e.g. query for symbol "ZZZZ" will returns `{"ZZZZ": null}`.

<details>
    <summary>A sample of response JSON (truncated)</summary>

```
/price?apikey=APIKEY&symbol=4715.KL,4634.KL
{
  "4715.KL": {
    "Open": {
      "1683680400000": 2.72,
      "1683680700000": 2.72,
      "1683681000000": 2.71,
      "1683681300000": 2.71,
      "1683681600000": 2.71,
      ...
      "1684225800000": 2.69,
      "1684226100000": 2.7,
      "1684226400000": 2.7,
      "1684227000000": 2.7,
      "1684227300000": 2.7
    },
    "High": {
      "1683680400000": 2.72,
      "1683680700000": 2.72,
      "1683681000000": 2.71,
      "1683681300000": 2.71,
      "1683681600000": 2.71,
      ...
      "1684225800000": 2.7,
      "1684226100000": 2.71,
      "1684226400000": 2.7,
      "1684227000000": 2.7,
      "1684227300000": 2.7
    },
    "Low": {
      "1683680400000": 2.71,
      "1683680700000": 2.72,
      "1683681000000": 2.7,
      "1683681300000": 2.71,
      "1683681600000": 2.7,
      ...
      "1684225800000": 2.69,
      "1684226100000": 2.69,
      "1684226400000": 2.69,
      "1684227000000": 2.7,
      "1684227300000": 2.7
    },
    "Close": {
      "1683680400000": 2.72,
      "1683680700000": 2.72,
      "1683681000000": 2.7,
      "1683681300000": 2.71,
      "1683681600000": 2.7,
      ...
      "1684225800000": 2.69,
      "1684226100000": 2.7,
      "1684226400000": 2.69,
      "1684227000000": 2.7,
      "1684227300000": 2.7
    },
    "Volume": {
      "1683680400000": 0,
      "1683680700000": 74000,
      "1683681000000": 98200,
      "1683681300000": 2100,
      "1683681600000": 21600,
      ...
      "1684225800000": 41200,
      "1684226100000": 109400,
      "1684226400000": 111600,
      "1684227000000": 27300,
      "1684227300000": 3000
    },
    "Dividends": {
      "1683680400000": 0.0,
      "1683680700000": 0.0,
      "1683681000000": 0.0,
      "1683681300000": 0.0,
      "1683681600000": 0.0,
      ...
      "1684225800000": 0.0,
      "1684226100000": 0.0,
      "1684226400000": 0.0,
      "1684227000000": 0.0,
      "1684227300000": 0.0
    },
    "Stock Splits": {
      "1683680400000": 0.0,
      "1683680700000": 0.0,
      "1683681000000": 0.0,
      "1683681300000": 0.0,
      "1683681600000": 0.0,
      ...
      "1684225800000": 0.0,
      "1684226100000": 0.0,
      "1684226400000": 0.0,
      "1684227000000": 0.0,
      "1684227300000": 0.0
    }
  },
  "4634.KL": {
    "Open": {...},
    "High": {...},
    "Low": {...},
    "Close": {...},
    "Volume": {...},
    "Dividends": {...},
    "Stock Splits": {...},
  }
}

```

</details>


An additional GET parameter `days` may be specified, which will return the stock price with the following interval:
* Less than 5 days: Interval of 1 minute
* 5 to 9 days: Interval of 5 minutes
* 10 to 30 days: Interval of 15 minutes
* 31 to 60 days: Interval of 1 day

Records are only available up to 60 days.

### `mylist`
List all available stock symbols that are in Malaysia.

API call: `/mylist?apikey=APIKEY`.

Return format: JSON of a list of dictionary, of which contains the symbol, name, currency, exchange, MIC code, country (Malaysia) and type of stock.

<details>
    <summary>A sample of response JSON (truncated)</summary>

```
/mylist?apikey=APIKEY
[
    {"symbol": "0001.MY", "name": "SCOMNET", "currency": "MYR", "exchange": "MYX", "mic_code": "XKLS", "country": "Malaysia", "type": "Common Stock"},
    {"symbol": "0002.MY", "name": "KOTRA", "currency": "MYR", "exchange": "MYX", "mic_code": "XKLS", "country": "Malaysia", "type": "Common Stock"},
    ...
]

```

</details>


## Running Locally

Requires npm and Python installation.

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

## One-Click Deploy

You may choose to deploy this service on [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples) yourself too:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/NFSL2001/wall-street-warriors-api)

Add an environment variable to your project with the name `keys`, then use the key you have added in your code to access the API to your own end.

## Report problems

You may report any problem related to this API in the [Issues tab]().

## Dependencies

This API heavily relies on [yfinance](https://github.com/ranaroussi/yfinance), a Python module, for the real time price data.
