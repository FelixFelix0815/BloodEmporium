# Tables

## unlockables Table
### Old:
| id        | name     | category                                | rarity   | notes                                 | type                            | order    |
|-----------|----------|-----------------------------------------|----------|---------------------------------------|---------------------------------|----------|
| _string_  | _string_ | _string_                                | _string_ | _string_                              | _string_                        | _int_    |
|           |          |                                         |          |                                       |                                 |          |
| unique_id | name     | state (retired/unused)                  | rarity   | character for retired/unused category | universal (mystery boxed, etc.) | order.md |
|           |          | survivor/killer for perks               |          | else null                             | perk                            |          |
|           |          | survivor/killer/universal for Offerings |          |                                       | offering                        |          |
|           |          | survivor/killer_name[¹] for Add-ons     |          |                                       | add-on                          |          |
|           |          | survivor for Items                      |          |                                       | item                            |          |

### New:
| id        | name     | category                                                  | rarity   | notes                                 | type                            | order    |
|-----------|----------|-----------------------------------------------------------|----------|---------------------------------------|---------------------------------|----------|
| _string_  | _string_ | _string_                                                  | _string_ | _string_                              | _string_                        | _int_    |
|           |          |                                                           |          |                                       |                                 |          |
| unique_id | name     | state (retired/unused)                                    | rarity   | character for retired/unused category | universal (mystery boxed, etc.) | order.md |
|           |          | survivor/killer/survivor_name[²]/killer_name[¹] for perks |          | else null                             | perk                            |          |
|           |          | survivor/killer/universal for Offerings                   |          |                                       | offering                        |          |
|           |          | survivor/killer_name[¹] for Add-ons                       |          |                                       | add-on                          |          |
|           |          | survivor for Items                                        |          |                                       | item                            |          |

## killers Table
| id[¹]     | alias      | name      |
|-----------|------------|-----------|
| _string_  | _string_   | _string_  |
|           |            |           |
| unique_id | short name | full name |

[¹]: #killers-table

## survivors Table

| id[²]     | alias      | name      |
|-----------|------------|-----------|
| _string_  | _string_   | _string_  |
|           |            |           |
| unique_id | short name | full name |

[²]: #survivors-table-todo