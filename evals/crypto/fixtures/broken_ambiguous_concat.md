# BROKEN: ambiguous transcript concatenation

transcript = hash(identity || message)

Variable-length identity/message without length prefixes can collide.
Expected finding: ambiguous_serialization
