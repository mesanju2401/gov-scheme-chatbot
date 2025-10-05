# backend/db.py

def find_matching_schemes(schemes, intent, keywords):
    """
    Filter the list of schemes by matching any of the given keywords
    in the scheme's name or description. Return up to 5 matches.
    """
    matched = []

    for scheme in schemes:
        name = scheme.get("name", "").lower()
        description = scheme.get("description", "").lower()

        for keyword in keywords:
            if keyword in name or keyword in description:
                matched.append(scheme)
                break  # stop checking this scheme as soon as one keyword matches

    return matched[:5]  # return top 5 matches
