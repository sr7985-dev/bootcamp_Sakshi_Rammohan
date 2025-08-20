# Credit Risk Assessment Project
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
The goal of this project is to create a Credit Risk Assessment model for a company, which evaluates a list of users to determine the likelihood of default. This is important because it helps the company reduce financial losses, allocate resources efficiently, and make informed lending decisions. The model should provide actionable insights into which users are high-risk and which are low-risk, enabling better decision-making.

## Stakeholder & User
The primary stakeholder is the **company’s risk management team**, who are responsible for approving loans and monitoring credit risk. The end users are the team members who will use the predictive scores to prioritize risk mitigation actions. The workflow is aligned with loan evaluation processes and internal reporting cycles.

## Useful Answer & Decision
The answer is **predictive**: each user will receive a **risk score or probability of default**. The deliverable is a model and associated outputs that the risk management team can use to guide lending decisions.

## Assumptions & Constraints
- Availability of historical user credit data.  
- Capacity to run predictive models on company infrastructure.  
- Compliance with data privacy and regulatory standards.  
- Model latency should allow timely decisions within operational cycles.

## Known Unknowns / Risks
- Quality and completeness of historical data.  
- Potential changes in user behavior or economic conditions.  
- Model overfitting or bias toward certain user segments.  
- Uncertainty in model predictions; will monitor via validation and backtesting.

## Lifecycle Mapping
Goal → Stage → Deliverable  
- Build predictive credit risk model → Problem Framing & Scoping (Stage 01) → Project scoping document, stakeholder context artifact  
- Data collection & preprocessing → Data Stage (Stage 02) → Cleaned datasets  
- Exploratory Data Analysis → Analysis Stage (Stage 03) → Insights & visualizations  
- Model selection & training → Modeling Stage (Stage 04) → Trained model  
- Validation & testing → Validation Stage (Stage 05) → Model performance report  
- Deployment/Reporting → Deployment Stage (Stage 06) → Risk score predictions & documentation

## Repo Plan
Project folders: `/data/`, `/src/`, `/notebooks/`, `/docs/`  
Update cadence: commits after each stage, weekly syncs with stakeholders, versioned releases for deliverables.



