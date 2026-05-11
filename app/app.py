import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import pickle
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Blinkit AI Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ---------------- LOGIN SYSTEM ----------------
USERNAME = "admin"
PASSWORD = "blinkit123"

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.markdown("""
    <style>
    .login-container {
        background: linear-gradient(135deg,#111827,#1f2937);
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #F7C600;
        box-shadow: 0px 4px 25px rgba(0,0,0,0.6);
        margin-top: 50px;
    }

    .login-title {
        text-align:center;
        color:#F7C600;
        font-size:42px;
        font-weight:bold;
    }

    .login-subtitle {
        text-align:center;
        color:gray;
        font-size:18px;
        margin-bottom:30px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("""
        <div class='login-container'>
        <div class='login-title'>🛒 Blinkit AI Dashboard</div>
        <div class='login-subtitle'>Smart Grocery Analytics & ML Prediction System</div>
        </div>
        """, unsafe_allow_html=True)

        st.image(
            "https://cdn-icons-png.flaticon.com/512/3081/3081559.png",
            width=120
        )

        username = st.text_input("👤 Username")
        password = st.text_input("🔒 Password", type="password")

        remember = st.checkbox("Remember Me")

        col_a, col_b = st.columns(2)

        with col_a:
            login_btn = st.button("🚀 Login", use_container_width=True)

        with col_b:
            guest_btn = st.button("👀 Guest Demo", use_container_width=True)

        if login_btn:

            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.success("✅ Login Successful")
                st.balloons()
                st.rerun()

            else:
                st.error("❌ Invalid Username or Password")

        if guest_btn:
            st.info("Demo Credentials → demo_user / guest123")

        st.markdown("---")

        st.markdown(
            """
            <center>
            <h4 style='color:#F7C600;'>✨ Features Included</h4>
            </center>
            """,
            unsafe_allow_html=True
        )

        f1, f2 = st.columns(2)

        with f1:
            st.success("📊 Interactive Analytics")
            st.success("🤖 AI Sales Prediction")
            st.success("📈 Advanced Charts")

        with f2:
            st.success("🔥 Real-Time Insights")
            st.success("📂 Download Reports")
            st.success("🎨 Blinkit Theme UI")

    st.stop()

# ---------------- LOAD DATA ----------------
# df = pd.read_excel("BlinkIT Grocery Data.xlsx")
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "BlinkIT Grocery Data.csv"
)

df = pd.read_csv(DATA_PATH)

# ---------------- CREATE DATE COLUMN ----------------
df['Date'] = pd.date_range(
    start='2025-01-01',
    periods=len(df),
    freq='D'
)

df['Date'] = pd.to_datetime(df['Date'])

# ---------------- LOAD MODEL ----------------
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "sales_prediction_model.pkl"
)

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

     # st.success("✅ ML Model Loaded Successfully")

except FileNotFoundError:
    st.error(f"❌ Model file not found:\n{MODEL_PATH}")
    st.stop()

# ---------------- COLUMN NAMES ----------------
item_col = 'Item Type'
sales_col = 'Sales'
rating_col = 'Rating'
outlet_col = 'Outlet Size'

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background:
    linear-gradient(
        135deg,
        #0f0c29,
        #302b63,
        #24243e
    );
    background-size: cover;
    color: white;
}

/* GLASS EFFECT LOGIN BOX */

.login-container {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    border: 2px solid rgba(255,255,255,0.2);
    padding: 40px;
    border-radius: 30px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    margin-top: 30px;
}

/* TITLE */

.login-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #FFD700;
}

/* SUBTITLE */

.login-subtitle {
    text-align: center;
    color: #d1d5db;
    font-size: 18px;
    margin-bottom: 20px;
}

/* INPUT BOXES */

.stTextInput > div > div > input {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* BUTTONS */

.stButton button {
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(
        90deg,
        #F7C600,
        #ff9900
    );
    color: black;
    border: none;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px #F7C600;
}

/* FEATURE BOXES */

[data-testid="stAlert"] {
    border-radius: 15px;
    border: none;
}

/* REMOVE STREAMLIT MENU */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGO ----------------
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/2/2c/Blinkit-yellow-app-icon.svg",
    width=100
)

# ---------------- TITLE ----------------
st.markdown(
    """
    <h1 style='text-align:center;'>
    🛒 Blinkit Grocery Analytics Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <marquee behavior='scroll' direction='left'
    style='color:yellow;font-size:22px;'>
    🚀 Welcome to Blinkit AI Powered Grocery Analytics Dashboard 🚀
    </marquee>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align:center;color:gray;font-size:18px;'>
    AI Powered Grocery Sales Intelligence System
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Dashboard Filters")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "ML Prediction",
        "Dataset"
    ]
)

