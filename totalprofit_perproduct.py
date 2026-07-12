SELECT
    product.ProductID,
    product.Name AS ProductName,
    ROUND(SUM(salesdetail.LineTotal - product.StandardCost * salesdetail.OrderQty), 2) AS TotalProfitPerProduct,
    ROUND((SUM(salesdetail.LineTotal - product.StandardCost * salesdetail.OrderQty) / NULLIF(SUM(salesdetail.LineTotal), 0)) * 100, 2) AS ProfitMargin
FROM 
    tc-da-1.adwentureworks_db.salesorderheader salesorder
INNER JOIN 
    tc-da-1.adwentureworks_db.salesorderdetail AS salesdetail
    ON salesorder.SalesOrderID = salesdetail.SalesOrderID
LEFT JOIN 
    tc-da-1.adwentureworks_db.specialofferproduct AS spec_offer_product
    ON salesdetail.ProductID = spec_offer_product.ProductID AND salesdetail.SpecialOfferID = spec_offer_product.SpecialOfferID
LEFT JOIN 
    tc-da-1.adwentureworks_db.product AS product
    ON spec_offer_product.ProductID = product.ProductID
GROUP BY 
    product.ProductID, product.Name
ORDER BY 
    TotalProfitPerProduct DESC;