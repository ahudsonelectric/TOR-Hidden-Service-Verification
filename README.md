# TOR Hidden Service Verification

### ...WORK IN PROGRESS

## The problem:

Many sites at TOR network have multiple mirrors for support their user load.

When connecting to one of these mirror sites we can have the following question:

Is this the right place or is a service impersonation?

## My proposal:

The client who wants to verify if a service is fake or real can download the PGP key of the service and send a challenge to a port of the service.

The challenge is a simple string defined by the client and the server must respond with the same string with a valid GPG signature to identify himself

## What i'm doing?

A client and a daemon with that concept