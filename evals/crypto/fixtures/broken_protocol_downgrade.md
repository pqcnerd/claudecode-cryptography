# BROKEN protocol: unauthenticated version negotiation

A -> B: Hello, versions=[1,2,3]
B -> A: Choose version=1   # NOT MACed/signed
A -> B: continues with v1 features

Expected finding: downgrade_unauthenticated_version; bind version into transcript/MAC.
