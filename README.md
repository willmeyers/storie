# storie
Started as a way to find TP in stores, now a way to find anything in popular US retailers.

## Install

```
pip install storie
```

## Documentation

At the moment, `storie` supports four large US retailers: Target, Costco, Walmart, and Walgreens.
I plan supporting more in the future. 

### Retailer

Each supported retailer inherits from an abstract `Retailer` class.

`storie` supports the following retialers:

```python
from storie import target, costco, walmart, walgreens



```

##### Quickstart

```python
from storie import target

t = target.Target(get_closest_store_to=10034)

t.get_products(category='Grocery')
# [<models.Item>, ...]

```

##### get_store

Returns a `Store` object or `None` if a store is not found.

##### get_stores

Returns a list of `Store` objects.

##### get_product

##### get_products

