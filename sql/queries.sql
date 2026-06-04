-- 1 Top 5 Funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV Per Month

SELECT
substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3 SIP Transactions Count

SELECT
COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP';

-- 4 Transactions By State

SELECT
state,
SUM(amount_inr) total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5 Funds With Expense Ratio < 1%

SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6 Average 5-Year Return

SELECT
AVG(return_5yr_pct)
FROM fact_performance;

-- 7 Top Performing Funds (5Y)

SELECT
amfi_code,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 8 Transactions By KYC Status

SELECT
kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- 9 NAV History Record Count

SELECT
amfi_code,
COUNT(*)
FROM fact_nav
GROUP BY amfi_code;

-- 10 Fund Count By Category

SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;