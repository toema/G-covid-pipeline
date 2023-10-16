CREATE TABLE IF NOT EXISTS minio.c19.country_wise_latest (
  Country_or_Region VARCHAR,
  Confirmed VARCHAR,
  Deaths VARCHAR,
  Recovered VARCHAR,
  Active VARCHAR,
  New_cases VARCHAR,
  New_deaths VARCHAR,
  New_recovered VARCHAR,
  Deaths_Per_100_Cases VARCHAR,
Recovered_Per_100_Cases VARCHAR,
Deaths_Per_100_Recovered VARCHAR,
Confirmed_last_week VARCHAR,
_1_week_change VARCHAR,
_1_week_Per_increase VARCHAR,
WHO_Region VARCHAR
)
WITH (
  external_location = 's3a://c19/',
  format = 'CSV'
);
