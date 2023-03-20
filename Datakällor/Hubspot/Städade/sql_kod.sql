-- Kod för att joina tables.

SELECT *
FROM companies c
JOIN contacts c2 ON c.CompanyName = c2.CompanyName
JOIN kunddatafilen k ON c.CompanyName = k.Företagsnamn
JOIN deals d ON c.CompanyName = d.AssociatedCompany;