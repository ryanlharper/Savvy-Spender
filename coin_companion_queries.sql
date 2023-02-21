-- check for over/under budget query 
WITH income AS (
	SELECT SUM(b.amount) AS income_budget FROM budgets b
	WHERE category_id = 7 AND user_id = 1)
SELECT (SELECT income_budget FROM income)-SUM(b.amount) AS "Remaining Money" FROM budgets b 
WHERE category_id <> 7 AND user_id = 1;

-- yearly amount spent by category query
SELECT ROUND(SUM(t.amount),2) AS "Amount Spent", c.name AS "Category" FROM transactions t
JOIN categories c ON c.id = t.category_id
WHERE t.date BETWEEN '2023-01-01' AND '2023-12-31' AND t.user_id = 1 AND c.id <> 7
GROUP BY c.name ORDER BY SUM(t.amount) DESC;

--yearly amount spent by subcategory
SELECT ROUND(SUM(t.amount),2) AS "Amount Spent", c.name AS "Category" FROM transactions t
JOIN categories c ON c.id = t.category_id
WHERE t.date BETWEEN '2023-01-01' AND '2023-12-31' AND t.user_id = 1 AND c.id <> 7
GROUP BY c.name ORDER BY SUM(t.amount) DESC;

-- spent versus budget by month
WITH income AS (
	SELECT SUM(t.amount) AS income_paid FROM transactions t
	WHERE category_id = 7 AND user_id = 1 AND date BETWEEN '2023-02-01' AND '2023-02-31')
SELECT (SELECT income_paid FROM income) - ROUND(SUM(t.amount),2) AS "Amount Remaining" FROM transactions t
WHERE t.date BETWEEN '2023-01-01' AND '2023-01-31' AND t.user_id = 1 AND t.category_id <> 7;

--budget year by category/subcategory query
SELECT b.amount, c.name, sc.subcategory_name FROM budgets b
JOIN categories c ON c.id = b.category_id
JOIN subcategories sc ON sc.id = b.subcategory_id
JOIN budget_years by ON by.id = b.budget_year_id
WHERE by.name = '2023'
ORDER BY b.amount DESC;