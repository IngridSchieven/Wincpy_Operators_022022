# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
# Exercise: Operators
# example
spain_total_area = 505307
switzerland_total_area = 41277
#print(spain_total_area > switzerland_total_area)

# 1. language most spoken - the same ==
switzerland_most_spoken_language = "Castilian Spanish"
spain_most_spoken_language = "German"
print(switzerland_most_spoken_language == spain_most_spoken_language)

# 2. most prevelant religion - the same ==
switzerland_most_prevalent_religion = "Roman Catholic"
spain_most_prevalent_religion = "Roman Catholic" 
print(switzerland_most_prevalent_religion == spain_most_prevalent_religion)

# 3. name lenght capital - not equal !=
spain_capital = "Madrid"
switzerland_capital = "Bern"
print(len(spain_capital) != len(switzerland_capital)) 

# 4. GDP
switzerland_gdp = 731.502 #billion
spain_gdp = 1393.351 #billion
print(switzerland_gdp > spain_gdp)

# 5. Population growth
switzerland_pop_growth = 0.65 #procent
spain_pop_growth = -0.03 #procent
#print(switzerland_pop_growth <1) and (spain_pop_growth <1)
#merge and add variable percent
percent_growth = 1 #procent
print(switzerland_pop_growth and spain_pop_growth < percent_growth)

# 6. Population count over 10 million at least (groter of gelijk >=)
spain_pop_count = 47260584
switzerland_pop_count = 8453550
pop_count_at_least = 10000000
print((spain_pop_count or switzerland_pop_count) >= pop_count_at_least)

#vergelijkings-variant
#if spain_pop_count or switzerland_pop_count >= pop_count_at_least:
#    print(True) 

# 7. Population count over 10 million exactly
print (switzerland_pop_count < pop_count_at_least and spain_pop_count > pop_count_at_least) or (switzerland_pop_count > pop_count_at_least and spain_pop_count < pop_count_at_least)
#vergelijkings-variant
#bedenk wanneer je 3 varianten zou hebben, hoe zou het er dan uit zien

#Ten_million_both1 = (Spain_population > 10) and (Switzerland_population > 10)
#Ten_million_both2 = (Spain_population < 10) and (Switzerland_population < 10)


