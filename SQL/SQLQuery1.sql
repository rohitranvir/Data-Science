with e as (
  select year , population,
  lag(population,1) over(order by year asc) as prev_yr_pct
  from population
 )
 select year,population,