selected_items = st.sidebar.multiselect(
    "Select Item Types",
    options=df[item_col].unique(),
    default=list(df[item_col].unique())[:5]
)

filtered_df = df[df[item_col].isin(selected_items)]

# ---------------- KPI SECTION ----------------
total_sales = filtered_df[sales_col].sum()
avg_sales = filtered_df[sales_col].mean()
avg_rating = filtered_df[rating_col].mean()
total_products = filtered_df.shape[0]

best_category = (
    filtered_df.groupby(item_col)[sales_col]
    .sum()
    .idxmax()
)

profit = total_sales * 0.18

# ---------------- WEEKLY SALES ----------------
weekly_sales = (
    filtered_df
    .resample('W', on='Date')[sales_col]
    .sum()
    .reset_index()
)

# ---------------- DASHBOARD PAGE ----------------
if page == "Dashboard":

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("💰 Revenue", f"₹ {total_sales:,.0f}")
    c2.metric("📈 Profit", f"₹ {profit:,.0f}")
    c3.metric("⭐ Avg Rating", f"{avg_rating:.1f}")
    c4.metric("📦 Products", total_products)
    c5.metric("🏆 Best Category", best_category)

    st.markdown("---")

    st.subheader("📌 Business Insights")

    highest_sales = (
        filtered_df.groupby(item_col)[sales_col]
        .sum()
        .max()
    )

    best_outlet = (
        filtered_df.groupby(outlet_col)[sales_col]
        .sum()
        .idxmax()
    )

    st.info(
        f"🏆 Highest Sales Category: {best_category}"
    )

    st.success(
        f"💰 Highest Revenue Generated: ₹ {highest_sales:,.0f}"
    )

    st.warning(
        f"🏪 Best Performing Outlet Size: {best_outlet}"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # BAR CHART
    with col1:

        st.subheader("Sales by Item Type")

        sales_data = filtered_df.groupby(
            item_col
        )[sales_col].sum().reset_index()

        fig1 = px.bar(
            sales_data,
            x=item_col,
            y=sales_col,
            color=sales_col,
            template="plotly_dark",
            text_auto=True
        )

        st.plotly_chart(fig1, use_container_width=True)

    # PIE CHART
    with col2:

        st.subheader("Outlet Distribution")

        fig2 = px.pie(
            filtered_df,
            names=outlet_col,
            hole=0.6,
            template="plotly_dark"
        )

        st.plotly_chart(fig2, use_container_width=True)

    # LINE CHART
    st.subheader("Sales Trend")

    trend_data = filtered_df.groupby(
        item_col
    )[sales_col].mean().reset_index()

    fig3 = px.line(
        trend_data,
        x=item_col,
        y=sales_col,
        markers=True,
        template="plotly_dark"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ---------------- WEEKLY REVENUE ----------------
    st.subheader("📅 Weekly Revenue Trend")
    fig_weekly = px.line(
    weekly_sales,
    x='Date',
    y='Sales',
    markers=True,
    template='plotly_dark',
    title='Weekly Revenue Analysis'
)
    st.plotly_chart(fig_weekly, use_container_width=True)
    
    # ---------------- NEXT WEEK PREDICTION ----------------
    last_week_sales = weekly_sales['Sales'].iloc[-1]
    predicted_next_week = last_week_sales * 1.10
    st.success(f"🔮 Predicted Next Week Revenue: ₹ {predicted_next_week:,.0f}"
               )

# ---------------- ANALYTICS PAGE ----------------
elif page == "Analytics":

    col3, col4 = st.columns(2)

    # SCATTER PLOT
    with col3:

        st.subheader("Sales vs Rating")

        fig4 = px.scatter(
            filtered_df,
            x=rating_col,
            y=sales_col,
            color=item_col,
            template="plotly_dark"
        )

        st.plotly_chart(fig4, use_container_width=True)

    # TREEMAP
    with col4:

        st.subheader("Treemap Analysis")

        fig5 = px.treemap(
            filtered_df,
            path=[item_col],
            values=sales_col,
            color=sales_col,
            template="plotly_dark"
        )

        st.plotly_chart(fig5, use_container_width=True)

    # SUNBURST
    st.subheader("Sunburst Chart")

    fig6 = px.sunburst(
        filtered_df,
        path=[outlet_col, item_col],
        values=sales_col,
        template="plotly_dark"
    )

    st.plotly_chart(fig6, use_container_width=True)

    # FUNNEL CHART
    st.subheader("📊 Sales Funnel")

    funnel_data = filtered_df.groupby(item_col)[sales_col].sum().reset_index()

    fig_funnel = px.funnel(
        funnel_data,
        x=sales_col,
        y=item_col,
        template='plotly_dark'
    )

    st.plotly_chart(fig_funnel, use_container_width=True)

    # HEATMAP
    st.subheader("🔥 Correlation Heatmap")

    numeric_df = filtered_df.select_dtypes(include='number')

    fig, ax = plt.subplots(figsize=(10,6))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap='YlGnBu',
        ax=ax
    )

    st.pyplot(fig)

    # GAUGE CHART
    st.subheader("⭐ Customer Rating Gauge")

    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = avg_rating,
        title = {'text': "Average Rating"},
        gauge = {
            'axis': {'range': [0, 5]},
            'bar': {'color': "yellow"}
        }
    ))

    st.plotly_chart(fig_gauge, use_container_width=True)

