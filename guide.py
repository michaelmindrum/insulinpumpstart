import streamlit as st

def calculate_pump_settings(tdd, weight):
    """Calculates insulin pump settings based on TDD and weight."""
    pump_tdd = tdd * 0.75
    weight_based_tdd = weight * 0.23
    averaged_pump_tdd = (pump_tdd + weight_based_tdd) / 2
    
    total_daily_basal = averaged_pump_tdd * 0.5
    initial_basal_rate = total_daily_basal / 24
    correction_factor = 1700 / averaged_pump_tdd
    carb_ratio = 450 / averaged_pump_tdd
    
    return {
        "Pump TDD": pump_tdd,
        "Weight-Based TDD": weight_based_tdd,
        "Averaged Pump TDD": averaged_pump_tdd,
        "Total Daily Basal": total_daily_basal,
        "Initial Basal Rate (U/hr)": initial_basal_rate,
        "Correction Factor (mg/dL per unit)": correction_factor,
        "Carb Ratio (g per unit)": carb_ratio,
    }

def main():
    st.title("MDI to Insulin Pump Transition Calculator")
    st.write("This tool helps transition from multiple daily injections (MDI) to an insulin pump.")
    
    tdd = st.number_input("Total Daily Insulin Dose (TDD) (units):", min_value=1.0, step=0.1)
    weight = st.number_input("Current Body Weight (lbs):", min_value=1.0, step=0.1)
    
    if st.button("Calculate Pump Settings"):
        results = calculate_pump_settings(tdd, weight)
        
        st.subheader("Calculated Pump Settings")
        for key, value in results.items():
            st.write(f"**{key}:** {value:.2f}")
    
if __name__ == "__main__":
    main()
