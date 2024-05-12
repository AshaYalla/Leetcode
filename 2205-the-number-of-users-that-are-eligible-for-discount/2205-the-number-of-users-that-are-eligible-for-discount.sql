CREATE FUNCTION getUserIDs(@startDate DATE, @endDate DATE, @minAmount INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        
        SELECT count(distinct user_id) FROM Purchases
WHERE time_stamp between @startDate and @EndDate and
amount >= @minAmount 
        
    );
END