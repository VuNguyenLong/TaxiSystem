create table Locations
(
    id serial8 primary key,
    driver_id int,
    long float4,
    lat float4,
    hash_0 bigint,
    time_stamp timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

create index hash_index
    on Locations using hash (hash_0);

create index driver_id_index
    on Locations using btree (driver_id);

create index timestamp_index
    on Locations using brin (time_stamp);