# ---------------- ML PREDICTION PAGE ----------------
elif page == "ML Prediction":

    st.subheader("🔮 Predict Grocery Sales")

    st.write("Enter product details below.")

    col1, col2 = st.columns(2)

    # ---------- COLUMN 1 ----------
    with col1:

        item_weight = st.number_input(
            "Item Weight",
            min_value=0.0,
            value=12.0
        )

        item_visibility = st.number_input(
            "Item Visibility",
            min_value=0.0,
            value=0.05
        )

        item_mrp = st.number_input(
            "Item MRP",
            min_value=0.0,
            value=150.0
        )

        outlet_age = st.number_input(
            "Outlet Age",
            min_value=1,
            value=10
        )

    # ---------- COLUMN 2 ----------
    with col2:

        item_fat = st.selectbox(
            "Item Fat Content",
            ["Low Fat", "Regular"]
        )

        outlet_size = st.selectbox(
            "Outlet Size",
            ["Small", "Medium", "High"]
        )

        outlet_location = st.selectbox(
            "Outlet Location Type",
            ["Tier 1", "Tier 2", "Tier 3"]
        )

        outlet_type = st.selectbox(
            "Outlet Type",
            [
                "Supermarket Type1",
                "Supermarket Type2",
                "Supermarket Type3",
                "Grocery Store"
            ]
        )

    # ---------- ENCODING ----------
    item_fat_encoded = 0 if item_fat == "Low Fat" else 1

    outlet_size_map = {
        "Small": 0,
        "Medium": 1,
        "High": 2
    }

    outlet_location_map = {
        "Tier 1": 0,
        "Tier 2": 1,
        "Tier 3": 2
    }

    outlet_type_map = {
        "Grocery Store": 0,
        "Supermarket Type1": 1,
        "Supermarket Type2": 2,
        "Supermarket Type3": 3
    }

    outlet_size_encoded = outlet_size_map[outlet_size]
    outlet_location_encoded = outlet_location_map[outlet_location]
    outlet_type_encoded = outlet_type_map[outlet_type]

    # Dummy encoded values
    item_type_encoded = 5
    item_identifier_encoded = 100
    outlet_identifier_encoded = 10

    # ---------- PREDICTION ----------
    if st.button("🚀 Predict Sales"):

    try:

        input_data = [
            item_weight,
            item_visibility,
            item_mrp,
            outlet_age,
            item_fat_encoded,
            item_type_encoded,
            outlet_size_encoded,
            outlet_location_encoded,
            outlet_type_encoded
        ]

        st.write("Input Features:", len(input_data))
        st.write(input_data)

        prediction = model.predict([input_data])

        st.success(
            f"🛒 Predicted Sales: ₹ {prediction[0]:,.2f}"
        )

    except Exception as e:

        st.error(f"❌ Error: {e}")


# ---------------- DATASET PAGE ----------------
elif page == "Dataset":

    st.subheader("📂 Dataset Preview")

    st.dataframe(filtered_df)

    csv = filtered_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 Download Dataset CSV",
        data=csv,
        file_name='blinkit_dataset.csv',
        mime='text/csv'
    )

# ---------------- CONCLUSION ----------------
st.markdown("---")

st.subheader("📌 Conclusion")

st.write(
    "This dashboard helps analyze grocery sales trends, customer behavior, outlet performance, and predicts future sales using Machine Learning."
)

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    """
    <center>
    <h4 style='color:gray;'>
    Developed using Streamlit • Plotly • Machine Learning
    </h4>
    </center>
    """,
    unsafe_allow_html=True
)
