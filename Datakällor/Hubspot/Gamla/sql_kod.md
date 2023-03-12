# Kod för att joina tables.


select *
FROM companies c 
join contacts c2 
on c.CompanyName = c2.CompanyName 

join kunddatafilen k 
on c.CompanyName = k.Företagsnamn 

join deals d 
on c.CompanyName = d.AssociatedCompany  