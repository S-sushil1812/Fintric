import streamlit as st
from streamlit_elements import elements, mui, nivo
import plotly.express as px
import pandas as pd
from datetime import date
import transactions as txmod
import ai_utils
from auth_utils import register_user, authenticate_user, google_oauth_url, handle_google_signin

def divider_glowing():
    """Render a premium glowing divider line with gradient"""
    st.markdown("""
    <hr style="
        border: none;
        height: 2px;
        background: linear-gradient(
            90deg,
            transparent,
            #00D1FF,
            #6366F1,
            transparent
        );
        margin: 25px 0;
        opacity: 0.7;
        box-shadow: 0 0 15px rgba(0, 209, 255, 0.4);
    ">
    """, unsafe_allow_html=True)

def  show_login_page():
    """Display a premium fintech SaaS login page (fixed layout with proper containers)"""
    handle_google_signin()
    
    st.markdown("""
        <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        html, body, [data-testid="stAppViewContainer"] {
            background: #0B0F19 !important;
        }
        
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 2rem !important;
            max-width: 1200px;
        }
        
        section.main > div {
            padding-top: 0 !important;
        }
        
        .background-glow {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(0, 209, 255, 0.04) 0%, rgba(99, 102, 241, 0.02) 50%, transparent 100%);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
        }
        
        .hero-section {
            width: 100%;
            max-width: 900px;
            margin: 2.5rem auto;
            padding: 0 1rem;
            text-align: center;
            animation: fadeInDown 0.6s ease-out;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .hero-title {
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 0 auto 0.3rem auto;
            letter-spacing: -0.5px;
            width: 100%;
        }
        
        .hero-subtitle {
            font-size: 0.95rem;
            color: #9CA3AF;
            max-width: 500px;
            margin: 0 auto;
            padding: 0 1rem;
            font-weight: 400;
            line-height: 1.5;
            text-align: center;
            width: 100%;
        }
        
        .card-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #E5E7EB;
            margin-bottom: 0.25rem;
            text-align: center;
        }
        
        .card-subtitle {
            font-size: 0.85rem;
            color: #6B7280;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        
        /* Style Streamlit container for card effect */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: #111827 !important;
            border: 1px solid rgba(0, 209, 255, 0.15) !important;
            border-radius: 14px !important;
            padding: 2rem !important;
            box-shadow: 0 15px 50px rgba(0, 209, 255, 0.08) !important;
        }
        
        /* Style input fields */
        input {
            background: #1F2937 !important;
            color: #E5E7EB !important;
            border: 1.5px solid #374151 !important;
            border-radius: 8px !important;
            padding: 0.85rem 1rem !important;
            font-size: 0.95rem !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        
        input::placeholder {
            color: #6B7280 !important;
        }
        
        input:focus {
            border-color: #00D1FF !important;
            box-shadow: 0 0 0 3px rgba(0, 209, 255, 0.1) !important;
        }
        
        /* Style buttons */
        button {
            font-weight: 600 !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            border-radius: 8px !important;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%) !important;
            color: #0B0F19 !important;
            border: none !important;
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(0, 209, 255, 0.3) !important;
        }
        
        .divider-container {
            margin: 1.3rem 0;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .divider-line {
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, transparent, #374151, transparent);
        }
        
        .divider-text {
            color: #6B7280;
            font-size: 0.8rem;
            font-weight: 500;
        }
        
        .google-btn {
            width: 100%;
            padding: 0.85rem 1rem;
            background: #1F2937 !important;
            border: 1.5px solid #374151 !important;
            border-radius: 8px !important;
            color: #E5E7EB !important;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .google-btn:hover {
            background: #2C3A4A !important;
            border-color: #6366F1 !important;
            transform: translateY(-2px);
        }
        
        .auth-toggle {
            text-align: center;
            margin-top: 1.2rem;
            font-size: 0.85rem;
            color: #9CA3AF;
        }
        
        .auth-toggle-link {
            color: #00D1FF;
            cursor: pointer;
            font-weight: 600;
            transition: color 0.2s;
        }
        
        .auth-toggle-link:hover {
            color: #6366F1;
        }
        
        .features-section {
            margin-top: 2.5rem;
            text-align: center;
        }
        
        .features-heading {
            font-size: 1.3rem;
            font-weight: 700;
            color: #E5E7EB;
            margin-bottom: 0.3rem;
        }
        
        .features-subheading {
            font-size: 0.9rem;
            color: #9CA3AF;
            margin-bottom: 1.8rem;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.3rem;
            max-width: 900px;
            margin: 0 auto;
        }
        
        .feature-card {
            background: #111827;
            border: 1px solid rgba(0, 209, 255, 0.1);
            border-radius: 10px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            animation: fadeInUp 0.6s ease-out backwards;
        }
        
        .feature-card:nth-child(1) { animation-delay: 0.2s; }
        .feature-card:nth-child(2) { animation-delay: 0.25s; }
        .feature-card:nth-child(3) { animation-delay: 0.3s; }
        
        .feature-card:hover {
            background: #1F2937;
            border-color: #00D1FF;
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0, 209, 255, 0.1);
        }
        
        .feature-icon {
            font-size: 2.2rem;
            margin-bottom: 0.8rem;
            transition: transform 0.3s;
        }
        
        .feature-card:hover .feature-icon {
            transform: scale(1.1);
        }
        
        .feature-title {
            font-size: 1rem;
            font-weight: 700;
            color: #E5E7EB;
            margin-bottom: 0.4rem;
        }
        
        .feature-desc {
            color: #9CA3AF;
            font-size: 0.85rem;
            line-height: 1.5;
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-15px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(15px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @media (max-width: 768px) {
            .hero-title { font-size: 1.8rem; }
            .hero-subtitle { font-size: 0.9rem; }
            .features-grid { grid-template-columns: 1fr; }
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="background-glow"></div>', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="hero-section">
        <h1 class="hero-title">AI Finance Tracker</h1>
        <h2 class="hero-subtitle">Take control of your finances with AI-powered insights</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    if 'auth_mode' not in st.session_state:
        st.session_state['auth_mode'] = 'login'
    
    # Center card using columns
    col_spacer1, col_main, col_spacer2 = st.columns([1, 2, 1])
    
    with col_main:
        if st.session_state['auth_mode'] == 'login':
            with st.container():
                st.markdown('<h2 class="card-title">Welcome Back</h2>', unsafe_allow_html=True)
                st.markdown('<p class="card-subtitle">Sign in to your account</p>', unsafe_allow_html=True)
                
                username = st.text_input('Email or Username', key='login_username', placeholder='Username', label_visibility='collapsed')
                password = st.text_input('Password', type='password', key='login_password', placeholder='••••••••', label_visibility='collapsed')
                
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    if st.button('🔓 Login', key='login_btn', use_container_width=True):
                        if username and password:
                            user = authenticate_user(username, password)
                            if user:
                                st.session_state['logged_in'] = True
                                st.session_state['user'] = {'id': user.id, 'username': user.username}
                                st.success('✓ Login successful!')
                                st.balloons()
                                st.rerun()
                            else:
                                st.error('✗ Invalid credentials')
                        else:
                            st.error('✗ Please fill in all fields')
                
                with btn_col2:
                    if st.button('Create Account', key='switch_to_register', use_container_width=True):
                        st.session_state['auth_mode'] = 'register'
                        st.rerun()
                
                st.markdown('<div class="divider-container"><div class="divider-line"></div><div class="divider-text">OR</div><div class="divider-line"></div></div>', unsafe_allow_html=True)
                
                oauth_url = google_oauth_url()
                if oauth_url:
                    st.markdown(f'<a href="{oauth_url}" target="_self"><button class="google-btn">🔍 Continue with Google</button></a>', unsafe_allow_html=True)
                
                st.markdown('<div class="auth-toggle">Don\'t have an account? <span class="auth-toggle-link" onclick="document.querySelectorAll(\'[data-testid=stButton]\')[1].click()">Sign up</span></div>', unsafe_allow_html=True)
        
        else:
            with st.container():
                st.markdown('<h2 class="card-title">Create Account</h2>', unsafe_allow_html=True)
                st.markdown('<p class="card-subtitle">Join thousands of users</p>', unsafe_allow_html=True)
                
                reg_username = st.text_input('Choose Username', key='register_username', placeholder='johndoe', label_visibility='collapsed')
                reg_password = st.text_input('Password', type='password', key='register_password', placeholder='••••••••', label_visibility='collapsed')
                reg_confirm = st.text_input('Confirm Password', type='password', key='confirm_password', placeholder='••••••••', label_visibility='collapsed')
                
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    if st.button('✓ Register', key='register_btn', use_container_width=True):
                        if reg_username and reg_password and reg_confirm:
                            if reg_password == reg_confirm:
                                user = register_user(reg_username, reg_password)
                                if user:
                                    st.success('✓ Account created! Please login.')
                                    st.session_state['auth_mode'] = 'login'
                                    st.rerun()
                                else:
                                    st.error('✗ Username already exists')
                            else:
                                st.error('✗ Passwords do not match')
                        else:
                            st.error('✗ Please fill in all fields')
                
                with btn_col2:
                    if st.button('Back to Login', key='switch_to_login', use_container_width=True):
                        st.session_state['auth_mode'] = 'login'
                        st.rerun()
    
    st.markdown('''
        <div class="features-section">
            <h2 class="features-heading">Why choose FINTRIC?</h2>
            <p class="features-subheading">Powerful features to manage your finances</p>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h4 class="feature-title">Smart Analytics</h4>
                    <p class="feature-desc">Get AI-powered insights into spending patterns</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🤖</div>
                    <h4 class="feature-title">AI Assistant</h4>
                    <p class="feature-desc">Ask natural language questions about finances</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📈</div>
                    <h4 class="feature-title">Visual Reports</h4>
                    <p class="feature-desc">Beautiful charts and graphs for tracking</p>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)


def show_dashboard(user_id):
    """Modern fintech dashboard with advanced UI/UX"""
    st.markdown("""
    <style>
    .hero-container {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #0B0F19 0%, #1F2937 50%, #111827 100%);
        border-radius: 16px;
        margin-bottom: 2rem;
        border: 1px solid rgba(0, 209, 255, 0.1);
    }
    .hero-title {
        background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: 800;
        margin: 0 0 1rem 0;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        color: #9CA3AF;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    .card {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        border: 1px solid rgba(0, 209, 255, 0.15);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    .card:hover {
        transform: translateY(-8px);
        border-color: rgba(0, 209, 255, 0.4);
        box-shadow: 0 20px 40px rgba(0, 209, 255, 0.15);
    }
    .card-label {
        color: #9CA3AF;
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    .card-value {
        color: #E5E7EB;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .card-change {
        font-size: 0.85rem;
    }
    .card-change.positive { color: #22C55E; }
    .card-change.negative { color: #EF4444; }
    .chart-container {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        border: 1px solid rgba(0, 209, 255, 0.15);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    .chart-title {
        color: #E5E7EB;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        border: 1px solid rgba(0, 209, 255, 0.15);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .feature-card:hover {
        transform: translateY(-6px);
        border-color: rgba(0, 209, 255, 0.5);
        box-shadow: 0 15px 40px rgba(0, 209, 255, 0.2);
    }
    .feature-icon { font-size: 2.5rem; margin-bottom: 1rem; }
    .feature-title { color: #E5E7EB; font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; }
    .feature-desc { color: #9CA3AF; font-size: 0.85rem; line-height: 1.4; }
    .section-title {
        color: #E5E7EB;
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        border-left: 4px solid #00D1FF;
        padding-left: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">💰 AI-powered Personal Finance Tracker</div>
        <div class="hero-subtitle">✨ Take control of your finances with intelligent insights</div>
    </div>
    """, unsafe_allow_html=True)
    
    rows_user = txmod.list_transactions(user_id)
    total_income = float(sum(r.amount for r in rows_user if r.amount > 0)) if rows_user else 0.0
    total_expenses = float(-sum(r.amount for r in rows_user if r.amount < 0)) if rows_user else 0.0
    total_balance = total_income - total_expenses
    savings_rate = ((total_balance / total_income) * 100) if total_income > 0 else 0
    
    st.markdown('<div class="section-title">📊 Financial Summary</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        balance_class = 'positive' if total_balance >= 0 else 'negative'
        balance_icon = '↗ Active' if total_balance >= 0 else '↘ Deficit'
        st.markdown(f'<div class="card"><div class="card-label">💰 Total Balance</div><div class="card-value">${total_balance:,.0f}</div><div class="card-change {balance_class}">{balance_icon}</div></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div class="card"><div class="card-label">📈 Total Income</div><div class="card-value" style="color: #22C55E;">${total_income:,.0f}</div><div class="card-change positive">From all sources</div></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'<div class="card"><div class="card-label">📉 Total Expenses</div><div class="card-value" style="color: #EF4444;">${total_expenses:,.0f}</div><div class="card-change negative">Outgoing funds</div></div>', unsafe_allow_html=True)
    
    with col4:
        savings_class = 'positive' if savings_rate >= 20 else 'negative'
        savings_text = 'On track' if savings_rate >= 20 else 'Improve needed'
        st.markdown(f'<div class="card"><div class="card-label">🎯 Savings Rate</div><div class="card-value">{savings_rate:.1f}%</div><div class="card-change {savings_class}">{savings_text}</div></div>', unsafe_allow_html=True)
    
    if rows_user:
        st.markdown('<div class="section-title">📊 Financial Insights</div>', unsafe_allow_html=True)
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            st.markdown('<div class="chart-container"><div class="chart-title">💳 Expense Breakdown</div>', unsafe_allow_html=True)
            expense_data = [r for r in rows_user if r.amount < 0]
            if expense_data:
                categories = {}
                for r in expense_data:
                    cat = r.category or 'Uncategorized'
                    categories[cat] = categories.get(cat, 0) + abs(r.amount)
                
                # Nivo Pie Chart with Fintech Colors
                color_palette = ['#00D1FF', '#6366F1', '#22C55E', '#EF4444', '#F59E0B', '#EC4899']
                pie_data = []
                for idx, (cat, amount) in enumerate(categories.items()):
                    pie_data.append({
                        'id': cat,
                        'label': cat,
                        'value': float(amount),
                        'color': color_palette[idx % len(color_palette)]
                    })
                
                with elements('dashboard_pie'):
                    with mui.Box(sx={"height": 450, "width": "100%"}):
                        nivo.Pie(
                            data=pie_data,
                            margin={"top": 80, "right": 100, "bottom": 80, "left": 80},
                            innerRadius=0.5,
                            padAngle=0.7,
                            cornerRadius=3,
                            activeOuterRadiusOffset=8,
                            borderWidth=2,
                            borderColor="#0B0F19",
                            arcLinkLabelsSkipAngle=10,
                            arcLinkLabelsTextColor="#9CA3AF",
                            arcLinkLabelsThickness=2,
                            arcLinkLabelsColor={"from": "color"},
                            arcLabelsSkipAngle=10,
                            arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                            legends=[
                                {
                                    "anchor": "bottom-right",
                                    "direction": "column",
                                    "justify": False,
                                    "translateX": 0,
                                    "translateY": 80,
                                    "itemsSpacing": 10,
                                    "itemWidth": 120,
                                    "itemHeight": 24,
                                    "itemTextColor": "#E5E7EB",
                                    "itemDirection": "left-to-right",
                                    "itemOpacity": 1,
                                    "symbolSize": 16,
                                    "symbolShape": "circle",
                                    "effects": [
                                        {"on": "hover", "style": {"itemTextColor": "#00D1FF", "itemOpacity": 1}}
                                    ],
                                }
                            ],
                            theme={
                                "background": "#0B0F19",
                                "textColor": "#E5E7EB",
                                "tooltip": {
                                    "container": {
                                        "background": "#111827",
                                        "color": "#E5E7EB",
                                        "borderRadius": "4px",
                                        "boxShadow": "0 0 20px rgba(0, 209, 255, 0.3)",
                                        "padding": "8px 12px"
                                    }
                                }
                            },
                        )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with chart_col2:
            st.markdown('<div class="chart-container"><div class="chart-title">📈 Monthly Trend</div>', unsafe_allow_html=True)
            data_for_chart = [{'date': r.date, 'amount': r.amount, 'type': 'Income' if r.amount > 0 else 'Expense'} for r in rows_user]
            if data_for_chart:
                df_trend = pd.DataFrame(data_for_chart)
                df_trend['date'] = pd.to_datetime(df_trend['date'])
                income_trend = df_trend[df_trend['type'] == 'Income'].groupby('date')['amount'].sum()
                expense_trend = df_trend[df_trend['type'] == 'Expense'].groupby('date')['amount'].sum()
                fig_line = px.line(title=None)
                if not income_trend.empty:
                    fig_line.add_scatter(x=income_trend.index, y=income_trend.values, name='Income', line=dict(color='#22C55E', width=3), fill='tozeroy', fillcolor='rgba(34, 197, 94, 0.1)', mode='lines+markers')
                if not expense_trend.empty:
                    fig_line.add_scatter(x=expense_trend.index, y=expense_trend.values, name='Expenses', line=dict(color='#EF4444', width=3), fill='tozeroy', fillcolor='rgba(239, 68, 68, 0.1)', mode='lines+markers')
                fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#E5E7EB', size=12), hovermode='x unified', legend=dict(x=0, y=1, bgcolor='rgba(0,0,0,0.5)', bordercolor='#6366F1'), xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(99, 102, 241, 0.1)'), yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(99, 102, 241, 0.1)'))
                st.plotly_chart(fig_line, use_container_width=True, config={'displayModeBar': False})
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">✨ Key Features</div>', unsafe_allow_html=True)
    st.markdown("""<div class="features-grid">
        <div class="feature-card"><div class="feature-icon">📊</div><div class="feature-title">Track Expenses</div><div class="feature-desc">Categorize and monitor all your spending</div></div>
        <div class="feature-card"><div class="feature-icon">🤖</div><div class="feature-title">AI Chatbot</div><div class="feature-desc">Get instant financial insights</div></div>
        <div class="feature-card"><div class="feature-icon">📥</div><div class="feature-title">Import CSV</div><div class="feature-desc">Bulk import transactions from bank</div></div>
        <div class="feature-card"><div class="feature-icon">📈</div><div class="feature-title">Analytics</div><div class="feature-desc">Visualize financial trends</div></div>
        <div class="feature-card"><div class="feature-icon">🧮</div><div class="feature-title">Calculators</div><div class="feature-desc">EMI, SIP, and more tools</div></div>
        <div class="feature-card"><div class="feature-icon">📱</div><div class="feature-title">Cloud Sync</div><div class="feature-desc">Access finances anytime</div></div>
    </div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">🚀 Quick Start</div>', unsafe_allow_html=True)
    qcol1, qcol2, qcol3 = st.columns(3)
    with qcol1:
        if st.button('➕ Add Transaction', width='stretch', key='dashboard_add_txn'):
            st.session_state['page'] = 'Transaction'
            st.rerun()
    with qcol2:
        if st.button('💬 Ask AI Chatbot', width='stretch', key='dashboard_chat'):
            st.session_state['page'] = 'Chatbot'
            st.rerun()
    with qcol3:
        if st.button('📥 Import CSV', width='stretch', key='dashboard_import'):
            st.session_state['page'] = 'Import CSV'
            st.rerun()
    
    # FAQ Section
    st.markdown("""
    <style>
    .faq-divider {
        height: 2px;
        background: linear-gradient(90deg, rgba(0, 209, 255, 0.3) 0%, rgba(0, 209, 255, 0) 100%);
        margin: 3rem 0 2rem 0;
    }
    
    .faq-section-title {
        color: #E5E7EB;
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 0.5rem;
        margin-bottom: 1.5rem;
        border-left: 4px solid #00D1FF;
        padding-left: 1rem;
    }
    
    div[data-testid="stExpander"] {
        background: rgba(31, 41, 55, 0.5) !important;
        border: 1px solid rgba(0, 209, 255, 0.1) !important;
        border-radius: 10px !important;
        margin-bottom: 0.8rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    div[data-testid="stExpander"]:hover {
        background: rgba(31, 41, 55, 0.8) !important;
        border-color: rgba(0, 209, 255, 0.3) !important;
        box-shadow: 0 8px 25px rgba(0, 209, 255, 0.1) !important;
    }
    
    div[data-testid="stExpander"] > div:first-child {
        color: #E5E7EB !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 1rem !important;
    }
    
    div[data-testid="stExpander"][aria-expanded="true"] > div:first-child {
        color: #00D1FF !important;
        font-weight: 700 !important;
    }
    
    div[data-testid="stExpander"] > div:last-child {
        color: #D1D5DB !important;
        padding: 1rem !important;
        font-size: 0.9rem !important;
        line-height: 1.6 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    divider_glowing()
    st.markdown('<div class="faq-section-title">❓ Frequently Asked Questions</div>', unsafe_allow_html=True)
    
    with st.expander("💰 How do I add transactions?"):
        st.markdown("""
        Adding transactions is simple:
        
        1. Click the **➕ Add Transaction** button in the Quick Start section
        2. Fill in the transaction details:
           - **Date**: Pick the transaction date
           - **Amount**: Enter the transaction amount
           - **Type**: Choose Credit (income) or Debit (expense)
           - **Category**: Select from predefined categories
           - **Description**: Add a brief description
           - **Notes**: Optional notes for reference
        3. Click **➕ Add Transaction** to save
        
        Transactions appear immediately in your dashboard and analytics!
        """)
    
    with st.expander("📥 How do I import CSV bank statements?"):
        st.markdown("""
        Import your bank statements in bulk:
        
        1. Click the **📥 Import CSV** button in the Quick Start section
        2. Click "Browse files" and select your CSV file
        3. The system will preview your data automatically
        4. Review the preview and make any necessary edits using the data editor
        5. Click **Import saved table to DB** to import all transactions
        
        Your bank statement data will be parsed and added to your account instantly!
        """)
    
    with st.expander("📊 What columns are required in CSV?"):
        st.markdown("""
        Your CSV file must contain these columns (exact names):
        
        **Required Columns:**
        - **Transaction Type** (or Type, Credit_Debit, DR/CR) - Use "Credit" or "Debit"
        - **Amount** (or Amt, Value) - The transaction amount
        
        **Recommended Columns:**
        - **Date** (or Transaction_Date, Posted, Value_Date) - Transaction date
        - **Description** (or Desc, Narration) - Description of transaction
        
        **Optional Columns:**
        - Any other columns will be imported but not used for categorization
        
        **Example CSV format:**
        ```
        Date, Description, Transaction Type, Amount
        2024-01-15, Salary, Credit, 50000
        2024-01-16, Rent Payment, Debit, 15000
        ```
        """)
    
    with st.expander("✏️ Can I edit or delete transactions?"):
        st.markdown("""
        Yes! You have full control over your transactions:
        
        **Edit Transactions:**
        - Go to the **Transaction** page
        - Use the **Preview (editable)** section to modify transactions
        - Click **Save table** to persist changes
        
        **Delete Transactions:**
        - Navigate to the **Delete Transactions** section
        - Select individual transactions from the dropdown
        - Click **🗑️ Delete Selected** and confirm
        - Or use **🗑️ Delete ALL Transactions** to clear everything
        
        Deleted transactions cannot be recovered, so proceed with caution!
        """)
    
    with st.expander("🏷️ How are categories assigned?"):
        st.markdown("""
        Categories help you organize your finances:
        
        **When Adding Transactions:**
        - Select from predefined categories during transaction entry
        - We provide smart suggestions based on transaction type
        
        **Credit Categories (Income):**
        Salary/Wages, Cheque Deposit, Cash Deposit, Bank Transfer Received, UPI Transfer Received, Refunds & Reimbursements, Rental Income, Insurance, Cashback & Rewards
        
        **Debit Categories (Expenses):**
        Home Rent, Groceries/Food, School Fee, Electricity Bill, Water Tax, Loan EMI, Travel, Entertainment, and more
        
        **When Importing:**
        - Categories are deduced from the description if available
        - You can manually assign categories in the preview
        
        Categories help generate detailed analytics and spending insights!
        """)
    
    with st.expander("📈 How do I view analytics and graphs?"):
        st.markdown("""
        Visualize your financial data with powerful analytics:
        
        **On Dashboard:**
        - View **Financial Summary** cards (income, expenses, balance, savings rate)
        - See **Monthly Trend** graph showing income vs expenses over time
        - Analyze **Expense Breakdown** pie chart by category
        
        **On Transaction Page:**
        - View **Category Analysis** with expense and income breakdowns
        - See **Monthly Breakdown** bar charts
        - Use filters to analyze specific periods or categories
        
        **On Import CSV Page:**
        - Preview automatically generated charts from imported data
        - See totals and breakdowns before saving
        
        All graphs update in real-time as you add or modify transactions!
        """)
    
    with st.expander("🤖 What does the AI chatbot do?"):
        st.markdown("""
        The AI chatbot provides instant financial insights:
        
        **What You Can Ask:**
        - 📊 "How much did I spend on groceries?"
        - 💰 "What's my total income this month?"
        - 📈 "Which category do I spend the most on?"
        - 🎯 "What's my savings rate?"
        - 📅 "Show me transactions from last week"
        - 🔍 "Analyze my spending patterns"
        
        **How It Works:**
        1. Click **💬 Ask AI Chatbot** from the dashboard
        2. Type your question in natural language
        3. The AI analyzes your recent transactions and responds
        4. Get instant insights without navigating through menus
        
        The chatbot is context-aware and uses your transaction history to provide personalized answers!
        """)
    
    with st.expander("🔒 Is my financial data secure?"):
        st.markdown("""
        Your financial security is our top priority:
        
        **Security Features:**
        - ✅ Password-protected accounts with encrypted storage
        - ✅ Only you can see your transaction data
        - ✅ Each user has isolated session and data
        - ✅ No financial data is shared with third parties
        - ✅ All data stored locally in the application database
        
        **Best Practices:**
        - Keep your password strong and unique
        - Don't share your account credentials
        - Log out when finished on shared devices
        - Review imported CSV files before importing
        
        Your privacy and security are fundamental to how we operate!
        """)


def show_transaction_page(user_id):
    st.markdown("""
    <style>
    .page-title { 
        text-align: center; 
        margin-bottom: 2.5rem; 
        margin-top: 1rem;
    }
    .page-title h1 {
        background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        text-shadow: 0 0 30px rgba(0, 209, 255, 0.4);
    }
    .page-title p { 
        color: #9CA3AF; 
        font-size: 1.05rem;
        margin-top: 0.75rem;
        font-weight: 400;
    }
    
    .form-card {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        border: 1px solid rgba(0, 209, 255, 0.15);
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 1.5rem;
    }
    
    .form-label {
        color: #E5E7EB;
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .input-field {
        width: 100%;
        padding: 0.75rem;
        background: #111827;
        border: 1px solid rgba(0, 209, 255, 0.2);
        border-radius: 8px;
        color: #E5E7EB;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .input-field:focus {
        outline: none;
        border-color: #00D1FF;
        box-shadow: 0 0 10px rgba(0, 209, 255, 0.3);
    }
    
    .type-toggle {
        display: flex;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .toggle-btn {
        flex: 1;
        padding: 0.75rem;
        border: 2px solid rgba(0, 209, 255, 0.3);
        background: #111827;
        color: #9CA3AF;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-weight: 600;
    }
    
    .toggle-btn.active {
        background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%);
        border-color: #00D1FF;
        color: #0B0F19;
    }
    
    .add-btn {
        width: 100%;
        padding: 1rem;
        background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%);
        color: #0B0F19;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 209, 255, 0.2);
    }
    
    .add-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 40px rgba(0, 209, 255, 0.35);
    }
    
    .summary-card {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        border: 1px solid rgba(0, 209, 255, 0.15);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .summary-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(0, 209, 255, 0.15);
    }
    
    .summary-label { color: #9CA3AF; font-size: 0.9rem; font-weight: 500; text-transform: uppercase; margin-bottom: 0.5rem; }
    .summary-value { font-size: 2rem; font-weight: 700; color: #E5E7EB; }
    .summary-gain .summary-value { color: #22C55E; }
    .summary-loss .summary-value { color: #EF4444; }
    .summary-net .summary-value { color: #00D1FF; }
    
    .section-title {
        color: #E5E7EB;
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        border-left: 4px solid #00D1FF;
        padding-left: 1rem;
    }
    
    .table-container {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        border: 1px solid rgba(0, 209, 255, 0.15);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        overflow-x: auto;
    }
    
    .search-filter-row {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }
    
    .search-box {
        flex: 1;
        min-width: 250px;
        padding: 0.75rem;
        background: #111827;
        border: 1px solid rgba(0, 209, 255, 0.2);
        border-radius: 8px;
        color: #E5E7EB;
    }
    
    .delete-section {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        border: 1px solid rgba(239, 68, 68, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 2rem;
    }
    
    .delete-btn {
        padding: 0.75rem 1.5rem;
        border: 2px solid #EF4444;
        background: rgba(239, 68, 68, 0.1);
        color: #EF4444;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-right: 1rem;
    }
    
    .delete-btn:hover {
        background: #EF4444;
        color: #0B0F19;
    }
    
    .delete-btn-primary {
        background: #EF4444;
        color: #0B0F19;
    }
    
    .txn-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .txn-table th {
        background: rgba(0, 209, 255, 0.1);
        color: #E5E7EB;
        padding: 1rem;
        text-align: left;
        font-weight: 600;
        border-bottom: 2px solid rgba(0, 209, 255, 0.2);
    }
    
    .txn-table td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid rgba(0, 209, 255, 0.1);
        color: #E5E7EB;
    }
    
    .txn-table tr:hover { background: rgba(0, 209, 255, 0.05); }
    .txn-credit { color: #22C55E; font-weight: 600; }
    .txn-debit { color: #EF4444; font-weight: 600; }
    
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""<div class="page-title">
        <h1>💸 Transactions</h1>
        <p>Manage and track your financial activity</p>
    </div>""", unsafe_allow_html=True)
    
    _, hcol_export = st.columns([0.85, 0.15])
    with hcol_export:
        if st.button('📥 Export Data', key='txn_export', use_container_width=True):
            rows_user = txmod.list_transactions(user_id)
            if rows_user:
                data = [{
                    'Date': r.date, 'Type': 'Credit' if r.amount > 0 else 'Debit',
                    'Description': r.description, 'Amount': r.amount,
                    'Category': r.category, 'Notes': r.notes
                } for r in rows_user]
                df_export = pd.DataFrame(data)
                csv = df_export.to_csv(index=False)
                st.download_button('Download CSV', csv, 'transactions.csv', 'text/csv')
                st.success('Ready to download!')
    
    # Form Card
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    
    form_col1, form_col2 = st.columns(2)
    
    with form_col1:
        st.markdown('<label class="form-label">📅 Date</label>', unsafe_allow_html=True)
        dt = st.date_input('date_input', value=date.today(), label_visibility='collapsed')
        
        st.markdown('<label class="form-label">💵 Amount</label>', unsafe_allow_html=True)
        amt = st.number_input('amount', min_value=0.0, value=0.0, format='%.2f', label_visibility='collapsed')
        
        st.markdown('<label class="form-label">📊 Type</label>', unsafe_allow_html=True)
        ttype = st.radio('type_select', ['Credit', 'Debit'], horizontal=True, label_visibility='collapsed')
    
    with form_col2:
        credit_categories = ['Salary / Wages', 'Cheque Deposit', 'Cash Deposit', 'Bank Transfer Received', 'UPI Transfer Received', 'Refunds & Reimbursements', 'Rental Income', 'Insurance Claim Settlement', 'Cashback & Rewards', 'Miscellaneous']
        debit_categories = ['Home rent', 'Groceries / Food', 'School fee', 'College fee', 'Electricity Bill', 'Water Tax', 'Loan EMI', 'Travel Expense', 'Entertainment', 'Miscellaneous']
        
        st.markdown('<label class="form-label">📂 Category</label>', unsafe_allow_html=True)
        cat = st.selectbox('category_select', credit_categories if ttype == 'Credit' else debit_categories, label_visibility='collapsed', key=f'cat_{ttype}')
        
        st.markdown('<label class="form-label">📝 Description</label>', unsafe_allow_html=True)
        desc = st.text_input('description', label_visibility='collapsed', placeholder='Enter description')
        
        st.markdown('<label class="form-label">📌 Notes</label>', unsafe_allow_html=True)
        notes = st.text_area('notes', label_visibility='collapsed', placeholder='Optional notes', height=60)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add Button
    if st.button('➕ Add Transaction', key='add_txn', use_container_width=True):
        signed = amt if ttype == 'Credit' else -amt
        desc_value = (desc or cat or 'Manual entry').strip()
        txmod.add_transaction(user_id, dt.isoformat(), desc_value, signed, category=cat, notes=(notes or None))
        st.success('✅ Transaction added successfully!')
        st.rerun()
    
    # Summary Cards
    rows_user = txmod.list_transactions(user_id)
    income = float(sum(r.amount for r in rows_user if r.amount > 0)) if rows_user else 0.0
    loss = float(-sum(r.amount for r in rows_user if r.amount < 0)) if rows_user else 0.0
    net = income - loss
    
    st.markdown('<div class="section-title">📊 Summary</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    
    with s1:
        st.markdown(f'<div class="summary-card summary-gain"><div class="summary-label">📈 Total Income</div><div class="summary-value">${income:,.2f}</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown(f'<div class="summary-card summary-loss"><div class="summary-label">📉 Total Expenses</div><div class="summary-value">${loss:,.2f}</div></div>', unsafe_allow_html=True)
    with s3:
        net_class = 'summary-gain' if net >= 0 else 'summary-loss'
        st.markdown(f'<div class="summary-card {net_class}"><div class="summary-label">💰 Net Balance</div><div class="summary-value">${net:,.2f}</div></div>', unsafe_allow_html=True)
    
    # Transactions Table
    st.markdown('<div class="section-title">📋 Your Transactions</div>', unsafe_allow_html=True)
    
    if rows_user:
        st.markdown('<div class="table-container">', unsafe_allow_html=True)
        
        # Search and filters
        search_col, type_col, cat_col = st.columns([2, 1, 1])
        with search_col:
            search_term = st.text_input('🔍 Search transactions', placeholder='Search by description or notes', label_visibility='collapsed')
        with type_col:
            filter_type = st.selectbox('Type', ['All', 'Credit', 'Debit'], label_visibility='collapsed')
        with cat_col:
            all_cats = list(set([r.category or 'Uncategorized' for r in rows_user]))
            filter_cat = st.selectbox('Category', ['All'] + all_cats, label_visibility='collapsed')
        
        # Filter data
        filtered_rows = rows_user
        if search_term:
            filtered_rows = [r for r in filtered_rows if search_term.lower() in (r.description or '').lower() or search_term.lower() in (r.notes or '').lower()]
        if filter_type != 'All':
            filtered_rows = [r for r in filtered_rows if (r.amount > 0 and filter_type == 'Credit') or (r.amount < 0 and filter_type == 'Debit')]
        if filter_cat != 'All':
            filtered_rows = [r for r in filtered_rows if (r.category or 'Uncategorized') == filter_cat]
        
        if filtered_rows:
            # Build table HTML
            table_html = '<table class="txn-table"><thead><tr><th>Date</th><th>Description</th><th>Category</th><th>Type</th><th>Amount</th></tr></thead><tbody>'
            for r in sorted(filtered_rows, key=lambda x: x.date, reverse=True):
                txn_type = 'Credit' if r.amount > 0 else 'Debit'
                type_class = 'txn-credit' if r.amount > 0 else 'txn-debit'
                table_html += f'<tr><td>{r.date}</td><td>{r.description}</td><td>{r.category or "N/A"}</td><td class="{type_class}">{txn_type}</td><td class="{type_class}">${abs(r.amount):,.2f}</td></tr>'
            table_html += '</tbody></table>'
            st.markdown(table_html, unsafe_allow_html=True)
        else:
            st.info('No transactions match your filters.')
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Delete Section
        st.markdown('<div class="delete-section">', unsafe_allow_html=True)
        st.markdown('<div class="section-title" style="margin-top: 0;">🗑️ Delete Transactions</div>', unsafe_allow_html=True)
        
        if rows_user:
            # Initialize session state for delete confirmations
            if 'delete_confirm_single' not in st.session_state:
                st.session_state.delete_confirm_single = False
            if 'delete_confirm_all' not in st.session_state:
                st.session_state.delete_confirm_all = False
            
            idx = st.selectbox('Select a transaction to delete', options=list(range(len(rows_user))), format_func=lambda i: f"{rows_user[i].date} | {rows_user[i].description} | ${abs(rows_user[i].amount):,.2f}", label_visibility='collapsed', key='delete_select')
            
            del_col1, del_col2 = st.columns(2)
            
            # Delete Single Transaction
            with del_col1:
                st.markdown('<p style="margin: 0; margin-bottom: 5px;"><small><b>Delete Selected</b></small></p>', unsafe_allow_html=True)
                if st.button('🗑️ Delete', key='del_one', use_container_width=True):
                    st.session_state.delete_confirm_single = True
                
                if st.session_state.delete_confirm_single:
                    confirm = st.checkbox('✅ I confirm to delete this transaction', key='conf_del_single', value=False)
                    if confirm:
                        try:
                            txmod.delete_transaction(rows_user[idx].id)
                            st.session_state.delete_confirm_single = False
                            st.success('✅ Transaction deleted successfully!')
                            st.rerun()
                        except Exception as e:
                            st.error(f'❌ Error deleting transaction: {str(e)}')
                    else:
                        st.warning('⚠️ Check the box above to confirm deletion')
            
            # Delete All Transactions
            with del_col2:
                st.markdown('<p style="margin: 0; margin-bottom: 5px;"><small><b>Delete All</b></small></p>', unsafe_allow_html=True)
                if st.button('🗑️ Delete ALL', key='del_all', use_container_width=True):
                    st.session_state.delete_confirm_all = True
                
                if st.session_state.delete_confirm_all:
                    confirm = st.checkbox('✅ I confirm to delete ALL transactions (Cannot undo!)', key='conf_del_all', value=False)
                    if confirm:
                        try:
                            for r in rows_user:
                                txmod.delete_transaction(r.id)
                            st.session_state.delete_confirm_all = False
                            st.success('✅ All transactions deleted successfully!')
                            st.rerun()
                        except Exception as e:
                            st.error(f'❌ Error deleting transactions: {str(e)}')
                    else:
                        st.warning('⚠️ Check the box above to confirm deletion')
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info('📭 No transactions yet. Start by adding one above!')
    
    # Category Analysis
    if rows_user:
        st.markdown('<div class="section-title">📊 Category Analysis</div>', unsafe_allow_html=True)
        
        df_cat = pd.DataFrame([{
            'category': (r.category or 'Uncategorized'),
            'expense': -r.amount if r.amount < 0 else 0.0,
            'income': r.amount if r.amount > 0 else 0.0,
        } for r in rows_user])
        
        c1, c2 = st.columns(2)
        
        color_palette = ['#00D1FF', '#6366F1', '#22C55E', '#EF4444', '#F59E0B', '#EC4899']
        
        with c1:
            if df_cat.empty or df_cat['expense'].sum() == 0:
                st.info('No expense data')
            else:
                agg = df_cat.groupby('category')['expense'].sum().reset_index().sort_values('expense', ascending=False)
                exp_data = []
                for idx, row in agg.iterrows():
                    exp_data.append({
                        'id': row['category'],
                        'label': row['category'],
                        'value': float(row['expense']),
                        'color': color_palette[idx % len(color_palette)]
                    })
                
                with elements('txn_expense_pie'):
                    with mui.Box(sx={"height": 400}):
                        nivo.Pie(
                            data=exp_data,
                            margin={"top": 60, "right": 80, "bottom": 60, "left": 80},
                            innerRadius=0.5,
                            padAngle=0.7,
                            cornerRadius=3,
                            activeOuterRadiusOffset=8,
                            borderWidth=2,
                            borderColor="#0B0F19",
                            arcLinkLabelsSkipAngle=10,
                            arcLinkLabelsTextColor="#9CA3AF",
                            arcLabelsSkipAngle=10,
                            arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                            legends=[{
                                "anchor": "bottom-right",
                                "direction": "column",
                                "justify": False,
                                "translateY": 60,
                                "itemsSpacing": 8,
                                "itemWidth": 100,
                                "itemHeight": 20,
                                "itemTextColor": "#E5E7EB",
                                "symbolSize": 14,
                                "effects": [{"on": "hover", "style": {"itemTextColor": "#00D1FF"}}],
                            }],
                            theme={
                                "background": "#0B0F19",
                                "textColor": "#E5E7EB",
                                "tooltip": {
                                    "container": {
                                        "background": "#111827",
                                        "color": "#E5E7EB",
                                        "borderRadius": "4px",
                                        "boxShadow": "0 0 15px rgba(239, 68, 68, 0.3)"
                                    }
                                }
                            },
                        )
        
        with c2:
            if df_cat.empty or df_cat['income'].sum() == 0:
                st.info('No income data')
            else:
                agg = df_cat.groupby('category')['income'].sum().reset_index().sort_values('income', ascending=False)
                inc_data = []
                for idx, row in agg.iterrows():
                    inc_data.append({
                        'id': row['category'],
                        'label': row['category'],
                        'value': float(row['income']),
                        'color': color_palette[idx % len(color_palette)]
                    })
                
                with elements('txn_income_pie'):
                    with mui.Box(sx={"height": 400}):
                        nivo.Pie(
                            data=inc_data,
                            margin={"top": 60, "right": 80, "bottom": 60, "left": 80},
                            innerRadius=0.5,
                            padAngle=0.7,
                            cornerRadius=3,
                            activeOuterRadiusOffset=8,
                            borderWidth=2,
                            borderColor="#0B0F19",
                            arcLinkLabelsSkipAngle=10,
                            arcLinkLabelsTextColor="#9CA3AF",
                            arcLabelsSkipAngle=10,
                            arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                            legends=[{
                                "anchor": "bottom-right",
                                "direction": "column",
                                "justify": False,
                                "translateY": 60,
                                "itemsSpacing": 8,
                                "itemWidth": 100,
                                "itemHeight": 20,
                                "itemTextColor": "#E5E7EB",
                                "symbolSize": 14,
                                "effects": [{"on": "hover", "style": {"itemTextColor": "#00D1FF"}}],
                            }],
                            theme={
                                "background": "#0B0F19",
                                "textColor": "#E5E7EB",
                                "tooltip": {
                                    "container": {
                                        "background": "#111827",
                                        "color": "#E5E7EB",
                                        "borderRadius": "4px",
                                        "boxShadow": "0 0 15px rgba(34, 197, 94, 0.3)"
                                    }
                                }
                            },
                        )
        
        divider_glowing()
        st.subheader('Monthly Breakdown')
        
        df_type = pd.DataFrame([{
            'date': r.date,
            'type': 'Credit' if r.amount > 0 else 'Debit',
            'value': abs(r.amount),
        } for r in rows_user])
        
        if not df_type.empty:
            df_type['month'] = pd.to_datetime(df_type['date']).dt.to_period('M').dt.to_timestamp()
            agg_t = df_type.groupby(['month', 'type'])['value'].sum().reset_index()
            
            fig_bar = px.bar(agg_t, x='month', y='value', color='type', barmode='group', color_discrete_map={'Credit': '#22C55E', 'Debit': '#EF4444'})
            fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#E5E7EB'), hovermode='x unified')
            st.plotly_chart(fig_bar, use_container_width=True)



def show_chatbot_page(user_id):
    st.markdown("""
    <style>
    .page-title { 
        text-align: center; 
        margin-bottom: 2.5rem; 
        margin-top: 1rem;
    }
    .page-title h1 {
        background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        text-shadow: 0 0 30px rgba(0, 209, 255, 0.4);
    }
    .page-title p { 
        color: #9CA3AF; 
        font-size: 1.05rem;
        margin-top: 0.75rem;
        font-weight: 400;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""<div class="page-title">
        <h1>🤖 AI Chatbot</h1>
        <p>Ask questions about your finances instantly</p>
    </div>""", unsafe_allow_html=True)
    q = st.text_input('Your question')
    if st.button('Send') and q.strip():
        with st.spinner('Contacting AI...'):
            resp = ai_utils.chat_with_data(user_id, q)
            st.write(resp)

def show_import_csv_page(user_id):
    st.markdown("""
    <style>
    .page-title { 
        text-align: center; 
        margin-bottom: 2.5rem; 
        margin-top: 1rem;
    }
    .page-title h1 {
        background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        text-shadow: 0 0 30px rgba(0, 209, 255, 0.4);
    }
    .page-title p { 
        color: #9CA3AF; 
        font-size: 1.05rem;
        margin-top: 0.75rem;
        font-weight: 400;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""<div class="page-title">
        <h1>📂 Import CSV</h1>
        <p>Upload and analyze your bank statements</p>
    </div>""", unsafe_allow_html=True)
    uploaded = st.file_uploader('Upload a CSV file 📤', type=['csv'], key='import_csv_uploader')

    # Load/save preview in session
    if uploaded is not None:
        uploaded.seek(0)
        df_preview = pd.read_csv(uploaded)
        st.session_state['import_preview_df'] = df_preview
    else:
        df_preview = st.session_state.get('import_preview_df')

    if df_preview is None or df_preview.empty:
        st.info('Upload a CSV to see and save a preview here.')
    else:
        # Totals (Transaction Type + Amount)
        dfp = df_preview.copy()
        dfp.columns = [str(c).strip().lower().replace(' ', '_') for c in dfp.columns]
        tcol = next((c for c in ['transaction_type','type','credit_debit','dr_cr'] if c in dfp.columns), None)
        acol = next((c for c in ['amount','amt','value'] if c in dfp.columns), None)

        if tcol and acol:
            vals  = pd.to_numeric(dfp[acol], errors='coerce').fillna(0)
            tvals = dfp[tcol].astype(str).str.strip().str.lower()
            credit_sum = float(vals.where(tvals.str.startswith('credit'), 0).sum())
            debit_sum  = float(vals.where(tvals.str.startswith('debit'),  0).sum())
            net = credit_sum - debit_sum

            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f"<div style='padding:14px;border-radius:10px;background:rgba(34, 197, 94, 0.1);border:1px solid #22C55E'><div style='color:#22C55E;font-size:13px;'>Total Credit</div><div style='font-size:24px;font-weight:700;'>{credit_sum:,.2f}</div></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div style='padding:14px;border-radius:10px;background:rgba(239, 68, 68, 0.1);border:1px solid #EF4444'><div style='color:#EF4444;font-size:13px;'>Total Debit</div><div style='font-size:24px;font-weight:700;'>{debit_sum:,.2f}</div></div>", unsafe_allow_html=True)
            with c3:
                color = '#22C55E' if net >= 0 else '#EF4444'
                bg    = 'rgba(34, 197, 94, 0.1)' if net >= 0 else 'rgba(239, 68, 68, 0.1)'
                border_color = '#22C55E' if net >= 0 else '#EF4444'
                st.markdown(f"<div style='padding:14px;border-radius:10px;background:{bg};border:1px solid {border_color}'><div style='color:{color};font-size:13px;'>Net</div><div style='font-size:24px;font-weight:700;'>{net:,.2f}</div></div>", unsafe_allow_html=True)
        else:
            st.warning('Preview must include Amount and Transaction Type columns for totals.')

        # After the totals cards on Import CSV page:
        divider_glowing()
        st.subheader('Preview (editable) 🧾 :')

        # Build/load saved table
        base_df = st.session_state.get('import_preview_df', df_preview)
        edited = st.data_editor(
            base_df,
            use_container_width=True,
            num_rows='dynamic',
            key='import_editor'
        )

        c1, c2, c3 = st.columns(3)
        if c1.button('Save table'):
            st.session_state['import_preview_df'] = edited
            st.success('Table saved. It will persist when you navigate away.')
        if c2.button('Clear saved table'):
            st.session_state.pop('import_preview_df', None)
            st.session_state.pop('import_csv_uploader', None)
            st.rerun()
        if c3.button('Import saved table to DB'):
            # import from the saved/edited table (no need to re-upload)
            from io import StringIO
            buf = StringIO(); edited.to_csv(buf, index=False); buf.seek(0)
            created = txmod.import_transactions_from_csv(user_id, buf)
            st.success(f'Imported {len(created)} transactions.')
            st.rerun()

        # Then your graphs
        divider_glowing()
        st.subheader('Preview graphs 📊 :')

        dfg = st.session_state.get('import_preview_df', edited).copy()
        dfg.columns = [str(c).strip().lower().replace(' ', '_') for c in dfg.columns]

        tcol = next((c for c in ['transaction_type','type','credit_debit','dr_cr'] if c in dfg.columns), None)
        acol = next((c for c in ['amount','amt','value'] if c in dfg.columns), None)
        dcol = next((c for c in ['date','transaction_date','posted','posted_date','value_date'] if c in dfg.columns), None)
        xdesc = 'description' if 'description' in dfg.columns else next((c for c in dfg.columns if 'desc' in c), None)

        if not (tcol and acol):
            st.warning('Graphs need Amount and Transaction Type columns in the preview.')
        else:
            vals  = pd.to_numeric(dfg[acol], errors='coerce').fillna(0)
            tvals = dfg[tcol].astype(str).str.strip().str.lower()

            # 1) Pie: Description (sum of amounts per description)
            st.caption('Description breakdown (total) :')
            if xdesc:
                desc_tot = dfg.assign(value=vals).groupby(xdesc)['value'].sum().reset_index().sort_values('value', ascending=False)
                if desc_tot.empty:
                    st.info('No data for description pie.')
                else:
                    with elements('import_desc_pie'):
                        DATA = [{'id': r[xdesc], 'label': r[xdesc], 'value': float(r['value'])} for _, r in desc_tot.iterrows()]
                        with mui.Box(sx={"height": 320, "backgroundColor": "#000"}):
                            nivo.Pie(
                                data=DATA,
                                margin={"top":20,"right":20,"bottom":20,"left":20},
                                innerRadius=0.5, padAngle=0.7, cornerRadius=3,
                                activeOuterRadiusOffset=8, arcLinkLabelsSkipAngle=10, arcLabelsSkipAngle=10,
                                legends=[{"anchor":"bottom","direction":"row","translateY":24,
                                          "itemWidth":100,"itemHeight":18,"symbolSize":14}],
                                theme={"background":"#0e1117","textColor":"#ddd",
                                       "tooltip":{"container":{"background":"#0222"}}},
                            )
            else:
                st.info('No Description column found for pie.')

            divider_glowing()

            # 2) Bar: Transaction Type (Credit vs Debit amounts)
            st.caption('Transaction Type — amounts :')
            bar_df = pd.DataFrame({
                'type': ['Credit','Debit'],
                'value': [
                    float(vals.where(tvals.str.startswith('credit'), 0).sum()),
                    float(vals.where(tvals.str.startswith('debit'),  0).sum())
                ]
            })
            fig_bar = px.bar(bar_df, x='type', y='value', color='type',
                             color_discrete_map={'Credit':'#2ECC71','Debit':'#E74C3C'})
            fig_bar.update_layout(template='plotly_dark', paper_bgcolor='#0e1117', plot_bgcolor='#0e1117',
                                  xaxis_title='', yaxis_title='Amount', legend_title='')
            st.plotly_chart(fig_bar, use_container_width=True)

            divider_glowing()

            # 3) Line: Daily trend (Credit vs Debit)
            st.caption('Daily trend — Credit vs Debit :')
            if dcol:
                dfd = pd.DataFrame({
                    'date': pd.to_datetime(dfg[dcol], errors='coerce'),
                    'credit': vals.where(tvals.str.startswith('credit'), 0),
                    'debit':  vals.where(tvals.str.startswith('debit'),  0),
                }).dropna(subset=['date'])
                if dfd.empty:
                    st.info('No date data to plot.')
                else:
                    daily = dfd.groupby('date')[['credit','debit']].sum().reset_index()
                    long = daily.melt(id_vars='date', value_vars=['credit','debit'],
                                      var_name='type', value_name='value')
                    fig_line = px.line(long, x='date', y='value', color='type', markers=True,
                                       color_discrete_map={'credit':'#2ECC71','debit':'#E74C3C'})
                    fig_line.update_layout(template='plotly_dark', paper_bgcolor='#0e1117', plot_bgcolor='#0e1117',
                                           xaxis_title='Date', yaxis_title='Amount', legend_title='')
                    st.plotly_chart(fig_line, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Summary Section
                    st.markdown('<div class="section-title-import">📄 Bank Statement Summary</div>', unsafe_allow_html=True)
                    st.markdown("""
                    <div style='background: linear-gradient(135deg, #1F2937 0%, #111827 100%); border: 1px solid rgba(0, 209, 255, 0.15); border-radius: 12px; padding: 2rem; color: #E5E7EB; line-height: 1.8; margin-bottom: 2rem;'>
                    <div style='color: #9CA3AF; margin-bottom: 1rem;'>📋 Bank Statement Analysis for <strong>{st.session_state['user']['username']}</strong></div>
                    """, unsafe_allow_html=True)
                    st.markdown(f"""
                    <div style='color: #E5E7EB; margin-bottom: 1.5rem;'>
                    Throughout the statement period, the account registered several inflows and outflows of funds.<br><br>
                    <strong style='color: #22C55E;'>📈 On the credit side:</strong> A total of <strong>₹{credit_sum:,.2f}</strong> was deposited into the account. These deposits included salary credits, fund transfers from other accounts, refunds, and miscellaneous credits.<br><br>
                    <strong style='color: #EF4444;'>📉 On the debit side:</strong> A total of <strong>₹{debit_sum:,.2f}</strong> was withdrawn or utilized. The debits consisted of ATM withdrawals, online payments, cheque clearances, utility bill payments, fund transfers, and service charges.<br><br>
                    <strong style='color: #00D1FF;'>💰 Net Balance:</strong> After adjusting all credits and debits, the account reflected a closing balance of <strong>₹{net:,.2f}</strong> at the end of the statement period.<br><br>
                    <span style='color: #9CA3AF; font-size: 0.9rem;'>This summary can be used for verification, financial assessment, loan applications, or any official requirement where proof of banking transactions is necessary.</span>
                    </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning('⚠️ Date column not found for trend analysis.')

def show_calculator_page(user_id):
    st.markdown("""
    <style>
    div[data-testid="stVerticalBlock"] > div:has(> div > div > button) {
        margin-bottom: 0.5rem;
    }
    .page-title { 
        text-align: center; 
        margin-bottom: 2.5rem; 
        margin-top: 1rem;
    }
    .page-title h1 {
        background: linear-gradient(135deg, #00D1FF 0%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
        text-shadow: 0 0 30px rgba(0, 209, 255, 0.4);
    }
    .page-title p { 
        color: #9CA3AF; 
        font-size: 1.05rem;
        margin-top: 0.75rem;
        font-weight: 400;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""<div class="page-title">
        <h1>🧮 Financial Calculators</h1>
        <p>Plan your finances with smart tools</p>
    </div>""", unsafe_allow_html=True)
    divider_glowing()
    
    calculator_options = [
        ("💳\nEMI", "EMI Calculator"),
        ("📈\nSIP", "SIP Calculator"),
        ("💰\nCompound", "Compound Interest Calculator"),
        ("🏦\nFD", "Fixed Deposit Calculator"),
        ("💵\nRD", "Recurring Deposit Calculator")
    ]

    col1, col2, col3, col4, col5 = st.columns(5, gap="medium")
    cols_list = [col1, col2, col3, col4, col5]
    
    for idx, (display_name, calc_name) in enumerate(calculator_options):
        with cols_list[idx]:
            if st.button(display_name, key=f"calc_{idx}", use_container_width=True):
                st.session_state['selected_calc'] = calc_name

    if 'selected_calc' not in st.session_state:
        st.session_state['selected_calc'] = "EMI Calculator"

    divider_glowing()
    
    selected_calculator = st.session_state['selected_calc']
    col_left, col_right = st.columns(2, gap="large")

    with col_left:
        if selected_calculator == "EMI Calculator":
            show_emi_inputs()
        elif selected_calculator == "SIP Calculator":
            show_sip_inputs()
        elif selected_calculator == "Compound Interest Calculator":
            show_compound_interest_inputs()
        elif selected_calculator == "Fixed Deposit Calculator":
            show_fd_inputs()
        elif selected_calculator == "Recurring Deposit Calculator":
            show_rd_inputs()

    with col_right:
        if selected_calculator == "EMI Calculator":
            show_emi_results()
        elif selected_calculator == "SIP Calculator":
            show_sip_results()
        elif selected_calculator == "Compound Interest Calculator":
            show_compound_interest_results()
        elif selected_calculator == "Fixed Deposit Calculator":
            show_fd_results()
        elif selected_calculator == "Recurring Deposit Calculator":
            show_rd_results()


def show_emi_inputs():
    st.subheader("💳 Loan Details")
    principal = st.slider(
        "Loan Amount (₹)",
        min_value=10000.0,
        max_value=5000000.0,
        value=100000.0,
        step=10000.0,
        key="emi_principal"
    )
    rate = st.slider(
        "Annual Interest Rate (%)",
        min_value=1.0,
        max_value=16.0,
        value=8.5,
        step=0.1,
        key="emi_rate"
    )
    tenure = st.slider(
        "Loan Tenure (Years)",
        min_value=1,
        max_value=30,
        value=5,
        step=1,
        key="emi_tenure"
    )
    st.session_state['emi_data'] = {'principal': principal, 'rate': rate, 'tenure': tenure}

def show_emi_results():
    if 'emi_data' not in st.session_state:
        st.info("Enter loan details to see results")
        return
    
    data = st.session_state['emi_data']
    principal = data['principal']
    rate = data['rate']
    tenure = data['tenure']
    
    monthly_rate = rate / (12 * 100)
    months = tenure * 12
    emi = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    total_payment = emi * months
    total_interest = total_payment - principal
    
    st.subheader("📊 Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Monthly EMI", f"₹{emi:,.2f}")
    with col2:
        st.metric("Total Interest", f"₹{total_interest:,.2f}")
    st.metric("Total Payment", f"₹{total_payment:,.2f}")
    
    divider_glowing()
    st.subheader("📈 Breakdown")
    color_palette = ['#00D1FF', '#6366F1', '#22C55E', '#EF4444', '#F59E0B', '#EC4899']
    data_chart = [
        {'id': 'Principal', 'label': 'Principal', 'value': float(principal), 'color': color_palette[0]},
        {'id': 'Interest', 'label': 'Interest', 'value': float(total_interest), 'color': color_palette[1]}
    ]
    with elements("emi_pie_chart"):
        with mui.Box(sx={"height": 450, "width": "100%"}):
            nivo.Pie(
                data=data_chart,
                margin={"top": 80, "right": 100, "bottom": 80, "left": 80},
                innerRadius=0.5,
                padAngle=0.7,
                cornerRadius=3,
                activeOuterRadiusOffset=8,
                borderWidth=2,
                borderColor="#0B0F19",
                arcLinkLabelsSkipAngle=10,
                arcLinkLabelsTextColor="#9CA3AF",
                arcLinkLabelsThickness=2,
                arcLinkLabelsColor={"from": "color"},
                arcLabelsSkipAngle=10,
                arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                legends=[{
                    "anchor": "bottom-right",
                    "direction": "column",
                    "justify": False,
                    "translateX": 0,
                    "translateY": 80,
                    "itemsSpacing": 10,
                    "itemWidth": 120,
                    "itemHeight": 24,
                    "itemTextColor": "#C2C3C5",
                    "itemDirection": "left-to-right",
                    "itemOpacity": 1,
                    "symbolSize": 16,
                    "symbolShape": "circle",
                    "effects": [{"on": "hover", "style": {"itemTextColor": "#00D1FF", "itemOpacity": 1}}],
                }],
                theme={
                    "background": "#0B0F19",
                    "textColor": "#515152",
                    "tooltip": {
                        "container": {
                            "background": "#111827",
                            "color": "#E5E7EB",
                            "borderRadius": "4px",
                            "boxShadow": "0 0 20px rgba(0, 209, 255, 0.3)",
                            "padding": "8px 12px"
                        }
                    }
                },
            )

def show_sip_inputs():
    st.subheader("📈 Investment Details")
    monthly_investment = st.slider(
        "Monthly Investment (₹)",
        min_value=500.0,
        max_value=100000.0,
        value=5000.0,
        step=500.0,
        key="sip_monthly"
    )
    rate = st.slider(
        "Expected Annual Return (%)",
        min_value=1.0,
        max_value=30.0,
        value=12.0,
        step=0.5,
        key="sip_rate"
    )
    period = st.slider(
        "Investment Period (Years)",
        min_value=1,
        max_value=40,
        value=10,
        step=1,
        key="sip_period"
    )
    st.session_state['sip_data'] = {'monthly_investment': monthly_investment, 'rate': rate, 'period': period}

def show_sip_results():
    if 'sip_data' not in st.session_state:
        st.info("Enter investment details to see results")
        return
    
    data = st.session_state['sip_data']
    monthly_investment = data['monthly_investment']
    rate = data['rate']
    period = data['period']
    
    monthly_rate = rate / (12 * 100)
    months = period * 12
    future_value = monthly_investment * (((1 + monthly_rate)**months - 1) / monthly_rate) * (1 + monthly_rate)
    invested_amount = monthly_investment * months
    estimated_returns = future_value - invested_amount
    
    st.subheader("💰 Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Invested", f"₹{invested_amount:,.2f}")
    with col2:
        st.metric("Estimated Returns", f"₹{estimated_returns:,.2f}")
    st.metric("Total Value", f"₹{future_value:,.2f}")
    
    divider_glowing()
    st.subheader("📊 Breakdown")
    color_palette = ['#00D1FF', '#6366F1', '#22C55E', '#EF4444', '#F59E0B', '#EC4899']
    data_chart = [
        {'id': 'Invested', 'label': 'Total Invested', 'value': float(invested_amount), 'color': color_palette[0]},
        {'id': 'Returns', 'label': 'Estimated Returns', 'value': float(estimated_returns), 'color': color_palette[2]}
    ]
    with elements("sip_pie_chart"):
        with mui.Box(sx={"height": 450, "width": "100%"}):
            nivo.Pie(
                data=data_chart,
                margin={"top": 80, "right": 100, "bottom": 80, "left": 80},
                innerRadius=0.5,
                padAngle=0.7,
                cornerRadius=3,
                activeOuterRadiusOffset=8,
                borderWidth=2,
                borderColor="#0B0F19",
                arcLinkLabelsSkipAngle=10,
                arcLinkLabelsTextColor="#9CA3AF",
                arcLinkLabelsThickness=2,
                arcLinkLabelsColor={"from": "color"},
                arcLabelsSkipAngle=10,
                arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                legends=[{
                    "anchor": "bottom-right",
                    "direction": "column",
                    "justify": False,
                    "translateX": 0,
                    "translateY": 80,
                    "itemsSpacing": 10,
                    "itemWidth": 120,
                    "itemHeight": 24,
                    "itemTextColor": "#E5E7EB",
                    "itemDirection": "left-to-right",
                    "itemOpacity": 1,
                    "symbolSize": 16,
                    "symbolShape": "circle",
                    "effects": [{"on": "hover", "style": {"itemTextColor": "#00D1FF", "itemOpacity": 1}}],
                }],
                theme={
                    "background": "#0B0F19",
                    "textColor": "#E5E7EB",
                    "tooltip": {
                        "container": {
                            "background": "#111827",
                            "color": "#E5E7EB",
                            "borderRadius": "4px",
                            "boxShadow": "0 0 20px rgba(0, 209, 255, 0.3)",
                            "padding": "8px 12px"
                        }
                    }
                },
            )

def show_compound_interest_inputs():
    st.subheader("💰 Investment Details")
    principal = st.slider(
        "Principal Amount (₹)",
        min_value=1000.0,
        max_value=10000000.0,
        value=10000.0,
        step=10000.0,
        key="ci_principal"
    )
    rate = st.slider(
        "Annual Interest Rate (%)",
        min_value=0.1,
        max_value=20.0,
        value=7.5,
        step=0.1,
        key="ci_rate"
    )
    time = st.slider(
        "Time Period (Years)",
        min_value=1,
        max_value=50,
        value=5,
        step=1,
        key="ci_time"
    )
    compounding = st.selectbox("Compounding Frequency", ["Annually", "Semi-Annually", "Quarterly", "Monthly"], index=0, key="ci_compounding")
    st.session_state['ci_data'] = {'principal': principal, 'rate': rate, 'time': time, 'compounding': compounding}

def show_compound_interest_results():
    if 'ci_data' not in st.session_state:
        st.info("Enter investment details to see results")
        return
    
    data = st.session_state['ci_data']
    principal = data['principal']
    rate = data['rate']
    time = data['time']
    compounding = data['compounding']
    
    n = {"Annually": 1, "Semi-Annually": 2, "Quarterly": 4, "Monthly": 12}[compounding]
    amount = principal * (1 + (rate / (100 * n)))**(n * time)
    total_interest = amount - principal
    
    st.subheader("📊 Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Principal Amount", f"₹{principal:,.2f}")
    with col2:
        st.metric("Interest Earned", f"₹{total_interest:,.2f}")
    st.metric("Maturity Value", f"₹{amount:,.2f}")
    
    divider_glowing()
    st.subheader("📈 Breakdown")
    color_palette = ['#00D1FF', '#6366F1', '#22C55E', '#EF4444', '#F59E0B', '#EC4899']
    data_chart = [
        {'id': 'Principal', 'label': 'Principal', 'value': float(principal), 'color': color_palette[0]},
        {'id': 'Interest', 'label': 'Interest', 'value': float(total_interest), 'color': color_palette[2]}
    ]
    with elements("ci_pie_chart"):
        with mui.Box(sx={"height": 450, "width": "100%"}):
            nivo.Pie(
                data=data_chart,
                margin={"top": 80, "right": 100, "bottom": 80, "left": 80},
                innerRadius=0.5,
                padAngle=0.7,
                cornerRadius=3,
                activeOuterRadiusOffset=8,
                borderWidth=2,
                borderColor="#0B0F19",
                arcLinkLabelsSkipAngle=10,
                arcLinkLabelsTextColor="#9CA3AF",
                arcLinkLabelsThickness=2,
                arcLinkLabelsColor={"from": "color"},
                arcLabelsSkipAngle=10,
                arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                legends=[{
                    "anchor": "bottom-right",
                    "direction": "column",
                    "justify": False,
                    "translateX": 0,
                    "translateY": 80,
                    "itemsSpacing": 10,
                    "itemWidth": 120,
                    "itemHeight": 24,
                    "itemTextColor": "#E5E7EB",
                    "itemDirection": "left-to-right",
                    "itemOpacity": 1,
                    "symbolSize": 16,
                    "symbolShape": "circle",
                    "effects": [{"on": "hover", "style": {"itemTextColor": "#00D1FF", "itemOpacity": 1}}],
                }],
                theme={
                    "background": "#0B0F19",
                    "textColor": "#E5E7EB",
                    "tooltip": {
                        "container": {
                            "background": "#111827",
                            "color": "#E5E7EB",
                            "borderRadius": "4px",
                            "boxShadow": "0 0 20px rgba(0, 209, 255, 0.3)",
                            "padding": "8px 12px"
                        }
                    }
                },
            )

def show_fd_inputs():
    st.subheader("🏦 FD Details")
    principal = st.slider(
        "Principal Amount (₹)",
        min_value=10000.0,
        max_value=10000000.0,
        value=50000.0,
        step=10000.0,
        key="fd_principal"
    )
    rate = st.slider(
        "Annual Interest Rate (%)",
        min_value=2.0,
        max_value=10.0,
        value=7.0,
        step=0.1,
        key="fd_rate"
    )
    tenure = st.slider(
        "Tenure (Years)",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        key="fd_tenure"
    )
    st.session_state['fd_data'] = {'principal': principal, 'rate': rate, 'tenure': tenure}

def show_fd_results():
    if 'fd_data' not in st.session_state:
        st.info("Enter FD details to see results")
        return
    
    data = st.session_state['fd_data']
    principal = data['principal']
    rate = data['rate']
    tenure = data['tenure']
    
    n = 4
    maturity_amount = principal * (1 + (rate / (100 * n)))**(n * tenure)
    interest_earned = maturity_amount - principal
    
    st.subheader("📊 Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Principal Amount", f"₹{principal:,.2f}")
    with col2:
        st.metric("Interest Earned", f"₹{interest_earned:,.2f}")
    st.metric("Maturity Amount", f"₹{maturity_amount:,.2f}")
    
    divider_glowing()
    st.subheader("📈 Breakdown")
    color_palette = ['#00D1FF', '#6366F1', '#22C55E', '#EF4444', '#F59E0B', '#EC4899']
    data_chart = [
        {'id': 'Principal', 'label': 'Principal', 'value': float(principal), 'color': color_palette[0]},
        {'id': 'Interest', 'label': 'Interest', 'value': float(interest_earned), 'color': color_palette[2]}
    ]
    with elements("fd_pie_chart"):
        with mui.Box(sx={"height": 450, "width": "100%"}):
            nivo.Pie(
                data=data_chart,
                margin={"top": 80, "right": 100, "bottom": 80, "left": 80},
                innerRadius=0.5,
                padAngle=0.7,
                cornerRadius=3,
                activeOuterRadiusOffset=8,
                borderWidth=2,
                borderColor="#0B0F19",
                arcLinkLabelsSkipAngle=10,
                arcLinkLabelsTextColor="#9CA3AF",
                arcLinkLabelsThickness=2,
                arcLinkLabelsColor={"from": "color"},
                arcLabelsSkipAngle=10,
                arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                legends=[{
                    "anchor": "bottom-right",
                    "direction": "column",
                    "justify": False,
                    "translateX": 0,
                    "translateY": 80,
                    "itemsSpacing": 10,
                    "itemWidth": 120,
                    "itemHeight": 24,
                    "itemTextColor": "#E5E7EB",
                    "itemDirection": "left-to-right",
                    "itemOpacity": 1,
                    "symbolSize": 16,
                    "symbolShape": "circle",
                    "effects": [{"on": "hover", "style": {"itemTextColor": "#00D1FF", "itemOpacity": 1}}],
                }],
                theme={
                    "background": "#0B0F19",
                    "textColor": "#E5E7EB",
                    "tooltip": {
                        "container": {
                            "background": "#111827",
                            "color": "#E5E7EB",
                            "borderRadius": "4px",
                            "boxShadow": "0 0 20px rgba(0, 209, 255, 0.3)",
                            "padding": "8px 12px"
                        }
                    }
                },
            )

def show_rd_inputs():
    st.subheader("💵 RD Details")
    monthly_deposit = st.slider(
        "Monthly Deposit (₹)",
        min_value=500.0,
        max_value=100000.0,
        value=5000.0,
        step=500.0,
        key="rd_monthly"
    )
    rate = st.slider(
        "Annual Interest Rate (%)",
        min_value=2.0,
        max_value=10.0,
        value=7.0,
        step=0.1,
        key="rd_rate"
    )
    tenure = st.slider(
        "Tenure (Years)",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        key="rd_tenure"
    )
    st.session_state['rd_data'] = {'monthly_deposit': monthly_deposit, 'rate': rate, 'tenure': tenure}

def show_rd_results():
    if 'rd_data' not in st.session_state:
        st.info("Enter RD details to see results")
        return
    
    data = st.session_state['rd_data']
    monthly_deposit = data['monthly_deposit']
    rate = data['rate']
    tenure = data['tenure']
    
    n = 12
    months = tenure * 12
    total_invested = monthly_deposit * months
    maturity_amount = monthly_deposit * (((1 + (rate / (100 * n)))**(n * tenure) - 1) / (1 - (1 + (rate / (100 * n)))**(-1)))
    interest_earned = maturity_amount - total_invested
    
    st.subheader("📊 Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Invested", f"₹{total_invested:,.2f}")
    with col2:
        st.metric("Interest Earned", f"₹{interest_earned:,.2f}")
    st.metric("Maturity Amount", f"₹{maturity_amount:,.2f}")
    
    divider_glowing()
    st.subheader("📈 Breakdown")
    color_palette = ['#00D1FF', '#6366F1', '#22C55E', '#EF4444', '#F59E0B', '#EC4899']
    data_chart = [
        {'id': 'Invested', 'label': 'Total Invested', 'value': float(total_invested), 'color': color_palette[0]},
        {'id': 'Interest', 'label': 'Interest Earned', 'value': float(interest_earned), 'color': color_palette[2]}
    ]
    with elements("rd_pie_chart"):
        with mui.Box(sx={"height": 450, "width": "100%"}):
            nivo.Pie(
                data=data_chart,
                margin={"top": 80, "right": 100, "bottom": 80, "left": 80},
                innerRadius=0.5,
                padAngle=0.7,
                cornerRadius=3,
                activeOuterRadiusOffset=8,
                borderWidth=2,
                borderColor="#0B0F19",
                arcLinkLabelsSkipAngle=10,
                arcLinkLabelsTextColor="#9CA3AF",
                arcLinkLabelsThickness=2,
                arcLinkLabelsColor={"from": "color"},
                arcLabelsSkipAngle=10,
                arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                legends=[{
                    "anchor": "bottom-right",
                    "direction": "column",
                    "justify": False,
                    "translateX": 0,
                    "translateY": 80,
                    "itemsSpacing": 10,
                    "itemWidth": 120,
                    "itemHeight": 24,
                    "itemTextColor": "#E5E7EB",
                    "itemDirection": "left-to-right",
                    "itemOpacity": 1,
                    "symbolSize": 16,
                    "symbolShape": "circle",
                    "effects": [{"on": "hover", "style": {"itemTextColor": "#00D1FF", "itemOpacity": 1}}],
                }],
                theme={
                    "background": "#0B0F19",
                    "textColor": "#E5E7EB",
                    "tooltip": {
                        "container": {
                            "background": "#111827",
                            "color": "#E5E7EB",
                            "borderRadius": "4px",
                            "boxShadow": "0 0 20px rgba(0, 209, 255, 0.3)",
                            "padding": "8px 12px"
                        }
                    }
                },
            )

def show_account_page(user):
    st.markdown('''
        <style>
        .profile-card {
            margin: 0 auto;
            margin-top: 40px;
            max-width: 480px;
            padding: 2.5rem 2rem 1.7rem 2rem;
            text-align: center;
           
        }
        .profile-avatar {
            height: 82px; width: 82px;
            display: block;
            margin: 0 auto 18px auto;
            border-radius: 22px;
            background: linear-gradient(135deg, #a0c6ff 0%, #70b0ff 100%);
            color: #205690;
            font-size: 48px;
            line-height: 82px;
            box-shadow: 0 4px 10px rgba(112,176,255,0.18);
        }
        .profile-username {
            font-size: 1.8rem;
            font-weight: 700;
            color: #ebebeb!important;
            margin-bottom: 0.2rem;
        }
        .profile-email {
            font-size: 1.07rem;
            color: #000 !important;
            margin-bottom: 0.7rem;
        }
        .profile-card-btn-row {
            margin: 22px auto 12px auto;
            display: flex;
            justify-content: center;
            gap: 18px;
            max-width: 420px;
        }
        </style>
    ''', unsafe_allow_html=True)

    username = user.get('username', 'NA')
    email = user.get('email', None)  # Google login may have, else None

    # Profile Card HTML
    st.markdown(f'''
    <div class="profile-card">
        <div class="profile-avatar">👤</div>
        <div class="profile-username">{username}</div>
        {f'<div class="profile-email" style="font-weight: 500; margin-bottom: 10px;">📧 {email}</div>' if email else ''}
    </div>
    ''', unsafe_allow_html=True)

    # Real interactive Streamlit buttons in a single row
    divider_glowing()
    style_btn = {
        "Show Email": "background:#e7f0fb;color:#234276;font-size:15px;font-weight:600;border-radius:7px;",
        "Show Full Name": "background:#e7f0fb;color:#234276;font-size:15px;font-weight:600;border-radius:7px;",
        "Delete my account": "background:linear-gradient(90deg,#fc8383 10%,#ed5151 96%);color:white;font-size:15px;font-weight:600;border-radius:7px;"
    }
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        btn_email = st.button("Show Email", key="show_email_btn_real", use_container_width=True)
    with col2:
        btn_fullname = st.button("Show Full Name", key="show_fullname_btn_real", use_container_width=True)
    with col3:
        btn_del = st.button("Delete my account", key="delete_btn_real", use_container_width=True)

    if btn_email:
        if email:
            st.success(f"User Email: {email}")
        else:
            st.info("Email not available")
    if btn_fullname:
        st.success(f"Full Name: {username}")
    if btn_del:
        from db import delete_user
        if delete_user(user.get('id')):
            st.session_state['logged_in'] = False
            st.session_state['user'] = None
            st.success("Account deleted. Redirecting to login page...")
            st.rerun()
        else:
            st.error("Account could not be deleted.")
