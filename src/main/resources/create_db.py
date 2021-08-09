import h3.api.basic_int as h3
import numpy as np
import sys
import pymongo

def create_data(n):
	c = np.arange(n)
	a = np.random.uniform(low=-90, high=90, size=(n, ))
	b = np.random.uniform(low=-180, high=180, size=(n, ))
	return c, a, b

def to_sql_form(c, a, b, resolution=7):
	func = lambda i, x, y: f"insert into Locations(driver_id, long, lat, hash_0) values({i}, {x}, {y}, {h3.geo_to_h3(x, y, resolution)});\n"
	func = np.vectorize(func)

	return func(c, a, b)

file = open('db_init.sql', 'w')
file.writelines(to_sql_form(*create_data(2000000), resolution=3))
file.close()