create table Locations
(
    id serial8 primary key,
    driver_id int,
    long float4,
    lat float4,
    hash_0 bigint,
    time_stamp timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    vehicle_type int,
    available boolean default true
);

create index hash_index
    on Locations using hash (hash_0);

create index driver_id_index
    on Locations using btree (driver_id);

create index timestamp_index
    on Locations using brin (time_stamp);

create table driver_table_view
(
	driver_id int primary key,
	max_time timestamp with time zone
);

create index table_driver_id_index
    on driver_table_view using btree (driver_id) include (max_time);


create table WAL
(
	_id serial8 primary key,
	driver_id int,
	max_time timestamp with time zone
);

create index wal_id_index
    on WAL using btree (_id) include (driver_id, max_time);

create or replace function update_driver_view (n int)
returns table(changed_rows bigint)
language plpgsql
as
$$
begin

	return query
		with rows as (
			update driver_table_view
			set max_time = update_list.max_time
			from (select * from WAL where _id >= n order by _id desc) as update_list
			where driver_table_view.driver_id = update_list.driver_id
			returning 1
		)
	select count(*) from rows;

end;
$$;

create or replace function __log()
returns trigger
language plpgsql
as 
$$
begin
	insert into WAL(driver_id, max_time) values (new.driver_id, new.time_stamp);
	return new;
end;
$$;

create trigger wal_log after insert on Locations
for each row
execute function __log();