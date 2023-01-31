# Govisetha-Lotteries

Scrap the [Sri Lanka's Govisetha Lottery's Past Results](https://www.nlb.lk/results/govisetha) and analyze them to get the most repeated values.

## How to Setup?

- Install Requirements
    ```
    python -m pip install -r requirements.txt
    ```

- Run the Script
    ```
    python govisetha.py
    ```

## Output

- By default, two files will be generated
    1. `govisetha_analyzed.csv`
    2. `govisetha_analyzed.png`

### Sample `govisetha_analyzed.csv` File:

- The first column is the Value and the second column is the Count (the number of times that the value has been repeated)

```
Value,Count
25,19
10,18
71,17
```

- In this example above, the Value "25" has been repeated 19 times
- the Value "10" has been repeated 18 times
- the Value "71" has been repeated 17 times

### Sample `govisetha_analyzed.png` File:

![govisetha_analyzed](https://user-images.githubusercontent.com/36286877/215818000-de861ecc-e966-4770-9412-a67a06323d29.png)


