.. datu_bazes_atjaunošana_no_backup_faila_izmantojot_sql_enterprise_manager

===============================================================
Datu bāzes atjaunošana no BackUp faila, izmantojot SQL Enterprise Manager
===============================================================

Lai atjaunotu Ozols datu bāzi, nepieciešama SQL Server Enterprise Manager programmatūra.

1. Nepieciešams pievienot jaunu SQL Server Group:

SQL Server Group -> Peles labais taustiņš ->New SQL Server Registration:

2. Nepieciešams pievienot datu bāzi, atjaunojot (Restore) to no esošā backup faila:

Serveris-> Databases-> Peles labais taustiņš -> All Tasks -> Restore Database:

Izvēloties šo darbību, nepieciešams norādīt datu bāzes vārdu: OZOLS, ceļu uz backup failu, no kura dati tiks atjaunoti:
 
Pēc tam, apstirpinot darbības ar OK, datu bāze tiks pievienota, atjaunojot datus no backup faila.