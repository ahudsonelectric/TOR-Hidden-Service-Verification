# TOR Hidden Service Verification

### ...WORK IN PROGRESS

## The problem:

Many sites at TOR network have multiple mirrors for support their user load.

When connecting to one of these mirror sites we can have the following question:

Is this the right place or is a service impersonation?

## My proposal:

The client who wants to verify if a service is fake or real can download the PGP key of the service and send a challenge to a port of the service.

## What i'm doing?

A client and a daemon with that concept

## How does the daemon work?

Initialize under the same domain the services listed in the configuration file with an additional port where customers can send their challenge to verify the identity of the author of the services provided by the domain

## How does the client work?

Loads the service's public key and sends a challenge to the domain to identify the author of the services provided

## How does the challenge look?

In short:

- Client send: json(rand_string)
- Server response: signed_block(json(rand_string,true_domain))
- Client: If signature is ok, and the rand_strings are the same the true_domain is the right one...it match?
