"""
Implement a function that returns the minimum number of platforms that are required for the train so that none of them waits.
"""

def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    if not arrival or not departure:
        return 0

    arrival.sort()
    departure.sort()
    total_length = len(arrival)

    result = 1
    platform = 1
    i, j = 1, 0

    while i < total_length and j < total_length:

        if arrival[i] <  departure[j]:
            platform += 1
            i += 1

            if platform > result:
                result = platform
        else:
            platform -= 1
            j += 1

    return result



# Driver code to test above function
if __name__ == '__main__':

    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]

    print(find_platform(arrival, departure))

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 240, 320, 430, 400, 520]

    print(find_platform(arrival, departure))