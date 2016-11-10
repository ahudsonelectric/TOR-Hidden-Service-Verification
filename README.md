# TOR Hidden Service Verification (Daemon)

## The problem:

Many sites at TOR network have multiple mirrors, when connecting to one of these mirror sites we can have the following question:

Is this the right place or is a service impersonation?

## My proposal:

The client who wants to verify if a service is fake or real can download the PGP key of the service and send a challenge to a port of the service.

## What i'm doing?

A browser add-on and a daemon with that concept

## How does the daemon work?

Initialize under the same domain the services listed in the configuration file with an additional port where customers can send their challenge to verify the identity of the author of the services provided by the domain

## How does the challenge look?

In short:

- Client send: ask for signed challenge
- Server response: signed_block
- Client process: If signature is not ok the domain is scam

## How does the browser add-on work?

- The client go into a domain for first time
- The client decided than that service is good for him and he would like to know in the future if a mirror of the service is from the same author
- The extension notes the client about that site is running hidden service verification
- The client accepts the data offered from the service to identify mirrors in the future , just clicking on extension icon
- Next time the client go into a service who claims to be a mirror of the original one the extension uses the stored info to advice the client if is realy true or if it is scam

## Daemon Install:

All you need to know is [here](https://github.com/arrase/TOR-Hidden-Service-Verification/wiki).

## Supported browsers:

* [Get for Firefox](https://github.com/arrase/Hidden-Service-Verification-WebExtension/releases)
* [Get for Google Chrome](https://github.com/arrase/Hidden-Service-Verification-WebExtension/releases)

Instructions for unsupported browsers:

* [Internet Explorer](https://github.com/arrase/TOR-Hidden-Service-Verification/wiki/Install-a-decent-browser)

## Developers: 

Adding support to Hidden Service Verification to your client:

If you are developing a client for a Tor hidden service you will find instructions to add support for the verification of the domain to your application in the [wiki](https://github.com/arrase/TOR-Hidden-Service-Verification/wiki)

## Be a contributor:

A project like this is very hard in terms of amount of work so if you think that project is something good for the community feel free to collaborate with code or with BTC.

Wallet: 1KUDR3ebaHUss8gjbx5vCqJ2m9LmC9EbRj
