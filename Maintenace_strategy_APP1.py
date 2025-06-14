import streamlit as st
import pandas as pd
from PIL import Image
import graphviz
import os
import smtplib
from email.mime.text import MIMEText

# Ordered list of sidebar topics
topics = [
    "🏠 Welcome",
    "Overview of Maintenance Types",
    "Strategy Recommendation Tool",
    "Condition Monitoring Techniques",
    "D-I-P-F Curve",
    "Bathtub Curve",
    "Root Cause Analysis",
    "Failure Mode Library (FMEA Style)",
    "Maintenance Planning & Scheduling",
    "Spare Parts & Inventory Management",
    "Digital Maintenance Tools (CMMS, IIoT, AI)",
    "Maintenance KPIs Calculator",
    "Maintenance Safety",
    "Common Maintenance Mistakes & Myths",
    "Maintenance Quiz",
    "About"
]


# --- Visit Counter ---
counter_file = "visit_counter.txt"

# Initialize counter state only once per session
if "visit_logged" not in st.session_state:
    st.session_state.visit_logged = False

# Read the current count from file
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

with open(counter_file, "r") as f:
    count = int(f.read())

# Increment only once per session
if not st.session_state.visit_logged:
    count += 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    st.session_state.visit_logged = True


st.set_page_config(page_title="Maintenance Engineering Guide", layout="centered")

# Show visit count
st.caption(f"👁️ Total visits: **{count}**")

