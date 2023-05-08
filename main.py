import pandas as pd
from pytrends.request import TrendReq
import time
import matplotlib.pyplot as plt
# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Keywords to search for
keywords = [
 'Digital exhaustion','Internet weariness','Cyber fatigue','Web burnout','Screen exhaustion','Electronic overload','Online stress','Internet strain','Digital overwhelm','E-fatigue','Virtual burnout','Screen weariness','Digital drained','Cyber burnout','Web fatigue','Connection overload','Online depletion','Internet overload','Screen burnout','E-strain','Digital distress','Cyber weariness','Internet exhaustion','Electronic fatigue','Screen strain','Virtual exhaustion','Online weariness','Digital saturation','Internet burnout','E-exhaustion','Screen overload','Cyber strain','Virtual fatigue','Web exhaustion','Electronic burnout','Online overload','Digital strain','Internet distress','Cyber exhaustion','Web weariness','Electronic strain','Screen saturation','E-depletion','Virtual burnout','Digital depletion','Online strain','Web overload','Internet fatigue','Cyber distress','E-weariness','Virtual strain','Screen exhaustion','Electronic exhaustion','Web strain','Digital burnout','Internet weariness','Cyber saturation','Online exhaustion','Connection fatigue','E-strain','Screen stress','Virtual weariness','Web burnout','Electronic stress','Online fatigue','Internet stress','Cyber fatigue','Connection strain','Web exhaustion','Screen overload','Virtual exhaustion','E-distress','Digital stress','Internet strain','Cyber exhaustion','Connection weariness','Online weariness','Web stress','Electronic overload','Screen burnout','Virtual burnout','Digital overload','Internet overload','Cyber stress','E-fatigue','Web fatigue','Connection distress','Online stress','Screen weariness','Virtual strain','Electronic fatigue','Web overload','Digital burnout','Internet stress','Cyber weariness','Connection exhaustion','Online strain','Web exhaustion','Electronic stress','Screen strain','Virtual weariness','Digital stress','Internet fatigue','Cyber overload','Connection burnout','Online exhaustion','Web weariness','Electronic burnout','Screen fatigue','Virtual strain','E-depletion','Digital weariness','Internet exhaustion','Cyber burnout','Connection strain','Online overload','Web stress','Electronic fatigue','Screen exhaustion','Virtual saturation','E-overload','Digital distress','Internet weariness','Cyber exhaustion','Connection fatigue','Online burnout','Web strain','Electronic overload','Screen burnout','Virtual exhaustion','E-distress','Digital saturation','Internet fatigue','Cyber stress','Connection weariness','Online exhaustion','Web overload','Electronic strain','Screen saturation','Virtual burnout','E-fatigue','Digital depletion','Internet strain','Cyber wear'
]

# Group the keywords in sets of 5 since pytrends only allows up to 5 keywords per request
keyword_groups = [keywords[i:i + 5] for i in range(0, len(keywords), 5)]

# Initialize a DataFrame to store the results
trend_data = pd.DataFrame()

# Get trend scores for each group of keywords
for group in keyword_groups:
    pytrends.build_payload(group, timeframe='today 5-y', geo='', gprop='')
    group_data = pytrends.interest_over_time().drop(columns=['isPartial'])
    
    # Join unique columns
    unique_columns = [col for col in group_data.columns if col not in trend_data.columns]
    trend_data = trend_data.join(group_data[unique_columns], how='outer')
    
    # Wait for 0.1 seconds before making the next request
    time.sleep(0.1)

# Reset the index of the DataFrame
trend_data.reset_index(inplace=True)

# Print the trend scores
print(trend_data)
trend_data.to_csv('trend_data.csv', index=False)

top_5_keywords = trend_data.mean().nlargest(5).index
trend_data.plot(x='date', y=top_5_keywords, figsize=(15, 8), title='Top 10 Keyword Trends')

plt.ylabel('Trend Score')
plt.show()