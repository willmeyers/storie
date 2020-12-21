# storie
Started as a way to find TP in stores, now a way to find anything in popular US retailers.

## Install

```
pip install storie
```

At the moment, `storie` supports four large US retailers: Target, Costco, Walmart, and Walgreens.
I plan supporting more in the future. 

### Retailer

Each supported retailer inherits from an abstract `Retailer` class.

`storie` supports the following retialers:

- Target
- Costco
- Walmart
- Walgreens

You can access each retailer by importing their respective modules.

```python
from storie import target, costco, walmart, walgreens

t = target.Target(...)
c = costco.Costco(...)
wm = walmart.Walmart(...)
wg = walgreens.Walgreens(...)
```

**All retailers inherit from the same abstract `Retailer`, hence all the public methods and models 
are the same throughout all retailers.**

#### Quickstart

As an example, we'll use Target, but the examples are the same on all other retailers.

##### Get Products from a Specific Category
```python
from storie.target import Target

t = Target(get_closest_store_to=10034)

t.get_products(query='apples', categories=['Grocery'])
# [<Product>, ...]
```

##### Check if a Product is in Stock

```python
from storie.target import Target

t = Target(get_closest_store_to=10034)

apples = t.get_products('apples', categories=['Grocery'])

in_stock_apples = filter(lambda p: p.in_stock, apples)
```

#### Documentation

##### get_store

Returns a `Store` or `None` if a store is not found.

##### get_stores

Returns a list of `Store` objects.

##### get_product

Returns a product that matches the given id.

##### get_products



Returns a list of products that match the given parameters

