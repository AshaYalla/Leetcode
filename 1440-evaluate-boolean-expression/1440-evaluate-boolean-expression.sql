select e.*,
case when operator = '>' and v1.value > v2.value then 'true'
when operator = '<' and v1.value < v2.value then 'true'
when operator = '=' and v1.value = v2.value then 'true'
else 'false'
end value

FROM Expressions e 
JOIN Variables v1 ON e.left_operand=v1.name
JOIN Variables v2 ON e.right_operand=v2.name;
