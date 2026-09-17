# Architecture

## ASCII Art


```none

                        HTTPS GET, POST, PUT     Postgres table SELECTs,
                        and DELETE requests      INSERTs, UPDATEs, DELETEs
                              /                     /
                             /                     /
    [HTTP/Browser Client] <---> [PostgREST API] <---> [Postgres Database]
            ^
            |
            |  -- OAuth / OIDC exchange (for access and refresh tokens)
            |
            v
    [External Identity Provider]



```
