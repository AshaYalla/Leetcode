WITH a AS
(SELECT SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) immediate
FROM Delivery)

SELECT ROUND(100*(SELECT * FROM a)/ COUNT(*),2) immediate_percentage
FROM Delivery