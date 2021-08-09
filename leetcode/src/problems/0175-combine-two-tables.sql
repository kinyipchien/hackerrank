SELECT FirstName, LastName, City, State
FROM person
LEFT JOIN address
USING(PersonId)
;