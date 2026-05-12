import pandas as pd
import random

channels = [
    "Meta",
    "Google",
    "YouTube",
    "Instagram",
    "LinkedIn",
    "Twitter",
    "Snapchat",
    "Pinterest",
    "TikTok",
    "Email"
]

data = []

for _ in range(2000):

    channel = random.choice(channels)

    spend = random.randint(500, 5000)

    revenue = spend * random.uniform(2.0, 6.0)

    impressions = random.randint(10000, 500000)

    clicks = random.randint(1000, 50000)

    conversions = random.randint(50, 5000)

    ctr = round((clicks / impressions) * 100, 2)

    roas = round(revenue / spend, 2)

    data.append([
        channel,
        spend,
        round(revenue, 2),
        impressions,
        clicks,
        conversions,
        ctr,
        roas
    ])

df = pd.DataFrame(
    data,
    columns=[
        "channel",
        "spend",
        "revenue",
        "impressions",
        "clicks",
        "conversions",
        "ctr",
        "roas"
    ]
)

df.to_csv(
    "data/incoming/marketing_data.csv",
    index=False
)

print("1000-row marketing dataset created successfully!")
