# checkson-webhook-self-check

This repository creates a Docker image that makes an HTTP request to a URL defined by the
environment variable `FLAPPING_STATE_URL`. This endpoint returns `{"state": true}` and 
`{"state": false}` in an alternating manner. This means that the check also alternates
between successful and unsuccessful runs, so that on each run a webhook notification is 
sent out.

An external metrics and alerting system (Influx Cloud) is used to detect if this notification
has been sent out.
