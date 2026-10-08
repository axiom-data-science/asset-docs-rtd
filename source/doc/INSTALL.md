# Installation

The Asset Docs stack is comprised of the following components:

*   [asset-docs-postgres-db](https://github.com/axiom-data-science/asset-docs-postgres-db)

    ...the "backend" of the stack, providing a reliable data persistence layer
    (using a Postgres database) as well as enforcement of authentication and
    authorization policies.

*   [asset-manager](https://github.com/axiom-data-science/asset-manager)

    ...the "frontend" of the stack, providing a user interface.

*   **(optionally)** An OAuth / OIDC Connect identity provider (for doing single sign-on
    authorization like with Google, Microsoft, other others).

The `asset-manager` and `asset-docs-postgres-db` repositories each have their
own technologies and deployment methods. More information for each repository
is available from their respective README documents (see:
[asset-manager][amreadme], and [asset-docs-postgres-db][adreadme]).

[amreadme]: https://github.com/axiom-data-science/asset-manager/blob/main/README.md
[adreadme]: https://github.com/axiom-data-science/asset-docs-postgres-db/blob/main/README.md

## Quick Start

### For `asset-docs-postgres-db`

Within the repo for the `asset-docs-postgres-db`, you can build and run the
backend with the following.

```shell
docker compose build
docker compose up
```

This will initialize the Postgres backend into a temporary in-memory database as well as run a PostgREST instance available via HTTP REST API calls here:

<http://localhost:3345/>


### For `asset-manager`

Within the repo for the `asset-manager`, you can build and run the
backend with the following.

```shell
docker compose build
docker compose up
```

This will build the `asset-manager` app and run an NGINX web server hosting the app at:

<http://localhost:9797>


### For both `asset-manager` and `asset-docs-postgres-db`

The easiest way to stand up the `asset-manager` frontend and the
`asset-docs-postgres-db` backend is via a `docker compose` stack.

If you have already built the docker images for `asset-manager:latest` and
`asset-docs-postgres-db`, you should be able to run both apps in a docker
compose stack wiht the following sample `docker-compose.yml` file:


```yaml
services:

  db:
    image: "asset-docs-postgres-db:latest"
    build:
      context:    .
      dockerfile: Dockerfile
    environment:
      # For postgres initialization
      - POSTGRES_DB
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      # custom envsubst variables borrowed from the environment
      - ADDB_DB_NAME
      - ADDB_OWNER_USER
      - ADDB_PASSWORD
      - ADDB_POSTGREST_USER
      - ADDB_POSTGREST_USER_PASSWORD
      - ADDB_READ_USER
      - ADDB_READ_USER
      - ADDB_READ_USER_PASSWORD
      - ADDB_RW_USER
      - ADDB_RW_USER_PASSWORD
      - ADDB_SCHEMA
    ports:
     - 2345:5432
    healthcheck:
          test: ["CMD", "pg_isready", "-U", "${ADDB_OWNER_USER}", "--dbname", "${ADDB_DB_NAME}" ]
          interval: 5s
          timeout: 3s
          retries: 3
          start_period: 2s
    # By default, don't create a persistent volume (for development). Instead,
    # init the postgres database every time
    tmpfs:
      - "/var/lib/postgresql"

  frontend:
    image: asset-manager:latest
    build:
      context:      .
      dockerfile:   Dockerfile
    environment:
    #   TWOWOLVES_OIDC_AUTHORITY: "${VITE_OIDC_AUTHORITY}"
    #   TWOWOLVES_OIDC_CLIENT_ID: "${VITE_OIDC_CLIENT_ID}"
    #   TWOWOLVES_OIDC_REDIRECT_URI: "${VITE_OIDC_REDIRECT_URI}"
    #   TWOWOLVES_OIDC_POST_LOGOUT_REDIRECT_URI: "${VITE_OIDC_POST_LOGOUT_REDIRECT_URI}"
    #   TWOWOLVES_OIDC_SCOPE: "${VITE_OIDC_SCOPE}"
        TWOWOLVES_APPS_API_BASE_URL: "${VITE_APPS_API_BASE_URL}"
    ports:
    - "9797:80"

  postinit:
    image: "asset-docs-postgres-db:latest"
    build:
      context:    .
      dockerfile: Dockerfile
    environment:
      # Used to specify a remote postgres host to run against (if not db service)
      - ADDB_HOST=db
      - ADDB_DB_NAME
      - ADDB_OWNER_USER
      - ADDB_PASSWORD
      - ADDB_POSTGREST_USER
      - ADDB_POSTGREST_USER_PASSWORD
      - ADDB_READ_USER
      - ADDB_READ_USER_PASSWORD
      - ADDB_RW_USER
      - ADDB_RW_USER_PASSWORD
      - ADDB_SCHEMA
      - ADDB_SUPERADMIN_ENTITLEMENT
      # psql to use PGPASSWORD env var instead of requiring user input
      - PGPASSWORD=${ADDB_PASSWORD}
      - ADDB_ENABLE_MOCK_DATA=${ADDB_ENABLE_MOCK_DATA:-false}
    depends_on:
      db:
        condition: service_healthy
        restart: true
    volumes:
      - "./templates/postinit/:/templates"
    command: >
      /usr/local/bin/run_templates.sh /templates

  postgrest:
    image: "postgrest/postgrest:v13.0.4"
    environment:
      PGRST_DB_URI: "postgresql://${ADDB_POSTGREST_USER}:${ADDB_POSTGREST_USER_PASSWORD}@db:5432/${ADDB_DB_NAME}"
      PGRST_DB_SCHEMAS: "asset_docs"
      PGRST_DB_ANON_ROLE: "${ADDB_READ_USER}"
      PGRST_JWT_SECRET: "${ADDB_PGRST_JWT_SECRET}"
      # When checking for a user's role, look under 'roles' for
      # the specific read/write role we're expecting the postgrest service
      # to be able to run (the not DB_ANON_ROLE) above. This will be the
      # real, actual Postgres role that is given the ability to read/write
      # to the schema in question.
      PGRST_JWT_ROLE_CLAIM_KEY: ".roles[?(@ == \"${ADDB_RW_USER}\")]"
      PGRST_JWT_AUD: "${ADDB_PGRST_JWT_REQUIRED_AUDIENCE}"
      # PGRST_OPENAPI_SERVER_PROXY_URI: "TODO"
      # Enable for debugging and/or logging the SQL statements emitted by
      # PostgREST
      PGRST_LOG_LEVEL: "debug"
      PGRST_LOG_QUERY: "main-query"
      # Allowt the use of aggregate functions within the postgrest instance.
      PGRST_DB_AGGREGATES_ENABLED: "true"
      # Helper function to maintain the 'person' table.
      PGRST_DB_PRE_REQUEST: "asset_docs_private.upsert_person"

    ports:
      - "3345:3000"
    depends_on:
      db:
        condition: service_healthy
        restart: true
      postinit:
        condition: service_completed_successfully
        restart: true

```
