from scheme import Scheme
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain.messages import HumanMessage, AIMessage, SystemMessage


load_dotenv()



api_key = os.getenv("GEMINI_API_KEY")
print(api_key)

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash",
    google_api_key=api_key)

structured_llm = llm.with_structured_output(Scheme)

SYSTEM_PROMPT = """
You are an information extraction system.

You will receive the text of an official government scheme webpage.

Extract ONLY information that is explicitly present in the supplied text.

Do not use your own knowledge.
Do not guess missing information.
Do not invent eligibility criteria, benefits, documents, amounts, dates,
or application procedures.

If information is not available, return an empty list or null where appropriate.

Normalize different headings into the following concepts:

- name
- description
- authority
- state
- benefits
- eligibility
- documents
- application_process
- source

Preserve important details such as:
- age limits
- income limits
- residency requirements
- caste/category requirements
- monetary benefits
- required documents
- application procedures
- deadlines
- official authorities

The source URL will be supplied separately.
"""


text = """Agriculture Infrastructure Fund
Welcome to West Bengal State Portal
Skip to main content
High Contrast
Normal Contrast
Screen Reader Access
Skip to main content
A
-
A
A
+
Screen Reader
A
-
A
A
+
A
A
Schemes
Circulars & Notification
Acts
Forms
Tenders
FAQ's
Information Centre > Schemes > Agriculture Infrastructure Fund (AIF)
Schemes - Agriculture Infrastructure Fund (AIF)
Other Schemes
Agriculture Infrastructure Fund (AIF) supports the development of post-harvest management infrastructure and community farming assets. It provides medium- to long-term debt financing with interest subvention and credit guarantees to farmers, agri-entrepreneurs, and cooperatives to strengthen agricultural supply chains and reduce post-harvest losses.
Benefits Offer Under the Scheme
Interest subvention:
3% per annum interest subsidy on loans, reducing borrowing cost for beneficiaries.
Credit guarantee support:
Credit guarantee coverage for loans up to Rs 2 crore through CGTMSE (fee borne by the government).
Collateral support:
Reduced or no collateral requirement for loans up to Rs 2 crore due to guarantee coverage.
Long-term financing facility:
Access to medium- and long-term loans for building post-harvest infrastructure and community farming assets.
Moratorium on repayment:
Moratorium period ranging from 6 months to 2 years on loan repayment.
Extended interest subsidy period:
Interest subvention available for up to 7 years.
Convergence with other schemes:
Ability to combine benefits with other central/state government schemes for greater support.
Multi-project eligibility:
Eligible entities can undertake multiple infrastructure projects (subject to limits).
Wide institutional financing:
Loans available through multiple institutions such as commercial banks, cooperative banks, NBFCs, etc.
Project support services:
Handholding through a Project Management Unit for project preparation and implementation.
Eligibility
Eligible Entities:
Farmers (individuals and groups), Farmer Producer Organizations and Companies, Agricultural Credit Societies and Cooperatives, AgriTech Startups and Agripreneurs, Central, State and Local Government Agencies, Public-Private Partnerships.
Multiple Projects:
Applications accepted for more than one project.
Nature of Project:
Feasible and economically viable post-harvest infrastructure such as warehouses, cold storage, grading, sorting units, pack houses, ripening chambers.
Land:
Applicant must own or have valid lease of the land.
Creditworthiness:
Applicant must meet the lending institution's credit norms.
Scheme Period:
The scheme is applicable for projects sanctioned during the designated scheme period (originally FY 2020-21 to FY 2025-26).
Last updated on: Friday, 26th June, 2026
Information Source: Department of Information & Cultural Affairs(I&CA), Government of West Bengal
Quick Links
Schemes
Emergency Contact
CM's Corner
State Holidays
News Letter
FAQ
Departmental Links
Web Directory
Awards & Honours
Ease of Doing Business
Home
|
About The Portal
|
Site Map
|
Copyright Policy
|
Terms Of Use
|
Feedback
|
Help
|
Contact Us
|
Downloads
Disclaimer: Site Contents owned, designed, developed, maintained and updated by the Information & Cultural Affairs Department, Government of West Bengal.
Official Site of Government of West Bengal, India | Copyright 2026, All Rights Reserved"""



system_msg = SystemMessage(SYSTEM_PROMPT)
human_msg = HumanMessage(text)
message = [system_msg,human_msg]


full_prompt = f"{SYSTEM_PROMPT}\n\nHere is the text to process:\n{text}"


# scheme = structured_llm.invoke(full_prompt)

response = structured_llm.invoke(message)  # Returns AIMessage

print(response)