st.markdown("""
    <style>
    .custom-sidebar-label {
        position: fixed;
        top: 13px;
        left: 50px;
        z-index: 1001;
        font-size: 16px;
        font-weight: bold;
        color: #444;
    }

    /* Adjust for dark mode, optional */
    @media (prefers-color-scheme: dark) {
        .custom-sidebar-label {
            color: #eee;
        }
    }
    </style>
    <div class="custom-sidebar-label">📂 Topics</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #007acc;
        color: white;
        font-size: 1.1em;
        font-weight: bold;
        padding: 0.6em 1.2em;
        border: none;
        border-radius: 8px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    div.stButton > button:first-child:hover {
        background-color: #005a99;
        transition: 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align: center;'>🛠️ Maintenance Engineering Guide</h1>",
    unsafe_allow_html=True
)

st.info("📂 Use the **Topics** menu on the left-Top sidebar to explore features.")

with st.sidebar:
    st.image("OMCO_Logo.png", use_container_width=True)
    st.markdown("## 📂 Topics")
    selection = st.radio("Go to:", topics)

# Allow tab navigation via session state (used by Start, Next, Previous buttons)
if "selected_tab" in st.session_state:
    selection = st.session_state.selected_tab
    del st.session_state.selected_tab


if selection == "🏠 Welcome":
    
    st.image("welcome_image.png", use_container_width=True)


elif selection == "Overview of Maintenance Types":
    st.header("📘 Types of Maintenance")
    st.markdown("""
    ### 🧠 Introduction
    Maintenance strategies are essential for ensuring the reliability, safety, and cost-effectiveness of equipment and systems across various industries.     These strategies define how maintenance activities are planned and executed to prevent failures, extend asset life, and optimize operational performance. The main types of maintenance strategies include **Corrective Maintenance (Run to Failure)**, **Preventive Maintenance (Time-Based)**, **Predictive Maintenance (Condition-Based)**, **Proactive Maintenance**, **Prescriptive Maintenace**, and **Reliability-Centered Maintenance (RCM)**. Each approach differs in terms of complexity, cost, required resources, and effectiveness in minimizing downtime. Understanding these strategies is crucial for selecting the most appropriate method based on equipment criticality, failure consequences, and operational context. 
    **Below are the most widely used strategies in engineering industries:**

    ### 1. 🛑 Corrective Maintenance (CM) — Also called Breakdown or Run-to-Failure
    - **Definition**: Maintenance performed only after equipment fails.
    - **Goal**: Restore functionality post-failure.
    - **Advantages**: No planning cost, simple.
    - **Disadvantages**: High risk, unplanned downtime, costly in critical systems.
    - **Best for**: Low-value, non-critical assets.
    - **Examples**: Light bulbs replacement, pumps/motors bearing replacement.

    ### 2. 🔁 Preventive Maintenance (PM)
    - **Definition**: Periodic maintenance at fixed time or usage intervals regardless of asset condition.
    - **Goal**: Prevent unexpected failures.
    - **Advantages**: Reduces failure risk, easy to plan.
    - **Disadvantages**: May result in unnecessary maintenance and costs.
    - **Best for**: Assets with predictable wear.
    - **Examples**: Replacing filters, monthly cleaning, oil changes, visual inspections.

    ### 3. 📊 Predictive Maintenance (PdM or CBM)
    - **Definition**: Uses real-time condition monitoring (vibration, temperature, oil analysis) to decide when to maintain.
    - **Goal**: Optimize timing of interventions.
    - **Advantages**: Prevents both under- and over-maintenance.
    - **Disadvantages**: Requires sensors and diagnostics.
    - **Best for**: High-value, rotating, or critical machines.
    - **Examples**: Vibration analysis for turbines/motors, DGA for transformers.

    ### 4. 🧠 Proactive Maintenance
    - **Definition**: Focuses on root cause elimination — redesigns, training, better lubrication, etc.
    - **Goal**: Stop failure before it begins.
    - **Advantages**: Long-term reliability improvement.
    - **Disadvantages**: Requires deep failure analysis.
    - **Best for**: Plants with high reliability goals.

    ### 5. 🤖 Prescriptive Maintenance (AI-driven)
    - **Definition**: Uses machine learning to recommend what action to take based on data.
    - **Goal**: Automate decisions using historical and real-time data.
    - **Advantages**: High efficiency, ideal for digital plants.
    - **Disadvantages**: Requires data integration, algorithm training.
    - **Best for**: Industry 4.0, digital twins.

    ### 6. 🔄 Reliability-Centered Maintenance (RCM)
    - **Definition**: Structured analysis method to select the best maintenance approach for each failure mode.
    - **Goal**: Balance safety, availability, and cost.
    - **Advantages**: Risk-based, asset-specific.
    - **Disadvantages**: Time-consuming and analytical.
    - **Best for**: Critical industries (power plants, aviation, oil & gas).

    ---
    **Choosing the right strategy** depends on asset criticality, failure behavior, cost, and available technology. Use the selector (next topic in this app) to help guide your decision.
    """)

    # --- Add comparison table ---
    st.markdown("### 🧾 Comparative Table of Maintenance Strategies")
    st.markdown("**Scroll the table to the right** to view all details. ➡️ ")  # <--- this line

    comparison_data = {
        "Strategy": ["Corrective", "Preventive", "Predictive", "Proactive", "Prescriptive", "RCM"],
        "Definition": [
            "Performed after failure occurs",
            "Scheduled at regular intervals",
            "Based on actual condition data",
            "Eliminates root causes before failure",
            "Uses AI to predict & prescribe actions",
            "Selects best strategy by criticality"
        ],
        "Trigger": [
            "Failure happens",
            "Time or usage interval",
            "Condition thresholds",
            "Root cause identification",
            "Data-driven prediction",
            "Function/failure analysis"
        ],
        "Tools/Techniques": [
            "Manual repair, fault diagnosis",
            "Calendar-based schedules",
            "Sensors, condition monitoring",
            "RCA, FMEA, tribology",
            "Machine learning, digital twins",
            "FMEA, reliability modeling"
        ],
        "Advantages": [
            "Simple, no upfront cost",
            "Reduces surprise failures",
            "Targets real issues, efficient",
            "Improves long-term reliability",
            "Optimizes decisions automatically",
            "Balances risk, cost, and performance"
        ],
        "Disadvantages": [
            "High downtime, costly failures",
            "Can cause over-maintenance",
            "Requires instrumentation, analysis",
            "Needs deep technical insights",
            "Complex implementation, data needs",
            "Time-consuming analysis"
        ],
        "Best Use Case": [
            "Low-value, non-critical assets",
            "Equipment with predictable aging",
            "Rotating/high-value machinery",
            "Recurring or systemic issues",
            "Smart/digitalized operations",
            "Critical assets with high consequences"
        ]
    }

    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)


    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "Strategy Recommendation Tool":
    st.header("🧩 Maintenance Strategy Selector")
    st.markdown("""
    Answer the following questions to get a strategy recommendation based on asset criticality, cost, and environment.
    """)

    criticality = st.selectbox("1️⃣ Asset Criticality", ["High", "Medium", "Low"],
        help="**Definition**: Importance of the asset to safety, production, or legal compliance.\n- High: Generator, main transformer, turbine\n- Medium: HVAC motor, feedwater pump, coolling fan\n- Low: Lights, admin printers")

    environment = st.selectbox("2️⃣ Operating Environment", ["Harsh", "Normal", "Clean"],
        help="**Definition**: Physical conditions around the asset.\n- Harsh: Heat, vibration, dust, chemicals\n- Clean: Lab or server room\n- Normal: Typical plant conditions")

    failure_history = st.selectbox("3️⃣ Failure History", ["Frequent", "Occasional", "Rare"],
        help="**Definition**: How often this asset fails.\nUse historical CMMS data if available.")

    maintenance_cost = st.selectbox("4️⃣ Maintenance Cost", ["High", "Medium", "Low"],
        help="**Definition**: Cost to repair, including labor, tools, spares, downtime.")

    downtime_cost = st.selectbox("5️⃣ Downtime Cost", ["High", "Medium", "Low"],
        help="**Definition**: Cost of system unavailability in terms of production, safety, or compliance.")

    recommendation = ""
    reason = ""
    examples = ""

    if criticality == "Low" and failure_history == "Rare":
        recommendation = "Run-to-Failure (RTF)"
        reason = "Non-critical asset with rare failures. Let it run until it fails."
        examples = "Small lights, backup indicators."
    elif criticality == "High" and environment == "Harsh" and failure_history != "Rare":
        recommendation = "Condition-Based Maintenance (CBM)"
        reason = "Critical asset in harsh conditions benefits from monitoring sensors."
        examples = "Pumps with vibration sensors, motors with IR thermography."
    elif criticality == "Medium" and failure_history == "Frequent":
        recommendation = "Time-Based Maintenance (TBM)"
        reason = "Frequent failures warrant a routine schedule."
        examples = "Monthly maintenance of air filters."
    elif criticality == "High" and downtime_cost == "High" and maintenance_cost == "High":
        recommendation = "Reliability-Centered Maintenance (RCM)"
        reason = "Critical and costly failures justify detailed RCM analysis."
        examples = "Turbine system, excitation panel."
    else:
        recommendation = "Preventive Maintenance (PM)"
        reason = "Standard scheduled checks fit this scenario."
        examples = "Lubrication plans, visual inspections."

    st.success(f"Recommended Strategy: **{recommendation}**")
    st.markdown(f"**Why:** {reason}")
    st.markdown(f"**Examples:** {examples}")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)


elif selection == "Condition Monitoring Techniques":
    st.header("📊 Condition Monitoring Techniques")
    st.markdown("""
    Condition monitoring is a key component of modern maintenance strategies, enabling the early detection of faults and degradation in assets before failures occur. It involves the continuous or periodic measurement and analysis of specific parameters that reflect the health and performance of equipment. By monitoring variables such as vibration, temperature, oil quality, acoustic emissions, and electrical signals, condition monitoring techniques help identify abnormal conditions, wear, or potential failures in advance. 

    **This proactive approach helps to:**
    - Support predictive maintenance
    - Reduce unplanned downtime
    - Enhances safety
    - Extends asset life
    - Detect developing faults
    - Prevent catastrophic failures

    ### Techniques & Tools:

    #### 1. **Vibration Analysis**
    - Detects: Imbalance, misalignment, bearing failure
    - Used with FFT to view frequency spectrum
    - Tools: Accelerometers, online monitoring systems
    - Applications: Generators, Turbines, Motors, Pumps 

    #### 2. **Infrared Thermography**
    - Detects: Overheating, phase imbalance, loose connections
    - Tools: Thermal cameras
    - Applications: Transformers, Switchgears, Motors

    #### 3. **Oil Analysis (including DGA)**
    - Detects: Vescosity, density, flash point, moisture, oxidation, breakdown voltage, gas generation,... etc
    - Tools: Lab. instruments
    - Applications: Transformers, turbines, engines, gearboxes,... etc

    #### 4. **Ultrasound Monitoring**
    - Detects: Air/gas leaks, bearing wear, arcing
    - Tools: Ultrasonic detectors
    - Applications: Pneumatic circuits, electrical cabinets

    #### 5. **Electrical Signature Analysis (ESA)**
    - Detects: Rotor bar faults, stator issues
    - Applications: Motors, generators

    ✅ Best Practice:
    - Combine techniques for reliability
    - Train technicians and analyze trends over time
    """)

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "D-I-P-F Curve":
    st.header("📉 D-I-P-F Curve: Detection, Indication, Prediction, and Failure")
    
    st.markdown("""
    ### 🧠 Introduction
    The **D-I-P-F curve** represents a modern approach to asset failure progression, commonly used in condition-based and predictive maintenance frameworks. It breaks down the failure process into four key stages:
    
    - **D (Design/Buy)**: The point when the asset or system is specified and engineered.
    - **I (Istallation)**: The point when the asset or system is installed and commissioned.
    - **P (Potential Failure)**: Sufficient data is available to estimate remaining useful life (RUL) or time to failure with predictive models.
    - **F (Failure)**: The asset fails or reaches a critical point where performance is lost or unsafe.

    This curve emphasizes the **window of opportunity** between Design and Failure, during which maintenance can be performed proactively to avoid unplanned downtime.
    """)

    st.image("dipf_curve_example.png", caption="Illustrative DIPF Curve", use_container_width=True)

    st.markdown("""
    ### 📌 Key Insights
    - 📍 The earlier the detection, the wider the window for predictive maintenance.
    - 🔍 Predictive models and condition monitoring can significantly shift interventions earlier in the curve.
    - 🧠 Understanding DIPF improves decision-making in AI-based maintenance strategies.
    """)

    st.success("DIPF is foundational to building effective predictive maintenance systems.")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "Bathtub Curve":
    st.header("🛁 Bathtub Curve")
    st.markdown("""
    The **Bathtub curve** is a visual representation of the failure rate of a product or group of products over time and guides maintenance strategy.
    By plotting the occurrences of failure over time, a bathtub curve maps out three phases that an asset experiences within its lifetime: Infant mortality phase, Useful life pase, and Wear-out phase.

    ### Lifecycle Phases:

    1. **Infant Mortality** (High failure rate)
       - Causes: Design or Manufacturing flaws, installation defects, improper commissioning.
       - Overcome by: QA/QC, commissioning, early inspections/testing, burn-in


    2. **Useful Life** (Constant, low rate)
       - Causes: Random, external events, process upsets, improper maintenance/operation, random failures, human errors.
       - Action: Condition monitoring, scheduled PM, proper operation, training.


    3. **Wear-Out Phase** (Increasing failures)
       - Causes: Fatigue, aging, erosion, corrosion.
       - Overcome by: Overhaul, replacement, RCM.

    ✅ Use this curve to match strategy with lifecycle stage.
    """)
    st.image("bathtub_curve_example.png", caption="Bathtub Curve with Maintenance Zones")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)


elif selection == "Root Cause Analysis":

    st.header("🛠 Root Cause Analysis (RCA) — Power Plant Focus")

    st.markdown("Root Cause Analysis (RCA) is a structured method used to identify the underlying cause of a problem or failure in complex systems such as power plant sytems. This tab provides both **educational theory** and **practical diagnostic tools**.")

    st.subheader("📖 1. What is Root Cause Analysis?")
    st.markdown("""
    **Root Cause Analysis (RCA)** is the process of identifying the fundamental cause of a problem, rather than just addressing its symptoms.

    It aims to answer:
    - **What happened?**
    - **Why did it happen?**
    - **What will prevent it from happening again?**

    RCA is a core tool in reliability engineering, maintenance strategy (RCM/CBM), and continuous improvement.
    """)

    st.subheader("📚 2. Types of Root Causes")
    st.markdown("""
    - **Physical Root Cause**: A component physically failed.
    - **Human Root Cause**: An error or omission during operation or maintenance.
    - **Latent/Systemic Cause**: A design flaw or policy allowed the issue to occur.
    """)

    st.subheader("🧰 3. Common RCA Methods")
    st.markdown("""
    - **🔍 5 Whys** – Repeated questioning to drill down to the root.
    - **🐟 Fishbone Diagram (Ishikawa)** – Cause categories (Human, Machine, Method...).
    - **🔢 Fault Tree Analysis (FTA)** – Logical paths leading to failure.
    - **📋 FMEA** – Anticipating failure modes and effects.
    """)

    st.subheader("⚙️ 4. How to Execute RCA")
    st.markdown("""
    1. Define the Problem
    2. Collect Operational & Historical Data
    3. Identify Contributing Factors
    4. Apply RCA Tools (5 Whys, Fishbone, etc.)
    5. Determine Corrective/Preventive Actions
    6. Implement and Monitor
    """)

    st.markdown("""
    ---
    """)

    st.subheader("🔎 5. Practical Diagnostic Tool")
    st.markdown("""
    Select **System** and **Symptom** to show the possible causes and recommended action
    """)

    system = st.selectbox("System", [
        "Steam Turbine", "Generator", "Transformer", "Pump/Motor", "Boiler", "Switchgear"
    ])

    symptom = st.selectbox("Symptom", [
        "Overheating", "Vibration", "Tripping", "Leakage", "Low Output", "Noise", "Electrical Flash"
    ])

    # Diagnostic logic for each system/symptom combination
    if system == "Generator" and symptom == "Overheating":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Blocked or inefficient cooling system (TEWAC, air, or hydrogen)
    	- Overloaded operation or poor power factor
    	- Stator or rotor winding insulation degradation
    	- Bearing friction or high ambient temperature

    	**✅ Actions:**
    	- Inspect and clean air filters, heat exchangers, or coolers
    	- Monitor load, PF, and reduce overloading
    	- Perform insulation resistance and hotspot checks
    	- Verify bearing lubrication and ventilation
    	""")

    elif system == "Generator" and symptom == "Vibration":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Rotor imbalance or misalignment
    	- Magnetic unbalance (eccentric air gap)
    	- Bearing wear or resonance
    	- Foundation looseness or coupling issues

    	**✅ Actions:**
    	- Perform rotor dynamic balancing
    	- Check shaft alignment and coupling condition
    	- Analyze vibration spectrum for electrical or mechanical sources
    	- Re-tighten foundation bolts and support structures
    	""")

    elif system == "Generator" and symptom == "Tripping":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Protection relay activation (differential, overcurrent, reverse power)
    	- Voltage or frequency instability
    	- AVR or excitation system malfunction
    	- Loss of prime mover input (e.g., turbine trip)
	- External trip

    	**✅ Actions:**
    	- Analyze protection relay logs and trip records
    	- Verify voltage and frequency stability
    	- Test AVR/excitation components (brushless or static)
    	- Check turbine/gas engine controls for faults
    	""")

    elif system == "Generator" and symptom == "Leakage":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Hydrogen or oil seal failure (in hydrogen-cooled machines)
    	- Shaft seal or cooler gasket wear
    	- Cooling water or lube oil system leak
    	- Loose terminal box grommets or penetrations

    	**✅ Actions:**
    	- Check hydrogen purity, pressure, and seal oil system
    	- Replace worn seals and tighten gasketed joints
    	- Inspect lube oil and coolant piping
    	- Apply leak detection methods (pressure test, sniffer, dye)
    	""")

    elif system == "Generator" and symptom == "Low Output":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Underexcitation or faulty AVR
    	- Partial winding short or high resistance joints
    	- Governor or prime mover input limitation
    	- Load rejection or control mismatch

    	**✅ Actions:**
    	- Check excitation current and AVR settings
    	- Test windings for shorted turns or thermal hotspots
    	- Analyze prime mover output and governor response
    	- Verify load sharing and synchronization
    	""")

    elif system == "Generator" and symptom == "Noise":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Loose lamination stacks or stator core vibration
    	- Magnetic noise due to flux imbalance
    	- Bearing noise or shaft rub
    	- Ventilation fan imbalance or damage

    	**✅ Actions:**
    	- Inspect stator core integrity and wedge tightness
    	- Verify air gap uniformity and excitation balance
    	- Check bearing condition and shaft alignment
    	- Balance or replace ventilation fan
    	""")

    elif system == "Generator" and symptom == "Electrical Flash":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Line terminal assembly insulation failure or loose connection
    	- Voltage surges or transients
    	- Ground fault or phase-to-phase short
    	- Contamination or tracking on busbars or bushings

    	**✅ Actions:**
    	- Isolate and inspect terminal connections and cable insulation
    	- Check for signs of arc tracking or corona
    	- Test for insulation resistance and partial discharge
    	- Verify surge protection devices and grounding integrity
    	""")


    elif system == "Transformer" and symptom == "Leakage":
        st.markdown("""
        **🧠 Possible Causes:**
        - Gasket aging or failure
    	- Cracks in tank welds or valve threads
        - Overpressure during load cycles
        - Corrosion or mechanical shock to radiators or bushings

        **✅ Actions:**
        - Inspect and tighten all gasket seals
        - Monitor oil level and gas accumulation
        - Conduct visual inspections and apply leak-detection tools
        """)

    elif system == "Transformer" and symptom == "Overheating":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Blocked radiator or degraded cooling system (fans/pumps)
    	- Overload or unbalanced loading
    	- High ambient temperature or poor ventilation
    	- Internal faults (e.g., winding hotspot or core heating)

    	**✅ Actions:**
    	- Inspect and clean radiators, check fan/pump operation
    	- Monitor load current vs. rated capacity
    	- Perform infrared scanning and DGA for internal fault detection
    	""")

    elif system == "Transformer" and symptom == "Vibration":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Core lamination looseness or magnetic flux imbalance
    	- Mechanical looseness of mounting or clamping structure
    	- Harmonics from non-linear loads
    	- Cooling fans or oil pumps vibrating

    	**✅ Actions:**
    	- Check core tightness and inspect for core noise
    	- Tighten anchor bolts and inspect for looseness
    	- Analyze power quality for harmonics
    	- Inspect rotating parts (Fans, oil pumps) and supports
    	""")

    elif system == "Transformer" and symptom == "Tripping":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Differential protection or Buchholz relay operation
    	- Sudden pressure or overcurrent fault
    	- Earth fault or winding short
    	- HV/LV side switching issues

    	**✅ Actions:**
    	- Review protection relay trip logs and gas relay records
    	- Test winding insulation and perform fault analysis
    	- Conduct DGA and sweep frequency response analysis
    	- Check upstream/downstream breaker coordination
    	""")

    elif system == "Transformer" and symptom == "Low Output":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Tap changer in incorrect position or malfunctioning
    	- Internal short circuits or high winding resistance
    	- Poor voltage regulation due to load changes
    	- Partial discharge or insulation degradation

    	**✅ Actions:**
    	- Verify tap changer position and functionality
    	- Test winding resistance and perform ratio test
    	- Analyze voltage profile across the network
    	- Conduct partial discharge and insulation analysis
    	""")

    elif system == "Transformer" and symptom == "Noise":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Magnetostriction of core laminations (normal hum)
    	- Loose core clamping or aging insulation
    	- Harmonics or DC bias in the system
    	- Fan or pump noise from cooling system

    	**✅ Actions:**
    	- Check if noise is within normal frequency range (100–150 Hz)
    	- Tighten internal clamping bolts (if offline possible)
    	- Perform harmonic analysis
    	- Inspect auxiliary components (fans, oil pumps) for noise
    	""")

    elif system == "Transformer" and symptom == "Electrical Flash":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Bushing flashover or tracking due to contamination
    	- Internal arc due to winding insulation failure
    	- Surge arrestor failure or poor grounding
    	- Improper cable termination or loosened lugs
	
    	**✅ Actions:**
    	- Inspect bushings for contamination, cracks, or partial discharge
    	- Perform insulation resistance and tan delta testing
    	- Test surge arrestors and inspect earthing
    	- Re-terminate and torque-check all cable connections
    	""")

    elif system == "Pump/Motor" and symptom == "Overheating":
        st.markdown("""
    	**🧠 Possible Causes:**
    	- Bearing failure or misalignment
    	- Blocked or restricted cooling flow
    	- Overloaded motor or pump duty beyond design
    	- Low insulation resistance increasing losses

    	**✅ Actions:**
    	- Check and lubricate bearings
    	- Inspect cooling fan or coolant lines
    	- Verify load vs. rated capacity
    	- Measure winding temperature and insulation resistance
    	""")

    elif system == "Pump/Motor" and symptom == "Vibration":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Shaft misalignment or imbalance
    	- Loose foundation bolts or mounting
    	- Cavitation or hydraulic instability
    	- Bearing wear

    	**✅ Actions:**
    	- Perform shaft alignment check
    	- Tighten foundation and coupling bolts
    	- Check suction conditions
    	- Inspect and replace worn bearings
    	""")

    elif system == "Pump/Motor" and symptom == "Tripping":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Overcurrent due to overload or phase imbalance
    	- Motor protection relay activation (e.g., thermal, short circuit)
    	- Electrical insulation failure
    	- Jammed impeller or motor stall

    	**✅ Actions:**
    	- Review protection relay settings and logs
    	- Check motor and cable insulation with IR test
    	- Inspect impeller and coupling for blockage
    	- Verify supply voltage and phase balance
    	""")

    elif system == "Pump/Motor" and symptom == "Leakage":
    	st.markdown("""
    	**🧠 Possible Causes:**
   	- Seal or gland packing failure
    	- Excessive system pressure or pulsation
    	- Worn shaft sleeve or housing
    	- Corrosion or cracked casing

    	**✅ Actions:**
    	- Replace mechanical seals or packing
    	- Check and regulate system pressure
    	- Inspect shaft and housing for damage
    	- Apply corrosion protection or replace damaged parts
    	""")

    elif system == "Pump/Motor" and symptom == "Low Output":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Clogged suction filter or strainer
    	- Impeller wear or erosion
    	- Incorrect pump rotation
    	- Air entrainment or vapor lock

    	**✅ Actions:**
    	- Clean suction line and filters
    	- Inspect and replace impeller if worn
    	- Verify direction of rotation
    	- Bleed air from the system
    	""")

    elif system == "Pump/Motor" and symptom == "Noise":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Cavitation in the pump
    	- Bearing damage or lack of lubrication
    	- Loose components or vibration
    	- Electrical hum from motor windings

    	**✅ Actions:**
    	- Improve suction conditions to avoid cavitation
    	- Lubricate or replace bearings
    	- Check for mechanical looseness
    	- Measure and assess electrical harmonics
    	""")

    elif system == "Pump/Motor" and symptom == "Electrical Flash":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Cable insulation breakdown or loose terminals
    	- Moisture ingress in terminal box
    	- Overvoltage or surge conditions
    	- Faulty motor winding insulation

    	**✅ Actions:**
    	- Inspect and re-terminate motor connections
    	- Dry and seal terminal box
    	- Check surge protection devices
    	- Perform dielectric and IR testing
    	""")

    elif system == "Boiler" and symptom == "Overheating":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Fouled heat transfer surfaces or tube scaling
    	- Inadequate water flow or pump failure
    	- Incorrect fuel-air ratio causing flame impingement
    	- Blocked flue gas path or malfunctioning dampers

    	**✅ Actions:**
    	- Clean boiler tubes and deslag if needed
    	- Check feedwater pump performance and flow rate
    	- Tune combustion system and adjust air/fuel ratio
    	- Inspect and clear flue gas ducts and dampers
    	""")

    elif system == "Boiler" and symptom == "Vibration":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Draft fan imbalance or loose mounting
    	- Pulsating combustion or unstable flame
    	- Loose casing or ductwork
    	- Resonance from connected piping

    	**✅ Actions:**
    	- Balance and align fans
    	- Stabilize burner operation and check flame detectors
    	- Tighten structural components and duct clamps
    	- Inspect steam lines for proper support
    	""")

    elif system == "Boiler" and symptom == "Tripping":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Low drum level or high steam pressure protection
    	- Flame failure or burner fault
    	- Overtemperature in furnace or superheater
    	- Electrical supply fault to controls or auxiliaries

    	**✅ Actions:**
    	- Review trip log and interlock history
    	- Check burner management system and sensors
    	- Inspect temperature sensors and protection setpoints
    	- Verify power supply and backup for control panels
    	""")

    elif system == "Boiler" and symptom == "Leakage":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Tube rupture or gasket failure
    	- Overpressure or thermal fatigue at weld joints
    	- Corrosion or erosion in water wall/furnace
    	- Valve packing or flange leaks

    	**✅ Actions:**
    	- Isolate and inspect leak location
    	- Conduct NDT on suspected tubes or joints
    	- Repair or replace damaged sections
    	- Retighten or repack leaking valves/flanges
    	""")

    elif system == "Boiler" and symptom == "Low Output":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Fouled heat exchange surfaces reducing efficiency
    	- Fuel quality or flow issues
    	- Improper combustion settings
    	- Feedwater system underperformance

    	**✅ Actions:**
    	- Conduct soot blowing and tube cleaning
    	- Verify fuel supply and atomization
    	- Re-calibrate air/fuel ratio controls
    	- Check feedwater flow and deaerator performance
    	""")

    elif system == "Boiler" and symptom == "Noise":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Water hammer in steam lines
    	- Flame pulsation or unstable combustion
    	- Scale formation causing boiling noise

    	**✅ Actions:**
    	- Check condensate removal and trap operation
    	- Tune burner and check flame pattern
    	- Inspect ID/FD fan condition
    	- Clean internal surfaces and monitor boiler chemistry
    	""")


    elif system == "Boiler" and symptom in ["Electrical Flash"]:
        st.markdown("**ℹ️ Not Applicable or No Common Root Cause Identified for this combination.**")

    elif system == "Switchgear" and symptom == "Overheating":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Loose or corroded busbar or cable connections
    	- Overloaded feeders or poor load distribution
    	- Aging contactors or circuit breakers
    	- Inadequate ventilation or blocked cooling path

    	**✅ Actions:**
    	- Perform thermographic scanning of joints and terminals
    	- Balance loads across phases/feeders
    	- Inspect and replace worn contacts or breakers
    	- Clean ventilation paths and verify fan operation (if present)
    	""")

    elif system == "Switchgear" and symptom == "Tripping":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Overcurrent or short circuit on downstream feeders
    	- Protection relay misoperation or faulty settings
    	- Earth fault or interphase short
    	- Mechanical latch failure in circuit breaker

    	**✅ Actions:**
    	- Analyze trip records and relay logs
    	- Verify relay settings and coordination study
    	- Perform insulation resistance and loop tests
    	- Inspect circuit breaker mechanism and test tripping coil
    	""")

    elif system == "Switchgear" and symptom == "Leakage":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- SF₆ gas leak in gas-insulated switchgear (GIS)
    	- Oil leak in older oil-type breakers
    	- Moisture ingress from door gaskets or conduit entry points
    	- Cable termination or sleeve degradation

    	**✅ Actions:**
    	- Perform SF₆ gas pressure and leak test (for GIS)
    	- Inspect seals, gaskets, and cable entry points
    	- Replace degraded components and reseal enclosures
    	- Dry and test affected zones with insulation testing
    	""")

    elif system == "Switchgear" and symptom == "Noise":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Loose relays, contactors, or panel covers
    	- Magnetic hum from energized coils
    	- Arcing inside bus compartments
    	- Fan or auxiliary device vibration

    	**✅ Actions:**
    	- Tighten internal components and panel fasteners
    	- Check for abnormal coil hum (possible overvoltage or DC offset)
    	- Perform visual inspection for arcing marks
    	- Inspect cooling fans or auxiliary devices
    	""")

    elif system == "Switchgear" and symptom == "Electrical Flash":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Arc flash from loose or corroded connections
    	- Tracking due to contamination or insulation failure
    	- Improper breaker racking or interlock bypass
    	- High fault current or delayed clearing time

    	**✅ Actions:**
    	- Conduct detailed visual inspection and thermal scan
    	- Clean and dry insulation surfaces
    	- Verify racking procedure and interlock integrity
    	- Perform arc flash study and ensure PPE compliance
    	""")

    elif system == "Switchgear" and symptom in ["Vibration", "Low Output"]:
        st.markdown("**ℹ️ Not Applicable or No Common Root Cause Identified for this combination.**")

    elif system == "Steam Turbine" and symptom == "Overheating":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Bearing lubrication failure or oil degradation
    	- Blocked or inefficient lube oil cooler
    	- Overloading or excessive backpressure
    	- Rotor rubbing due to thermal expansion

    	**✅ Actions:**
    	- Check lube oil pressure, flow, and quality
    	- Clean or replace oil coolers
    	- Analyze process parameters and steam conditions
    	- Inspect clearances and vibration trends for signs of rubbing
    	""")

    elif system == "Steam Turbine" and symptom == "Vibration":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Rotor imbalance or misalignment
    	- Bearing wear or damage
    	- Steam flow disturbance (e.g., wet steam, water induction)
    	- Foundation settlement or soft foot

    	**✅ Actions:**
    	- Perform shaft alignment and rotor balancing
    	- Inspect journal and thrust bearings
    	- Verify steam quality and check for water carryover
    	- Conduct foundation level and bolt torque check
    	""")

    elif system == "Steam Turbine" and symptom == "Tripping":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Overspeed or vibration protection activation
    	- Low lube oil pressure or seal oil failure
    	- Emergency trip valve actuation
    	- Generator or process interlock triggering trip

    	**✅ Actions:**
    	- Review trip log and overspeed test records
    	- Check turbine protection systems and trip oil circuits
    	- Test and verify operation of trip valves and solenoids
    	- Investigate related systems like generator load or condenser vacuum
    	""")

    elif system == "Steam Turbine" and symptom == "Leakage":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Steam seal packing wear or failure
    	- Gasket failure at flanges or inspection covers
    	- Lube oil or seal oil leakage
    	- Drain piping blockage causing backpressure

    	**✅ Actions:**
    	- Inspect and replace worn gland or labyrinth seals
    	- Tighten or re-gasket leaking joints
    	- Check oil piping and pump seals
    	- Ensure proper drainage and venting of seal systems
    	""")

    elif system == "Steam Turbine" and symptom == "Low Output":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Reduced steam inlet pressure or flow
    	- Fouled turbine blades or deposits on nozzles
    	- Throttle valve malfunction or partial stroke
    	- Vacuum loss in the condenser

    	**✅ Actions:**
    	- Monitor steam parameters and check control valves
    	- Perform turbine inspection and cleaning (offline if needed)
    	- Test throttle valve actuation and feedback loop
    	- Inspect condenser performance and ejector operation
    	""")

    elif system == "Steam Turbine" and symptom == "Noise":
    	st.markdown("""
    	**🧠 Possible Causes:**
    	- Blade vibration or steam whistle due to partial flow
    	- Bearing noise due to wear or oil starvation
    	- Loose casing bolts or insulation panels
    	- Water hammer in steam lines

    	**✅ Actions:**
    	- Analyze acoustic signals and vibration spectrum
    	- Check oil film condition and replace worn bearings
    	- Tighten casing bolts and panels
    	- Verify proper startup/shutdown procedures to avoid water hammer
    	""")

    elif system == "Steam Turbine" and symptom in ["Electrical Flash"]:
        st.markdown("**ℹ️ Not Applicable or No Common Root Cause Identified for this combination.**")

    st.markdown("""
    ---
    """)

    st.subheader("🖼 Interactive Fishbone Diagram Builder (Ishikawa)")

    st.markdown("Fill in the cause categories to automatically generate the fishbone diagram.")

    problem = st.text_input("Main Problem", "High Bearing Temperature")

    categories = ["Human", "Machine", "Method", "Material", "Environment", "Measurement"]
    causes = {}

    for cat in categories:
        user_input = st.text_area(f"Possible causes from {cat}", f"Example: {cat} issue 1\n{cat} issue 2")
        causes[cat] = user_input.strip().split("\n")

    # Generate Graphviz Fishbone
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR', size='8')
    dot.node("Problem", problem, shape="ellipse", style="filled", fillcolor="lightcoral")

    for cat in categories:
        dot.node(cat, cat, shape="box", style="filled", fillcolor="lightblue")
        dot.edge(cat, "Problem")
        for idx, item in enumerate(causes[cat]):
            sub_id = f"{cat}_{idx}"
            dot.node(sub_id, item.strip(), shape="note")
            dot.edge(sub_id, cat)

    st.graphviz_chart(dot, use_container_width=True)

    st.info("This diagram is auto-generated based on your inputs and follows standard RCA fishbone structure.")


    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "Failure Mode Library (FMEA Style)":
    st.header("📚 Failure Mode Library – FMEA Style")

    st.markdown("""
    Failure Mode and Effects Analysis (FMEA) is a structured approach for identifying, prioritizing, and mitigating potential failure modes of assets and systems. This tab provides a **reference library of common failure modes** in power plant equipment using FMEA methodology.

    ---

    ### 🧠 FMEA Overview
    - **Failure Mode:** The specific way a component can fail
    - **Effect:** The impact of the failure on operation/safety
    - **Cause:** Root contributors to the failure
    - **Detection:** Method to identify the failure
    - **Severity, Occurrence, Detection (S-O-D):** Scoring criteria to rank risk
    - **RPN (Risk Priority Number):** Severity × Occurrence × Detection

    ---

    ### 📊 S-O-D Scoring Guidance

    | Score Range | Severity (S)        | Occurrence (O) | Detection (D)          |
    |-------------|----------------------|----------------|------------------------|
    | 9–10        | Hazardous/Catastrophic | Frequent       | Very rarely detected   |
    | 7–8         | High                 | Occasional     | Hard to detect         |
    | 4–6         | Moderate             | Infrequent     | Occasionally detected  |
    | 1–3         | Low/Minor            | Rare/Unlikely  | Easily/Always detected |

    This scoring is used to calculate the RPN (S × O × D) and prioritize risks for mitigation.

    ---

    ### 🔧 Common Power Plant Failure Modes (Examples by System)

    #### 🔌 Generator
    | Failure Mode         | Cause                             | Effect                          | Detection Method          |
    |----------------------|------------------------------------|----------------------------------|----------------------------|
    | Bearing overheating  | Lubrication failure                | High vibration, shutdown        | IR gun, temp. sensor   |
    | Rotor winding short  | Insulation aging                  | Load imbalance, tripping        | Resistance test     |

    #### 🔋 Transformer
    | Failure Mode        | Cause                        | Effect                        | Detection Method         |
    |---------------------|-------------------------------|-------------------------------|---------------------------|
    | Partial discharge   | High voltage stress          | Insulation failure, fire risk | UHF sensor, DGA           |
    | Bushing failure     | Oil contamination             | Flashover                     | Capacitance & power factor|

    #### 💧 Pump/Motor
    | Failure Mode      | Cause                     | Effect                   | Detection Method        |
    |-------------------|----------------------------|---------------------------|--------------------------|
    | Seal leakage      | Misalignment, wear         | Fluid loss                | Visual, pressure drop    |
    | Motor burnout     | Overload, unbalanced phase | Loss of pumping capability| IR camera, current drop  |

    #### 🔥 Boiler
    | Failure Mode      | Cause                        | Effect                     | Detection Method         |
    |-------------------|-----------------------------|-----------------------------|---------------------------|
    | Tube rupture      | Scaling, high pressure      | Shutdown, safety risk       | Pressure drop, acoustic   |
    | Flame instability | Fuel/air imbalance          | Inefficient combustion       | Flame scanner, gas analysis|

    #### ⚙️ Auxiliary Systems
    | Failure Mode       | Cause                  | Effect                    | Detection Method      |
    |--------------------|-------------------------|----------------------------|------------------------|
    | Air cooler clogging| Dirt/oil accumulation   | Overheating                | ΔT monitoring, IR scan |
    | Valve stuck        | Debris, corrosion       | Process disruption         | Manual stroke test     |

    ---

    ### 🧮 Risk Evaluation Table (FMEA Template)
    | Failure Mode         | Severity (1–10) | Occurrence (1–10) | Detection (1–10) | RPN (S×O×D) | Action Plan             |
    |----------------------|------------------|--------------------|------------------|-------------|--------------------------|
    | Bearing Overheat     | 8                | 5                  | 6                | 240         | Add sensor + CM strategy |
    | Bushing Failure      | 9                | 4                  | 3                | 108         | Improve oil testing freq |

    ---

    ### 🧠 Best Practices for FMEA Libraries
    - Use standardized tags and link to CMMS
    - Update after each root cause analysis
    - Include detection tools and action plans
    - Integrate digital records for each asset
    - Classify failures by type (electrical, mechanical, process)

    ---

    ### 🖼️ RPN Matrix (Visual Prioritization)
    """)
    st.image("Failure_Mode_Lib.png", caption="RPN Matrix and S-O-D Scoring Guidance", use_container_width=True)

    st.markdown("""
    ---

    👤 Developed by **Eng. Mohammed Assaf – CMRP, CEPSS**
    """)


elif selection == "Maintenance Planning & Scheduling":
    st.header("🗓️ Maintenance Planning & Scheduling")

    st.markdown("""
    Maintenance planning and scheduling are vital processes for ensuring that maintenance work is executed efficiently, safely, and at the lowest possible cost.

    Proper planning prevents chaos, minimizes unplanned downtime, ensures availability of materials/resources, and allows better coordination among teams.
    
    ---

    ### 📘 Key Differences
    | Aspect        | Planning                           | Scheduling                           |
    |---------------|------------------------------------|--------------------------------------|
    | Purpose       | Define *what* to do and *how*      | Define *when* and *by whom*          |
    | Focus         | Scope, materials, instructions      | Time slots, resources, priorities     |
    | Owner         | Planner (typically office-based)    | Scheduler / Supervisor                |
    | Output        | Work packages, BOM, job card        | Daily/weekly schedule, work orders    |

    ---

    ### 🧰 Planning Steps:
    1. **Work Identification**: Source of request (inspection, PM, breakdown, etc.)
    2. **Work Approval**: Determine if valid/needed
    3. **Job Scope Definition**: Clear steps and safety procedures
    4. **Parts & Tools Check**: Confirm availability
    5. **Work Package Creation**: Include drawings, permits, SOPs

    ---

    ### 📆 Scheduling Steps:
    1. **Prioritize Work Orders**: Criticality and urgency
    2. **Align Resources**: Assign technicians and tools
    3. **Coordinate with Operations**: Confirm asset availability
    4. **Issue Daily or Weekly Schedule**
    5. **Track Progress and Feedback

    ---

    ### 🖼️ Visual Example: Planning vs Scheduling Roles
    """)

    st.image("planning_vs_scheduling.png", caption="Planning vs Scheduling – Role Clarity", use_container_width=True)

    st.markdown("""
    ---

    ### 🧠 Best Practices
    - Use **CMMS** or scheduling software
    - Integrate with operations for downtime planning
    - Maintain a backlog of approved work
    - Always review job history before planning
    - Apply the 80/20 rule: 80% planned, 20% reactive

    ---
    👤 Developed by **Eng. Mohammed Assaf - CMRP, CEPSS**
    """)


elif selection == "Spare Parts & Inventory Management":
    st.header("📦 Spare Parts & Inventory Management")
    st.markdown("""
    Effective spare parts and inventory management is critical for ensuring **asset uptime**, reducing **MTTR**, and optimizing **maintenance costs**.

    ### 🧠 Why It Matters
    - Spare parts availability directly impacts **equipment availability**.
    - Overstocking leads to **capital waste**, while understocking causes **production loss**.
    - Must balance **service level** vs. **inventory carrying cost**.

    ---    

    ### 🧱 Spare Part Categories (ABC or A-B-C Analysis)
    Spare parts are typically classified based on **criticality and consumption**:

    | Type | Description | Risk | Strategy |
    |------|-------------|------|----------|
    | 🔴 A - Critical | High impact on safety/production if unavailable | Very High | Always in stock, rapid replenishment |
    | 🟡 B - Essential | Medium importance | Medium | Stock based on failure history |
    | 🟢 C - Non-critical | Low impact if delayed | Low | Stock occasionally or order as needed |

    🛠 **Tip:** Apply Pareto Principle (80/20 Rule): 20% of parts cause 80% of downtime.

    ---

    ### 🗂️ Inventory Strategies

    #### 1. 📅 Time-Based Reorder
    - Reorder based on fixed schedule (e.g., monthly).
    - 🔁 Easy but may cause overstock.

    #### 2. 📉 Stock-Level Triggered (Min-Max)
    - Reorder when quantity drops below minimum threshold.
    - Better suited for predictable failure rates.

    #### 3. 📊 Consumption-Based Forecasting
    - Uses historical usage data to predict future needs.
    - Ideal for medium-turnover spare parts.

    #### 4. 📡 Predictive Analytics (AI/CMMS)
    - Predicts failures from condition monitoring + triggers part procurement in advance.
    - Requires digital systems and integration with sensors or CMMS.

    ---

    ### 🔄 Integration with Maintenance

    | Spare Mgmt Practice | Maintenance Benefit |
    |----------------------|---------------------|
    | Auto-reorder based on usage | Faster response to breakdowns |
    | Stock critical parts for known failure modes | Reduces MTTR |
    | Classify spares by failure modes (FMEA link) | Aligns with reliability goals |
    | Link spares to asset hierarchy (via CMMS) | Traceability & better planning |

    ---

    ### 💡 Best Practices

    - ✔️ Use barcode/RFID for parts tracking.
    - ✔️ Audit spare part movements monthly.
    - ✔️ Train technicians on part request workflows.
    - ✔️ Don’t confuse **operational consumables** with **strategic spares**.
    - ✔️ Use failure history to define stocking levels.

    ---

    ### 📈 KPIs for Inventory Effectiveness

    | KPI | Formula | Target |
    |-----|---------|--------|
    | Stockout Rate | (# of stockouts) / (total requests) | < 2-8% |
    | Inventory Turnover | (Annual usage) / (Avg inventory value) | 3–5x/year |
    | Fill Rate | Orders fulfilled from stock / Total orders | > 95% |
    | Dead Stock % | (Value of unused items >1yr) / Total inventory | < 10% |

    ---

    ### 🧭 Visual Guide: Spare Management Cycle
    """)

    st.image("spare_parts_cycle.png", caption="Spare Parts Management Cycle", use_container_width=True)

    st.markdown("""
    ---

    ### ⚙️ CMMS Integration Example
    - Link spare parts database to equipment BOM.
    - Trigger spares requests from maintenance work orders.
    - Monitor part usage trends for each asset category.

    ---

    👤 Developed by **Eng. Mohammed Assaf – CMRP, CEPSS**
    """)


elif selection == "Digital Maintenance Tools (CMMS, IIoT, AI)":
    st.header("🤖 Digital Maintenance Tools")
    st.markdown("""
    In the modern era of **Industry 4.0**, maintenance is no longer just about wrenches and inspections. Today, smart digital tools help predict, optimize, and automate maintenance activities, making operations safer, more efficient, and more data-driven.

    ### 🔧 Categories of Digital Tools
    
    #### 🖥️ 1. **CMMS — Computerized Maintenance Management Systems**
    - Used for scheduling, logging, and tracking all maintenance activities.
    - Common Features:
        - Work order management
        - Maintenance history
        - Asset tracking
        - Inventory & spare parts
    - Popular CMMS tools: **IBM Maximo**, **SAP PM**, **Fiix**, **UpKeep**

    #### 🌐 2. **IIoT — Industrial Internet of Things**
    - Connects physical assets to sensors and networks.
    - Enables **real-time monitoring** of:
        - Temperature, vibration, current, pressure
        - Alarms and threshold breaches
    - Data is sent to edge or cloud platforms.

    #### 🧠 3. **AI & Machine Learning in Maintenance**
    - AI can detect **patterns and anomalies** that humans miss.
    - Predict Remaining Useful Life (RUL)
    - Recommend actions (prescriptive maintenance)
    - Models used: **XGBoost**, **Random Forest**, **Neural Networks**
    - Tools: Python, TensorFlow, ONNX, Azure ML

    ---
    ### 📱 Examples in Power Plants
    - **Generator bearing temperature** predicted using ML based on MVAR/MW trends.
    - **Transformer DGA gas levels** monitored via IoT sensors + AI classification.
    - **CBM dashboard** showing motor vibration trends.

    ---
    ### ✅ Benefits
    - Early fault detection
    - Optimized maintenance windows
    - Fewer unplanned outages
    - Data-driven decisions

    ### ⚠️ Challenges
    - Requires clean and structured data
    - Integration with legacy systems
    - Cybersecurity concerns 

    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)


