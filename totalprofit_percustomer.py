SELECT
    customer.CustomerID,
    CONCAT(contact.FirstName, ' ', contact.LastName) AS CustomerName,
    ROUND(SUM(salesdetail.LineTotal - product.StandardCost * salesdetail.OrderQty), 2) AS TotalProfitPerCustomer

FROM `tc-da-1.adwentureworks_db.customer` AS customer

INNER JOIN `tc-da-1.adwentureworks_db.salesorderheader` AS salesorder
    ON customer.CustomerID = salesorder.CustomerID

INNER JOIN `tc-da-1.adwentureworks_db.contact` AS contact
   ON salesorder.ContactID = contact.ContactId

INNER JOIN `tc-da-1.adwentureworks_db.salesorderdetail` AS salesdetail
    ON salesorder.SalesOrderID = salesdetail.SalesOrderID
LEFT JOIN `tc-da-1.adwentureworks_db.specialofferproduct` AS spec_offer_product
    ON salesdetail.ProductID = spec_offer_product.ProductID AND salesdetail.SpecialOfferID = spec_offer_product.SpecialOfferID
LEFT JOIN `tc-da-1.adwentureworks_db.product` AS product
    ON spec_offer_product.ProductID = product.ProductID

GROUP BY customer.CustomerID, contact.FirstName, contact.LastName
ORDER BY TotalProfitPerCustomer DESC;