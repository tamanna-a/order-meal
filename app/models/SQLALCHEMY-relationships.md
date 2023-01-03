Flask & Flask- SQL Alchemy Model Relationships

# One to Many Relationship
- relationship defined on the one object

Kitchen to Items (One to Many Relationship)
One- Kitchen
Many - Items

In `Kitchen`,
- define relationship
  - lets database know that it has a relationship to something else
- `items = db.relationship('Item, backref = 'kitchen')`
  - 'Item' 
    - in upper case, the class name
  - `backref = 'kitchen'` 
    - how the Item class is going to refer back to kitchen class
    - so if we have an Item, and we say Item.kitchen
    - it would return a Kitchen object
this defines half the relationship.

## How does Item refer to kitchen?
In Items,
- add kitchen_id
- define foreign key
  - use the kitchen table and use the id column to relate the table

# One to One relationship
similar to one to many, but has additional property `uselist`
- set `uselist = False`
  - instead of maintaining list, it keeps a one-to-one relationship
`guild = db.relationship("Guild", backref = 'director', uselist = False`
- in Guild, add director_id = Foreignkey..

# Many to many relationship
- requires join tables to maintain id mapping/relationships
- do not need to use `relationship`

# convert to json
- jsonify
  - from flask, converts to response object
  - returns a response object
  - `rsp_str = {"status": "healthy"}
    jsonify(rsp_str)`
- 
- json.dumps
  - converts dictionary to json
  - `rsp_str = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)`
  - then need response object
    - `rsp = Response(rsp_str, status=200, content_type="application/json")
`
  - 
- 