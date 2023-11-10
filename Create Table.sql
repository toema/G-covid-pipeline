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
<<<<<<< HEAD

CREATE TABLE IF NOT EXISTS minio.c19.aggregated_cc_by (
  open_covid_region_code VARCHAR,
  region_name VARCHAR,
  date VARCHAR,
  cases_cumulative VARCHAR,
  cases_new VARCHAR,
  cases_cumulative_per_million VARCHAR,
  cases_new_per_million VARCHAR,
  deaths_cumulative VARCHAR,
  deaths_new VARCHAR,
deaths_cumulative_per_million VARCHAR,
deaths_new_per_million VARCHAR,
tests_cumulative VARCHAR,
tests_new VARCHAR,
tests_cumulative_per_thousand VARCHAR,
tests_new_per_thousand VARCHAR,
 test_units VARCHAR,
 hospitalized_current VARCHAR,
 icu_current VARCHAR,
 ventilator_current VARCHAR
)
WITH (
  external_location = 's3a://c19/exports',
  format = 'CSV'
);
=======
>>>>>>> refs/remotes/origin/main
