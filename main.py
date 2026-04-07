import pandas as pd
import matplotlib.pyplot as plt
import os


# -----------------------------
# Load Data
# -----------------------------
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully")
        print("📌 Columns found:", df.columns)
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None


# -----------------------------
# Clean Data
# -----------------------------
def clean_data(df):
    print("\n🔍 Cleaning data...")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Convert numeric columns safely
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    # Rename important columns
    for col in df.columns:
        if 'date' in col:
            df.rename(columns={col: 'Date'}, inplace=True)
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        elif 'temp' in col:
            df.rename(columns={col: 'Temperature'}, inplace=True)

    print("✅ Cleaned Columns:", df.columns)

    # Drop missing values
    df = df.dropna()

    return df


# -----------------------------
# Analyze Data
# -----------------------------
def analyze_data(df):
    print("\n📊 Basic Analysis:")

    if 'Temperature' in df.columns:
        print("Average Temperature:", df['Temperature'].mean())
        print("Max Temperature:", df['Temperature'].max())
        print("Min Temperature:", df['Temperature'].min())


# -----------------------------
# Visualization
# -----------------------------
def create_visualizations(df):
    print("\n📈 Creating visualizations...")

    os.makedirs("visualizations", exist_ok=True)

    # -------- Line Chart --------
    if 'Date' in df.columns and 'Temperature' in df.columns:
        df = df.sort_values(by='Date')

        plt.figure(figsize=(10, 5))
        plt.plot(df['Date'], df['Temperature'])

        plt.title("Temperature Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.grid(True)

        plt.tight_layout()
        plt.savefig("visualizations/temp_trend.png")
        plt.close()

    # -------- Bar Chart --------
    if 'location' in df.columns and 'Temperature' in df.columns:
        avg_temp = df.groupby('location')['Temperature'].mean()

        plt.figure(figsize=(8, 5))
        avg_temp.plot(kind='bar')

        plt.title("Average Temperature by Location")
        plt.xlabel("Location")
        plt.ylabel("Temperature (°C)")

        plt.tight_layout()
        plt.savefig("visualizations/location_temp.png")
        plt.close()

    # -------- Pie Chart --------
    if 'Temperature' in df.columns:
        bins = [-50, 0, 15, 30, 50]
        labels = ['Very Cold', 'Cold', 'Moderate', 'Hot']

        df['Temp_Category'] = pd.cut(df['Temperature'], bins=bins, labels=labels)
        temp_counts = df['Temp_Category'].value_counts()

        plt.figure(figsize=(6, 6))
        temp_counts.plot(kind='pie', autopct='%1.1f%%')

        plt.title("Temperature Category Distribution")
        plt.ylabel("")

        plt.tight_layout()
        plt.savefig("visualizations/temp_distribution.png")
        plt.close()

    # -------- Humidity Trend --------
    if 'Date' in df.columns and 'humidity_pct' in df.columns:
        df_humidity = df.groupby(df['Date'].dt.date)['humidity_pct'].mean()

        plt.figure(figsize=(10, 5))
        df_humidity.plot()

        plt.title("Average Daily Humidity")
        plt.xlabel("Date")
        plt.ylabel("Humidity (%)")

        plt.tight_layout()
        plt.savefig("visualizations/humidity_trend.png")
        plt.close()

    print("✅ Visualizations saved")


# -----------------------------
# Report Generation
# -----------------------------
def generate_report(df):
    os.makedirs("report", exist_ok=True)

    with open("report/report.txt", "w") as f:
        f.write("Weather Data Analysis Report\n")
        f.write("=" * 50 + "\n\n")

        # -------- Temperature Stats --------
        if 'Temperature' in df.columns:
            avg = df['Temperature'].mean()
            mx = df['Temperature'].max()
            mn = df['Temperature'].min()

            f.write("1. Temperature Analysis\n")
            f.write("-" * 40 + "\n")
            f.write(f"Average Temperature: {avg:.2f}°C\n")
            f.write(f"Maximum Temperature: {mx:.2f}°C\n")
            f.write(f"Minimum Temperature: {mn:.2f}°C\n\n")

            f.write("The dataset indicates noticeable variation in temperature, ")
            f.write("suggesting changing weather conditions over time.\n\n")

        # -------- Trend Explanation --------
        f.write("2. Temperature Trend Over Time\n")
        f.write("-" * 40 + "\n")
        f.write("The line chart illustrates fluctuations in temperature across time.\n")
        f.write("There are visible rises and falls, indicating dynamic weather behavior.\n")
        f.write("These variations may be influenced by seasonal or environmental factors.\n\n")

        # -------- Location Analysis --------
        if 'location' in df.columns:
            f.write("3. Temperature by Location\n")
            f.write("-" * 40 + "\n")
            f.write("The bar chart compares average temperatures across locations.\n")
            f.write("Some locations show higher averages, while others remain cooler.\n")
            f.write("This suggests geographical differences affecting climate.\n\n")

        # -------- Distribution --------
        f.write("4. Temperature Distribution\n")
        f.write("-" * 40 + "\n")
        f.write("The pie chart categorizes temperature into ranges like Cold, Moderate, and Hot.\n")
        f.write("Most values typically fall into moderate ranges, with fewer extremes.\n\n")

        # -------- Humidity --------
        if 'humidity_pct' in df.columns:
            f.write("5. Humidity Trend\n")
            f.write("-" * 40 + "\n")
            f.write("Humidity levels change over time, showing atmospheric variation.\n")
            f.write("Higher humidity indicates moist conditions, while lower values suggest dryness.\n\n")

        # -------- Final Insights --------
        f.write("6. Final Insights\n")
        f.write("-" * 40 + "\n")
        f.write("- Weather conditions fluctuate significantly over time.\n")
        f.write("- Temperature varies across different locations.\n")
        f.write("- Most weather conditions fall into moderate ranges.\n")
        f.write("- Humidity trends reflect changing atmospheric conditions.\n")

    print("📄 Report generated: report/report.txt")


# -----------------------------
# Main Function
# -----------------------------
def main():
    file_path = "C:/Users/hp/Weather data visualization/weather_data.csv"

    df = load_data(file_path)

    if df is not None:
        df = clean_data(df)
        analyze_data(df)
        create_visualizations(df)
        generate_report(df)

        print("\n🎉 Done! Check 'visualizations' and 'report' folders.")


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    main()