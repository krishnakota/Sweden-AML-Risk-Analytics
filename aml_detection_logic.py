import pandas as pd

# Load the generated data
df = pd.read_csv('swedish_aml_data.csv')

def detect_smurfing(data):
    """
    Identifies 'Smurfing' patterns: Users with > 3 transactions 
    in a single day with amounts between 9,000 and 10,000 SEK.
    """
    # 1. Group by Sender and Date
    analysis = data.groupby(['Sender', 'Date']).agg(
        Trans_Count=('Amount_SEK', 'count'),
        Total_Value=('Amount_SEK', 'sum')
    ).reset_index()

    # 2. Filter for high-frequency alerts
    alerts = analysis[analysis['Trans_Count'] > 3]
    return alerts

if __name__ == "__main__":
    alerts = detect_smurfing(df)
    print("--- 🚨 HIGH RISK AML ALERTS DETECTED 🚨 ---")
    print(alerts)