elif selection == "Maintenance KPIs Calculator":
    st.header("📈 Maintenance KPIs Calculator — Interactive Dashboard")
    st.markdown("""
    KPIs provide a measurable way to assess and improve your maintenance program.
    Enter data below to calculate:
    """)

    st.subheader("1. 🔁 MTBF (Mean Time Between Failures)")
    st.markdown(r"""
    **Formula:**
    $$\text{MTBF} = \frac{\text{Total Uptime}}{\text{Number of Failures}}$$
    """)
    uptime = st.number_input("Total Uptime (hours)", value=1000)
    failures = st.number_input("Number of Failures", value=5)
    if failures > 0:
        st.success(f"MTBF = {uptime / failures:.2f} hours")

    st.subheader("2. 🔧 MTTR (Mean Time to Repair)")
    st.markdown(r"""
    **Formula:**
    $$\text{MTTR} = \frac{\text{Total Downtime}}{\text{Number of Repairs}}$$
    """)
    downtime = st.number_input("Total Downtime (hours)", value=50)
    repairs = st.number_input("Number of Repairs", value=5)
    if repairs > 0:
        st.success(f"MTTR = {downtime / repairs:.2f} hours")

    st.subheader("3. ⚙️ Availability")
    st.markdown(r"""
    **Formula:**
    $$\text{Availability} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
    or equivalently:
    $$\text{Availability} = \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}}$$
    """)
    if (uptime + downtime) > 0:
        availability = uptime / (uptime + downtime)
        st.success(f"Availability = {availability:.2%}")

    st.subheader("4. 📦 Maintenance Cost per Unit Output")
    st.markdown(r"""
    **Formula:**
    $$\text{Cost per Unit} = \frac{\text{Total Maintenance Cost}}{\text{Total Output}}$$
    """)
    cost = st.number_input("Total Maintenance Cost ($)", value=15000)
    output = st.number_input("Total Output (e.g., MWh, Tons)", value=1000)
    if output > 0:
        st.success(f"Cost per unit = ${cost/output:.2f}")

    st.subheader("5. 📅 Schedule Compliance (%)")
    st.markdown(r"""
    **Formula:**
    $$\text{Schedule Compliance} = \frac{\text{Completed On Time}}{\text{Scheduled Jobs}} \times 100$$
    """)
    scheduled = st.number_input("Scheduled Jobs", value=120)
    completed = st.number_input("Completed On Time", value=108)
    if scheduled > 0:
        st.success(f"Schedule Compliance = {completed/scheduled*100:.2f}%")

    st.subheader("6. 💰 Maintenance Budget Adherence")
    st.markdown(r"""
    **Formula:**
    $$\text{Budget Variance} = \frac{\text{Actual Spend} - \text{Planned Budget}}{\text{Planned Budget}} \times 100$$
    """)
    budget = st.number_input("Planned Budget ($)", value=20000)
    actual = st.number_input("Actual Spend ($)", value=18500)
    if budget > 0:
        variance = (actual - budget) / budget * 100
        st.success(f"Budget Variance = {variance:.2f}%")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)

