from os import environ


def get_env_vigilantly(env_var):
    """Get the value of the environment variable or print an alert message
    and return None if not found.

    This has the same functionality as `environ.get("ENV_VAR")` except for
    that it prints a warning when an environment variable is not found.

    :param env_var: The environment variable to get the value of.
    :type env_var: str.
    :returns: str or None.

    """
    try:
        return environ[env_var]
    except KeyError:
        print "ALERT: The environment variable `{0}` is not set!".format(env_var)
        print ""
        return None


SENTRY_DSN = get_env_vigilantly("SENTRY_DSN")
