# Orchestrate SDK Contribution Guide

The Orchestrate SDK is a TypeScript and JavaScript library for interacting with the Orchestrate API at <https://api.careevolutionapi.com>. Releases are tagged and generated from `main`. Development should be forked from `main` and a PR created to merge back into it.

## Installation

For TypeScript, navigate to the `./typescript` directory and install dependencies with `npm i`. For Python, navigate to the `./python` directory and install dependencies with `poetry install`.

## Tests

TypeScript tests can be run and watched with `npm run test:watch`. Python tests can be run with `poetry run pytest`.

To run Local Hashing Service tests, docker must be installed and running. Tests against the Identity API do not use data directly from the Local Hashing Service, so any valid hash key can be used to start the container. See the [Orchestrate Docs](https://orchestrate.docs.careevolution.com/identity/local_hash/hosting.html) for information on starting the container.