elif selection == "Maintenance Safety":
    st.header("🦺 Maintenance Safety Excellence")

    st.markdown("""
    Maintenance work—whether routine, preventive, or corrective—often involves **exposure to high-risk environments**. Unlike normal operations, maintenance tasks frequently involve opening equipment, isolating energy sources, working in confined spaces, or handling hazardous substances. **Injuries and fatalities during maintenance** are often caused by inadequate planning, failure to follow procedures, or a breakdown in communication.

    This section outlines a professional, structured approach to maintenance safety, suitable for engineers, supervisors, technicians, and plant managers.

    ---

    ### 🧠 Understanding the Risk Landscape

    - **70% of electrical injuries** occur during maintenance activities.
    - **60% of confined space fatalities** involve would-be rescuers.
    - Maintenance contributes to **up to 30% of industrial accidents** in many sectors.
    - Risk is often highest during **shutdowns, startups, or emergency repairs**.

    Maintenance safety is not about caution alone—it's about implementing **systematic controls**, fostering a **zero-harm culture**, and ensuring **compliance with national and international standards**.

    ---

    ### 🧱 Key Pillars of Maintenance Safety

    #### 🔍 1. Risk Identification & Assessment
    - Perform **Job Hazard Analysis (JHA)** or **Task Risk Assessment (TRA)** before every job.
    - Identify all forms of energy: electrical, mechanical, pneumatic, hydraulic, thermal, chemical, and gravitational.
    - Assess likelihood and severity of harm—apply controls accordingly.

    #### 🔐 2. Lockout / Tagout / Tryout (LOTOTO)
    - Use **LOTO to isolate all energy sources** before performing work.
    - Apply physical locks and danger tags; never rely on just control signals.
    - Verify isolation by attempting startup after lockout (try-out step).
    - Maintain a **LOTO register** with key assignments, sign-off, and removal procedures.

    #### 🧑‍🏭 3. Personal Protective Equipment (PPE)
    - **Electrical work**: Arc-rated suits, gloves, face shields (NFPA 70E category-rated).
    - **Hot work**: Flame-resistant clothing, goggles, respirators.
    - **Mechanical work**: Cut-resistant gloves, steel-toe boots, eye protection.
    - **Confined space**: SCBA (if oxygen-deficient), gas detectors, retrieval harnesses.

    #### 🛠️ 4. Procedures and Work Permits
    - Implement a **Permit-to-Work (PTW)** system for non-routine, hazardous, or isolated work.
    - Include confined space entry, hot work, electrical isolation, and working at height permits.
    - Ensure all involved personnel review the procedure and sign off.

    #### 🧰 5. Tools, Equipment, and Calibration
    - Only use **tested and calibrated tools**—especially for electrical and pressure work.
    - Inspect all tools for damage before use.
    - Tag out or discard any defective equipment.

    #### 📣 6. Communication & Human Factors
    - Use **toolbox talks** before every shift or job to align the team.
    - Maintain clear radio or verbal communication during complex operations.
    - Address fatigue, distraction, or overconfidence—common precursors to errors.

    #### 🚨 7. Emergency Preparedness
    - Have trained **first responders** and CPR-certified staff on every shift.
    - Know locations of **eyewash stations, fire extinguishers, and emergency shutoffs**.
    - Conduct periodic emergency drills for arc flash, gas leak, fire, and rescue operations.

    ---

    ### 🧱 High-Risk Maintenance Scenarios & Mitigations

    | Task | Risk | Safety Measures |
    |------|------|-----------------|
    | Live Electrical Testing | Arc flash, shock | NFPA 70E-compliant PPE, insulated tools, clearances |
    | Confined Space Entry | Asphyxiation, entrapment | Gas testing, continuous monitoring, standby rescue |
    | Hot Work | Fire, burns, explosion | Fire watch, permits, ventilation, spark arrestors |
    | Working at Height | Falls | Fall arrest system, anchor points, scaffolding checks |
    | Valve / Piping Maintenance | Pressure release, chemical exposure | Depressurize, drain, tag, wear chemical PPE |

    ---

    ### 📊 Safety KPIs for Maintenance Teams

    - **LTIFR**: Lost Time Injury Frequency Rate
    - **PTW Compliance Rate**
    - **PPE Usage Adherence**
    - **Near Miss Reporting Rate**
    - **Emergency Drill Completion Score**

    Monitoring these indicators helps track the maturity and effectiveness of your maintenance safety program.

      ---

    ### 🧭 Building a Zero Harm Maintenance Culture

    A strong maintenance safety program isn’t reactive—it’s **proactive, behavior-based, and embedded in daily routines**. Every technician, planner, and manager shares the responsibility. Empower workers with Stop Work Authority. Celebrate hazard reporting. Make safety personal.

    Remember: **No job is so urgent or important that it cannot be done safely.**
    """)

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)


