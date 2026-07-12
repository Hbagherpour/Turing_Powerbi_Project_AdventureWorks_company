SELECT 
      sales.SalesOrderId,
      product.ProductId,
      product.Name,
      subcategory.Name as SubCategory,
      category.Name as Category,
      product.ListPrice,
      sales.TotalDue

FROM `tc-da-1.adwentureworks_db.salesorderheader` as sales
LEFT JOIN `tc-da-1.adwentureworks_db.salesorderdetail`  as sales_detail
ON sales.SalesOrderID = sales_detail.SalesOrderID


LEFT JOIN `tc-da-1.adwentureworks_db.specialofferproduct` as spec_offer_product
ON sales_detail.productId = spec_offer_product.ProductID AND sales_detail.SpecialOfferID = spec_offer_product.SpecialOfferID

LEFT JOIN `tc-da-1.adwentureworks_db.product` as product
ON spec_offer_product.ProductID = product.ProductID

LEFT JOIN `tc-da-1.adwentureworks_db.productsubcategory` as subcategory
ON product.ProductSubcategoryID = subcategory.ProductSubcategoryID
LEFT JOIN `tc-da-1.adwentureworks_db.productcategory` as category
ON subcategory.ProductCategoryID = category.ProductCategoryID 

ORDER BY SalesOrderId;