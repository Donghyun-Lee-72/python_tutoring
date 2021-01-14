# error.py
# This is collection of user-defined error for RIOT API project


# CONSTANT
response_error = {
    400: "Bad request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Data not found",
    405: "Method not allowed",
    415: "Unsupported media type",
    429: "Rate limit exceeded",
    500: "Internal server error",
    502: "Bad gateway",
    503: "Service unavailable",
    504: "Gateway timeout"
}


class StatusError(Exception):
    def __init__(self, code):
        self.status_code = code     # int

    def __str__(self):
        return str(self.status_code) + ": " + response_error[self.status_code]