elif selection == "Common Maintenance Mistakes & Myths":
    st.header("🧯 Common Maintenance Mistakes & Myths")

    st.markdown("""
    Many maintenance programs suffer due to **misconceptions**, outdated practices, or avoidable mistakes.
    Recognizing these myths and errors is essential to improving reliability, safety, and efficiency.

    ### ⚠️ Common Mistakes & Myths in Power Plant Maintenance
    """)

    myths = [
        ("🧰 **Myth: Run-to-failure is cheaper than planned maintenance.**",
         "Reality: Emergency repairs are often **3-10x more expensive** than scheduled maintenance, especially in power plants."),
        
        ("⏱️ **Myth: Time-based PM ensures maximum reliability.**",
         "Reality: Time-based maintenance can lead to **over-maintenance** or missing unpredictable failures. Condition-based strategies are often more effective."),
        
        ("🧪 **Myth: Equipment needs maintenance only when it breaks.**",
         "Reality: Many faults develop gradually and can be detected early using vibration, IR, oil, or ultrasound monitoring."),
        
        ("📦 **Myth: Spare parts availability equals readiness.**",
         "Reality: Without proper inventory management, parts may be obsolete, damaged, or misplaced when needed."),
        
        ("📈 **Myth: More data always leads to better decisions.**",
         "Reality: Data without interpretation leads to confusion. Use **diagnostics, trend analysis**, and AI only when they serve a decision."),
        
        ("📉 **Mistake: Ignoring early warning signs.**",
         "Vibrations, temperature rises, or minor leaks are often early symptoms of deeper issues."),
        
        ("🧑‍🔧 **Mistake: No feedback from technicians.**",
         "Technicians' observations are a valuable **source of failure clues**, yet often overlooked."),
        
        ("📅 **Mistake: Poor planning & scheduling.**",
         "Uncoordinated maintenance increases downtime. Planning improves labor efficiency and spare part usage."),
        
        ("📋 **Mistake: Relying on outdated CMMS entries.**",
         "CMMS data must be **updated and reviewed** regularly to reflect current asset status."),
        
        ("💸 **Mistake: Focusing only on cost, not consequences.**",
         "Low-cost choices in maintenance (e.g., cheap parts, skipped PM) often lead to **high-consequence failures** later."),
    ]

    for myth, reality in myths:
        st.markdown(f"""
        <div style="margin-bottom: 1em; border-left: 4px solid #007acc; padding-left: 1em;">
        <h5 style="color:#cc3300;">{myth}</h5>
        <p style="color:#444;">{reality}</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("✅ Awareness of these mistakes helps avoid downtime, reduces cost, and strengthens plant reliability.")

    st.markdown("""
    ---
    👤 Developed by **Eng. Mohammed Assaf - CMPR, CEPSS**
    """)



elif selection == "Maintenance Quiz":
    st.header("🧠 Maintenance Knowledge Quiz")
    st.markdown("""
    Test your knowledge on maintenance strategies, condition monitoring, KPIs, safety, and reliability concepts.  
    Answer all questions and press the button below to see your score and detailed feedback.
    """)

    quiz_questions = [
        ("Which maintenance strategy is best suited for low-cost, non-critical assets?", ["RCM", "CBM", "Run-to-Failure", "PdM"], 2, "RTF is ideal for non-critical, inexpensive assets."),
        ("Which strategy is based on regularly scheduled interventions?", ["Corrective", "Predictive", "Preventive", "Reactive"], 2, "Preventive maintenance follows a time or usage-based schedule."),
        ("Which factor is most critical in selecting a maintenance strategy?", ["Asset color", "Manufacturer name", "Failure impact", "Location"], 2, "RCM selects strategies based on consequences of failure."),
        ("What does a strategy recommendation matrix usually compare?", ["Voltage vs. temperature", "Risk vs. maintenance cost", "Color vs. size", "Speed vs. power"], 1, "Strategy tools map risk vs. cost."),
        ("Which technique detects electrical insulation faults?", ["Ultrasound", "IR Thermography", "Megger Testing", "Vibration"], 2, "Megger testing is used to detect insulation weaknesses."),
        ("Which of these is not a condition monitoring method?", ["Oil analysis", "Thermal imaging", "Hammering", "Ultrasound"], 2, "Hammering is not a diagnostic technique."),
        ("In the DIPF model, when is the best time to apply predictive maintenance?", ["Design", "Installation", "Prediction", "Failure"], 2, "Predictive maintenance is most useful during the prediction phase."),
        ("The 'F' in DIPF represents:", ["Fix", "Flow", "Failure", "Forecast"], 2, "'F' in DIPF stands for Failure."),
        ("The early failure period of the bathtub curve is also known as:", ["Random zone", "Infant mortality", "Steady state", "Burn-in phase"], 1, "Infant mortality phase has high initial failure rates."),
        ("The constant failure rate phase in the bathtub curve is called:", ["Useful life", "Obsolete life", "Initial wear", "Shutdown phase"], 0, "Useful life has a low and constant failure rate."),
        ("Which of the following tools is commonly used in RCA?", ["CMMS", "Fishbone diagram", "PLC", "SCADA"], 1, "Fishbone diagrams help identify root causes."),
        ("Why is RCA important in maintenance?", ["It makes checklists", "It increases paperwork", "It prevents recurrence", "It reduces cleaning"], 2, "RCA aims to eliminate the true cause of failure."),
        ("In FMEA, the Risk Priority Number (RPN) is calculated by:", ["Severity + Occurrence + Detection", "Severity × Occurrence × Detection", "Failure ÷ Risk × Time", "Risk – Detection + Time"], 1, "RPN = Severity × Occurrence × Detection."),
        ("Which failure mode is most critical in FMEA?", ["High severity, low detection", "Low severity, high detection", "High detection, low occurrence", "None of the above"], 0, "High severity + low detectability = high risk."),
        ("What does a Gantt chart show in maintenance?", ["Power consumption", "Spare parts", "Job schedules over time", "Efficiency"], 2, "Gantt charts visualize maintenance timelines."),
        ("Which role ensures planned work is executed on time?", ["Storekeeper", "Operator", "Planner", "Driver"], 2, "Planners ensure scheduled work is ready and organized."),
        ("Which analysis helps prioritize spare parts?", ["ABC Analysis", "RCA", "P-F Curve", "Fishbone"], 0, "ABC classifies inventory by value and criticality."),
        ("What is the risk of overstocking spare parts?", ["No impact", "Waste of capital", "Improved uptime", "More failures"], 1, "Overstocking ties up capital and storage space."),
        ("A CMMS is used for:", ["Motor cooling", "Maintenance tracking", "Lubrication", "Vibration analysis"], 1, "CMMS tracks work orders, history, assets."),
        ("Which technology helps predict equipment failure using big data?", ["IIoT", "RTF", "Thermography", "ABC"], 0, "IIoT sensors stream real-time data for analysis."),
        ("Availability is calculated as:", ["Uptime / Total time", "Downtime / Uptime", "Load × Speed", "Cycle time – MTBF"], 0, "Availability = Uptime / (Uptime + Downtime)."),
        ("Which KPI reflects repair efficiency?", ["MTBF", "MTTR", "OEE", "P-F"], 1, "MTTR (Mean Time To Repair) shows how fast a system is restored."),
        ("Which safety procedure ensures all energy is removed before maintenance?", ["LOTO", "FMEA", "PPE", "TPM"], 0, "LOTO (Lockout Tagout) isolates energy sources."),
        ("Which hazard is most common during confined space maintenance?", ["Vibration", "Overheating", "Asphyxiation", "Noise"], 2, "Lack of oxygen is a leading risk in confined spaces."),
        ("What is the purpose of proactive maintenance?", ["Replace all components regularly", "React after failure", "Eliminate root causes of failure", "Ignore minor defects"], 2, "Proactive maintenance eliminates root causes before failure occurs."),
        ("CBM stands for:", ["Corrective Based Monitoring", "Condition Based Maintenance", "Continuous Battery Maintenance", "Certified Breakdown Model"], 1, "CBM relies on actual equipment condition to determine maintenance needs."),
        ("The wear-out period of an asset is characterized by:", ["Low failure rate", "Sudden voltage spikes", "High and increasing failure rate", "Noisy operations"], 2, "Failures increase due to age-related wear and fatigue."),
        ("Which KPI shows how much of the scheduled work was done?", ["MTTR", "MTBF", "Schedule Compliance", "Availability"], 2, "Schedule Compliance measures % of jobs completed on time."),
        ("RCM aims to:", ["Reduce staffing levels", "Select optimal strategy per failure mode", "Use one strategy for all equipment", "Eliminate the need for monitoring"], 1, "RCM chooses maintenance strategy based on risk and function."),
        ("Electrical Signature Analysis is mainly used for:", ["Pipe thickness", "Bearing vibration", "Motor diagnostics", "Gas insulation"], 2, "ESA identifies motor faults via voltage/current waveform analysis."),
        ("What does PdM stand for?", ["Proactive diagnostic Maintenance", "Prescribed digital Maintenance", "Predictive Maintenance", "Preventive deep Maintenance"], 2, "PdM stands for Predictive Maintenance, which uses data trends to forecast failures."),
        ("What is the main goal of Total Productive Maintenance (TPM)?", ["Increase overtime", "Eliminate planned maintenance", "Maximize equipment effectiveness", "Minimize staff involvement"], 2, "TPM aims to maximize equipment effectiveness with operator involvement."),
        ("Which tool is used to analyze and visualize failure trends?", ["Piping and Instrument Diagram", "Pareto chart", "Maintenance checklist", "Gantt chart"], 1, "Pareto charts highlight the most frequent or impactful causes."),
        ("Which technique monitors particle contamination in oil?", ["Vibration", "Infrared", "Oil analysis", "Ultrasound"], 2, "Oil analysis checks for wear particles, contamination, and fluid properties."),
        ("In the P-F Curve, what does 'P' stand for?", ["Preventive", "Potential failure", "Physical wear", "Performance drop"], 1, "'P' stands for Potential Failure—the point where degradation becomes detectable."),
        ("Which software tool helps in planning and tracking maintenance work?", ["ERP", "SCADA", "CMMS", "PLC"], 2, "CMMS stands for Computerized Maintenance Management System."),
        ("The main benefit of predictive over preventive maintenance is:", ["Lower reliability", "Higher manpower", "Less data required", "Longer asset life"], 3, "Predictive maintenance extends asset life by addressing issues before failure."),
        ("Which condition monitoring technique is best for rotating equipment?", ["Thermal camera", "Vibration analysis", "Oil level inspection", "Ultrasound"], 1, "Vibration analysis is ideal for rotating components like motors and pumps."),
        ("What is the typical shape of the failure rate in the bathtub curve?", ["S-curve", "Straight line", "U-curve", "Bathtub-shaped"], 3, "The bathtub curve shows early, constant, and wear-out failure rates."),
        ("Which of the following is not part of the OEE formula?", ["Availability", "Quality", "Utilization", "Performance"], 2, "OEE includes Availability, Performance, and Quality."),
        ("What does the 'criticality' of an asset refer to?", ["Size", "Color", "Impact of its failure", "Speed of operation"], 2, "Criticality measures how failure affects safety, production, or cost."),
        ("When is 'Run to Failure' acceptable?", ["For mission-critical assets", "For non-critical, low-cost items", "For transformer bushings", "For gas turbines"], 1, "RTF is acceptable for inexpensive, low-impact equipment."),
        ("Which failure detection method is most immediate?", ["Visual inspection", "Manual records", "Online sensor monitoring", "Annual audits"], 2, "Sensors enable continuous, real-time monitoring."),
        ("What does MTBF measure?", ["Maintenance time before fix", "Mean time between failures", "Machine tuning before fault", "Minimum temperature before fire"], 1, "MTBF is the average time between failures."),
        ("A low MTTR value means:", ["Slow repairs", "Frequent failures", "Fast recovery after failure", "Less data collected"], 2, "Low MTTR = equipment is restored quickly."),
        ("Why is schedule compliance important?", ["To track fuel levels", "To improve warehouse layout", "To ensure timely execution of PM tasks", "To reduce meeting duration"], 2, "It measures how much planned work is done on time."),
        ("Root cause analysis should be done after:", ["Every successful job", "Random sampling", "A major or repeated failure", "Quarterly audits"], 2, "RCA is conducted to understand and prevent recurring or serious failures."),
        ("Which of the following improves mean time between failures?", ["Overloading equipment", "Skipping lubrication", "Proper preventive maintenance", "Ignoring wear"], 2, "Preventive actions reduce stress and extend lifespan."),
        ("What does a high RPN in FMEA indicate?", ["Low priority", "No concern", "High risk", "Maintenance completed"], 2, "A high Risk Priority Number requires action."),
        ("Infrared thermography is used mainly for:", ["Voltage testing", "Visual inspection", "Detecting hotspots", "Harmonics measurement"], 2, "IR thermography detects heat anomalies in electrical and mechanical systems."),
    ]

    user_answers = {}
    submitted = st.button("📊 Submit All Answers")
    score = 0

    for i, (question, options, correct_idx, explanation) in enumerate(quiz_questions):
        st.subheader(f"Q{i+1}: {question}")
        user_choice = st.radio("Select one:", options, key=f"quiz_{i}")
        user_answers[i] = user_choice

        if submitted:
            correct_answer = options[correct_idx]
            if user_choice == correct_answer:
                st.success(f"✅ Correct — {explanation}")
                score += 1
            else:
                st.error(f"❌ Incorrect. Correct answer: {correct_answer} — {explanation}")

    if submitted:
        st.markdown("----")
        st.subheader(f"🏁 Final Score: **{score} out of {len(quiz_questions)}**")

        if score < 25:
            st.warning("📘 Level: **Beginner** — Keep learning! Review key concepts and try again.")
        elif 25 <= score < 40:
            st.info("📗 Level: **Intermediate** — Great job! You're well on your way.")
        else:
            st.success("📙 Level: **Expert** — Excellent! You have strong maintenance knowledge.")

        st.markdown("""
        ---
        👤 Developed by **Eng. Mohammed Assaf – CMRP, CEPSS**
        """)


elif selection == "About":
    st.header("ℹ️ About App Developer")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("Assaf_pic.png", width=130)  # Update with your actual file name
    with col2:
    	st.markdown("""
	👤 **Mohammed S. Assaf – CMRP, CEPSS**  
	⚡ **Power Plant Electrical Maintenance Engineer**  
	🏭 **Attarat Operation and Maintenance Company (OMCO), Jordan**  
	📘 **Author of – Power Transformers Electrical Testing Handbook**  
	📧 **Email:** [Mohammad.assaf@aom.com.jo](mailto:Mohammad.assaf@aom.com.jo)
	""")
    

    st.subheader("📨 Feedback Form")
    with st.form(key="feedback_form"):
        name = st.text_input("Your Name")
        title = st.text_input("Your Designation")
        feedback = st.text_area("Your Feedback")
        send_button = st.form_submit_button("📤 Send Feedback")

    if send_button:
        if name and feedback:
            sender_email = "Assaf.Maintenance.fb@gmail.com"
            receiver_email = "Assaf.Maintenance.fb@gmail.com"
            app_password = "gykeilyvzxdsxwyu"  # Replace with your Gmail App Password

            message = MIMEText(f"Name: {name}\nDesignation: {title}\n\nFeedback:\n{feedback}")
            message["Subject"] = "📩 New Feedback from Maintenance App"
            message["From"] = sender_email
            message["To"] = receiver_email

            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login(sender_email, app_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                server.quit()
                st.success("✅ Thank you! Your feedback has been sent to Eng. Mohammed Assaf.")
            except Exception as e:
                st.error(f"❌ Could not send feedback. Error: {e}")
        else:
            st.warning("⚠️ Please fill in your name and feedback.")