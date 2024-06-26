import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

cc1, cc2, cc3 = st.columns(3)

cc1.image(Image.open("images/fico.png"),width= 200, clamp=True)
cc2.image(Image.open("images/vs(3).png"),width= 200, clamp=True)
cc3.image(Image.open("images/vantage.png"),width= 210, clamp=True)

with st.expander("**What is a credit score?**"):
    st.write("The concept of a credit score may feel complicated, but in essence it looks simply at your payment history, amount of debt, how long you have had debt and how many recent applications you have made for credit accounts. Information about these items are reported to the three credit bureaus, Experian, TransUnion and Equifax, who compile your credit report. The information on your credit report is used to calculate your credit score. Your three-digit credit score captures your experiences with credit and debt and can help you track changes in your financial history over time, from the very first debt you encounter—such as the credit card you opened in college—up to the present. Credit score is a powerful tool that signals to prospective lenders your ability to make payments in a timely manner. This number is unique to you but publicly available under federal law to lenders considering you as a borrower. Your score can be a point of personal pride for good financial management and a point of public documentation. A credit score is an easy way to explain to another person or prospective lender that you can honor your commitment to make timely payments on outstanding debts. In turn, higher scores might lead a lender to extend interest rates lower than they would for consumers with less-favorable credit scores. You can get your credit score as part of a request for a credit report or independently of a credit report. A comprehensive solution is to open a free Credit Sesame account. This provides you with fast access to everything you need to know about your credit history, including your credit score. It includes helpful supporting information that makes sense of your score and report. ")
    
with st.expander("**What are the types of credit scores?**"):
    st.write("There are several different credit scores available to you as a consumer, lender-based scores and generic scores. Lender-based scores are maintained by companies that might consider lending money to you in the future. Common generic scores are the FICO Score and the VantageScore, and they are most widely known by the average consumer. Often, people access their credit score by requesting it from one of the three credit bureaus—Equifax, Experian or TransUnion. You can also access this information in a single location via Credit Sesame. An important note is that your credit score may differ from one report to the next, depending on which bureau lenders report to. Each of the credit bureaus compiles information about your financial history independently of the others. Some credit bureaus might have more information than others. It is possible that a credit report can contain inaccurate information. In this case, you can challenge the innacuracy and have it rectified. It is import to monitor your score regularly and take action if you see a sudden change that cannot be explained by your credit behavior. Rather than focusing only on a single credit score, it’s a good idea to review as many sources as possible with information on your credit history. This gives you a better understanding of your financial health, including strengths and areas for improvement, as you plan future financial decisions. ")

with st.expander("**Who uses my credit score?**"):
    st.write('''Legally, a variety of entities and people can request a copy of your credit report, which is the information that feeds into your credit score. According to the Consumer Financial Protection Bureau (CFPB), this list includes:

    -Businesses to whom you owe money
    -Government agencies
    -Landlords
    -Employers
    -Insurance providers
    -Banks and financial providers
    -Legal entities (in the event of court orders, for example)
    -Others you have authorized in writing to receive a copy''')
    
st.title("How are credit scores calculated?")

c1, c2, c3 = st.columns(3)

name = ["Payment History", "Credit Age", "Credit Utilization", "Credit MIX", "Enquiries", "Available Credit"]
fico = [35,15,30,10,10,0]
vantage = [41,20,20,11,6,2]

# FICO
c1.plotly_chart(px.pie(names=name, values=fico, title="F I C O   S C O R E", color_discrete_sequence=px.colors.sequential.Sunset_r, hole=0.3), use_container_width=True)
c1.write("**FICO Scores Levels**")
c1.dataframe(pd.DataFrame({"Score Rating": ["Exceptional/Excellent", "Very Good/Good", "Good/Fair", "Fair/Poor", "Poor/Very Poor"], "Range": ["800-850", "740-799", "670-739", "580-669", "300-579"]}), hide_index=True)
c1.write("**Scoring Requirements**")
c1.markdown("In order to create a credit score for an individual, FICO requires at least six months of credit history and at least one credit account reported within the last six months.")
c1.write("**Rate Shopping**")
c1.markdown('''FICO’s shopping window is larger, allowing 45 days to compare rates.''')
c1.write("**Late Payments**")
c1.markdown("FICO treats all late payments the same, whether it’s your credit card or mortgage.")

# Vantage
c3.plotly_chart(px.pie(names=name, values=vantage, title="V A N T A G E   S C O R E   4.0", color_discrete_sequence=px.colors.sequential.Sunset, hole=0.3), use_container_width=True)
c3.write("**Vantage Scores Levels**")
c3.dataframe(pd.DataFrame({"Score Rating": ["Exceptional/Excellent", "Very Good/Good", "Good/Fair", "Fair/Poor", "Poor/Very Poor"], "Range": ["781-850", "661-780", "601-660", "500-600", "300-499"]}), hide_index=True)
c3.write("**Scoring Requirements**")
c3.markdown("VantageScore only requires one month of credit history and one account reported within the past two years.")
c3.write("**Rate Shopping**")
c3.markdown('''VantageScore allows just 14 days for rate-shopping.''')
c3.write("**Late Payments**")
c3.markdown("VantageScore judges late payments differently – with mortgages carrying a heavier penalty than a credit card or other type of credit. For consumers whose creditors note that they have been affected by a natural or declared disaster, VantageScore counts negative information as “neutral” during that time but continues to reflect positive information in their score calculations.")