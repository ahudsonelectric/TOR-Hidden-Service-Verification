# TOR Hidden Service Verification

### ...WORK IN PROGRESS

## The problem:

Many sites at TOR network have multiple mirrors for support their user load.

When connecting to one of these mirror sites we can have the following question:

Is this the right place or is a service impersonation?

## My proposal:

The client who wants to verify if a service is fake or real can download the PGP key of the service and send a challenge to a port of the service.

## What i'm doing?

A browser add-on and a daemon with that concept

## How does the daemon work?

Initialize under the same domain the services listed in the configuration file with an additional port where customers can send their challenge to verify the identity of the author of the services provided by the domain

## How does the challenge look?

In short:

- Client send: json(hello)
- Server response: json(gpg_key_id)
- Client process: do preliminary checks against his db, can stop here if don't trust the site or if is all ok maybe wants to accepts the id
- Client send: ask for signed challenge
- Server response: signed_block(json(true_domain))
- Client process: If signature is ok the true_domain should be the right one...it match?

## How does the browser add-on work?

- The client go into a domain for first time
- The client decided than that service is good for him and he would like to know in the future if a mirror of the service is from the same author
- The extension notes the client about that site is running hidden service verification
- The client accepts the data offered from the service to identify mirrors in the future , just clicking on extension icon
- Next time the client go into a service who claims to be a mirror of the original one the extension uses the stored info to advice the client if is realy true or if it is scam

Supported browsers:

* [Firefox Add-on](https://github.com/arrase/HSVerify-Firefox)
- [Chrome Add-on](https://github.com/arrase/HSVerify-Chrome)

## Future:

A way to automatically maintain a list of trusted mirrors for help user to reconnect if one mirror is offline

## Be a contributor:

A project like this is very hard in terms of amount of work so if you think that project is something good for the community feel free to collaborate with code or with BTC.

Wallet: 1KUDR3ebaHUss8gjbx5vCqJ2m9LmC9EbRj
