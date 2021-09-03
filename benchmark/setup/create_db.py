import h3.api.basic_int as h3
import numpy as np
import sys
import pymongo

def create_data(n):
	c = np.arange(n)
	a = np.random.uniform(low=10.361150797591193, high=11.14905794904022, size=(n, ))
	b = np.random.uniform(low=106.59572659658203, high=106.67503415273437, size=(n, ))
	d = np.random.randint(1, 10, size=(n, ))
	return c, a, b, d

def to_sql_form(c, a, b, d, resolution=7):
	func = lambda i, x, y, z: f"insert into Locations(driver_id, long, lat, hash_0, vehicle_type) values({i}, {x}, {y}, {h3.geo_to_h3(x, y, resolution)}, {z});\n"
	func = np.vectorize(func)

	return func(c, a, b, d)

file = open('db_init.sql', 'w')
file.writelines(to_sql_form(*create_data(int(sys.argv[1])), resolution=7))
file.write('insert into driver_table_view select driver_id, time_stamp from Locations;\n')
file.close()