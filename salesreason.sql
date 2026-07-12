WITH sales_per_reason AS (
 SELECT
   sales.SalesOrderID AS SalesOrderID,
   DATE_TRUNC(OrderDate, MONTH) AS year_month,
   sales_reason.SalesReasonID,
   SUM(sales.TotalDue) AS sales_amount
 FROM
   `tc-da-1.adwentureworks_db.salesorderheader` AS sales
 INNER JOIN
   `tc-da-1.adwentureworks_db.salesorderheadersalesreason` AS sales_reason
 ON
   sales.SalesOrderID = sales_reason.salesOrderID
 GROUP BY 1,2,3
)
SELECT
 sales_per_reason.SalesOrderID,
 sales_per_reason.year_month,
 reason.Name AS sales_reason,
 sales_per_reason.sales_amount,
 
FROM
 sales_per_reason
LEFT JOIN
 `tc-da-1.adwentureworks_db.salesreason` AS reason
ON
 sales_per_reason.SalesReasonID = reason.SalesReasonID