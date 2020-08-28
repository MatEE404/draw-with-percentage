### Draw with percentages
Python library for randomizing given elements with the appropriate percentage chance.

#### Example:
Sample library usage

##### Code:
```python
from draw_with_percentage import draw_with_percentage

percentages = [
    ["option1", "10"],
    ["option2", "20"],
    ["option3", "30"],
    ["option4", "40"]
]

res = draw_with_percentage(percentages)
```

##### Response:
1. Option 1 10% chance will be refunded.
2. Option 2 20% chance will be refunded.
3. Option 3 30% chance will be refunded.
4. Option 4 40% chance will be refunded.


#### Request:
```json5
[
    ["name", "percent"],
    ["name", "percent"],
    ["name", "percent"],
    ["name", "percent"]
    // etc.
]
```
##### Remember:
* In the first field we give the name of the element.
* In the second field we give the percentage written as a string.
    * We write the percentage down to **three places** after the decimal point.
* The sum of all percentages must be 100.